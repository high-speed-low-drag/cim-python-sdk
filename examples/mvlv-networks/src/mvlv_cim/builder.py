"""Build a CIM100 object graph of one MV-LV-Networks workbook.

``build_network(xlsx_path)`` reads the workbook (:mod:`mvlv_cim.excel`) and returns a
:class:`BuiltNetwork`. The modelling rules are documented in the README; the short version:

- Containers: GeographicalRegion ``AusNet`` > SubGeographicalRegion (network) > zone Substation
  (66 kV and 22 kV VoltageLevels) and one Substation per distribution transformer (with an LV
  VoltageLevel). One Feeder holds the MV ConnectivityNodes and MV equipment.
- One ConnectivityNode per bus; every ConductingEquipment has numbered, phased Terminals.
- Lines are ACLineSegments with a PerLengthSequenceImpedance per used linecode and a CurrentLimit.
- Transformers are PowerTransformers with two PowerTransformerEnds (series impedance on end 1).
- The LV network is replaced by one EquivalentInjection per distribution transformer.

Data problems never raise: they are recorded in ``BuiltNetwork.issues`` and handled.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path

from cim_python_sdk import (
    ACLineSegment,
    ACLineSegmentPhase,
    BaseVoltage,
    ConnectivityNode,
    CoordinateSystem,
    CurrentLimit,
    EquivalentInjection,
    ExternalNetworkInjection,
    Feeder,
    GeographicalRegion,
    LinearShuntCompensator,
    Location,
    Name,
    NameType,
    OperationalLimitDirectionKind,
    OperationalLimitSet,
    OperationalLimitType,
    PerLengthSequenceImpedance,
    PhaseCode,
    PhaseShuntConnectionKind,
    PositionPoint,
    PowerTransformer,
    PowerTransformerEnd,
    RatioTapChanger,
    SubGeographicalRegion,
    Substation,
    Terminal,
    VoltageLevel,
    WindingConnection,
)
from cim_python_sdk._runtime import CimObject

from mvlv_cim.excel import (
    Issue,
    Line,
    LineCode,
    NetworkData,
    Transformer,
    load_network,
)
from mvlv_cim.ids import SHARED, make_mrid
from mvlv_cim.phases import (
    conn_type_phases,
    lv_secondary_code,
    node_spec_phases,
    phase_code,
    single_phase_kind,
)

#: Nominal voltages (kV) of the BaseVoltages; ratings within 5 % snap to these.
STANDARD_KV = (66.0, 22.0, 12.7, 0.433, 0.24)
CRS_URN = "urn:x-local:anonymised-xy"
SOURCE_BUS = "SourceBus"
#: backend.py ``voltage_source()``: the final ``edit vsource.source`` values (ohm at 66 kV).
SOURCE_Z = {"r1": 0.52824, "x1": 2.113, "r0": 0.59157, "x0": 1.7}
#: Length unit (OpenDSS ``units=``) to metres.
METRES_PER_UNIT = {"km": 1000.0, "m": 1.0, "mi": 1609.344, "kft": 304.8, "ft": 0.3048}

#: Findings reported once per network with the list of affected rows.
GROUPED = {
    "pvs_null": "PVs is 'Null'; reported as pvs=unknown",
    "shared_mv_bus": "several distribution transformers on one MV bus (Substation_ID@bus)",
    "backend_centre_tap_differs": (
        "2-colour secondary modelled as s12N at the sheet's 433 V; backend.py builds a "
        "0.25+0.25 kV centre tap with the kVA on each leg"
    ),
    "single_phase_to_earth_rating": (
        "1-colour (phase-to-earth) unit rated 22 kV on the 22 kV network, where it sees 12.7 kV; "
        "rating kept as in the sheet and backend.py"
    ),
}

#: ``BuiltNetwork.elements`` keys, i.e. the element kinds counted against the sheets.
KINDS = (
    "line",
    "distribution_transformer",
    "isolating_transformer",
    "regulator",
    "inline_transformer",
    "capacitor",
    "lv_equivalent",
    "zone_transformer",
    "source",
)


@dataclass
class BuiltNetwork:
    """The result of :func:`build_network`."""

    name: str
    path: Path
    objects: list[CimObject]
    feeder: Feeder
    zone_substation: Substation
    source: ExternalNetworkInjection
    issues: list[Issue]
    elements: dict[str, list[CimObject]]
    #: Bus id (int, ``"SourceBus"``, or ``("lv", key)`` for LV busbars) -> ConnectivityNode.
    nodes: dict[object, ConnectivityNode]
    #: Islands found in the data: lists of MV bus ids not reachable from the source.
    islands: list[list[object]] = field(default_factory=list)

    @property
    def counts(self) -> Counter[str]:
        """Number of objects per CIM class name."""
        return Counter(type(o).__name__ for o in self.objects)

    @property
    def element_counts(self) -> dict[str, int]:
        return {k: len(self.elements.get(k, ())) for k in KINDS}

    def issue_summary(self) -> Counter[str]:
        return Counter(i.code for i in self.issues)

    def validate(self, *, ignore: tuple[str, ...] = ("'instance_set'",)) -> list[str]:
        """``validate()`` messages of all objects, without the known ``instance_set`` quirk."""
        out = []
        for o in self.objects:
            out.extend(m for m in o.validate() if not any(s in m for s in ignore))
        return out


def build_network(xlsx_path: str | Path) -> BuiltNetwork:
    """Build the CIM model of one ``Network_*.xlsx`` workbook."""
    data = load_network(xlsx_path)
    return _Builder(data).build()


def nominal_kv(kv: float) -> float | None:
    """The standard nominal voltage within 5 % of ``kv``, or None."""
    for s in STANDARD_KV:
        if abs(kv - s) <= 0.05 * s:
            return s
    return None


def _fmt(v: float | None) -> str:
    if v is None:
        return "unknown"
    return f"{v:g}"


def _conn_kind(value: str | None) -> WindingConnection | None:
    v = (value or "").strip().lower()
    if v in ("delta", "d", "ll"):
        return WindingConnection.D
    if v in ("wye", "y", "star", "ln"):
        # OpenDSS wye windings are solidly grounded unless rneut is given.
        return WindingConnection.Yn
    return None


@dataclass
class _EndSpec:
    node: ConnectivityNode
    phases: PhaseCode
    bv: BaseVoltage
    rated_kv: float | None
    kva: float | None
    connection: WindingConnection | None


@dataclass
class _TapSpec:
    numtaps: int
    maxtap: float
    mintap: float
    tap: float
    ltc: bool
    description: str | None = None
    fixed: bool = False


class _Builder:
    def __init__(self, data: NetworkData) -> None:
        self.data = data
        self.net = data.path.stem
        self.issues: list[Issue] = list(data.issues)
        self.objects: list[CimObject] = []
        self.elements: dict[str, list[CimObject]] = {k: [] for k in KINDS}
        self.nodes: dict[object, ConnectivityNode] = {}
        self.node_kv: dict[object, float] = {}
        self.bvs: dict[int, BaseVoltage] = {}
        self.plsi: dict[str, PerLengthSequenceImpedance] = {}
        self.used_keys: dict[str, set[str]] = defaultdict(set)
        self.coords: dict[int, tuple[float, float]] = {}
        self.islands: list[list[object]] = []
        self.lvtx_not_in_conn: list[str] = []
        self.grouped: dict[tuple[str, str], list[str]] = {}
        for i in data.issues:  # the loader reports 'Null' PVs per row; group them
            if i.code == "pvs_null":
                self.group("pvs_null", "lvtx", i.source_id)
        self.issues = [i for i in self.issues if i.code != "pvs_null"]

    # ------------------------------------------------------------------ helpers
    def issue(self, code: str, message: str, sheet: str | None = None, sid: object = None) -> None:
        self.issues.append(Issue(code, message, sheet, None if sid is None else str(sid)))

    def group(self, code: str, sheet: str, sid: object) -> None:
        """Collect a per-element finding that is reported once, as a list (see GROUPED)."""
        self.grouped.setdefault((code, sheet), []).append(str(sid))

    def flush_groups(self) -> None:
        for (code, sheet), ids in self.grouped.items():
            more = " ..." if len(ids) > 15 else ""
            self.issue(code, f"{len(ids)} rows: {GROUPED[code]}: {ids[:15]}{more}", sheet)

    def add[T: CimObject](self, obj: T) -> T:
        self.objects.append(obj)
        return obj

    def mrid(self, kind: str, key: object) -> str:
        return make_mrid(self.net, kind, key)

    def unique_key(self, kind: str, element_id: int | None, row: int, sheet: str) -> str:
        """A per-kind unique source key: the Element_ID, made unique if missing or duplicated."""
        if element_id is None:
            key = f"row{row}"
            self.issue(
                "missing_element_id",
                f"no Element_ID; keyed as {key!r}",
                sheet,
                f"row {row}",
            )
        else:
            key = str(element_id)
            if key in self.used_keys[kind]:
                new = f"{key}#row{row}"
                self.issue(
                    "duplicate_element_id",
                    f"Element_ID {key} used before; keyed as {new!r}",
                    sheet,
                    key,
                )
                key = new
        self.used_keys[kind].add(key)
        return key

    def base_voltage(self, kv: float) -> BaseVoltage:
        volts = round(kv * 1000)
        bv = self.bvs.get(volts)
        if bv is None:
            bv = self.add(
                BaseVoltage(
                    mrid=make_mrid(SHARED, "BaseVoltage", volts),
                    name=f"{volts / 1000:g} kV",
                    nominal_voltage=float(volts),
                )
            )
            self.bvs[volts] = bv
        return bv

    def nominal(self, kv: float | None, what: str, sheet: str, sid: object) -> float | None:
        if kv is None:
            return None
        nom = nominal_kv(kv)
        if nom is None:
            self.issue(
                "nonstandard_voltage",
                f"{what} {kv:g} kV used as its own BaseVoltage",
                sheet,
                sid,
            )
            return kv
        return nom

    def location(self, key: str, name: str, points: list[tuple[float, float]]) -> Location | None:
        if not points:
            return None
        loc = self.add(
            Location(mrid=self.mrid("Location", key), name=name, coordinate_system=self.cs)
        )
        for i, (x, y) in enumerate(points, start=1):
            self.add(
                PositionPoint(
                    sequence_number=i,
                    x_position=str(x),
                    y_position=str(y),
                    location=loc,
                )
            )
        return loc

    def bus_point(self, bus: object) -> list[tuple[float, float]]:
        p = self.coords.get(bus) if isinstance(bus, int) else None
        return [p] if p else []

    def source_name(self, obj: CimObject, element_id: int | None) -> None:
        if element_id is not None:
            self.add(
                Name(
                    name=str(element_id),
                    identified_object=obj,
                    name_type=self.name_type,
                )
            )

    def terminal(
        self,
        ce: CimObject,
        key: str,
        seq: int,
        node: ConnectivityNode,
        phases: PhaseCode,
    ) -> Terminal:
        name = getattr(ce, "name", None)
        return self.add(
            Terminal(
                mrid=self.mrid("Terminal", f"{key}:{seq}"),
                name=f"{name} T{seq}",
                sequence_number=seq,
                phases=phases,
                connected=True,
                conducting_equipment=ce,
                connectivity_node=node,
            )
        )

    # -------------------------------------------------------------------- build
    def build(self) -> BuiltNetwork:
        d = self.data
        if not d.mv_net_txs:
            raise ValueError(
                f"{d.path}: no mv_net_txs row; cannot place the source"
            )  # pragma: no cover
        self.zone = d.mv_net_txs[0]
        for extra in d.mv_net_txs[1:]:
            self.issue(
                "extra_zone_transformer",
                "only the first mv_net_txs row is modelled",
                "mv_net_txs",
                extra.substation_id,
            )
        self._coords()
        self._containers()
        self.lines = self._included_lines()
        self._classify_mvtx()
        self._node_voltages()
        self._nodes()
        self._source_and_zone()
        self._lines()
        self._mv_transformers()
        self._distribution_transformers()
        self._capacitors()
        self._cross_checks()
        self.flush_groups()
        return BuiltNetwork(
            name=self.net,
            path=d.path,
            objects=self.objects,
            feeder=self.feeder,
            zone_substation=self.zone_sub,
            source=self.source,
            issues=self.issues,
            elements=self.elements,
            nodes=self.nodes,
            islands=self.islands,
        )

    def _coords(self) -> None:
        seen: dict[int, tuple[float, float]] = {}
        for bc in self.data.buscoords:
            if bc.x is None or bc.y is None:
                self.issue("missing_coordinates", "no x/y", "buscoords", bc.node_id)
                continue
            if bc.node_id in seen:
                self.issue(
                    "duplicate_buscoord",
                    f"Node_ID listed twice ({seen[bc.node_id]} and {(bc.x, bc.y)}); first kept",
                    "buscoords",
                    bc.node_id,
                )
                continue
            seen[bc.node_id] = (bc.x, bc.y)
        self.coords = seen

    def _containers(self) -> None:
        z = self.zone
        zid = z.substation_id or self.net
        self.region = self.add(
            GeographicalRegion(
                mrid=make_mrid(SHARED, "GeographicalRegion", "AusNet"), name="AusNet"
            )
        )
        self.subregion = self.add(
            SubGeographicalRegion(
                mrid=self.mrid("SubGeographicalRegion", self.net),
                name=self.net,
                description=f"MV-LV-Networks {self.data.path.name}",
                region=self.region,
            )
        )
        self.cs = self.add(
            CoordinateSystem(
                mrid=self.mrid("CoordinateSystem", "xy"),
                name=f"{self.net} anonymised x/y",
                crs_urn=CRS_URN,
            )
        )
        self.name_type = self.add(
            NameType(
                name="source_element_id",
                description="Element_ID in the MV-LV-Networks workbook",
            )
        )
        self.limit_type = self.add(
            OperationalLimitType(
                mrid=self.mrid("OperationalLimitType", "PATL"),
                name="PATL",
                description="Permanent current rating (OpenDSS normamp)",
                direction=OperationalLimitDirectionKind.absoluteValue,
                is_infinite_duration=True,
            )
        )
        loc = self.location("zone", f"{zid} zone substation", self.bus_point(z.bus2))
        self.zone_sub = self.add(
            Substation(
                mrid=self.mrid("Substation", f"zone:{zid}"),
                name=f"{zid} zone substation",
                region=self.subregion,
                location=loc,
            )
        )
        self.zone_loc = loc
        kv1 = self.nominal(z.kv_primary, "zone primary", "mv_net_txs", zid) or 66.0
        kv2 = self.nominal(z.kv_secondary, "zone secondary", "mv_net_txs", zid) or 22.0
        self.zone_kv = (kv1, kv2)
        self.vl_hv = self.add(
            VoltageLevel(
                mrid=self.mrid("VoltageLevel", f"zone:{zid}:hv"),
                name=f"{zid} {kv1:g} kV",
                substation=self.zone_sub,
                base_voltage=self.base_voltage(kv1),
            )
        )
        self.vl_mv = self.add(
            VoltageLevel(
                mrid=self.mrid("VoltageLevel", f"zone:{zid}:mv"),
                name=f"{zid} {kv2:g} kV",
                substation=self.zone_sub,
                base_voltage=self.base_voltage(kv2),
            )
        )
        self.feeder = self.add(
            Feeder(
                mrid=self.mrid("Feeder", zid),
                name=zid,
                description=f"MV feeder of {self.data.path.name}",
                normal_energizing_substation=self.zone_sub,
            )
        )
        for base in (66.0, 22.0, 12.7, 0.433, 0.24):
            self.base_voltage(base)

    def _included_lines(self) -> list[Line]:
        out, deleted = [], []
        for ln in self.data.lines:
            if ln.deleted:
                deleted.append(ln.element_id)
                continue
            if ln.start_node is None or ln.end_node is None:
                self.issue(
                    "line_missing_node",
                    "Start_Node or End_Node missing; line skipped",
                    "lines",
                    ln.element_id,
                )
                continue
            out.append(ln)
        if deleted:
            self.issue(
                "deleted_lines_skipped",
                f"{len(deleted)} lines named 'Delete' skipped as in backend.py "
                f"(total {sum(ln.length or 0 for ln in self.data.lines if ln.deleted):.3f} km): "
                f"{deleted[:10]}{' ...' if len(deleted) > 10 else ''}",
                "lines",
            )
        return out

    def _classify_mvtx(self) -> None:
        """Split ``mvtx`` into isolating transformers, regulators and plain in-line transformers."""
        ctype = {c.element_id: c.type for c in self.data.connections if c.element_id is not None}
        self.mvtx_kind: list[tuple[Transformer, str]] = []
        for t in self.data.mvtx:
            label = ctype.get(t.element_id) or ""
            backend = "iso" if t.kv_primary != t.kv_secondary else "reg"
            if label.endswith("-ISO"):
                kind = "iso"
            elif label.endswith("-REG"):
                kind = "reg"
            elif label == "InLineTransformer":
                kind = "inline"
            else:
                kind = backend
                self.issue(
                    "mvtx_unlabelled",
                    f"no connections Type; classified as {kind!r} from its voltages",
                    "mvtx",
                    t.substation_id,
                )
            if (kind == "iso" and backend != "iso") or (kind != "iso" and backend == "iso"):
                self.issue(
                    "mvtx_type_mismatch",
                    f"labelled {label!r} but kvs {t.kv_primary}/{t.kv_secondary}",
                    "mvtx",
                    t.substation_id,
                )
            if kind == "inline":
                self.issue(
                    "mvtx_plain_inline",
                    f"connections Type 'InLineTransformer', {_fmt(t.kv_primary)}/"
                    f"{_fmt(t.kv_secondary)} kV, wdg1_numtaps={t.numtaps}: modelled as a 3-phase "
                    "in-line transformer without tap changer (backend.py builds every "
                    "equal-voltage mvtx as a regulator)",
                    "mvtx",
                    t.substation_id,
                )
            self.mvtx_kind.append((t, kind))

    def _node_voltages(self) -> None:
        """Assign a nominal kV to every MV bus by propagating from the zone substation.

        Lines keep the voltage; an mvtx sets its secondary (Bus1 -> Bus2) or primary voltage.
        Buses not reachable from the source are islands: reported, and given a voltage from
        their equipment (1-phase lines 12.7 kV, otherwise 22 kV).
        """
        adj: dict[object, list[tuple[object, float | None]]] = defaultdict(list)
        for ln in self.lines:
            adj[ln.start_node].append((ln.end_node, None))
            adj[ln.end_node].append((ln.start_node, None))
        for t, _ in self.mvtx_kind:
            if t.bus1 is None or t.bus2 is None:
                continue
            k2 = self.nominal(t.kv_secondary, "secondary", "mvtx", t.substation_id)
            k1 = self.nominal(t.kv_primary, "primary", "mvtx", t.substation_id)
            adj[t.bus1].append((t.bus2, k2))
            adj[t.bus2].append((t.bus1, k1))
        all_buses = set(adj)
        for t in self.data.lvtx:
            if t.bus1 is not None:
                all_buses.add(t.bus1)
        for c in self.data.mvcaps:
            if c.bus1 is not None:
                all_buses.add(c.bus1)
        z = self.zone
        all_buses.add(z.bus2)
        kv = self.node_kv
        kv[SOURCE_BUS] = self.zone_kv[0]
        kv[z.bus2] = self.zone_kv[1]
        conflicts: set[object] = set()

        def bfs(start: object) -> list[object]:
            seen = [start]
            q = deque([start])
            while q:
                n = q.popleft()
                for m, edge_kv in adj[n]:
                    v = kv[n] if edge_kv is None else edge_kv
                    if m in kv:
                        if kv[m] != v and m not in conflicts:
                            conflicts.add(m)
                            self.issue(
                                "voltage_conflict",
                                f"bus reached at {kv[m]:g} and {v:g} kV; first kept",
                                "buscoords",
                                m,
                            )
                        continue
                    kv[m] = v
                    seen.append(m)
                    q.append(m)
            return seen

        bfs(z.bus2)
        one_phase = {ln.start_node for ln in self.lines if ln.phases == 1}
        one_phase |= {ln.end_node for ln in self.lines if ln.phases == 1}
        for bus in sorted(all_buses - set(kv), key=str):
            if bus in kv:
                continue
            kv[bus] = 12.7 if bus in one_phase else self.zone_kv[1]
            island = bfs(bus)
            self.islands.append(island)
            self.issue(
                "island",
                f"{len(island)} buses not connected to the source "
                f"(voltage assumed {kv[bus]:g} kV): "
                f"{island[:10]}",
                "lines",
                bus,
            )
        self.all_buses = all_buses

    def _nodes(self) -> None:
        z = self.zone
        self.nodes[SOURCE_BUS] = self.add(
            ConnectivityNode(
                mrid=self.mrid("ConnectivityNode", SOURCE_BUS),
                name=SOURCE_BUS,
                connectivity_node_container=self.vl_hv,
            )
        )
        for bus in sorted(
            self.all_buses,
            key=lambda b: (isinstance(b, str), str(b) if isinstance(b, str) else b),
        ):
            if bus == SOURCE_BUS:
                continue
            container = self.vl_mv if bus == z.bus2 else self.feeder
            self.nodes[bus] = self.add(
                ConnectivityNode(
                    mrid=self.mrid("ConnectivityNode", bus),
                    name=f"N{bus}",
                    connectivity_node_container=container,
                )
            )
            if isinstance(bus, int) and bus not in self.coords:
                self.issue(
                    "missing_buscoord",
                    "bus used by equipment has no coordinates",
                    "buscoords",
                    bus,
                )
        used = {b for b in self.all_buses if isinstance(b, int)}
        orphans = sorted(set(self.coords) - used)
        if orphans:
            self.issue(
                "orphan_buscoords",
                f"{len(orphans)} buscoords nodes not used by any modelled element "
                "(no node created): "
                f"{orphans[:15]}{' ...' if len(orphans) > 15 else ''}",
                "buscoords",
            )

    def _node_bv(self, bus: object) -> BaseVoltage:
        return self.base_voltage(self.node_kv[bus])

    # ---------------------------------------------------------------- equipment
    def _source_and_zone(self) -> None:
        z = self.zone
        zid = z.substation_id or self.net
        r1, x1, r0, x0 = SOURCE_Z["r1"], SOURCE_Z["x1"], SOURCE_Z["r0"], SOURCE_Z["x0"]
        z1, z0 = math.hypot(r1, x1), math.hypot(r0, x0)
        u = self.zone_kv[0] * 1000
        self.source = self.add(
            ExternalNetworkInjection(
                mrid=self.mrid("ExternalNetworkInjection", "source"),
                name=f"{zid} grid source",
                description=(
                    f"backend.py vsource: basekv={self.zone_kv[0]:g} pu=1 "
                    f"R1={r1} X1={x1} R0={r0} X0={x0} ohm"
                ),
                equipment_container=self.vl_hv,
                base_voltage=self.base_voltage(self.zone_kv[0]),
                max_initial_sym_sh_c_current=u / (math.sqrt(3) * z1),
                max_r1_to_x1_ratio=r1 / x1,
                max_r0_to_x0_ratio=r0 / x0,
                max_z0_to_z1_ratio=z0 / z1,
                voltage_factor=1.0,
                location=self.zone_loc,
            )
        )
        self.terminal(self.source, "source", 1, self.nodes[SOURCE_BUS], PhaseCode.ABC)
        self.elements["source"].append(self.source)
        if z.bus1 != SOURCE_BUS:
            self.issue(
                "zone_bus1",
                f"Bus1 is {z.bus1!r}, expected 'SourceBus'; connected to SourceBus",
                "mv_net_txs",
                zid,
            )
        key = self.unique_key("zone", z.element_id, z.row, "mv_net_txs")
        c1, c2 = _conn_kind(z.connection_primary), _conn_kind(z.connection_secondary)
        pt = self._transformer(
            kind="zone",
            key=key,
            row=z,
            name=zid,
            container=self.zone_sub,
            location=self.zone_loc,
            ends=[
                _EndSpec(
                    self.nodes[SOURCE_BUS],
                    PhaseCode.ABC,
                    self.base_voltage(self.zone_kv[0]),
                    z.kv_primary,
                    z.kva_primary,
                    c1,
                ),
                _EndSpec(
                    self.nodes[z.bus2],
                    PhaseCode.ABC,
                    self.base_voltage(self.zone_kv[1]),
                    z.kv_secondary,
                    z.kva_secondary,
                    c2,
                ),
            ],
            tap=self._tap_spec(z, regulator=False),
            description=f"source=mv_net_txs; conn_type={z.conn_type}",
        )
        self.elements["zone_transformer"].append(pt)
        # Feeder head: the zone transformer's 22 kV terminal.
        head = next(t for t in pt.terminals if t.sequence_number == 2)
        head.normal_head_feeder = self.feeder

    def _linecode(self, lc_id: str | None, line_id: object) -> PerLengthSequenceImpedance | None:
        if lc_id is None:
            self.issue("missing_linecode", "no Linecode/Phases", "lines", line_id)
            return None
        if lc_id in self.plsi:
            return self.plsi[lc_id]
        lc = self.linecode_rows.get(lc_id)
        if lc is None:
            self.issue(
                "missing_linecode",
                f"linecode {lc_id!r} not in linecodes; no impedance set",
                "lines",
                line_id,
            )
            self.plsi[lc_id] = None  # type: ignore[assignment]
            return None
        unit = (lc.units or "km").lower()
        per_m = METRES_PER_UNIT.get(unit)
        if per_m is None:
            self.issue("unknown_unit", f"Units {lc.units!r}; km assumed", "linecodes", lc_id)
            per_m = 1000.0

        def ohm(v: float | None) -> float | None:
            return None if v is None else v / per_m

        def siemens(v: float | None) -> float | None:
            # OpenDSS b1/b0 are in microsiemens per length unit.
            return None if v is None else v * 1e-6 / per_m

        desc = "; ".join(
            f"{k}={v}"
            for k, v in (
                ("full_name_code", lc.full_name_code),
                ("material", lc.material),
                ("size", lc.size),
                ("phases", lc.phases),
                ("ampacity1_A", lc.ampacity1),
                ("ampacity2_A", lc.ampacity2),
            )
            if v is not None
        )
        p = self.add(
            PerLengthSequenceImpedance(
                mrid=self.mrid("PerLengthSequenceImpedance", lc_id),
                name=f"lc_{lc_id}",
                description=desc,
                r=ohm(lc.r1),
                x=ohm(lc.x1),
                bch=siemens(lc.b1),
                r0=ohm(lc.r0),
                x0=ohm(lc.x0),
                b0ch=siemens(lc.b0),
                gch=0.0,
                g0ch=0.0,
            )
        )
        self.plsi[lc_id] = p
        return p

    def _linecodes(self) -> None:
        rows: dict[str, LineCode] = {}
        for lc in self.data.linecodes:
            if lc.linecode_id in rows:
                old = rows[lc.linecode_id]
                same = (
                    old.r1,
                    old.x1,
                    old.b1,
                    old.r0,
                    old.x0,
                    old.b0,
                    old.ampacity1,
                    old.ampacity2,
                ) == (
                    lc.r1,
                    lc.x1,
                    lc.b1,
                    lc.r0,
                    lc.x0,
                    lc.b0,
                    lc.ampacity1,
                    lc.ampacity2,
                )
                self.issue(
                    "duplicate_linecode",
                    f"defined twice (rows {old.row} and {lc.row}, "
                    f"{'identical' if same else 'different values'}); "
                    "the last definition is used, as OpenDSS redefines on a repeated 'new'",
                    "linecodes",
                    lc.linecode_id,
                )
            rows[lc.linecode_id] = lc
        self.linecode_rows = rows

    def _lines(self) -> None:
        self._linecodes()
        conns = {c.element_id: c for c in self.data.connections if c.element_id is not None}
        no_conn = []
        used_lc: set[str] = set()
        for ln in self.lines:
            key = self.unique_key("line", ln.element_id, ln.row, "lines")
            sid = ln.element_id
            name = ln.element_name or f"L{ln.line_number}"
            # Phases
            letters = node_spec_phases(ln.start_node_phase)
            end_letters = node_spec_phases(ln.end_node_phase)
            if letters is None:
                letters = "ABC" if ln.phases != 1 else "A"
                self.issue(
                    "bad_phase_spec",
                    f"Start_Node_Phase {ln.start_node_phase!r}; {letters} assumed",
                    "lines",
                    sid,
                )
            if end_letters is not None and end_letters != letters:
                self.issue(
                    "phase_spec_mismatch",
                    f"start {ln.start_node_phase!r} vs end {ln.end_node_phase!r}; start used",
                    "lines",
                    sid,
                )
            if ln.phases is not None and len(letters) != ln.phases:
                self.issue(
                    "phase_count_mismatch",
                    f"Phases={ln.phases} but node spec {ln.start_node_phase!r}",
                    "lines",
                    sid,
                )
            # Length
            unit = (ln.units or "km").lower()
            per_m = METRES_PER_UNIT.get(unit)
            if per_m is None:
                self.issue("unknown_unit", f"Units {ln.units!r}; km assumed", "lines", sid)
                per_m = 1000.0
            length = None if ln.length is None else ln.length * per_m
            if length is None:
                self.issue("missing_length", "no Length", "lines", sid)
            elif length <= 0:
                self.issue(
                    "zero_length",
                    f"Length {ln.length}; kept as {length} m",
                    "lines",
                    sid,
                )
            if ln.start_node == ln.end_node:
                self.issue(
                    "self_loop",
                    f"line from bus {ln.start_node} to itself",
                    "lines",
                    sid,
                )
            kv = self.node_kv[ln.start_node]
            if self.node_kv[ln.end_node] != kv:
                self.issue("line_voltage_mismatch", "ends at different voltages", "lines", sid)
            plsi = self._linecode(ln.linecode_id, sid)
            if ln.linecode_id:
                used_lc.add(ln.linecode_id)
            # Geography
            c = conns.get(ln.element_id)
            if c is not None and None not in (c.x1, c.y1, c.x2, c.y2):
                pts = [(c.x1, c.y1), (c.x2, c.y2)]
            else:
                no_conn.append(sid)
                pts = self.bus_point(ln.start_node) + self.bus_point(ln.end_node)
                if len(pts) < 2:
                    pts = []
            loc = self.location(f"line:{key}", name, pts)  # type: ignore[arg-type]
            desc = f"linecode={ln.linecode_id}; line_number={ln.line_number}"
            seg = self.add(
                ACLineSegment(
                    mrid=self.mrid("ACLineSegment", key),
                    name=name,
                    description=desc,
                    length=length,
                    base_voltage=self.base_voltage(kv),
                    equipment_container=self.feeder,
                    per_length_impedance=plsi,
                    location=loc,
                )
            )
            self.source_name(seg, ln.element_id)
            pc = phase_code(letters)
            self.terminal(seg, f"line:{key}", 1, self.nodes[ln.start_node], pc)
            self.terminal(seg, f"line:{key}", 2, self.nodes[ln.end_node], pc)
            if len(letters) == 1:
                self.add(
                    ACLineSegmentPhase(
                        mrid=self.mrid("ACLineSegmentPhase", f"{key}:{letters}"),
                        name=f"{name} {letters}",
                        phase=single_phase_kind(letters),
                        sequence_number=1,
                        ac_line_segment=seg,
                    )
                )
            # Current rating (OpenDSS normamp = min(Ampacity1, Ampacity2))
            lc = self.linecode_rows.get(ln.linecode_id or "")
            amps = [
                a for a in ((lc.ampacity1, lc.ampacity2) if lc else ()) if a is not None and a > 0
            ]
            if amps:
                ols = self.add(
                    OperationalLimitSet(
                        mrid=self.mrid("OperationalLimitSet", key),
                        name=f"{name} limits",
                        equipment=seg,
                    )
                )
                self.add(
                    CurrentLimit(
                        mrid=self.mrid("CurrentLimit", key),
                        name=f"{name} PATL",
                        normal_value=min(amps),
                        value=min(amps),
                        operational_limit_set=ols,
                        operational_limit_type=self.limit_type,
                    )
                )
            elif lc is not None:
                self.issue(
                    "missing_ampacity",
                    "linecode has no positive ampacity",
                    "linecodes",
                    ln.linecode_id,
                )
            self.elements["line"].append(seg)
        if no_conn:
            self.issue(
                "line_not_in_connections",
                f"{len(no_conn)} lines have no connections row; location from buscoords: "
                f"{no_conn[:10]}",
                "lines",
            )
        dup_used = sorted(
            i.source_id
            for i in self.issues
            if i.code == "duplicate_linecode" and i.source_id in used_lc
        )
        if dup_used:
            self.issue(
                "duplicate_linecode_used",
                f"duplicated linecodes used by lines: {dup_used}",
                "linecodes",
            )

    def _tap_spec(self, t: Transformer, regulator: bool) -> _TapSpec | None:
        n = t.numtaps or 1
        tap = t.tap if t.tap is not None else 1.0
        mx = t.maxtap if t.maxtap is not None else 1.0
        mn = t.mintap if t.mintap is not None else 1.0
        if n > 1 and mx > mn:
            return _TapSpec(n, mx, mn, tap, ltc=regulator)
        if regulator:
            self.issue(
                "regulator_no_tap_range",
                "no tap range in the sheet; no RatioTapChanger emitted",
                t.sheet,
                t.substation_id,
            )
            return None
        if abs(tap - 1.0) > 1e-9:
            # A fixed off-load tap with no range in the sheet: encode it without inventing a range.
            return _TapSpec(
                n,
                mx,
                mn,
                tap,
                ltc=False,
                description="fixed off-load tap from sheet (no range given)",
                fixed=True,
            )
        return None

    def _transformer(
        self,
        *,
        kind: str,
        key: str,
        row: Transformer,
        name: str,
        container: CimObject,
        location: Location | None,
        ends: list[_EndSpec],
        tap: _TapSpec | None,
        description: str,
    ) -> PowerTransformer:
        e1, e2 = ends
        clock = 0
        if e1.connection and e2.connection:
            d1 = e1.connection is WindingConnection.D
            d2 = e2.connection is WindingConnection.D
            clock = 1 if d1 != d2 else 0  # OpenDSS default LeadLag=Lag (ANSI): LV lags by 30 deg
        letters = {
            WindingConnection.D: "D",
            WindingConnection.Y: "Y",
            WindingConnection.Yn: "YN",
            WindingConnection.I: "I",
        }
        vg = None
        if e1.connection in letters and e2.connection in letters:
            vg = f"{letters[e1.connection]}{letters[e2.connection].lower()}{clock}"
        pt = self.add(
            PowerTransformer(
                mrid=self.mrid("PowerTransformer", f"{kind}:{key}"),
                name=name,
                description=description,
                equipment_container=container,
                location=location,
                vector_group=vg,
            )
        )
        self.source_name(pt, row.element_id)
        s = (row.kva_primary or 0) * 1000
        u1 = (e1.rated_kv or 0) * 1000
        r = x = g = None
        if s > 0 and u1 > 0:
            zb = u1 * u1 / s
            r = None if row.loadloss is None else row.loadloss / 100 * zb
            x = None if row.xhl is None else row.xhl / 100 * zb
            g = None if row.noloadloss is None else row.noloadloss / 100 / zb
        if None in (r, x, g):
            self.issue(
                "missing_impedance",
                "rating, %loadloss, xhl or %noloadloss missing",
                row.sheet,
                name,
            )
        for i, e in enumerate(ends, start=1):
            if e.connection is None:
                self.issue(
                    "unknown_connection",
                    "winding connection not recognised",
                    row.sheet,
                    name,
                )
            if e.rated_kv is None or e.kva is None:
                self.issue("missing_rating", f"end {i} has no kV or kVA", row.sheet, name)
            term = self.terminal(pt, f"{kind}:{key}", i, e.node, e.phases)
            end = self.add(
                PowerTransformerEnd(
                    mrid=self.mrid("PowerTransformerEnd", f"{kind}:{key}:{i}"),
                    name=f"{name} end {i}",
                    end_number=i,
                    rated_s=None if e.kva is None else e.kva * 1000,
                    rated_u=None if e.rated_kv is None else e.rated_kv * 1000,
                    connection_kind=e.connection,
                    phase_angle_clock=0 if i == 1 else clock,
                    grounded=e.connection is WindingConnection.Yn or None,
                    r=r if i == 1 else 0.0,
                    x=x if i == 1 else 0.0,
                    g=g if i == 1 else 0.0,
                    b=0.0,
                    base_voltage=e.bv,
                    terminal=term,
                    power_transformer=pt,
                )
            )
            if i == 1 and tap is not None:
                self._ratio_tap_changer(end, f"{kind}:{key}", name, tap, e.rated_kv)
        return pt

    def _ratio_tap_changer(
        self,
        end: PowerTransformerEnd,
        key: str,
        name: str,
        t: _TapSpec,
        kv: float | None,
    ) -> None:
        if t.fixed:
            # Two positions: neutral (tap 1, step 0) and the sheet's tap (step 1).
            self.add(
                RatioTapChanger(
                    mrid=self.mrid("RatioTapChanger", key),
                    name=f"{name} tap changer",
                    description=t.description,
                    step_voltage_increment=round((t.tap - 1.0) * 100, 9),
                    low_step=0,
                    high_step=1,
                    neutral_step=0,
                    normal_step=1,
                    step=1.0,
                    neutral_u=None if kv is None else kv * 1000,
                    ltc_flag=False,
                    control_enabled=False,
                    transformer_end=end,
                )
            )
            return
        inc = (t.maxtap - t.mintap) / (t.numtaps - 1)
        high = round((t.maxtap - 1.0) / inc)
        low = high - (t.numtaps - 1)
        step = (t.tap - 1.0) / inc
        normal = min(max(round(step), low), high)
        self.add(
            RatioTapChanger(
                mrid=self.mrid("RatioTapChanger", key),
                name=f"{name} tap changer",
                description=t.description
                or f"sheet: numtaps={t.numtaps} maxtap={t.maxtap:g} mintap={t.mintap:g} "
                f"tap={t.tap:g}",
                step_voltage_increment=round(inc * 100, 9),
                low_step=low,
                high_step=high,
                neutral_step=0,
                normal_step=normal,
                step=round(step, 9),
                neutral_u=None if kv is None else kv * 1000,
                ltc_flag=t.ltc,
                control_enabled=t.ltc,
                transformer_end=end,
            )
        )

    def _mv_transformers(self) -> None:
        for t, kind in self.mvtx_kind:
            sid = t.substation_id or f"mvtx row {t.row}"
            if t.bus1 is None or t.bus2 is None:
                self.issue("mvtx_missing_bus", "Bus1 or Bus2 missing; skipped", "mvtx", sid)
                continue
            key = self.unique_key("mvtx", t.element_id, t.row, "mvtx")
            letters = conn_type_phases(t.conn_type)
            n1, n2 = self.nodes[t.bus1], self.nodes[t.bus2]
            bv1, bv2 = self._node_bv(t.bus1), self._node_bv(t.bus2)
            loc = self.location(f"mvtx:{key}", sid, self.bus_point(t.bus1))
            desc = f"source=mvtx; conn_type={t.conn_type}"
            if kind == "iso":
                if letters is None or len(letters) != 2:
                    self.issue(
                        "bad_conn_type",
                        f"Conn_Type {t.conn_type!r} for an isolating transformer; AB assumed",
                        "mvtx",
                        sid,
                    )
                    letters = "AB"
                # backend.py: buses=[Bus1.<2 phases> Bus2.1.0 Bus2.0.2]; the SWER lines use Bus2.1.
                ends = [
                    _EndSpec(
                        n1,
                        phase_code(letters),
                        bv1,
                        t.kv_primary,
                        t.kva_primary,
                        WindingConnection.I,
                    ),
                    _EndSpec(
                        n2,
                        PhaseCode.A,
                        bv2,
                        t.kv_secondary,
                        t.kva_secondary,
                        WindingConnection.I,
                    ),
                ]
                tap = self._tap_spec(t, regulator=False)
                out = "isolating_transformer"
            else:
                if letters != "ABC":
                    self.issue(
                        "bad_conn_type",
                        f"Conn_Type {t.conn_type!r} for a 3-phase in-line unit; ABC used",
                        "mvtx",
                        sid,
                    )
                # backend.py models regulators as three single-phase grounded-wye autotransformers;
                # the sheet's delta/wye would imply a 30 degree shift on a 22/22 kV unit.
                ends = [
                    _EndSpec(
                        n1,
                        PhaseCode.ABC,
                        bv1,
                        t.kv_primary,
                        t.kva_primary,
                        WindingConnection.Yn,
                    ),
                    _EndSpec(
                        n2,
                        PhaseCode.ABC,
                        bv2,
                        t.kv_secondary,
                        t.kva_secondary,
                        WindingConnection.Yn,
                    ),
                ]
                if kind == "reg":
                    tap = self._tap_spec(t, regulator=True)
                    if tap is not None:
                        tap.description = (
                            f"sheet: numtaps={t.numtaps} maxtap={_fmt(t.maxtap)} "
                            f"mintap={_fmt(t.mintap)} tap={_fmt(t.tap)}; backend.py RegControl "
                            "vreg=100 band=3 ptratio=127 on winding 2"
                        )
                    out = "regulator"
                else:
                    tap = self._tap_spec(t, regulator=False)
                    out = "inline_transformer"
            pt = self._transformer(
                kind=out,
                key=key,
                row=t,
                name=sid,
                container=self.feeder,
                location=loc,
                ends=ends,
                tap=tap,
                description=desc,
            )
            self.elements[out].append(pt)

    def _distribution_transformers(self) -> None:
        conn_ids = {c.element_id for c in self.data.connections if c.type == "SecondarySub"}
        bus_count = Counter(t.bus1 for t in self.data.lvtx)
        for t in self.data.lvtx:
            sid = t.substation_id or f"lvtx row {t.row}"
            if t.bus1 is None or t.bus1 not in self.nodes:
                self.issue("lvtx_missing_bus", f"Bus1 {t.bus1!r} unknown; skipped", "lvtx", sid)
                continue
            if t.element_id is None:
                key = f"sub:{sid}"
                self.issue(
                    "missing_element_id",
                    f"no Element_ID; keyed by Substation_ID as {key!r}",
                    "lvtx",
                    sid,
                )
                self.used_keys["lvtx"].add(key)
            else:
                key = self.unique_key("lvtx", t.element_id, t.row, "lvtx")
            if t.bus2 not in (0, None):
                self.issue(
                    "lvtx_bus2",
                    f"Bus2 is {t.bus2!r} (expected 0); LV busbar synthesised anyway",
                    "lvtx",
                    sid,
                )
            if bus_count[t.bus1] > 1:
                self.group("shared_mv_bus", "lvtx", f"{sid}@{t.bus1}")
            ct = (t.conn_type or "").strip()
            letters = conn_type_phases(ct)
            if letters is None or len(letters) not in (1, 2, 3):
                self.issue(
                    "bad_conn_type",
                    f"Conn_Type {t.conn_type!r}; RWB assumed",
                    "lvtx",
                    sid,
                )
                ct, letters = "RWB", "ABC"
            nph = len(ct)
            mv_kv = self.node_kv[t.bus1]
            kv1 = self.nominal(t.kv_primary, "primary", "lvtx", sid)
            if kv1 is not None and kv1 != mv_kv:
                self.issue(
                    "rating_mismatch",
                    f"kvs_primary {t.kv_primary} kV on a {mv_kv:g} kV bus",
                    "lvtx",
                    sid,
                )
            if nph == 2:
                self.group("backend_centre_tap_differs", "lvtx", sid)
            if nph == 1 and kv1 is not None and kv1 != 12.7:
                self.group("single_phase_to_earth_rating", "lvtx", sid)
            kv2 = self.nominal(t.kv_secondary, "secondary", "lvtx", sid)
            if kv2 is None:
                kv2 = 0.433 if nph >= 2 else 0.24
                self.issue("missing_rating", f"no kvs_secondary; {kv2} kV assumed", "lvtx", sid)
            lv_bv = self.base_voltage(kv2)
            loc = self.location(f"lvtx:{key}", sid, self.bus_point(t.bus1))
            sub = self.add(
                Substation(
                    mrid=self.mrid("Substation", f"lvtx:{key}"),
                    name=sid,
                    description=f"distribution substation; type={t.type}",
                    region=self.subregion,
                    location=loc,
                    normal_energizing_feeder=[self.feeder],
                )
            )
            vl = self.add(
                VoltageLevel(
                    mrid=self.mrid("VoltageLevel", f"lvtx:{key}"),
                    name=f"{sid} {kv2:g} kV",
                    substation=sub,
                    base_voltage=lv_bv,
                )
            )
            lv_key = ("lv", key)
            lv_node = self.nodes[lv_key] = self.add(
                ConnectivityNode(
                    mrid=self.mrid("ConnectivityNode", f"lv:{key}"),
                    name=f"{sid} LV",
                    connectivity_node_container=vl,
                )
            )
            self.node_kv[lv_key] = kv2
            sec = lv_secondary_code(nph)
            if nph == 3:
                c1, c2 = (
                    _conn_kind(t.connection_primary),
                    _conn_kind(t.connection_secondary),
                )
            else:
                c1 = c2 = WindingConnection.I
            pt = self._transformer(
                kind="lvtx",
                key=key,
                row=t,
                name=sid,
                container=sub,
                location=loc,
                ends=[
                    _EndSpec(
                        self.nodes[t.bus1],
                        phase_code(letters),
                        self._node_bv(t.bus1),
                        t.kv_primary,
                        t.kva_primary,
                        c1,
                    ),
                    _EndSpec(lv_node, sec, lv_bv, t.kv_secondary, t.kva_secondary, c2),
                ],
                tap=self._tap_spec(t, regulator=False),
                description=f"source=lvtx; conn_type={ct}; wdg1_tap={_fmt(t.tap)}",
            )
            self.elements["distribution_transformer"].append(pt)
            pvs = "unknown" if t.pvs is None else t.pvs
            ei = self.add(
                EquivalentInjection(
                    mrid=self.mrid("EquivalentInjection", f"lvtx:{key}"),
                    name=f"{sid} LV equivalent",
                    description=(
                        f"type={t.type}; customers={_int(t.customers)}; pvs={pvs}; "
                        f"lv_feeders={_int(t.feeders)}"
                    ),
                    regulation_capability=False,
                    base_voltage=lv_bv,
                    equipment_container=vl,
                    location=loc,
                )
            )
            self.terminal(ei, f"ei:{key}", 1, lv_node, sec)
            self.elements["lv_equivalent"].append(ei)
            if t.element_id is not None and conn_ids and t.element_id not in conn_ids:
                self.lvtx_not_in_conn.append(sid)

    def _capacitors(self) -> None:
        for c in self.data.mvcaps:
            name = c.name or f"cap row {c.row}"
            if c.bus1 is None or c.bus1 not in self.nodes:
                self.issue(
                    "cap_missing_bus",
                    f"Bus1 {c.bus1!r} unknown; skipped",
                    "mvcaps",
                    name,
                )
                continue
            key = self.unique_key("cap", c.element_id, c.row, "mvcaps")
            node_kv = self.node_kv[c.bus1]
            kv = c.kv if c.kv else node_kv
            if c.kv and self.nominal(c.kv, "rating", "mvcaps", name) != node_kv:
                self.issue(
                    "rating_mismatch",
                    f"kvs {c.kv} on a {node_kv:g} kV bus",
                    "mvcaps",
                    name,
                )
            if c.phases != 3:
                self.issue(
                    "cap_phases",
                    f"phases={c.phases}; backend.py connects bus1.1.2.3, ABC used",
                    "mvcaps",
                    name,
                )
            u = kv * 1000
            b = None if c.kvar is None else c.kvar * 1e3 / (u * u)
            if b is None:
                self.issue("missing_rating", "no kvar", "mvcaps", name)
            loc = self.location(f"cap:{key}", name, self.bus_point(c.bus1))
            lsc = self.add(
                LinearShuntCompensator(
                    mrid=self.mrid("LinearShuntCompensator", key),
                    name=name,
                    description=f"kvar={_fmt(c.kvar)}; kv={_fmt(c.kv)}",
                    nom_u=u,
                    b_per_section=b,
                    g_per_section=0.0,
                    maximum_sections=1,
                    normal_sections=1,
                    sections=1.0,
                    grounded=True,
                    phase_connection=PhaseShuntConnectionKind.Y,
                    base_voltage=self._node_bv(c.bus1),
                    equipment_container=self.feeder,
                    location=loc,
                )
            )
            self.source_name(lsc, c.element_id)
            self.terminal(lsc, f"cap:{key}", 1, self.nodes[c.bus1], PhaseCode.ABC)
            self.elements["capacitor"].append(lsc)

    def _cross_checks(self) -> None:
        """Compare the element sheets with ``connections`` (used only for coordinates)."""
        if self.lvtx_not_in_conn:
            self.issue(
                "lvtx_not_in_connections",
                f"{len(self.lvtx_not_in_conn)} lvtx Element_IDs have no SecondarySub "
                "connections row "
                f"(IDs do not match): {self.lvtx_not_in_conn[:5]}",
                "lvtx",
            )
        ids = {
            "SecondarySub": {t.element_id for t in self.data.lvtx},
            "Capacitor": {c.element_id for c in self.data.mvcaps},
            "Line": {ln.element_id for ln in self.data.lines},
        }
        for typ, have in ids.items():
            extra = [
                c.element_id
                for c in self.data.connections
                if c.type == typ and c.element_id not in have
            ]
            if extra:
                self.issue(
                    "connection_without_element",
                    f"{len(extra)} connections rows of Type {typ!r} match no element: {extra[:10]}",
                    "connections",
                )


def _int(v: int | None) -> str:
    return "unknown" if v is None else str(v)
