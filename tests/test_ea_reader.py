"""EA reader and IR tests.

Tests marked with the `model` fixture need the cached .qea and are skipped otherwise.
Tests on `snapshot` only read the committed codegen/snapshot/cim100_ir.json.
"""

from collections import Counter
from pathlib import Path

import pytest

from codegen import model_source as ms
from codegen.ea_reader import EAReadError, clean_notes, parse_cardinality, read_model
from codegen.ir import Model

SNAPSHOT = Path(__file__).resolve().parent.parent / "codegen" / "snapshot" / "cim100_ir.json"

# Verified against the model (see docs/PLAN.md "Model facts").
EXPECTED = {
    "classifiers": 1947,
    "class": 1426,
    "enumeration": 405,
    "cimdatatype": 56,
    "compound": 50,
    "primitive": 10,
    "literals": 3211,
    "attributes": 6334,
    "Association": 1356,
    "Aggregation": 18,
    "generalizations": 1238,
    "packages": 173,  # TC57CIM and its descendants; 174 incl. the "Model" root
}


def _model_file() -> Path:
    path = ms.model_path()
    if not path.is_file():
        pytest.skip("model not cached; run tools/fetch_model.py")
    return path


@pytest.fixture(scope="module")
def model() -> Model:
    return read_model(_model_file())


@pytest.fixture(scope="module")
def snapshot() -> Model:
    return Model.from_json(SNAPSHOT.read_text(encoding="utf-8"))


def _counts(m: Model) -> dict[str, int]:
    kinds = Counter(c.kind for c in m.classifiers)
    types = Counter(a.type for a in m.associations)
    return {
        "classifiers": len(m.classifiers),
        **{k: kinds[k] for k in ("class", "enumeration", "cimdatatype", "compound", "primitive")},
        "literals": sum(len(c.literals) for c in m.classifiers),
        "attributes": sum(len(c.attributes) for c in m.classifiers),
        "Association": types["Association"],
        "Aggregation": types["Aggregation"],
        "generalizations": sum(c.superclass is not None for c in m.classifiers),
        "packages": len(m.packages),
    }


def _one(m: Model, name: str):
    found = m.classifiers_named(name)
    assert len(found) == 1, f"{name}: {len(found)} matches"
    return found[0]


def _ends(m: Model, a: str, b: str):
    """Ends of the single association between classes a and b, keyed by owner name."""
    ga, gb = _one(m, a).guid, _one(m, b).guid
    assocs = [x for x in m.associations if {e.owner for e in x.ends} == {ga, gb}]
    assert len(assocs) == 1
    names = {ga: a, gb: b}
    return assocs[0], {names[e.owner]: e for e in assocs[0].ends}


# ---------------------------------------------------------------- pure unit tests


@pytest.mark.parametrize(
    "text,expected",
    [
        ("1", (1, 1)),
        ("0..1", (0, 1)),
        ("0..*", (0, None)),
        ("*", (0, None)),
        ("1..*", (1, None)),
        ("2..*", (2, None)),
        ("0..2", (0, 2)),
        ("0..n", (0, None)),
        ("1..", (1, None)),
        (" 0..1 ", (0, 1)),
    ],
)
def test_parse_cardinality(text, expected):
    assert parse_cardinality(text) == expected


@pytest.mark.parametrize("text", [None, "", "many", "1..2..3", "2..1", "0..0", "-1", "1-*"])
def test_parse_cardinality_rejects_unknown(text):
    with pytest.raises(EAReadError):
        parse_cardinality(text)


def test_clean_notes_strips_rich_text_only():
    raw = '<b>Bold</b> &lt;&lt;enum&gt;&gt;\r\n<ul>\r\n\t<li>one</li>\r\n</ul>\r\n<was old.>'
    assert clean_notes(raw) == "Bold <<enum>>\n\n- one\n\n<was old.>"
    assert clean_notes(None) == ""


# ---------------------------------------------------------------- snapshot (offline)


def test_snapshot_counts(snapshot):
    assert _counts(snapshot) == EXPECTED
    assert snapshot.unresolved_types == ()


def test_snapshot_round_trip(snapshot):
    assert snapshot.to_json() == SNAPSHOT.read_text(encoding="utf-8")


def test_snapshot_versions(snapshot):
    assert snapshot.versions["IEC61970CIMVersion"] == "IEC61970CIM17v40"
    assert snapshot.versions["IEC61968CIMVersion"] == "IEC61968CIM13v13b"
    assert snapshot.versions["IEC62325CIMVersion"] == "IEC62325CIM03v17b"


def test_single_inheritance_and_valid_refs(snapshot):
    by_guid = snapshot.classifier_by_guid()
    for c in snapshot.classifiers:
        if c.superclass is not None:
            assert c.superclass in by_guid
        for a in c.attributes:
            assert a.type_guid is None or a.type_guid in by_guid
    for a in snapshot.associations:
        for e in a.ends:
            assert e.owner in by_guid and e.target in by_guid
        assert a.ends[0].owner == a.ends[1].target and a.ends[1].owner == a.ends[0].target


def test_no_cycles_in_inheritance(snapshot):
    by_guid = snapshot.classifier_by_guid()
    for c in snapshot.classifiers:
        seen = set()
        while c.superclass is not None:
            assert c.guid not in seen
            seen.add(c.guid)
            c = by_guid[c.superclass]


# ---------------------------------------------------------------- live model


def test_counts(model):
    assert _counts(model) == EXPECTED
    assert model.stats["duplicate_attributes_removed"] == 0
    assert model.unresolved_types == ()


def test_deterministic(model):
    again = read_model(_model_file())
    assert again.to_json() == model.to_json()


def test_snapshot_matches_model(model):
    assert SNAPSHOT.read_text(encoding="utf-8") == model.to_json(), "run tools/dump_ir.py"


def test_generalization_direction(model):
    by_guid = model.classifier_by_guid()
    acl = _one(model, "ACLineSegment")
    assert by_guid[acl.superclass].name == "Conductor"
    assert by_guid[by_guid[acl.superclass].superclass].name == "ConductingEquipment"
    assert _one(model, "IdentifiedObject").superclass is None


def test_terminal_conducting_equipment_roles(model):
    assoc, ends = _ends(model, "Terminal", "ConductingEquipment")
    t, ce = ends["Terminal"], ends["ConductingEquipment"]
    assert assoc.type == "Association"
    # Terminal.ConductingEquipment: 1 (0..1 or 1 acceptable per CIM)
    assert t.role == "ConductingEquipment"
    assert t.target == _one(model, "ConductingEquipment").guid
    assert (t.lower, t.upper) == (1, 1)
    # ConductingEquipment.Terminals: 0..*
    assert ce.role == "Terminals"
    assert ce.target == _one(model, "Terminal").guid
    assert (ce.lower, ce.upper) == (0, None)


def test_contingency_roles(model):
    assoc, ends = _ends(model, "Contingency", "ContingencyElement")
    c, ce = ends["Contingency"], ends["ContingencyElement"]
    assert assoc.type == "Aggregation"
    assert c.role == "ContingencyElement" and (c.lower, c.upper) == (0, None)
    assert ce.role == "Contingency" and (ce.lower, ce.upper) == (1, 1)
    assert c.owner_aggregation == "shared"  # Contingency is the whole
    assert ce.owner_aggregation == "none"


def test_aclinesegment_r(model):
    r = {a.name: a for a in _one(model, "ACLineSegment").attributes}["r"]
    assert r.type_name == "Resistance"
    resistance = _one(model, "Resistance")
    assert r.type_guid == resistance.guid and resistance.kind == "cimdatatype"


def test_unit_multiplier(model):
    um = _one(model, "UnitMultiplier")
    assert um.kind == "enumeration"
    lits = {x.name: x for x in um.literals}
    assert "k" in lits and lits["k"].value == "3"
    assert "M" in lits and "m" in lits  # case-sensitive, not deduplicated


def test_identified_object_mrid(model):
    attrs = {a.name: a for a in _one(model, "IdentifiedObject").attributes}
    assert attrs["mRID"].type_name == "String"
    assert model.classifier_by_guid()[attrs["mRID"].type_guid].kind == "primitive"


def test_names_are_stripped(model):
    for c in model.classifiers:
        for a in c.attributes:
            assert a.name == a.name.strip()
    roles = {e.role for a in model.associations for e in a.ends if e.role}
    assert "MktContingencyA" in roles
    assert all(r == r.strip() for r in roles)


def test_missing_roles(model):
    no_role = [a for a in model.associations if all(e.role is None for e in a.ends)]
    one_role = [a for a in model.associations if sum(e.role is None for e in a.ends) == 1]
    assert (len(no_role), len(one_role)) == (33, 0)
