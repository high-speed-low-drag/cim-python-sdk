"""End-to-end checks of the CIM models built from the four MV-LV-Networks workbooks."""

from __future__ import annotations

import re
import time
import tracemalloc
from collections import Counter, deque

import openpyxl
from cim_python_sdk import (
    ACLineSegment,
    ConnectivityNode,
    EquivalentInjection,
    ExternalNetworkInjection,
    IdentifiedObject,
    LinearShuntCompensator,
    PowerTransformer,
    RatioTapChanger,
    Substation,
    Terminal,
    VoltageLevel,
)
from conftest import REPORT, network_path

from mvlv_cim.builder import BuiltNetwork, build_network
from mvlv_cim.phases import phase_letters

#: Per-network element counts, as derived from the sheets (lines exclude backend's 'Delete' rows).
EXPECTED = {
    "Network_1_Rural_SMR8": dict(
        line=3611,
        distribution_transformer=704,
        isolating_transformer=10,
        regulator=2,
        inline_transformer=0,
        capacitor=2,
    ),
    "Network_2_Rural_KLO14": dict(
        line=3824,
        distribution_transformer=700,
        isolating_transformer=7,
        regulator=2,
        inline_transformer=1,
        capacitor=2,
    ),
    "Network_3_Urban_HPK11": dict(
        line=593,
        distribution_transformer=44,
        isolating_transformer=0,
        regulator=0,
        inline_transformer=0,
        capacitor=0,
    ),
    "Network_4_Urban_CRE21": dict(
        line=649,
        distribution_transformer=79,
        isolating_transformer=0,
        regulator=0,
        inline_transformer=0,
        capacitor=0,
    ),
}
MVTX_KIND = {
    "InLineTransformer-ISO": "isolating_transformer",
    "InLineTransformer-REG": "regulator",
    "InLineTransformer": "inline_transformer",
}


def sheet_counts(name: str) -> dict[str, int]:
    """Count the element rows straight from the workbook, independently of the loader."""
    wb = openpyxl.load_workbook(network_path(name), read_only=True, data_only=True)
    try:

        def rows(sheet: str) -> list[dict]:
            if sheet not in wb.sheetnames:
                return []
            it = wb[sheet].iter_rows(values_only=True)
            header = next(it)
            return [dict(zip(header, r, strict=False)) for r in it if any(v is not None for v in r)]

        conn_type = {r["Element_ID"]: r["Type"] for r in rows("connections")}
        out = Counter(
            line=sum(1 for r in rows("lines") if str(r["Element_Name"]).lower() != "delete"),
            distribution_transformer=len(rows("lvtx")),
            capacitor=len(rows("mvcaps")),
        )
        for r in rows("mvtx"):
            out[MVTX_KIND[conn_type[r["Element_ID"]]]] += 1
        return {k: out.get(k, 0) for k in EXPECTED[name]}
    finally:
        wb.close()


def of_type[T](built: BuiltNetwork, cls: type[T]) -> list[T]:
    return [o for o in built.objects if isinstance(o, cls)]


def terminal_bv(t: Terminal):
    ce = t.conducting_equipment
    if isinstance(ce, PowerTransformer):
        (end,) = [e for e in ce.power_transformer_end if e.terminal is t]
        return end.base_voltage
    return ce.base_voltage


def bfs(built: BuiltNetwork) -> tuple[set[ConnectivityNode], dict[ConnectivityNode, Terminal]]:
    """Walk node -> terminal -> equipment -> other terminals -> nodes from the source.

    Returns the reached nodes and, per node, the terminal of the equipment that first reached it.
    """
    (src_term,) = built.source.terminals
    start = src_term.connectivity_node
    parent = {start: src_term}
    q = deque([start])
    while q:
        n = q.popleft()
        for t in n.terminals:
            for t2 in t.conducting_equipment.terminals:
                m = t2.connectivity_node
                if t2 is t or m in parent:
                    continue
                parent[m] = t2
                q.append(m)
    return set(parent), parent


def test_element_counts_match_sheets(built: BuiltNetwork) -> None:
    expected = EXPECTED[built.name]
    assert sheet_counts(built.name) == expected
    got = {k: built.element_counts[k] for k in expected}
    assert got == expected
    assert built.element_counts["zone_transformer"] == 1
    assert built.element_counts["source"] == 1
    c = built.counts
    assert c["ACLineSegment"] == expected["line"]
    assert c["LinearShuntCompensator"] == expected["capacitor"]
    n_tx = sum(v for k, v in expected.items() if k.endswith(("transformer", "regulator")))
    assert c["PowerTransformer"] == n_tx + 1
    assert c["PowerTransformerEnd"] == 2 * c["PowerTransformer"]
    REPORT.setdefault(built.name, {})["objects"] = len(built.objects)


def test_one_lv_equivalent_per_distribution_transformer(built: BuiltNetwork) -> None:
    txs = built.elements["distribution_transformer"]
    eis = of_type(built, EquivalentInjection)
    assert len(eis) == len(txs) == EXPECTED[built.name]["distribution_transformer"]
    seen = set()
    for pt in txs:
        (end2,) = [e for e in pt.power_transformer_end if e.end_number == 2]
        lv_node = end2.terminal.connectivity_node
        at_node = [t.conducting_equipment for t in lv_node.terminals]
        injections = [ce for ce in at_node if isinstance(ce, EquivalentInjection)]
        assert len(injections) == 1 and len(at_node) == 2
        ei = injections[0]
        seen.add(ei)
        assert ei.name == f"{pt.name} LV equivalent"
        assert ei.p is None and ei.q is None
        assert ei.regulation_capability is False
        assert ei.base_voltage is end2.base_voltage
        assert ei.terminals[0].phases is end2.terminal.phases
        assert re.fullmatch(
            r"type=(RES|COM); customers=\d+; pvs=(\d+|unknown); lv_feeders=\d+", ei.description
        )
        vl = ei.equipment_container
        assert isinstance(vl, VoltageLevel) and vl.substation is pt.equipment_container
        assert lv_node.connectivity_node_container is vl
    assert seen == set(eis)


def test_containers(built: BuiltNetwork) -> None:
    f = built.feeder
    zone = built.zone_substation
    assert f.normal_energizing_substation is zone
    dist_subs = {pt.equipment_container for pt in built.elements["distribution_transformer"]}
    assert all(isinstance(s, Substation) for s in dist_subs)
    assert set(f.normal_energized_substation) == dist_subs
    assert {vl.base_voltage.nominal_voltage for vl in zone.voltage_levels} == {66000.0, 22000.0}
    assert len(f.normal_head_terminal) == 1
    for s in of_type(built, Substation):
        assert s.region is not None and s.region.region.name == "AusNet"
    for kind in ("line", "isolating_transformer", "regulator", "inline_transformer", "capacitor"):
        assert all(e.equipment_container is f for e in built.elements[kind])


def test_terminals_and_nodes(built: BuiltNetwork) -> None:
    expected_terminals = {
        ACLineSegment: 2,
        PowerTransformer: 2,
        LinearShuntCompensator: 1,
        EquivalentInjection: 1,
        ExternalNetworkInjection: 1,
    }
    for o in built.objects:
        n = next((v for k, v in expected_terminals.items() if isinstance(o, k)), None)
        if n is None:
            continue
        ts = o.terminals
        assert len(ts) == n, o
        assert sorted(t.sequence_number for t in ts) == list(range(1, n + 1))
        for t in ts:
            assert t.phases is not None
            assert t.connectivity_node is not None, t
    for t in of_type(built, Terminal):
        assert t.conducting_equipment is not None and t.connectivity_node is not None
    for pt in of_type(built, PowerTransformer):
        ends = sorted(pt.power_transformer_end, key=lambda e: e.end_number)
        assert [e.end_number for e in ends] == [1, 2]
        assert {e.terminal for e in ends} == set(pt.terminals)
        for e in ends:
            assert e.rated_s and e.rated_u and e.connection_kind is not None
        assert ends[0].r is not None and ends[0].x is not None and ends[0].g is not None


def test_connected_from_source(built: BuiltNetwork) -> None:
    reached, _ = bfs(built)
    nodes = set(of_type(built, ConnectivityNode))
    island_nodes = {built.nodes[b] for isl in built.islands for b in isl}
    unreached = nodes - reached
    # Islands are allowed only when they come from the data (and are reported in issues).
    assert unreached <= island_nodes, sorted(n.name for n in unreached - island_nodes)[:20]
    REPORT.setdefault(built.name, {})["islands"] = [len(i) for i in built.islands]


def test_voltage_consistency(built: BuiltNetwork) -> None:
    for n in of_type(built, ConnectivityNode):
        bvs = {terminal_bv(t) for t in n.terminals}
        container = n.connectivity_node_container
        if isinstance(container, VoltageLevel):
            bvs.add(container.base_voltage)
        assert len(bvs) == 1 and None not in bvs, (n.name, bvs)


def test_phase_consistency(built: BuiltNetwork) -> None:
    """Every terminal entered from upstream carries a subset of the upstream terminal's phases."""
    _, parent = bfs(built)
    order = {n: i for i, n in enumerate(parent)}
    n_swer = 0
    for seg in of_type(built, ACLineSegment) + of_type(built, PowerTransformer):
        terms = list(seg.terminals)
        up = [
            t
            for t in terms
            if t.connectivity_node in parent and parent[t.connectivity_node] is not t
        ]
        if not up:
            continue
        # The upstream terminal is the one whose node was reached via other equipment first.
        t = min(up, key=lambda t: order[t.connectivity_node])
        mine = phase_letters(t.phases)
        theirs = phase_letters(parent[t.connectivity_node].phases)
        assert mine <= theirs, (seg.name, t.phases, parent[t.connectivity_node].phases)
        if isinstance(seg, ACLineSegment) and len(mine) == 1:
            n_swer += 1
            assert [p.phase.name for p in seg.ac_line_segment_phases] == [next(iter(mine))]
    assert n_swer == sum(1 for s in of_type(built, ACLineSegment) if s.ac_line_segment_phases)


def test_mrids_deterministic(built: BuiltNetwork) -> None:
    again = build_network(built.path)

    def ids(b: BuiltNetwork) -> list[tuple[str, str, str | None]]:
        return [
            (type(o).__name__, o.mrid, o.name) for o in b.objects if isinstance(o, IdentifiedObject)
        ]

    first = ids(built)
    assert first == ids(again)
    assert len({m for _, m, _ in first}) == len(first)
    assert [str(i) for i in built.issues] == [str(i) for i in again.issues]


def test_validate(built: BuiltNetwork) -> None:
    quirk = sum(1 for o in built.objects for m in o.validate() if "'instance_set'" in m)
    others = built.validate()
    REPORT.setdefault(built.name, {})["validate"] = f"{len(others)} (+{quirk} instance_set)"
    REPORT[built.name]["issues"] = dict(built.issue_summary())
    assert others == [], others[:20]


def test_build_time_and_memory(built: BuiltNetwork) -> None:
    tracemalloc.start()
    try:
        t0 = time.perf_counter()
        b = build_network(built.path)
        traced_s = time.perf_counter() - t0
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    assert len(b.objects) == len(built.objects)
    REPORT.setdefault(built.name, {})["peak_mib"] = peak / 2**20
    assert REPORT[built.name]["build_s"] < 60
    assert traced_s < 180


def sheet_taps(name: str) -> list[dict]:
    """Transformer rows (lvtx, mvtx) straight from the workbook, with their regulator flag."""
    wb = openpyxl.load_workbook(network_path(name), read_only=True, data_only=True)
    try:
        out = []
        conn_type = {}
        it = wb["connections"].iter_rows(values_only=True)
        header = next(it)
        for r in it:
            d = dict(zip(header, r, strict=False))
            conn_type[d["Element_ID"]] = d["Type"]
        for sheet in ("lvtx", "mvtx"):
            if sheet not in wb.sheetnames:
                continue
            it = wb[sheet].iter_rows(values_only=True)
            header = next(it)
            for r in it:
                d = dict(zip(header, r, strict=False))
                if not any(v is not None for v in r):
                    continue
                d["_reg"] = sheet == "mvtx" and conn_type[d["Element_ID"]].endswith("-REG")
                out.append(d)
        return out
    finally:
        wb.close()


def test_tap_changers_are_faithful(built: BuiltNetwork) -> None:
    rows = sheet_taps(built.name)
    fixed_rows = [
        r
        for r in rows
        if not r["_reg"] and (r["wdg1_numtaps"] or 1) <= 1 and abs((r["wdg1_tap"] or 1) - 1) > 1e-9
    ]
    reg_rows = [r for r in rows if r["_reg"] and (r["wdg1_numtaps"] or 1) > 1]
    tcs = of_type(built, RatioTapChanger)
    fixed, ranged = [], []
    for tc in tcs:
        (fixed if tc.ltc_flag is False else ranged).append(tc)
    # Counts: one tap changer per fixed-tap transformer and per regulator with a range.
    assert len(fixed) == len(fixed_rows)
    assert len(ranged) == len(reg_rows)
    assert len(tcs) == len({tc.mrid for tc in tcs})
    REPORT.setdefault(built.name, {})["tap_changers"] = f"{len(fixed)} fixed + {len(ranged)} reg"
    # No invented ranges.
    for tc in fixed:
        assert (tc.low_step, tc.neutral_step, tc.high_step) == (0, 0, 1)
        assert (tc.normal_step, tc.step) == (1, 1)
        assert tc.description == "fixed off-load tap from sheet (no range given)"
        assert tc.low_step <= tc.neutral_step <= tc.high_step
    # Every fixed tap reproduces rated_u x sheet tap at the current step.
    got = Counter()
    for tc in fixed:
        end = tc.transformer_end
        u = end.rated_u * (1 + tc.step_voltage_increment / 100 * (tc.step - tc.neutral_step))
        assert tc.neutral_u == end.rated_u
        got[(end.power_transformer.name, round(u, 6))] += 1
    want = Counter()
    for r in fixed_rows:
        want[(r["Substation_ID"], round(r["kvs_primary"] * 1000 * r["wdg1_tap"], 6))] += 1
    assert got == want
    # Regulators keep the sheet's range: low <= neutral <= high and the step reproduces the tap.
    for tc in ranged:
        assert tc.low_step <= tc.neutral_step <= tc.high_step
        assert tc.high_step - tc.low_step + 1 == 17
        assert tc.ltc_flag is True
    assert not [i for i in built.issues if i.code == "regulator_no_tap_range"]
