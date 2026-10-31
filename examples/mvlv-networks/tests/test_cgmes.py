"""CGMES 3.0 export: valid against EQ/SSH/TP, round trip, what is and is not carried.

N1 and N2 only run with MVLV_FULL=1 (a few seconds each), like the other export tests.
"""

from __future__ import annotations

import os
import zipfile
from collections import Counter

import pytest
from cim_python_sdk import (
    ACLineSegment,
    BaseVoltage,
    ConnectivityNode,
    EquivalentInjection,
    ExternalNetworkInjection,
    OperationalLimitSet,
    PowerTransformerEnd,
    Terminal,
    TopologicalNode,
)
from cim_python_sdk.profiles import cgmes3, validate_profile
from cim_python_sdk.serialization import read_cgmes
from cim_python_sdk.serialization._common import canonical_dump
from conftest import DATA_DIR

from mvlv_cim import cgmes
from mvlv_cim.builder import build_network
from mvlv_cim.cli import main
from mvlv_cim.export import AUTHORITY_SET, LICENCE, SOURCE_URL, find_workbooks
from mvlv_cim.verify import verify_cgmes, verify_network

FULL = os.environ.get("MVLV_FULL") == "1"
CASES = [
    pytest.param(1, marks=pytest.mark.skipif(not FULL, reason="set MVLV_FULL=1")),
    pytest.param(2, marks=pytest.mark.skipif(not FULL, reason="set MVLV_FULL=1")),
    3,
    4,
]
CREATED = "2024-01-02T03:04:05Z"

pytestmark = pytest.mark.skipif(not DATA_DIR.exists(), reason="MV-LV-Networks not found")


def workbook(number: int):
    (wb,) = find_workbooks(DATA_DIR, [number])
    return wb


@pytest.fixture(scope="module")
def n3(tmp_path_factory):
    """Network 3, exported once: (CgmesExport, directory)."""
    out = tmp_path_factory.mktemp("n3")
    return cgmes.export_cgmes(workbook(3), out, created=CREATED)


# --------------------------------------------------------------------------------------
# validity and round trip
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("number", CASES)
def test_valid_round_trip_deterministic(number, tmp_path):
    check = verify_cgmes(workbook(number), tmp_path, created=CREATED)
    assert check.errors == []  # validate_profile against EQ, SSH, TP
    assert check.equal, check.diff
    assert check.deterministic
    assert check.read_warnings == []
    assert check.dangling == 0
    assert set(check.sizes) == {"EQ", "SSH", "TP"} and all(check.sizes.values())
    assert check.ok


@pytest.mark.parametrize("number", [3, 4])
def test_geographic_profile(number, tmp_path):
    check = verify_cgmes(workbook(number), tmp_path, cgmes.GL_PROFILES, CREATED)
    assert check.ok, (check.errors[:3], check.diff)
    assert set(check.sizes) == {"EQ", "SSH", "TP", "GL"}
    for key in ("PositionPoint (object)", "Location (object)", "CoordinateSystem (object)"):
        assert key not in check.dropped  # carried by GL
    assert "Name (object)" in check.dropped


def test_verify_network_includes_cgmes(tmp_path):
    r = verify_network(workbook(3), tmp_path, created=CREATED, cgmes_profiles=cgmes.PROFILES)
    assert r.cgmes is not None and r.cgmes.ok and r.ok


def test_plain_build_is_not_cgmes_and_stays_plain():
    wb = workbook(3)
    plain = build_network(wb.path)
    issues = validate_profile(plain.objects, cgmes3.profile_set.by_keyword("EQ"))
    missing = {(i.object.__class__.__name__, i.property) for i in issues if i.severity == "error"}
    assert ("ACLineSegment", "ACLineSegment.r") in missing
    assert not [o for o in plain.objects if isinstance(o, TopologicalNode)]
    before = Counter(type(o).__name__ for o in plain.objects)
    prep = cgmes.prepare(build_network(wb.path))
    assert Counter(type(o).__name__ for o in plain.objects) == before  # separate builds
    assert Counter(type(o).__name__ for o in prep.objects) != before


# --------------------------------------------------------------------------------------
# what prepare does
# --------------------------------------------------------------------------------------


def test_topological_nodes_one_to_one(n3):
    objs = n3.prepared.objects
    nodes = [o for o in objs if isinstance(o, ConnectivityNode)]
    tns = [o for o in objs if isinstance(o, TopologicalNode)]
    assert len(nodes) == len(tns) == 639
    assert all(len(n.topological_node.connectivity_nodes) == 1 for n in nodes)
    assert all(t.topological_node is not None for t in objs if isinstance(t, Terminal))
    assert all(tn.base_voltage is not None and tn.connectivity_node_container for tn in tns)
    assert n3.prepared.added["TopologicalNode"] == 639


def test_every_transformer_node_is_in_its_substation(n3):
    from cim_python_sdk import PowerTransformer, Substation, VoltageLevel

    for tr in (o for o in n3.prepared.objects if isinstance(o, PowerTransformer)):
        assert isinstance(tr.equipment_container, Substation)
        for t in tr.terminals:
            vl = t.connectivity_node.connectivity_node_container
            assert isinstance(vl, VoltageLevel) and vl.substation is tr.equipment_container


def test_feeder_becomes_a_line_container(n3):
    from cim_python_sdk import Line

    net = n3.prepared.network
    (line,) = [o for o in net.objects if isinstance(o, Line)]
    assert line.name == net.feeder.name
    assert not net.feeder.equipments and not net.feeder.connectivity_nodes
    # the 44 nodes of the distribution transformers moved on into their substations' voltage levels
    assert len(line.equipments) == 593 and len(line.connectivity_nodes) == 593 - 44


def test_units_si_in_graph_cgmes_in_files(n3):
    # the graph keeps the builder's SI values; write_cgmes scales them to kV, MVA and km
    objs = n3.prepared.objects
    assert sorted(b.nominal_voltage for b in objs if isinstance(b, BaseVoltage)) == [
        240.0,
        433.0,
        12700.0,
        22000.0,
        66000.0,
    ]
    plain = build_network(workbook(3).path)
    plain_by_mrid = {o.mrid: o for o in plain.objects if isinstance(o, ACLineSegment)}
    for seg in (o for o in objs if isinstance(o, ACLineSegment)):
        src = plain_by_mrid[seg.mrid]
        length_m, pli = src.length, src.per_length_impedance
        assert seg.length == length_m
        assert seg.r == pytest.approx(pli.r * length_m)  # ohm
        assert seg.bch == pytest.approx(pli.bch * length_m)
    raw = read_cgmes(n3.target, units="cgmes").objects  # the numbers as written
    assert sorted(b.nominal_voltage for b in raw if isinstance(b, BaseVoltage)) == [
        0.24,
        0.433,
        12.7,
        22.0,
        66.0,
    ]
    by_mrid = {o.mrid: o for o in objs if isinstance(o, ACLineSegment)}
    for seg in (o for o in raw if isinstance(o, ACLineSegment)):
        assert seg.length == pytest.approx(by_mrid[seg.mrid].length / 1000)  # km
    for end in (o for o in raw if isinstance(o, PowerTransformerEnd)):
        assert end.rated_u in (66.0, 22.9, 22.0, 12.7, 0.433, 0.24)  # kV
        assert 0 < end.rated_s <= 100  # MVA


def test_placeholders_are_zero_and_documented(n3):
    objs = n3.prepared.objects
    eis = [o for o in objs if isinstance(o, EquivalentInjection)]
    assert len(eis) == 44 and all(e.p == 0 and e.q == 0 for e in eis)
    (src,) = [o for o in objs if isinstance(o, ExternalNetworkInjection)]
    for name in ("p", "q", "min_p", "max_p", "min_q", "max_q", "governor_scd"):
        assert getattr(src, name) == 0
    assert src.reference_priority == 1
    assert (
        "placeholder"
        in cgmes.make_cgmes_header(workbook(3), n3.prepared.network, cgmes.PROFILES).description
    )


def test_limit_sets_on_both_terminals(n3):
    sets = [o for o in n3.prepared.objects if isinstance(o, OperationalLimitSet)]
    assert len(sets) == 2 * 593
    by_line = Counter(s.equipment for s in sets)
    assert set(by_line.values()) == {2}
    for s in sets:
        assert s.terminal is not None and s.terminal.conducting_equipment is s.equipment
        (limit,) = s.operational_limit_value
        assert limit.value > 0
    assert len({s.terminal for s in sets}) == len(sets)


# --------------------------------------------------------------------------------------
# what CGMES cannot carry
# --------------------------------------------------------------------------------------


def test_dropped_is_reported(n3):
    d = n3.dropped
    assert d["PositionPoint (object)"] == 1231
    assert d["Location (object)"] == 638 and d["PowerSystemResource.Location"] == 728
    assert d["Name (object)"] == 638 and d["IdentifiedObject.Names"] == 638
    assert d["PerLengthSequenceImpedance (object)"] == 10
    assert d["ACLineSegment.PerLengthImpedance"] == 593
    assert d["PowerTransformer.vectorGroup"] == 45
    assert d["PowerTransformerEnd.phaseAngleClock"] == 90
    assert d["TransformerEnd.grounded"] == 45
    assert d["Feeder (object)"] == 1 and d["Terminal.NormalHeadFeeder"] == 1
    assert d["ExternalNetworkInjection.maxInitialSymShCCurrent"] == 1
    assert "ACLineSegmentPhase (object)" not in d  # N3 has no single-phase lines
    assert n3.errors == [] and len(n3.warnings) == 2190


@pytest.mark.skipif(not FULL, reason="set MVLV_FULL=1")
def test_single_phase_sections_lose_their_phase_objects(tmp_path):
    res = cgmes.export_cgmes(workbook(1), tmp_path, created=CREATED)
    assert res.dropped["ACLineSegmentPhase (object)"] == 1059
    assert res.dropped["ACLineSegment.ACLineSegmentPhases"] == 1059
    assert res.errors == []
    # the phase itself survives as Terminal.phases
    doc = read_cgmes(res.target)
    single = [
        t
        for t in doc.objects
        if isinstance(t, Terminal) and t.phases is not None and t.phases.value == "A"
    ]
    assert single


def test_view_is_a_strict_subset_of_the_graph(n3):
    full = {d["id"]: d for d in canonical_dump(n3.prepared.objects, include_reachable=False)}
    view = {d["id"]: d for d in cgmes.cgmes_view(n3.prepared.objects, cgmes.PROFILES)}
    assert 0 < len(view) < len(full)
    line = next(i for i, d in view.items() if d["class"] == "ACLineSegment")
    assert "ACLineSegment.PerLengthImpedance" in full[line]["links"]
    assert "ACLineSegment.PerLengthImpedance" not in view[line]["links"]
    assert "ACLineSegment.r" in view[line]["attrs"]


# --------------------------------------------------------------------------------------
# files, headers, CLI
# --------------------------------------------------------------------------------------


def test_cli_export_cgmes_directory_and_zip(tmp_path):
    base = ["export", "-n", "3", "--source", str(DATA_DIR), "--created", CREATED]
    a, b = tmp_path / "a", tmp_path / "b"
    assert main([*base, "--format", "cgmes", "--out", str(a)]) == 0
    assert main([*base, "--format", "cgmes", "--zip", "--out", str(b)]) == 0
    folder = a / "Network_3_Urban_HPK11_CGMES"
    assert sorted(p.name for p in folder.iterdir()) == [
        "Network_3_Urban_HPK11_EQ.xml",
        "Network_3_Urban_HPK11_SSH.xml",
        "Network_3_Urban_HPK11_TP.xml",
    ]
    archive = b / "Network_3_Urban_HPK11_CGMES.zip"
    with zipfile.ZipFile(archive) as zf:
        assert sorted(zf.namelist()) == sorted(p.name for p in folder.iterdir())
        for p in folder.iterdir():
            assert zf.read(p.name) == p.read_bytes()  # same bytes in the zip
    assert canonical_dump(read_cgmes(folder).objects) == canonical_dump(read_cgmes(archive).objects)


def test_cli_format_all_writes_every_format(tmp_path):
    args = ["export", "-n", "3", "--source", str(DATA_DIR), "--format", "all", "--out"]
    assert main([*args, str(tmp_path)]) == 0
    assert sorted(p.name for p in tmp_path.iterdir()) == [
        "Network_3_Urban_HPK11.jsonld",
        "Network_3_Urban_HPK11.xml",
        "Network_3_Urban_HPK11_CGMES",
    ]


def test_cli_verify_cgmes(tmp_path, capsys):
    args = ["verify", "-n", "3", "--cgmes", "--source", str(DATA_DIR), "--out", str(tmp_path)]
    assert main(args) == 0
    assert "cgmes   EQ+SSH+TP" in capsys.readouterr().out


def test_cli_gl_replaces_old_files(tmp_path):
    """A GL run followed by a plain run in the same directory must not leave the GL file."""
    args = ["export", "-n", "3", "--source", str(DATA_DIR), "--format", "cgmes", "--out"]
    assert main([*args, str(tmp_path), "--gl"]) == 0
    folder = tmp_path / "Network_3_Urban_HPK11_CGMES"
    assert len(list(folder.iterdir())) == 4
    assert main([*args, str(tmp_path)]) == 0
    assert len(list(folder.iterdir())) == 3


def test_headers(n3):
    doc = read_cgmes(n3.target)
    wb = workbook(3)
    assert set(doc.headers) == {"Network_3_Urban_HPK11_EQ.xml", "Network_3_Urban_HPK11_SSH.xml",
                                "Network_3_Urban_HPK11_TP.xml"}  # fmt: skip
    ids = {}
    for name, h in doc.headers.items():
        kw = name.rsplit("_", 1)[1][:-4]
        ids[kw] = h.model_id
        assert h.modeling_authority_set == AUTHORITY_SET
        assert h.created.strftime("%Y-%m-%dT%H:%M:%SZ") == CREATED
        assert h.scenario_time == h.created
        assert SOURCE_URL in h.description and LICENCE in h.description
        assert wb.path.name in h.description
        assert h.profile_uris == (cgmes3.profile_set.by_keyword(kw).uri,)
    assert doc.headers["Network_3_Urban_HPK11_SSH.xml"].dependent_on == (ids["EQ"],)
    assert doc.headers["Network_3_Urban_HPK11_TP.xml"].dependent_on == (ids["SSH"],)
    assert doc.headers["Network_3_Urban_HPK11_EQ.xml"].dependent_on == ()
    assert len(set(ids.values())) == 3 and all(i.startswith("urn:uuid:") for i in ids.values())
