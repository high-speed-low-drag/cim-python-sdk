"""Export and round-trip tests. N1 and N2 only run with MVLV_FULL=1 (about a minute each)."""

from __future__ import annotations

import os

import pytest
from cim_python_sdk.serialization import read_cimxml, read_jsonld
from conftest import DATA_DIR

from mvlv_cim.cli import main
from mvlv_cim.export import LICENCE, SOURCE_URL, find_workbooks
from mvlv_cim.verify import verify_network

FULL = os.environ.get("MVLV_FULL") == "1"
CASES = [
    pytest.param(1, marks=pytest.mark.skipif(not FULL, reason="set MVLV_FULL=1")),
    pytest.param(2, marks=pytest.mark.skipif(not FULL, reason="set MVLV_FULL=1")),
    3,
    4,
]


@pytest.mark.parametrize("number", CASES)
def test_round_trip(number, tmp_path):
    if not DATA_DIR.exists():
        pytest.skip("MV-LV-Networks not found")
    (wb,) = find_workbooks(DATA_DIR, [number])
    r = verify_network(wb, tmp_path)
    for fmt, fr in r.formats.items():
        assert fr.equal, f"{fmt}: {fr.diff}"
        assert fr.deterministic, fmt
        assert fr.warnings == [], fmt
        assert fr.dangling == 0, fmt
        assert fr.size > 0
    assert r.cross_equal
    assert r.ok
    assert sum(r.counts.values()) == r.n_objects


@pytest.mark.parametrize("number", [3, 4])
def test_cli_export_header_and_determinism(number, tmp_path):
    if not DATA_DIR.exists():
        pytest.skip("MV-LV-Networks not found")
    a, b = tmp_path / "a", tmp_path / "b"
    args = ["export", "--network", str(number), "--source", str(DATA_DIR)]
    assert main([*args, "--out", str(a), "--created", "2024-01-02T03:04:05Z"]) == 0
    assert main([*args, "--out", str(b), "--created", "2024-01-02T03:04:05Z"]) == 0
    files = sorted(p.name for p in a.iterdir())
    assert len(files) == 2 and {p.suffix for p in a.iterdir()} == {".xml", ".jsonld"}
    for name in files:
        assert (a / name).read_bytes() == (b / name).read_bytes()
    xml = next(a.glob("*.xml"))
    for doc in (read_cimxml(xml), read_jsonld(next(a.glob("*.jsonld")))):
        text = repr(doc.header)
        assert doc.header is not None
        assert "2024-01-02T03:04:05" in text
        assert SOURCE_URL in text and LICENCE in text
        assert "urn:x-mvlv-cim:authority" in text
        assert doc.warnings == [] and doc.dangling == []


def test_cli_single_format(tmp_path):
    if not DATA_DIR.exists():
        pytest.skip("MV-LV-Networks not found")
    main(
        [
            "export",
            "-n",
            "3",
            "--format",
            "jsonld",
            "--out",
            str(tmp_path),
            "--source",
            str(DATA_DIR),
        ]
    )
    assert [p.suffix for p in tmp_path.iterdir()] == [".jsonld"]
