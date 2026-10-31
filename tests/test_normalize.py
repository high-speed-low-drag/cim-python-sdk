"""Normalization tests; all offline, from the committed IR snapshot."""

import keyword

import pytest

from codegen.normalize import (
    NormalizeError,
    load_snapshot,
    normalize,
    pluralize,
    singularize,
    snake,
)


@pytest.fixture(scope="module")
def ir():
    return load_snapshot()


@pytest.fixture(scope="module")
def rm(ir):
    return normalize(ir)


@pytest.fixture(scope="module")
def classes(rm):
    return {c.guid: c for c in rm.classes}


def by_name(rm, name):
    return [c for c in rm.classes if c.cim_name == name]


def one(rm, name):
    (c,) = [c for c in by_name(rm, name) if c.is_canonical]
    return c


def end(c, cim_role):
    (e,) = [e for e in c.ends if e.cim_role == cim_role]
    return e


@pytest.mark.parametrize(
    ("src", "out"),
    [
        ("mRID", "mrid"),
        ("ACLineSegment", "ac_line_segment"),
        ("r0", "r0"),
        ("bPerSection", "b_per_section"),
        ("Import_EnergyTransactions", "import_energy_transactions"),
        ("IEC61970CIMVersion", "iec61970_cim_version"),
        ("ratedU", "rated_u"),
        ("pPerUnit", "p_per_unit"),
        ("x0", "x0"),
        ("gch", "gch"),
        ("HVDC", "hvdc"),
        ("EnergyConsumerPhase", "energy_consumer_phase"),
        ("DER Function", "der_function"),
        ("subjectMRID", "subject_mrid"),
        ("DesignLocationCUs", "design_location_cus"),
        ("CUs", "cus"),
    ],
)
def test_snake(src, out):
    assert snake(src) == out


def test_singularize():
    assert singularize("entries") == "entry"
    assert singularize("classes") == "class"
    assert singularize("addresses") == "address"
    assert singularize("terminals") == "terminal"
    assert singularize("class") == "class"


@pytest.mark.parametrize(
    ("src", "out"),
    [
        ("time_series", "time_series"),
        ("switch_status", "switch_status"),
        ("proprietary_parameter_dynamics", "proprietary_parameter_dynamics"),
        ("terminals", "terminal"),
        ("bushings", "bushing"),
        ("addresses", "address"),
        ("boundaries", "boundary"),
        ("design_location_cus", "design_location_cu"),
        ("species", "species"),
        ("analysis", "analysis"),
    ],
)
def test_singularize_cases(src, out):
    assert singularize(src) == out


@pytest.mark.parametrize(
    ("src", "out"),
    [
        ("network_boundary", "network_boundaries"),
        ("terminal", "terminals"),
        ("key", "keys"),
        ("address", "addresses"),
        ("box", "boxes"),
        ("batch", "batches"),
        ("component2", "component2s"),
    ],
)
def test_pluralize(src, out):
    assert pluralize(src) == out


def test_module_path(rm):
    assert one(rm, "ACLineSegment").module == "cim_python_sdk.model.iec61970.base.wires.ac_line_segment"


def test_duplicate_classes(rm):
    for name in ("Profile", "ResourceCertification", "IEC61968CIMVersion", "TroubleReportingKind"):
        copies = by_name(rm, name) + [e for e in rm.enums if e.cim_name == name]
        assert sum(c.is_canonical for c in copies) == 1
        assert len({c.module for c in copies}) == len(copies)
    trk = [e for e in rm.enums if e.cim_name == "TroubleReportingKind"]
    assert sorted(e.py_name for e in trk) == ["TroubleReportingKind", "TroubleReportingKind_2"]
    assert all(e.module.endswith(("trouble_reporting_kind", "trouble_reporting_kind_2")) for e in trk)
    ver = by_name(rm, "IEC61968CIMVersion")
    assert sorted(c.py_name for c in ver) == [
        "IEC61968CIMVersion", "IEC61968CIMVersion", "IEC61968CIMVersion_2"]
    canon = next(c for c in ver if c.is_canonical)
    assert canon.package == "TC57CIM/IEC61968"
    # different packages: names kept, only module differs
    assert {c.py_name for c in by_name(rm, "Profile")} == {"Profile"}
    assert {c.py_name for c in by_name(rm, "ResourceCertification")} == {"ResourceCertification"}
    prof = next(c for c in by_name(rm, "Profile") if c.is_canonical)
    assert "inf" not in prof.module


def test_deterministic(ir, rm):
    assert normalize(ir) == rm


def test_unique_names_and_modules(rm):
    canon = [x.py_name for x in (*rm.classes, *rm.enums) if x.is_canonical]
    assert len(canon) == len(set(canon))
    mods = [x.module for x in (*rm.classes, *rm.enums)]
    assert len(mods) == len(set(mods))
    assert all(m.startswith("cim_python_sdk.model.") for m in mods)
    assert all(part.isidentifier() and not keyword.iskeyword(part) for m in mods for part in m.split("."))


def test_literals(rm):
    for e in rm.enums:
        names = [lit.py_name for lit in e.literals]
        assert len(names) == len(set(names)), e.cim_name
        for lit in e.literals:
            assert lit.py_name.isidentifier()
            assert not keyword.iskeyword(lit.py_name)
            if lit.cim_value.isidentifier() and not keyword.iskeyword(lit.cim_value):
                assert lit.py_name == lit.cim_value
    us = next(e for e in rm.enums if e.cim_name == "UnitSymbol")
    d = {lit.cim_value: lit.py_name for lit in us.literals}
    assert d["m"] == "m"
    assert d["M"] == "M"


def test_literal_sanitizing(rm):
    uom = next(e for e in rm.enums if e.cim_name == "UOMType")
    d = {lit.cim_value: lit.py_name for lit in uom.literals}
    assert d["US$"] == "US_dollar"
    y = next(e for e in rm.enums if e.cim_name == "IECStandardEditionKind")
    assert {lit.cim_value: lit.py_name for lit in y.literals}["1963"] == "v1963"


def test_literal_rule():
    from codegen.normalize import literal_ident

    assert literal_ident("01") == "v01"
    assert literal_ident("_00_2005_") == "v00_2005"
    assert literal_ident("and") == "and_"
    assert literal_ident("US$") == "US_dollar"
    assert literal_ident("%") == "percent"
    assert literal_ident("") == "v"


def test_enums_constructible(rm):
    import enum

    for e in rm.enums:
        m = enum.Enum(e.py_name, [(lit.py_name, lit.cim_value) for lit in e.literals])
        assert len(m.__members__) == len(e.literals), e.cim_name


def test_no_leading_underscore(rm):
    assert all(not lit.py_name.startswith("_") for e in rm.enums for lit in e.literals)
    names = [x.py_name for x in (*rm.classes, *rm.enums)]
    names += [a.py_name for c in rm.classes for a in c.attributes]
    names += [e.py_name for c in rm.classes for e in c.ends]
    assert all(not n.startswith("_") for n in names)


def test_mrid_methods_only_with_mrid(rm, classes):
    def has_mrid(c):
        return any(a.py_name == "mrid" for k in (c, *(classes[g] for g in c.ancestors)) for a in k.attributes)

    n = 0
    for c in rm.classes:
        for e in c.ends:
            got = any(m.endswith("_by_mrid") for m in e.methods)
            assert got == (e.many and has_mrid(classes[e.target_guid])), (c.cim_name, e.py_name)
            n += got
    assert n > 0


def test_defaults_evaluate(rm):
    from datetime import date, datetime, time
    from decimal import Decimal

    ns = {e.py_name: __import__("enum").Enum(e.py_name, [(l.py_name, l.cim_value) for l in e.literals])
          for e in rm.enums if e.is_canonical}
    ns.update(_dt=__import__("datetime"), Decimal=Decimal, datetime=datetime, date=date, time=time)
    n = 0
    for c in rm.classes:
        for a in c.attributes:
            if a.default is not None:
                eval(a.default, {"__builtins__": {}}, ns)
                n += 1
    assert n > 0


def test_facility_kind_incompatible(rm):
    bad = [(c.cim_name, a.cim_name) for c in rm.classes for a in c.attributes
           if a.overrides and not a.override_compatible]
    assert bad == [("Facility", "kind")]


def _member_names(c, classes):
    names = []
    chain = [classes[g] for g in reversed(c.ancestors)] + [c]
    for k in chain:
        own = [a.py_name for a in k.attributes if not a.overrides]
        for e in k.ends:
            own.append(e.py_name)
            own.extend(e.methods)
        names.extend((k.guid, n) for n in own)
    return names


def test_no_duplicate_members(rm, classes):
    for c in rm.classes:
        names = [n for _, n in _member_names(c, classes)]
        assert len(names) == len(set(names)), (c.cim_name, [n for n in names if names.count(n) > 1])
        for n in names:
            assert not n.startswith("_")
            assert n != "validate"
            assert not keyword.iskeyword(n)
        for a in c.attributes:
            assert a.py_name.isidentifier()


def test_inverses(rm, classes):
    for c in rm.classes:
        for e in c.ends:
            og, oname = e.inverse
            (back,) = [x for x in classes[og].ends if x.py_name == oname]
            assert back.inverse == (c.guid, e.py_name)
            assert back.association_guid == e.association_guid
            assert back.target_guid == c.guid
            assert e.target_guid == og
            assert e.many == (e.upper is None or e.upper > 1)


def test_ends_counts(rm, ir):
    assert sum(len(c.ends) for c in rm.classes) == 2 * len(ir.associations)
    selfs = [a for a in ir.associations if a.ends[0].owner == a.ends[1].owner]
    assert len(selfs) == 14
    assert dict(rm.report.counts)["self_associations"] == 14


def test_generated_roles(rm):
    assert len(rm.report.generated_roles) == 66  # 33 associations x 2 ends
    gen = [e for c in rm.classes for e in c.ends if e.generated_role]
    assert len(gen) == 66
    tgt = {c.guid: c for c in rm.classes}
    for e in gen:
        assert e.cim_role is None
        base = (e.renamed_from or e.py_name)
        stem = snake(tgt[e.target_guid].py_name)
        assert base.startswith(stem.removesuffix("y"))
        assert base.endswith("s") == e.many or not e.many
    assert any(e.py_name == "network_boundaries" for e in gen)
    assert any(e.many and (e.renamed_from or e.py_name).endswith("s") for e in gen)


def test_spot_terminal(rm, classes):
    t = one(rm, "Terminal")
    ce = end(t, "ConductingEquipment")
    assert ce.py_name == "conducting_equipment"
    assert not ce.many
    assert ce.item_name == "conducting_equipment"
    og, oname = ce.inverse
    assert classes[og].cim_name == "ConductingEquipment"
    assert oname == "terminals"
    (back,) = [e for e in classes[og].ends if e.py_name == "terminals"]
    assert back.item_name == "terminal"
    assert back.many
    assert back.methods == (
        "add_terminal", "remove_terminal", "clear_terminals", "num_terminal", "get_terminal_by_mrid")


def test_spot_ac_line_segment_r(rm):
    a = next(x for x in one(rm, "ACLineSegment").attributes if x.cim_name == "r")
    assert a.py_type == "Resistance"
    assert a.type_kind == "cimdatatype"
    assert a.value_py_type == "float"


def test_datatype_attributes(rm):
    length = one(rm, "Length")
    d = {a.cim_name: a for a in length.attributes}
    assert d["value"].py_type == "float"
    assert d["unit"].default == "UnitSymbol.m"
    assert d["unit"].is_static
    assert d["unit"].type_kind == "enumeration"


def test_primitive_types(rm):
    ident = one(rm, "IdentifiedObject")
    a = {x.cim_name: x for x in ident.attributes}
    assert a["mRID"].py_name == "mrid"
    assert a["mRID"].py_type == "str"
    assert a["mRID"].type_kind == "primitive"
    assert not rm.report.primitive_fallbacks


def test_keyword_escape(rm):
    a = next(x for x in one(rm, "FTR").attributes if x.cim_name == "class")
    assert a.py_name == "class_"


@pytest.mark.parametrize("cname", ["FACTSDevice", "Facility", "StructureSupport", "UndergroundStructure"])
def test_kind_override(rm, classes, cname):
    a = next(x for x in one(rm, cname).attributes if x.cim_name == "kind")
    assert a.py_name == "kind"
    assert a.overrides is not None
    assert classes[a.overrides].cim_name == "Asset"


@pytest.mark.parametrize("cname", ["OutageOrder", "TroubleTicket", "TroubleOrder"])
def test_comment_override(rm, cname):
    a = next(x for x in one(rm, cname).attributes if x.cim_name == "comment")
    assert a.overrides is not None


COLLISIONS = [
    ("EndDevice", "ServiceLocation"),
    ("HostControlArea", "Controls"),
    ("IncidentHazard", "Incident"),
    ("IncidentHazard", "TroubleTicket"),
    ("ServiceLocation", "TroubleTicket"),
    ("UnplannedOutage", "Incident"),
    ("DERFunction", "EndDeviceGroup"),
    ("UsagePoint", "Outage"),
    ("Customer", "Customer"),
    ("InterrupterUnit", "Bushing"),
    ("Quantity", "quantity"),
]


@pytest.mark.parametrize(("cname", "role"), COLLISIONS)
def test_end_collisions_resolved(rm, classes, cname, role):
    c = one(rm, cname)
    ends = [e for e in c.ends if e.cim_role == role]
    assert ends
    renamed = [e for e in ends if e.renamed_from]
    if role == "quantity":
        assert [a.py_name for a in c.attributes if a.cim_name == "quantity"] == ["quantity"]
    assert renamed or any(e.renamed_from for e in c.ends if e.cim_role != role) or len(ends) == 1
    # inverses point at the final names
    for e in ends:
        og, oname = e.inverse
        assert any(x.py_name == oname and x.inverse == (c.guid, e.py_name) for x in classes[og].ends)
    names = [e.py_name for e in ends]
    assert len(names) == len(set(names))


def test_known_renames_present(rm):
    renamed = {(c.cim_name, e.cim_role) for c in rm.classes for e in c.ends if e.renamed_from}
    for key in [("Customer", "Customer"), ("InterrupterUnit", "Bushing"), ("Quantity", "quantity"),
                ("UnplannedOutage", "Incident"), ("EndDevice", "ServiceLocation")]:
        assert key in renamed, key


def test_unresolvable_collision_raises(ir):
    from dataclasses import replace

    # give two attributes of one class the same name
    c = next(x for x in ir.classifiers if x.name == "Terminal")
    a0 = c.attributes[0] if c.attributes else None
    if a0 is None:
        pytest.skip("Terminal has no attributes")
    bad = replace(c, attributes=(*c.attributes, replace(a0, guid="{X}")))
    m2 = replace(ir, classifiers=tuple(bad if x.guid == c.guid else x for x in ir.classifiers))
    with pytest.raises(NormalizeError):
        normalize(m2)


def test_date_default_expression(rm):
    c = next(c for c in rm.classes if c.cim_name == "IEC61970CIMVersion")
    d = next(a for a in c.attributes if a.cim_name == "date")
    assert d.default == "_dt.date(2020, 8, 24)"
