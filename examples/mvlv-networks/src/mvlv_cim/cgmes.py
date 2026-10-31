"""CGMES 3.0 export of the built networks: EQ, SSH and TP (and optionally GL) file sets.

The plain build (``build_network``) is a CIM100 graph, not a CGMES one. ``prepare`` adds what the
CGMES profiles require and nothing else; ``write`` writes the file set with ``write_cgmes``;
``cgmes_view`` projects a graph onto what the selected profiles can carry, which is what a read of
the written files must give back. Everything ``prepare`` adds is listed in :class:`Prepared`.

Choices (also documented in docs/EXPORT_REPORT.md):

* **Containers.** CGMES 3.0 has no ``Feeder``. The feeder's connectivity nodes and conducting
  equipment move to a new ``Line`` (a CGMES equipment container) named after the feeder.
* **Line totals.** CGMES ``ACLineSegment`` carries total ``r``, ``x``, ``bch``, ``gch`` (not
  per-length impedance): per-length value of the linecode times the line length, both from the
  source. Zero-sequence values (``r0``, ``x0``, ...) belong to the ShortCircuit profile, which is
  not written (it requires data the source does not have, e.g. ``shortCircuitEndTemperature``).
* **TopologicalNodes.** One per ConnectivityNode (1:1). The data has no switch, so merging across
  closed switches would give the same result. ``BaseVoltage`` comes from the equipment at the node.
* **SSH.** ``Terminal.connected`` and ``Equipment.inService`` are true (the data has no open
  state); ``RatioTapChanger.step`` and ``LinearShuntCompensator.sections`` are the source values.
  **The data has no load, injection or dispatch values**: ``EquivalentInjection.p/q`` and
  ``ExternalNetworkInjection.p/q`` are 0 and the injection limits ``minP/maxP/minQ/maxQ`` and
  ``governorSCD`` of the source are 0 as well. They are placeholders required by the profile and
  say nothing about the real network. ``ExternalNetworkInjection.referencePriority`` is 1: it is
  the only infeed of the model.
* **Units.** The graph stays in SI base units (V, W, VA, m), as the builder makes it.
  ``write_cgmes`` scales to the CGMES multipliers (kV, MW, MVAr, MVA, km) in the files and
  ``read_cgmes`` back to SI.
* **Limits.** ``OperationalLimitSet.Terminal`` is required, so each line's limit set is tied to
  terminal 1 and a copy (same value, new mRID) to terminal 2. ``OperationalLimitType.kind`` is
  ``patl``, the name of the type in the builder.
"""

from __future__ import annotations

import datetime as dt
import uuid
import warnings
import zipfile
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import cim_python_sdk
from cim_python_sdk._runtime import CimObject
from cim_python_sdk.profiles import cgmes3
from cim_python_sdk.serialization import CgmesHeader, CgmesReport, read_cgmes, write_cgmes
from cim_python_sdk.serialization._common import (
    assign_ids,
    class_plan,
    collect,
    encode_value,
)

from mvlv_cim.builder import BuiltNetwork, build_network
from mvlv_cim.export import AUTHORITY_SET, LICENCE, SOURCE_URL, Workbook, created_from_mtime
from mvlv_cim.ids import NAMESPACE, make_mrid

#: Profiles of the default CGMES export. ``GL`` adds Location, PositionPoint and CoordinateSystem.
PROFILES = ("EQ", "SSH", "TP")
GL_PROFILES = (*PROFILES, "GL")
SUFFIX = "_CGMES"


class CgmesPrepareError(ValueError):
    """The graph cannot be turned into a CGMES model (data the profiles need is missing)."""


@dataclass
class Prepared:
    """What :func:`prepare` added or set, for the report."""

    network: BuiltNetwork
    added: Counter[str] = field(default_factory=Counter)  # objects created, per class
    set_values: Counter[str] = field(default_factory=Counter)  # values set, per "Class.property"
    notes: list[str] = field(default_factory=list)

    @property
    def objects(self) -> list[CimObject]:
        return self.network.objects


def _by_class(objects: Iterable[CimObject], cls: type) -> list[Any]:
    return [o for o in objects if isinstance(o, cls)]


def _set(prep: Prepared, obj: Any, name: str, value: Any, *, label: str | None = None) -> None:
    setattr(obj, name, value)
    prep.set_values[label or f"{type(obj).__name__}.{name}"] += 1


def _new(prep: Prepared, obj: CimObject) -> CimObject:
    prep.network.objects.append(obj)
    prep.added[type(obj).__name__] += 1
    return obj


def prepare(net: BuiltNetwork, *, geographic: bool = False) -> Prepared:
    """Add what CGMES EQ, SSH and TP need to the graph of ``net`` (in place).

    ``geographic=True`` also makes the GL profile valid (see :func:`_split_locations`).

    Call it on a fresh ``build_network`` result and use ``net`` for CGMES only: the plain exports
    of the same graph afterwards would carry the added objects. Idempotence is not provided.
    """
    prep = Prepared(net)
    objs = net.objects
    _feeder_to_line(prep)
    _transformer_sites(prep)
    _line_totals(prep)
    _limits(prep)
    _topological_nodes(prep)
    _ssh_values(prep)
    if geographic:
        _split_locations(prep)
    del objs
    return prep


# --------------------------------------------------------------------------------------
# EQ
# --------------------------------------------------------------------------------------


def _feeder_to_line(prep: Prepared) -> None:
    net = prep.network
    feeder = net.feeder
    region = net.zone_substation.region
    line = cim_python_sdk.Line(
        mrid=make_mrid(net.name, "cgmes_line", feeder.mrid),
        name=feeder.name,
        description=f"feeder {feeder.name} as a Line container (CGMES 3.0 has no Feeder)",
    )
    line.region = region
    _new(prep, line)
    moved = Counter()
    for node in list(feeder.connectivity_nodes):
        node.connectivity_node_container = line
        moved["ConnectivityNode"] += 1
    for eq in list(feeder.equipments):
        eq.equipment_container = line
        moved[type(eq).__name__] += 1
    prep.notes.append(
        "Feeder -> Line "
        + ", ".join(f"{n} {k}" for k, n in sorted(moved.items()))
        + " moved to the Line"
    )


def _transformer_sites(prep: Prepared) -> None:
    """Every transformer sits in a Substation and each of its terminals' nodes in a VoltageLevel
    of that Substation (CGMES tools such as pypowsybl need it). Distribution transformers get a
    VoltageLevel for their MV node; in-line transformers (isolating, regulating) get a new
    Substation "<name> site". A node that two transformers share can belong to one Substation
    only: it stays where the first put it and the later transformer is listed in ``notes``."""
    net = prep.network
    region = net.zone_substation.region
    placed: dict[Any, Any] = {}  # ConnectivityNode -> its VoltageLevel
    for node in _by_class(prep.objects, cim_python_sdk.ConnectivityNode):
        if isinstance(node.connectivity_node_container, cim_python_sdk.VoltageLevel):
            placed[node] = node.connectivity_node_container
    shared = []
    for tr in _by_class(list(prep.objects), cim_python_sdk.PowerTransformer):
        sub = tr.equipment_container
        if not isinstance(sub, cim_python_sdk.Substation):
            sub = _new(
                prep,
                cim_python_sdk.Substation(
                    mrid=make_mrid(net.name, "cgmes_site", tr.mrid),
                    name=f"{tr.name} site",
                    description="substation of an in-line transformer (CGMES needs one)",
                ),
            )
            sub.region = region
            tr.equipment_container = sub
        used: set[int] = set()
        for t in sorted(tr.terminals, key=lambda t: t.sequence_number):
            node = t.connectivity_node
            have = placed.get(node)
            if have is not None:
                if have.substation is not sub:
                    shared.append(f"{tr.name} T{t.sequence_number}")
                used.add(id(have))
                continue
            bv = t.transformer_end[0].base_voltage
            vl = next(
                (v for v in sub.voltage_levels if v.base_voltage is bv and id(v) not in used),
                None,
            )
            if vl is None:
                vl = _new(
                    prep,
                    cim_python_sdk.VoltageLevel(
                        mrid=make_mrid(net.name, "cgmes_vl", f"{sub.mrid}/{t.mrid}"),
                        name=f"{sub.name} {bv.nominal_voltage / 1000:g} kV",
                    ),
                )
                vl.substation = sub
                vl.base_voltage = bv
            used.add(id(vl))
            node.connectivity_node_container = vl
            placed[node] = vl
    if shared:
        prep.notes.append(
            f"{len(shared)} transformer terminal(s) on a node that another substation's "
            f"transformer already holds: {', '.join(shared)}"
        )


def _line_totals(prep: Prepared) -> None:
    for seg in _by_class(prep.objects, cim_python_sdk.ACLineSegment):
        pli = seg.per_length_impedance
        if seg.length is None or pli is None:
            raise CgmesPrepareError(f"{seg.name}: length or linecode missing")
        for name in ("r", "x", "bch", "gch"):
            per_m = getattr(pli, name)
            if per_m is None:
                raise CgmesPrepareError(f"{seg.name}: linecode {pli.name} has no {name}")
            _set(prep, seg, name, per_m * seg.length)


def _limits(prep: Prepared) -> None:
    patl = _by_class(prep.objects, cim_python_sdk.OperationalLimitType)
    for t in patl:
        if t.kind is None:
            _set(prep, t, "kind", cim_python_sdk.LimitKind.patl)
    net = prep.network
    for ols in _by_class(list(prep.objects), cim_python_sdk.OperationalLimitSet):
        eq = ols.equipment
        terms = sorted(eq.terminals, key=lambda t: t.sequence_number)
        if not terms:
            raise CgmesPrepareError(f"{ols.name}: equipment has no terminal")
        ols.terminal = terms[0]
        prep.set_values["OperationalLimitSet.terminal"] += 1
        for extra in terms[1:]:
            copy = _new(
                prep,
                cim_python_sdk.OperationalLimitSet(
                    mrid=make_mrid(net.name, "cgmes_limit_set", f"{ols.mrid}/{extra.mrid}"),
                    name=f"{ols.name} T{extra.sequence_number}",
                ),
            )
            copy.equipment = eq
            copy.terminal = extra
            for lim in list(ols.operational_limit_value):
                new = _new(
                    prep,
                    type(lim)(
                        mrid=make_mrid(net.name, "cgmes_limit", f"{lim.mrid}/{extra.mrid}"),
                        name=f"{lim.name} T{extra.sequence_number}",
                        normal_value=lim.normal_value,
                        value=lim.value,
                    ),
                )
                new.operational_limit_set = copy
                new.operational_limit_type = lim.operational_limit_type


# --------------------------------------------------------------------------------------
# TP
# --------------------------------------------------------------------------------------


def _node_base_voltage(node: Any) -> Any:
    """The BaseVoltage of the equipment at ``node`` (all must agree), else its container's."""
    found = {}
    for t in node.terminals:
        for end in t.transformer_end:
            if end.base_voltage is not None:
                found[id(end.base_voltage)] = end.base_voltage
        eq = t.conducting_equipment
        if eq is not None and not isinstance(eq, cim_python_sdk.PowerTransformer):
            bv = getattr(eq, "base_voltage", None)
            if bv is not None:
                found[id(bv)] = bv
    container = node.connectivity_node_container
    if isinstance(container, cim_python_sdk.VoltageLevel) and container.base_voltage is not None:
        found.setdefault(id(container.base_voltage), container.base_voltage)
    if len(found) != 1:
        volts = sorted(b.nominal_voltage for b in found.values())
        raise CgmesPrepareError(f"node {node.name}: base voltages {volts}")
    return next(iter(found.values()))


def _topological_nodes(prep: Prepared) -> None:
    net = prep.network
    nodes = _by_class(list(prep.objects), cim_python_sdk.ConnectivityNode)
    for node in nodes:
        tn = _new(
            prep,
            cim_python_sdk.TopologicalNode(
                mrid=make_mrid(net.name, "topological_node", node.mrid),
                name=node.name,
                description=f"1:1 from ConnectivityNode {node.name}",
            ),
        )
        tn.base_voltage = _node_base_voltage(node)
        tn.connectivity_node_container = node.connectivity_node_container
        node.topological_node = tn
        for t in node.terminals:
            t.topological_node = tn
    prep.notes.append(f"{len(nodes)} ConnectivityNodes -> {len(nodes)} TopologicalNodes (1:1)")


# --------------------------------------------------------------------------------------
# SSH
# --------------------------------------------------------------------------------------


def _ssh_values(prep: Prepared) -> None:
    for t in _by_class(prep.objects, cim_python_sdk.Terminal):
        if t.connected is None:
            _set(prep, t, "connected", True)
    for eq in _by_class(prep.objects, cim_python_sdk.Equipment):
        if eq.in_service is None:
            _set(prep, eq, "in_service", True, label="Equipment.in_service")
    for inj in _by_class(prep.objects, cim_python_sdk.EquivalentInjection):
        for name in ("p", "q"):
            if getattr(inj, name) is None:
                _set(prep, inj, name, 0.0)
    for src in _by_class(prep.objects, cim_python_sdk.ExternalNetworkInjection):
        for name in ("p", "q", "min_p", "max_p", "min_q", "max_q", "governor_scd"):
            if getattr(src, name) is None:
                _set(prep, src, name, 0.0)
        if src.reference_priority is None:
            _set(prep, src, "reference_priority", 1)
        if src.control_enabled is None:
            _set(prep, src, "control_enabled", False)
    for comp in _by_class(prep.objects, cim_python_sdk.LinearShuntCompensator):
        if comp.control_enabled is None:
            _set(prep, comp, "control_enabled", False)


# --------------------------------------------------------------------------------------
# GL
# --------------------------------------------------------------------------------------


def _split_locations(prep: Prepared) -> None:
    """The GL profile allows exactly one ``PowerSystemResource`` per ``Location``, while the
    builder shares the location of a transformer site between the substation, the transformer and
    the LV injection. Each extra resource gets a copy of the Location and its PositionPoints."""
    net = prep.network
    for loc in _by_class(list(prep.objects), cim_python_sdk.Location):
        extra = sorted(loc.power_system_resources, key=lambda r: r.mrid)[1:]
        for psr in extra:
            copy = _new(
                prep,
                cim_python_sdk.Location(
                    mrid=make_mrid(net.name, "cgmes_location", f"{loc.mrid}/{psr.mrid}"),
                    name=loc.name,
                    description=loc.description,
                ),
            )
            copy.coordinate_system = loc.coordinate_system
            for pt in sorted(loc.position_points, key=lambda q: q.sequence_number or 0):
                _new(
                    prep,
                    cim_python_sdk.PositionPoint(
                        x_position=pt.x_position,
                        y_position=pt.y_position,
                        z_position=pt.z_position,
                        sequence_number=pt.sequence_number,
                    ),
                ).location = copy
            psr.location = copy
            prep.set_values["Location.copy"] += 1


# --------------------------------------------------------------------------------------
# header, writing
# --------------------------------------------------------------------------------------


def make_cgmes_header(
    wb: Workbook, net: BuiltNetwork, profiles: Iterable[str], created: str | None = None
) -> CgmesHeader:
    """Deterministic header: times from ``created`` (default: source mtime), uuid5 model ids."""
    when = dt.datetime.strptime(created or created_from_mtime(wb.path), "%Y-%m-%dT%H:%M:%SZ")
    when = when.replace(tzinfo=dt.UTC)
    return CgmesHeader(
        created=when,
        scenario_time=when,
        modeling_authority_set=AUTHORITY_SET,
        version="1",
        description=(
            f"CGMES 3.0 model of {wb.stem} (feeder {net.feeder.name}); MV network with LV "
            "equivalents. Load, injection and dispatch values are 0 placeholders (the source has "
            f"none). Source data: {SOURCE_URL} (workbook {wb.path.name}), licence {LICENCE}, "
            "(c) 2024 Team Nando"
        ),
        model_ids={
            kw: str(uuid.uuid5(NAMESPACE, f"{net.name}/cgmes-model/{kw}")) for kw in profiles
        },
    )


def cgmes_network(path: str | Path, *, geographic: bool = False) -> Prepared:
    """Build the workbook and prepare it for CGMES."""
    return prepare(build_network(path), geographic=geographic)


def cgmes_target(out: Path, wb: Workbook, zip_file: bool = False) -> Path:
    """``out/<stem>_CGMES`` (a directory) or ``out/<stem>_CGMES.zip``."""
    return Path(out) / (wb.stem + SUFFIX + (".zip" if zip_file else ""))


def write(
    prep: Prepared,
    wb: Workbook,
    out: Path,
    *,
    profiles: tuple[str, ...] = PROFILES,
    zip_file: bool = False,
    created: str | None = None,
) -> tuple[Path, CgmesReport]:
    """Write the CGMES file set of a prepared network to ``out``; returns the path and report."""
    target = cgmes_target(out, wb, zip_file)
    if target.is_dir():  # files of an earlier run with other profiles would be read as part of it
        for old in target.glob(f"{wb.stem}_*.xml"):
            old.unlink()
    header = make_cgmes_header(wb, prep.network, profiles, created)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # the report carries the same information
        report = write_cgmes(
            prep.objects,  # incl. objects no profile defines: the report lists them as dropped
            target,
            profiles=profiles,
            header=header,
            name=wb.stem,
            file_name="{name}_{keyword}.xml",
            include_reachable=False,
            validate=False,
        )
    return target, report


def dropped_summary(report: CgmesReport) -> Counter[str]:
    """Objects or values the written files do not carry, counted per property or class."""
    out: Counter[str] = Counter()
    for i in report.dropped:
        out[i.property or f"{type(i.object).__name__} (object)"] += 1
    return out


@dataclass
class CgmesExport:
    """Result of :func:`export_cgmes`."""

    workbook: Workbook
    target: Path
    prepared: Prepared
    report: CgmesReport
    profiles: tuple[str, ...]
    errors: list[Any]  # validate_profile errors of the CGMES objects (expected: none)
    warnings: list[Any]  # validate_profile warnings (properties the profiles do not list)
    sizes: dict[str, int]  # keyword -> XML size in bytes

    @property
    def n_objects(self) -> int:
        return len(cgmes_objects(self.prepared.objects, self.profiles))

    @property
    def dropped(self) -> Counter[str]:
        return dropped_summary(self.report)


def export_cgmes(
    wb: Workbook,
    out: Path,
    *,
    profiles: tuple[str, ...] = PROFILES,
    zip_file: bool = False,
    created: str | None = None,
) -> CgmesExport:
    """Build, prepare, validate and write the CGMES file set of one workbook."""
    prep = cgmes_network(wb.path, geographic="GL" in profiles)
    errors, warns = validate(prep, profiles)
    target, report = write(prep, wb, out, profiles=profiles, zip_file=zip_file, created=created)
    return CgmesExport(
        wb, target, prep, report, profiles, errors, warns, file_sizes(target, report)
    )


def file_sizes(target: Path, report: CgmesReport) -> dict[str, int]:
    """Size in bytes of each written XML file (uncompressed when ``target`` is a zip)."""
    if target.suffix == ".zip":
        with zipfile.ZipFile(target) as zf:
            by_name = {i.filename: i.file_size for i in zf.infolist()}
    else:
        by_name = {p.name: p.stat().st_size for p in target.iterdir()}
    return {kw: by_name[name] for kw, name in report.files.items()}


# --------------------------------------------------------------------------------------
# validation and the CGMES view
# --------------------------------------------------------------------------------------


def cgmes_objects(objects: Iterable[CimObject], profiles: Iterable[str]) -> list[CimObject]:
    """The objects of ``objects`` whose class some selected profile defines (the rest cannot be
    written: Feeder, Name, PerLengthSequenceImpedance, ... and GL classes without ``GL``)."""
    selected = [cgmes3.by_keyword(k) for k in profiles]
    return [
        o for o in objects if any(p.has_class(type(o)) and p.is_concrete(type(o)) for p in selected)
    ]


def validate(prep: Prepared, profiles: tuple[str, ...] = PROFILES):
    """``validate_profile`` of the CGMES objects only; returns (errors, warnings)."""
    from cim_python_sdk.profiles import validate_profile

    selected = [cgmes3.by_keyword(k) for k in profiles]
    view = cgmes_objects(prep.objects, profiles)
    issues = validate_profile(view, selected, include_reachable=False)
    return (
        [i for i in issues if i.severity == "error"],
        [i for i in issues if i.severity == "warning"],
    )


def _listed(profiles: list[Any], cls: type) -> set[str]:
    """Python names of the attributes and ends the selected profiles list for ``cls``, including
    those listed under an ancestor in a profile that lacks the class (SSH ``inService``)."""
    names: set[str] = set()
    for p in profiles:
        el = p.element_class(cls)
        if el is not None:
            names.update(i.python_name for i in p.properties(el) if i.python_name)
    return names


def cgmes_view(objects: Iterable[CimObject], profiles: Iterable[str]) -> list[dict[str, Any]]:
    """``canonical_dump``-shaped description of the graph restricted to what the profiles carry:
    objects of profile classes, the attributes and ends the profiles list, and links between
    those objects (an association counts when a profile lists either of its ends). Independent
    of the writer; a read of the written files must equal it."""
    selected = [cgmes3.by_keyword(k) for k in profiles]
    objs = cgmes_objects(collect(list(objects), False), profiles)
    inview = set(objs)
    ids = assign_ids(objs)
    listed: dict[type, set[str]] = {}

    def names(cls: type) -> set[str]:
        if cls not in listed:
            listed[cls] = _listed(selected, cls)
        return listed[cls]

    out = []
    for obj in objs:
        plan = class_plan(type(obj))
        attrs = {}
        for s in plan.attrs:
            v = getattr(obj, s.name, None)
            if v is not None and not s.is_id and s.name in names(type(obj)):
                attrs[s.prop] = encode_value(v)
        links = {}
        for es in plan.ends:
            v = es.desc.__get__(obj)
            targets = v if es.many else (() if v is None else (v,))
            inv = es.desc.inverse.name
            own = es.name in names(type(obj))
            tids = sorted(ids[t] for t in targets if t in inview and (own or inv in names(type(t))))
            if tids:
                links[es.prop] = tids
        out.append({"class": plan.cim_name, "id": ids[obj], "attrs": attrs, "links": links})
    return out


def read_back_equals_view(
    prep: Prepared, target: Path, profiles: tuple[str, ...] = PROFILES
) -> tuple[bool, str, Any]:
    """Read the written file set and compare it with :func:`cgmes_view`.

    Returns (equal, short diff, the CgmesDocument)."""
    from mvlv_cim.verify import describe_diff

    doc = read_cgmes(target)
    got = _canonical(doc.objects)
    want = cgmes_view(prep.objects, profiles)
    return got == want, describe_diff(want, got), doc


def _canonical(objects: Iterable[CimObject]) -> list[dict[str, Any]]:
    from cim_python_sdk.serialization._common import canonical_dump

    return canonical_dump(objects, include_reachable=False)
