"""Facts of the committed CGMES 3.0 snapshot (runs offline)."""

import json
import subprocess
import sys
from importlib import resources
from pathlib import Path

import pytest

from codegen import profile_source

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def snap():
    text = resources.files("cim_python_sdk.profiles").joinpath("data/cgmes_3_0.json").read_text("utf-8")
    return json.loads(text)


# keyword: (classes, properties, eu properties, concrete, enumerations, associations,
#           min 1 properties)
COUNTS = {
    "DL": (12, 26, 0, 8, 3, 7, 9),
    "DY": (260, 2787, 0, 193, 21, 95, 2707),
    "EQ": (180, 286, 14, 125, 20, 77, 148),
    "EQBD": (22, 27, 11, 12, 2, 11, 17),
    "GL": (11, 39, 0, 4, 0, 3, 7),
    "OP": (37, 57, 0, 20, 5, 20, 30),
    "SC": (35, 105, 0, 16, 4, 2, 75),
    "SSH": (72, 65, 0, 46, 9, 0, 44),
    "SV": (23, 30, 0, 11, 2, 10, 29),
    "TP": (14, 13, 2, 7, 0, 8, 7),
}

NAMES = {
    "DL": "DiagramLayout",
    "DY": "Dynamics",
    "EQ": "CoreEquipment",
    "EQBD": "EquipmentBoundary",
    "GL": "GeographicalLocation",
    "OP": "Operation",
    "SC": "ShortCircuit",
    "SSH": "SteadyStateHypothesis",
    "SV": "StateVariables",
    "TP": "Topology",
}


def test_source_and_namespaces(snap):
    cfg = profile_source.load_source_config()
    assert snap["source"] == {"repo": cfg["repo"], "commit": cfg["commit"], "license": "Apache-2.0"}
    assert snap["namespaces"]["cim"] == "http://iec.ch/TC57/CIM100#"
    assert snap["namespaces"]["eu"] == "http://iec.ch/TC57/CIM100-European#"


def test_profile_headers(snap):
    assert set(snap["profiles"]) == set(NAMES)
    for kw, p in snap["profiles"].items():
        name = NAMES[kw]
        voc = "Equipment" if kw == "EQ" else name
        assert p["keyword"] == kw and p["name"] == name
        assert p["file"] == f"61970-600-2_{voc}-AP-Voc-RDFS2020.rdf"
        major = "1.0" if kw == "DY" else "3.0"
        assert p["uri"] == f"http://iec.ch/TC57/ns/CIM/{name}-EU/{major}"
        assert p["version"] == f"{major}.0"
        assert p["base"] == f"http://iec.ch/TC57/ns/CIM/{name}-EU#"


@pytest.mark.parametrize("kw", sorted(COUNTS))
def test_counts(snap, kw):
    classes = snap["profiles"][kw]["classes"].values()
    props = [p for c in classes for p in c["properties"].values()]
    got = (
        len(classes),
        len(props),
        sum(p["ns"] == "eu" for p in props),
        sum(c["concrete"] for c in classes),
        sum(c["enumeration"] for c in classes),
        sum(p["kind"] == "association" for p in props),
        sum(p["min"] == 1 for p in props),
    )
    assert got == COUNTS[kw]


def test_internal_consistency(snap):
    for kw, p in snap["profiles"].items():
        classes = p["classes"]
        for name, c in classes.items():
            assert c["super"] is None or c["super"] in classes, (kw, name)
            assert c["literals"] is None or c["enumeration"], (kw, name)
            assert (c["ns"] == "eu") == ("european" in c["stereotypes"]), (kw, name)
            for pname, prop in c["properties"].items():
                assert all(t in classes for t in prop["targets"]), (kw, pname)
                assert (prop["ns"] == "eu") == ("european" in prop["stereotypes"]), (kw, pname)
                assert prop["max"] in (None, 1) and prop["min"] in (0, 1)
                assert prop["kind"] in ("attribute", "association") and prop["range"]


LIMIT_KINDS = [
    "patl", "patlt", "tatl", "tc", "tct", "highVoltage", "lowVoltage",
    "operationalVoltageLimit", "alarmVoltage", "warningVoltage", "stability",
]  # fmt: skip


def test_spot_facts(snap):
    eq, tp, ssh, sv = (snap["profiles"][k]["classes"] for k in ("EQ", "TP", "SSH", "SV"))
    r = eq["ACLineSegment"]["properties"]["ACLineSegment.r"]
    assert (r["kind"], r["min"], r["range"], r["range_kind"]) == (
        "attribute",
        1,
        "cim:Resistance",
        "datatype",
    )
    tn = tp["Terminal"]["properties"]["Terminal.TopologicalNode"]
    assert (tn["kind"], tn["max"], tn["targets"]) == ("association", 1, ["TopologicalNode"])
    assert tp["Terminal"]["stereotypes"] == ["concrete", "description"]
    assert "description" not in tp["TopologicalNode"]["stereotypes"]
    assert ssh["AsynchronousMachineKind"]["literals"] == ["generator", "motor"]
    assert eq["LimitKind"] == {
        "concrete": False,
        "enumeration": True,
        "literals": LIMIT_KINDS,
        "ns": "eu",
        "properties": {},
        "stereotypes": ["enumeration", "european"],
        "super": None,
    }
    kind = eq["OperationalLimitType"]["properties"]["OperationalLimitType.kind"]
    assert (kind["ns"], kind["range"], kind["range_kind"]) == ("eu", "eu:LimitKind", "enumeration")
    # the 1..1 terminal-equipment link (0..n in the CIMTool OWL)
    te = eq["Terminal"]["properties"]["Terminal.ConductingEquipment"]
    assert (te["min"], te["max"]) == (1, 1)
    # OWL-only members are gone; Simple_Float ranges are xsd:float
    assert "VsConverter.uf" not in sv["VsConverter"]["properties"]
    assert sv["SvTapStep"]["properties"]["SvTapStep.position"]["range"] == "xsd:float"
    # the [[corrections]] of profile-source.toml
    assert ssh["Equipment"]["stereotypes"] == ["concrete", "description"]
    # fixed units, read from the datatypes of the vocabularies
    assert snap["units"]["Voltage"] == {"multiplier": "k", "unit": "V"}
    assert snap["units"]["ActivePower"] == {"multiplier": "M", "unit": "W"}
    assert snap["units"]["Money"] == {"multiplier": "none"}
    assert len(snap["units"]) == 27


def test_dump_check_is_clean():
    if profile_source.cached_profiles() is None:
        pytest.skip("profiles not cached; run tools/fetch_profiles.py")
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "dump_profiles.py"), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0, r.stdout + r.stderr
