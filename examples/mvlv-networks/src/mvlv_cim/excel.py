"""Typed loading of the MV-LV-Networks workbooks.

The workbooks are treated as untrusted input: cells are read as values only (``data_only``), every
field is coerced to the expected type, and anything that does not fit is recorded as an
:class:`Issue` and replaced by ``None`` instead of raising. The ``lv_lines`` and ``lv_loads`` sheets
are never read (LV is represented by an equivalent injection, see the README).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import openpyxl

SHEETS = (
    "buscoords",
    "connections",
    "lines",
    "linecodes",
    "lvtx",
    "mvtx",
    "mvcaps",
    "mv_net_txs",
)
OPTIONAL_SHEETS = frozenset({"mvtx", "mvcaps"})


@dataclass(frozen=True)
class Issue:
    """A data problem found and handled while loading or building."""

    code: str
    message: str
    sheet: str | None = None
    source_id: str | None = None

    def __str__(self) -> str:
        where = self.sheet or ""
        if self.source_id is not None:
            where += f"[{self.source_id}]"
        return f"{self.code}: {where}: {self.message}" if where else f"{self.code}: {self.message}"


@dataclass(frozen=True)
class BusCoord:
    node_id: int
    x: float | None
    y: float | None


@dataclass(frozen=True)
class Connection:
    element_id: int | None
    start_node: int | str | None
    end_node: int | str | None
    length_km: float | None
    type: str | None
    name: str | None
    x1: float | None
    y1: float | None
    x2: float | None
    y2: float | None
    phase_num: int | None


@dataclass(frozen=True)
class Line:
    row: int
    line_number: int | None
    element_id: int | None
    element_name: str | None
    start_node: int | None
    start_node_phase: str | None
    end_node: int | None
    end_node_phase: str | None
    phases: int | None
    length: float | None
    units: str | None
    linecode: str | None

    @property
    def linecode_id(self) -> str | None:
        """The ``linecodes.Linecode_ID`` this line uses (backend: ``f"{Linecode}-{Phases}ph"``)."""
        if self.linecode is None or self.phases is None:
            return None
        return f"{self.linecode}-{self.phases}ph"

    @property
    def deleted(self) -> bool:
        """Rows named ``Delete`` are skipped by backend.py and therefore by the builder."""
        return (self.element_name or "").strip().lower() == "delete"


@dataclass(frozen=True)
class LineCode:
    row: int
    linecode_id: str
    phases: int | None
    r1: float | None
    x1: float | None
    b1: float | None
    r0: float | None
    x0: float | None
    b0: float | None
    units: str | None
    ampacity1: float | None
    ampacity2: float | None
    full_name_code: str | None
    material: str | None
    size: str | None


@dataclass(frozen=True)
class Transformer:
    """A row of ``lvtx``, ``mvtx`` or ``mv_net_txs`` (they share their columns)."""

    sheet: str
    row: int
    element_id: int | None
    substation_id: str | None
    bus1: int | str | None
    bus2: int | str | None
    connection_primary: str | None
    connection_secondary: str | None
    kv_primary: float | None
    kv_secondary: float | None
    kva_primary: float | None
    kva_secondary: float | None
    xhl: float | None
    loadloss: float | None
    noloadloss: float | None
    numtaps: int | None
    tap: float | None
    maxtap: float | None
    mintap: float | None
    conn_type: str | None
    # lvtx only
    type: str | None = None
    customers: int | None = None
    pvs: int | None = None
    feeders: int | None = None


@dataclass(frozen=True)
class Capacitor:
    row: int
    element_id: int | None
    name: str | None
    bus1: int | None
    phases: int | None
    kv: float | None
    kvar: float | None


@dataclass
class NetworkData:
    path: Path
    buscoords: list[BusCoord] = field(default_factory=list)
    connections: list[Connection] = field(default_factory=list)
    lines: list[Line] = field(default_factory=list)
    linecodes: list[LineCode] = field(default_factory=list)
    lvtx: list[Transformer] = field(default_factory=list)
    mvtx: list[Transformer] = field(default_factory=list)
    mvcaps: list[Capacitor] = field(default_factory=list)
    mv_net_txs: list[Transformer] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)


class _Row:
    """One sheet row with typed getters; bad cells become ``None`` plus an Issue."""

    __slots__ = ("idx", "issues", "sheet", "values")

    def __init__(self, sheet: str, idx: int, values: dict[str, Any], issues: list[Issue]):
        self.sheet = sheet
        self.idx = idx
        self.values = values
        self.issues = issues

    def _bad(self, col: str, value: Any, want: str) -> None:
        self.issues.append(
            Issue(
                "bad_value",
                f"column {col!r}: {value!r} is not {want}; treated as missing",
                self.sheet,
                f"row {self.idx}",
            )
        )

    def raw(self, col: str) -> Any:
        v = self.values.get(col)
        if isinstance(v, str):
            v = v.strip()
            if v == "":
                return None
        return v

    def as_float(self, col: str) -> float | None:
        v = self.raw(col)
        if v is None or isinstance(v, bool):
            return None
        if isinstance(v, (int, float)):
            return float(v)
        try:
            return float(v)
        except (TypeError, ValueError):
            self._bad(col, v, "a number")
            return None

    def as_int(self, col: str) -> int | None:
        v = self.raw(col)
        if v is None or isinstance(v, bool):
            return None
        if isinstance(v, int):
            return v
        if isinstance(v, float) and v.is_integer():
            return int(v)
        if isinstance(v, str):
            try:
                return int(v)
            except ValueError:
                pass
        self._bad(col, v, "an integer")
        return None

    def as_str(self, col: str) -> str | None:
        v = self.raw(col)
        if v is None:
            return None
        if isinstance(v, float) and v.is_integer():
            v = int(v)
        return str(v)

    def as_node(self, col: str) -> int | str | None:
        """A bus reference: an integer node id, or a name such as ``SourceBus``."""
        v = self.raw(col)
        if v is None:
            return None
        if isinstance(v, int) and not isinstance(v, bool):
            return v
        if isinstance(v, float) and v.is_integer():
            return int(v)
        if isinstance(v, str):
            return int(v) if v.isdigit() else v
        self._bad(col, v, "a bus reference")
        return None


def _rows(wb: Any, sheet: str, issues: list[Issue]) -> list[_Row]:
    ws = wb[sheet]
    it = ws.iter_rows(values_only=True)
    header = next(it, None)
    if header is None:
        return []
    cols = [str(h).strip() if h is not None else "" for h in header]
    out = []
    for i, values in enumerate(it, start=2):  # spreadsheet row number
        if values is None or all(v is None for v in values):
            continue
        out.append(_Row(sheet, i, dict(zip(cols, values, strict=False)), issues))
    return out


def _transformer(r: _Row, lv: bool) -> Transformer:
    pvs = r.raw("PVs") if lv else None
    pv_value: int | None = None
    if lv:
        if isinstance(pvs, str) and pvs.lower() == "null":
            r.issues.append(
                Issue(
                    "pvs_null",
                    "PVs is 'Null'; left unknown",
                    r.sheet,
                    r.as_str("Substation_ID"),
                )
            )
        else:
            pv_value = r.as_int("PVs")
    return Transformer(
        sheet=r.sheet,
        row=r.idx,
        element_id=r.as_int("Element_ID"),
        substation_id=r.as_str("Substation_ID"),
        bus1=r.as_node("Bus1"),
        bus2=r.as_node("Bus2"),
        connection_primary=r.as_str("Connection_Primary"),
        connection_secondary=r.as_str("Connection_Secondary"),
        kv_primary=r.as_float("kvs_primary"),
        kv_secondary=r.as_float("kvs_secondary"),
        kva_primary=r.as_float("kvas_primary"),
        kva_secondary=r.as_float("kvas_secondary"),
        xhl=r.as_float("xhl"),
        loadloss=r.as_float("loadloss"),
        noloadloss=r.as_float("noloadloss"),
        numtaps=r.as_int("wdg1_numtaps"),
        tap=r.as_float("wdg1_tap"),
        maxtap=r.as_float("wdg1_maxtap"),
        mintap=r.as_float("wdg1_mintap"),
        conn_type=r.as_str("Conn_Type"),
        type=r.as_str("Type") if lv else None,
        customers=r.as_int("Customers") if lv else None,
        pvs=pv_value,
        feeders=r.as_int("Feeders") if lv else None,
    )


def load_network(path: str | Path) -> NetworkData:
    """Read the sheets the builder needs from one ``Network_*.xlsx`` workbook."""
    path = Path(path)
    data = NetworkData(path=path)
    issues = data.issues
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        present = set(wb.sheetnames)
        for sheet in SHEETS:
            if sheet not in present:
                if sheet not in OPTIONAL_SHEETS:
                    issues.append(Issue("missing_sheet", "sheet not found", sheet))
                continue
            rows = _rows(wb, sheet, issues)
            if sheet == "buscoords":
                for r in rows:
                    nid = r.as_int("Node_ID")
                    if nid is None:
                        issues.append(Issue("missing_id", "no Node_ID", sheet, f"row {r.idx}"))
                        continue
                    data.buscoords.append(
                        BusCoord(nid, r.as_float("NodeStartX"), r.as_float("NodeStartY"))
                    )
            elif sheet == "connections":
                for r in rows:
                    data.connections.append(
                        Connection(
                            element_id=r.as_int("Element_ID"),
                            start_node=r.as_node("Start_Node"),
                            end_node=r.as_node("End_Node"),
                            length_km=r.as_float("Length"),
                            type=r.as_str("Type"),
                            name=r.as_str("Name"),
                            x1=r.as_float("Xcor1"),
                            y1=r.as_float("Ycor1"),
                            x2=r.as_float("Xcor2"),
                            y2=r.as_float("Ycor2"),
                            phase_num=r.as_int("PhaseNum"),
                        )
                    )
            elif sheet == "lines":
                for r in rows:
                    start, end = r.as_node("Start_Node"), r.as_node("End_Node")
                    data.lines.append(
                        Line(
                            row=r.idx,
                            line_number=r.as_int("Line_Number"),
                            element_id=r.as_int("Element_ID"),
                            element_name=r.as_str("Element_Name"),
                            start_node=start if isinstance(start, int) else None,
                            start_node_phase=r.as_str("Start_Node_Phase"),
                            end_node=end if isinstance(end, int) else None,
                            end_node_phase=r.as_str("End_Node_Phase"),
                            phases=r.as_int("Phases"),
                            length=r.as_float("Length"),
                            units=r.as_str("Units"),
                            linecode=r.as_str("Linecode"),
                        )
                    )
            elif sheet == "linecodes":
                for r in rows:
                    lid = r.as_str("Linecode_ID")
                    if lid is None:
                        issues.append(Issue("missing_id", "no Linecode_ID", sheet, f"row {r.idx}"))
                        continue
                    data.linecodes.append(
                        LineCode(
                            row=r.idx,
                            linecode_id=lid,
                            phases=r.as_int("Phases"),
                            r1=r.as_float("r1"),
                            x1=r.as_float("x1"),
                            b1=r.as_float("b1"),
                            r0=r.as_float("r0"),
                            x0=r.as_float("x0"),
                            b0=r.as_float("b0"),
                            units=r.as_str("Units"),
                            ampacity1=r.as_float("Ampacity1"),
                            ampacity2=r.as_float("Ampacity2"),
                            full_name_code=r.as_str("Full_Name_Code"),
                            material=r.as_str("Material"),
                            size=r.as_str("Size"),
                        )
                    )
            elif sheet in ("lvtx", "mvtx", "mv_net_txs"):
                getattr(data, sheet).extend(_transformer(r, sheet == "lvtx") for r in rows)
            elif sheet == "mvcaps":
                for r in rows:
                    bus = r.as_node("Bus1")
                    data.mvcaps.append(
                        Capacitor(
                            row=r.idx,
                            element_id=r.as_int("Element_ID"),
                            name=r.as_str("Name"),
                            bus1=bus if isinstance(bus, int) else None,
                            phases=r.as_int("phases"),
                            kv=r.as_float("kvs"),
                            kvar=r.as_float("kvar"),
                        )
                    )
    finally:
        wb.close()
    return data
