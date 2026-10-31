"""`Profile` / `ProfileSet` / `cgmes3` facts (runs offline against the committed snapshot)."""

import dataclasses

import pytest

import cim_python_sdk as c
from cim_python_sdk.profiles import Profile, ProfileSet, cgmes3


def names(infos):
    return [i.python_name for i in infos]


def test_profile_set_and_headers():
    assert [p.keyword for p in cgmes3.profiles] == [
        "EQ", "SSH", "TP", "SV", "DL", "GL", "OP", "SC", "EQBD", "DY",
    ]  # fmt: skip
    assert cgmes3.EQ is cgmes3.by_keyword("EQ") is cgmes3.profile_set["EQ"]
    assert cgmes3.EQ.uri == "http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0"
    assert cgmes3.by_uri(cgmes3.SSH.uri) is cgmes3.SSH
    assert cgmes3.EQ.name == "CoreEquipment" and cgmes3.EQ.version == "3.0.0"
    assert len(cgmes3.DY.classes) == 260 and cgmes3.DY.version == "1.0.0"
    with pytest.raises(KeyError, match="NOPE"):
        cgmes3.by_keyword("NOPE")
    with pytest.raises(KeyError):
        cgmes3.by_uri("http://example.com/")
    with pytest.raises(dataclasses.FrozenInstanceError):
        cgmes3.EQ.keyword = "X"  # type: ignore[misc]


def test_classes_resolve_to_sdk_classes():
    assert c.ACLineSegment in cgmes3.EQ.classes
    assert cgmes3.EQ.has_class(c.ACLineSegment) and cgmes3.EQ.has_class("ACLineSegment")
    assert cgmes3.EQ.has_class("cim:ACLineSegment") and c.ACLineSegment in cgmes3.EQ
    assert c.BoundaryPoint in cgmes3.EQ.classes  # eu class
    assert c.TopologicalNode in cgmes3.TP.classes and not cgmes3.EQ.has_class(c.TopologicalNode)
    assert len(cgmes3.EQ.class_names) == len(cgmes3.EQ.classes) == 180
    assert set(cgmes3.classes) == {k for p in cgmes3.profiles for k in p.classes}
    assert len(cgmes3.classes) == len(cgmes3.class_names) == 490
    assert cgmes3.DY.is_concrete(c.ExcIEEEST1A) and not cgmes3.EQ.has_class(c.ExcIEEEST1A)
    assert not cgmes3.profile_set.has_class(c.Bid)


def test_concrete_description_enumeration():
    assert cgmes3.EQ.is_concrete(c.ACLineSegment)
    assert not cgmes3.EQ.is_concrete(c.Equipment) and not cgmes3.EQ.is_concrete(c.Bid)
    assert c.ACLineSegment in cgmes3.EQ.concrete_classes
    assert not cgmes3.EQ.is_description(c.Terminal)
    assert cgmes3.SSH.is_description(c.Terminal) and cgmes3.TP.is_description(c.Terminal)
    assert cgmes3.TP.is_concrete(c.TopologicalNode) and not cgmes3.SV.is_concrete(c.TopologicalNode)
    assert cgmes3.EQ.is_enumeration(c.UnitSymbol) and not cgmes3.EQ.is_enumeration(c.Terminal)
    assert cgmes3.EQ.superclass(c.ACLineSegment) is c.Conductor
    assert cgmes3.EQ.superclass("IdentifiedObject") is None


def test_eq_acline_segment_properties():
    props = cgmes3.EQ.properties(c.ACLineSegment)
    assert names(props)[:3] == ["description", "energy_ident_code_eic", "mrid"]  # base class first
    by = {p.name: p for p in props}
    r = by["ACLineSegment.r"]
    assert (r.python_name, r.namespace, r.kind, r.min, r.max) == ("r", "cim", "attribute", 1, 1)
    assert r.range == "cim:Resistance" and r.range_kind == "datatype" and r.required
    assert r.owner is c.ACLineSegment and r.qname == "cim:ACLineSegment.r"
    assert by["IdentifiedObject.name"].owner is c.IdentifiedObject
    assert by["ACLineSegment.gch"].min == 0 and not by["ACLineSegment.gch"].required
    base = by["ConductingEquipment.BaseVoltage"]
    assert base.is_association and base.python_name == "base_voltage" and base.max == 1
    assert base.targets == ("BaseVoltage",) and not base.many
    req = {p.python_name for p in cgmes3.EQ.required(c.ACLineSegment)}
    assert {"r", "x", "bch", "name", "mrid"} <= req and "gch" not in req
    assert cgmes3.EQ.properties(c.TopologicalNode) == ()
    assert cgmes3.EQ.properties("ACLineSegment") == props


def test_property_lookup_forms():
    p = cgmes3.EQ.property(c.ACLineSegment, "r")
    assert p is cgmes3.EQ.property(c.ACLineSegment, "ACLineSegment.r")
    assert p is cgmes3.EQ.property(c.ACLineSegment, "cim:ACLineSegment.r")
    assert cgmes3.EQ.property(c.ACLineSegment, "mRID").python_name == "mrid"
    assert cgmes3.EQ.property(c.ACLineSegment, "nope") is None
    assert cgmes3.EQ.has_property(c.ACLineSegment, "short_name")
    assert not cgmes3.EQ.has_property(c.Bid, "name")


def test_ssh_energy_consumer_p_q_required():
    req = cgmes3.SSH.required(c.EnergyConsumer)
    assert {"p", "q"} <= {p.python_name for p in req}
    assert not cgmes3.EQ.has_property(c.EnergyConsumer, "p")
    assert cgmes3.EQ.has_property(c.EnergyConsumer, "pfixed")


def test_terminal_in_several_profiles():
    names_by = {
        p.keyword: {i.python_name for i in p.properties(c.Terminal)}
        for p in cgmes3.profiles
        if p.has_class(c.Terminal)
    }
    assert {"EQ", "SSH", "TP"} <= set(names_by)
    assert {"conducting_equipment", "sequence_number", "connectivity_node"} <= names_by["EQ"]
    assert "connected" in names_by["SSH"] and "connected" not in names_by["EQ"]
    assert "topological_node" in names_by["TP"] and "topological_node" not in names_by["EQ"]
    assert cgmes3.profiles_of(c.Terminal, "connected") == (cgmes3.SSH,)
    assert cgmes3.profiles_of(c.Terminal, "topological_node") == (cgmes3.TP,)
    assert cgmes3.profiles_of(c.Terminal, "sequence_number") == (cgmes3.EQ,)
    assert cgmes3.profiles_of(c.Terminal)[:3] == (cgmes3.EQ, cgmes3.SSH, cgmes3.TP)
    assert cgmes3.defining_profiles(c.Terminal) == (cgmes3.EQ, cgmes3.EQBD)
    assert cgmes3.defining_profiles(c.TopologicalNode) == (cgmes3.TP,)


def test_european_extensions():
    p = cgmes3.EQ.property(c.ACLineSegment, "short_name")
    assert p.namespace == "eu" and p.qname == "eu:IdentifiedObject.shortName"
    assert p.range == "xsd:string"
    assert cgmes3.profiles_of(c.ACLineSegment, "short_name") == (cgmes3.EQ,)
    assert cgmes3.profiles_of(c.IdentifiedObject, "shortName") == (
        cgmes3.EQ, cgmes3.TP, cgmes3.EQBD,
    )  # fmt: skip
    bp = cgmes3.EQ.property(c.BoundaryPoint, "from_end_iso_code")
    assert bp.namespace == "eu" and bp.owner is c.BoundaryPoint
    kind = cgmes3.EQ.property(c.OperationalLimitType, "kind")
    assert kind.range == "eu:LimitKind" and kind.literals == cgmes3.EQ.allowed_literals(c.LimitKind)
    assert "patl" in cgmes3.EQ.allowed_literals(c.LimitKind)


def test_enum_literals():
    assert cgmes3.SSH.allowed_literals(c.SynchronousMachineOperatingMode) == (
        "generator", "condenser", "motor",
    )  # fmt: skip
    # the vocabularies list every literal of the CIM enumeration (none is narrowed)
    full = tuple(m.value for m in c.UnitSymbol)
    assert cgmes3.EQ.allowed_literals(c.UnitSymbol) == full
    op = cgmes3.OP.allowed_literals("UnitSymbol")
    assert set(op) == set(full)
    assert cgmes3.OP.property(c.Analog, "unit_symbol").literals == op
    assert set(cgmes3.EQ.property(c.Terminal, "phases").literals) == {m.value for m in c.PhaseCode}
    assert cgmes3.TP.allowed_literals(c.SynchronousMachineOperatingMode) == ()


def test_max_falls_back_to_sdk_multiplicity():
    p = cgmes3.SV.property(c.TopologicalIsland, "topological_nodes")
    assert p.many and p.max is None and p.min == 1
    assert cgmes3.GL.property(c.Location, "power_system_resources").max == 1  # profile max wins


def test_no_sdk_gaps():
    # the CIMTool OWL listed VsConverter.uf and a stale cim15 member; the vocabularies do not
    assert cgmes3.SV.property(c.VsConverter, "VsConverter.uf") is None
    assert cgmes3.SC.property(c.SynchronousMachine, "SynchronousMachine.GeneratingUnit") is None
    gaps = {
        (p.keyword, i.name)
        for p in cgmes3.profiles
        for cls in p.classes
        for i in p.properties(cls)
        if i.python_name is None
    }
    assert gaps == set()
    assert not cgmes3.SSH.has_property(c.VsConverter, "uf")


def test_python_names_exist_on_sdk_classes():
    for p in cgmes3.profiles:
        for cls in p.classes:
            if cls._cim_meta.kind not in ("class", "compound"):
                continue
            for i in p.properties(cls):
                if i.python_name is not None:
                    assert hasattr(cls, i.python_name), (p.keyword, cls, i.name)


def test_other_profile_set_from_snapshot():
    snap = {
        "namespaces": {"cim": "x"},
        "source": {"repo": "r"},
        "profiles": {
            "ZZ": {
                "keyword": "ZZ", "name": "Zed", "uri": "urn:zz", "version": "1", "base": "",
                "comment": "", "classes": {
                    "Substation": {
                        "ns": "cim", "super": None, "concrete": True, "enumeration": False,
                        "stereotypes": ["concrete"], "literals": None, "min_instances": None,
                        "properties": {
                            "Substation.Region": {
                                "ns": "cim", "kind": "association", "min": 1, "max": None,
                                "range": "cim:SubGeographicalRegion", "range_kind": "class",
                                "targets": [], "stereotypes": [],
                            }
                        },
                    }
                },
            }
        },
    }  # fmt: skip
    s = ProfileSet.from_snapshot(snap, "Test")
    assert isinstance(s.ZZ, Profile) and s.keywords == ("ZZ",) and "ZZ" in s
    info = s.ZZ.property(c.Substation, "region")
    assert info.python_name == "region" and info.required and info.max == 1
    assert s.profiles_of(c.Substation, "Region") == (s.ZZ,)
    with pytest.raises(AttributeError):
        s.QQ  # noqa: B018
