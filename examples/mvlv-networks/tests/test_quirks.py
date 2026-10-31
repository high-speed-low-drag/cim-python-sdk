"""Synthetic workbook with deliberate data problems: the build must not crash and reports them."""

from __future__ import annotations

from pathlib import Path

import openpyxl
import pytest
from cim_python_sdk import ACLineSegment, EquivalentInjection, PhaseCode, RatioTapChanger

from mvlv_cim.builder import build_network
from mvlv_cim.phases import conn_type_phases, lv_secondary_code, node_spec_phases, phase_letters

TX_COLS = [
    "Element_ID",
    "Substation_ID",
    "Bus1",
    "Bus2",
    "Connection_Primary",
    "Connection_Secondary",
    "kvs_primary",
    "kvs_secondary",
    "kvas_primary",
    "kvas_secondary",
    "xhl",
    "loadloss",
    "noloadloss",
    "wdg1_numtaps",
    "wdg1_tap",
    "wdg1_maxtap",
    "wdg1_mintap",
    "Conn_Type",
]
LINE_COLS = [
    "Line_Number",
    "Start_Node",
    "Start_Node_Phase",
    "End_Node",
    "End_Node_Phase",
    "Phases",
    "Length",
    "Units",
    "Linecode",
    "Element_Name",
    "Element_ID",
]
LC_COLS = [
    "Linecode_ID",
    "Phases",
    "r1",
    "x1",
    "b1",
    "r0",
    "x0",
    "b0",
    "Units",
    "Ampacity1",
    "Ampacity2",
]


def write(path: Path, sheets: dict[str, list[list]]) -> Path:
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    for name, rows in sheets.items():
        ws = wb.create_sheet(name)
        for r in rows:
            ws.append(r)
    wb.save(path)
    return path


@pytest.fixture
def quirky(tmp_path: Path) -> Path:
    return write(
        tmp_path / "Network_9_Quirky.xlsx",
        {
            "buscoords": [["Node_ID", "NodeStartX", "NodeStartY"]]
            + [[i, float(i), float(i)] for i in range(1, 9)]
            + [[99, 0.0, 0.0], [3, 5.0, 5.0]],  # orphan 99, duplicate 3
            "connections": [
                [
                    "Element_ID",
                    "Start_Node",
                    "End_Node",
                    "Length",
                    "Units",
                    "Type",
                    "Name",
                    "Xcor1",
                    "Ycor1",
                    "Xcor2",
                    "Ycor2",
                    "PhaseNum",
                ],
                [5, 2, 3, 0, "km", "InLineTransformer-REG", "REG_X", 0, 0, 0, 0, 3],
            ],
            "lines": [
                LINE_COLS,
                [0, 1, "1.2.3", 2, "1.2.3", 3, 0.5, "km", 7, "A", 10],
                [1, 2, "1.2.3", 3, "1.2.3", 3, 0.0, "km", 7, "B", 11],  # zero length
                [2, 3, "1.2.3", 4, "1.2.3", 3, 0.2, "km", 42, "C", 11],  # dup id, no lc
                [3, 4, "1.2.3", 5, "1.2.3", 3, 0.1, "km", 7, "Delete", 13],
                [4, 7, "1.2.3", 8, "1.2.3", 3, 0.1, "km", 7, "D", 14],  # island 7-8
                [5, 2, "9", 6, "9", 1, 0.1, "km", 7, "E", 15],
            ],  # bad phase spec
            "linecodes": [
                LC_COLS,
                ["7-3ph", 3, 0.2, 0.3, 3.0, 0.4, 0.9, 2.0, "km", 300, 250],
                ["7-1ph", 1, 0.2, 0.3, 3.0, 0.4, 0.9, 2.0, "km", 300, 250],
            ],
            "lvtx": [
                [*TX_COLS, "Type", "Customers", "PVs", "Feeders"],
                [
                    None,
                    "SUB_A",
                    2,
                    0,
                    "delta",
                    "wye",
                    22,
                    0.433,
                    100,
                    100,
                    4,
                    1,
                    0.1,
                    1,
                    1.05,
                    1,
                    1,
                    "RWB",
                    "RES",
                    12,
                    "Null",
                    2,
                ],
                [
                    21,
                    "SUB_B",
                    3,
                    0,
                    "delta",
                    "wye",
                    22,
                    0.433,
                    50,
                    50,
                    4,
                    1,
                    0.1,
                    1,
                    1,
                    1,
                    1,
                    "RX",
                    "COM",
                    "many",
                    3,
                    1,
                ],
            ],
            "mvtx": [
                TX_COLS,
                [
                    5,
                    "REG_X",
                    2,
                    3,
                    "wye",
                    "wye",
                    22,
                    22,
                    1000,
                    1000,
                    0.1,
                    0.1,
                    0.1,
                    1,
                    1,
                    1,
                    1,
                    "RWB",
                ],
            ],
            "mv_net_txs": [
                TX_COLS,
                [
                    1,
                    "ZONE",
                    "SourceBus",
                    1,
                    "delta",
                    "wye",
                    66,
                    22,
                    10000,
                    10000,
                    0.1,
                    0.1,
                    0.1,
                    1,
                    1,
                    1,
                    1,
                    "RWB",
                ],
            ],
        },
    )


def test_quirky_workbook_builds_and_reports(quirky: Path) -> None:
    b = build_network(quirky)
    codes = b.issue_summary()
    for code in (
        "zero_length",
        "missing_linecode",
        "duplicate_element_id",
        "deleted_lines_skipped",
        "island",
        "orphan_buscoords",
        "duplicate_buscoord",
        "missing_element_id",
        "bad_phase_spec",
        "bad_conn_type",
        "bad_value",
        "pvs_null",
        "regulator_no_tap_range",
    ):
        assert codes[code] >= 1, (code, codes)
    assert b.element_counts["line"] == 5
    assert b.element_counts["distribution_transformer"] == 2
    assert len([o for o in b.objects if isinstance(o, EquivalentInjection)]) == 2
    no_lc = [
        s for s in b.objects if isinstance(s, ACLineSegment) and s.per_length_impedance is None
    ]
    assert [s.name for s in no_lc] == ["C"]
    assert len({o.mrid for o in b.objects if hasattr(o, "mrid")}) == sum(
        1 for o in b.objects if hasattr(o, "mrid")
    )
    assert b.element_counts["regulator"] == 1
    # The regulator has no range: no invented tap changer.  SUB_A's fixed 1.05 tap is exact.
    tcs = [o for o in b.objects if isinstance(o, RatioTapChanger)]
    assert [tc.transformer_end.power_transformer.name for tc in tcs] == ["SUB_A"]
    assert (tcs[0].low_step, tcs[0].neutral_step, tcs[0].high_step) == (0, 0, 1)
    assert b.islands and sorted(b.islands[0]) == [7, 8]
    assert b.validate() == []


def test_phase_helpers() -> None:
    assert conn_type_phases("BWR") == "ABC"
    assert conn_type_phases("BR") == "AC"
    assert conn_type_phases("W") == "B"
    assert conn_type_phases("RX") is None and conn_type_phases("RR") is None
    assert node_spec_phases("1.2.3") == "ABC" and node_spec_phases("1") == "A"
    assert node_spec_phases(3) == "C" and node_spec_phases("4") is None
    assert lv_secondary_code(2) is PhaseCode.s12N and lv_secondary_code(1) is PhaseCode.s1N
    assert phase_letters(PhaseCode.ABCN) == {"A", "B", "C"}
    assert phase_letters(PhaseCode.s12N) == {"s1", "s2"}
