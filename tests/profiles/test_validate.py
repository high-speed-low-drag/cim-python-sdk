"""`validate_profile`: a valid network is clean and each check fires on a crafted one."""

import json
import time
from importlib import resources

import pytest

import cim_python_sdk as c
from cim_python_sdk.profiles import ProfileIssue, ProfileSet, cgmes3, validate_profile
from tests.profiles.eq_network import build_eq


def find(issues, *, severity=None, prop=None, profile=None, text=None):
    return [
        i
        for i in issues
        if (severity is None or i.severity == severity)
        and (prop is None or i.property == prop)
        and (profile is None or i.profile == profile)
        and (text is None or text in i.message)
    ]


def test_valid_eq_network_is_clean():
    net = build_eq(3)
    assert validate_profile(net.values(), cgmes3.EQ) == []
    assert validate_profile([net["line0"]], [cgmes3.EQ]) == []  # reachable objects
    assert cgmes3.EQ.validate(net.values()) == []
    assert cgmes3.profile_set.validate(net.values(), [cgmes3.EQ]) == []


def test_valid_eq_tp_network_is_clean():
    net = build_eq(3, topology=True)
    assert validate_profile(net.values(), [cgmes3.EQ, cgmes3.TP]) == []


def test_include_reachable_false_checks_only_the_roots():
    net = build_eq(1)
    line = net["line0"]
    line.r = None
    only = validate_profile([line], cgmes3.EQ, include_reachable=False)
    assert [i.property for i in only] == ["ACLineSegment.r"]
    assert validate_profile([net["bv"]], cgmes3.EQ, include_reachable=False) == []


def test_class_not_in_selected_profiles():
    net = build_eq(1, topology=True)
    issues = validate_profile(net.values(), cgmes3.EQ)
    tn = find(issues, severity="error", text="not in the selected profiles")
    assert {type(i.object) for i in tn} == {c.TopologicalNode} and len(tn) == 2
    assert tn[0].profile is None and tn[0].property is None
    bid = validate_profile([c.Bid(mrid="b1", name="bid")], cgmes3.EQ)
    assert len(bid) == 1 and bid[0].severity == "error"
    assert "Bid" in str(bid[0])


def test_class_not_concrete_in_profile():
    bv = c.BaseVoltage(mrid="bv", name="x", nominal_voltage=1.0)
    issues = validate_profile([bv], cgmes3.TP)  # a reference class in TP
    assert find(issues, severity="error", text="not concrete in TP")
    assert not find(validate_profile([bv], cgmes3.EQ), text="concrete")
    assert not find(validate_profile([bv], [cgmes3.TP, cgmes3.EQ]), text="concrete")


def test_property_outside_selected_profiles_is_a_warning():
    net = build_eq(1)
    t, t2 = net["line0"].terminals
    t.connected = t2.connected = True  # SSH
    issues = validate_profile(net.values(), cgmes3.EQ)
    assert len(issues) == 2
    w = next(i for i in issues if i.object is t)
    assert (w.severity, w.property, w.profile) == ("warning", "ACDCTerminal.connected", None)
    assert w.object is t and "EQ" in w.message
    both = validate_profile(net.values(), [cgmes3.EQ, cgmes3.SSH])
    assert not find(both, severity="warning")  # SSH also requires Equipment.inService etc.
    # an end of a class that is not in the profile at all
    assert find(validate_profile([t], cgmes3.SSH), prop="Terminal.ConductingEquipment")


def test_mrid_is_not_reported_and_defaults_are_ignored():
    # TP lists BaseVoltage as a plain reference without IdentifiedObject.mRID
    bv = c.BaseVoltage(mrid="bv", name="x", nominal_voltage=1.0)
    issues = validate_profile([bv], cgmes3.TP)
    assert not find(issues, prop="IdentifiedObject.mRID")
    assert {i.property for i in issues if i.severity == "warning"} == {
        "IdentifiedObject.name",
        "BaseVoltage.nominalVoltage",
    }


def test_required_property_missing():
    net = build_eq(1)
    line = net["line0"]
    line.r = None
    line.bch = None
    line.name = None
    line.base_voltage = None
    issues = validate_profile(net.values(), cgmes3.EQ)
    props = {i.property for i in find(issues, severity="error", profile="EQ")}
    assert props == {"ACLineSegment.r", "ACLineSegment.bch", "IdentifiedObject.name"}
    assert all(i.object is line for i in issues)  # BaseVoltage is optional
    line.mrid = None
    assert find(validate_profile([line], cgmes3.EQ), prop="IdentifiedObject.mRID")
    assert "ACLineSegment.r is not set" in str(find(issues, prop="ACLineSegment.r")[0])


def test_required_depends_on_the_selected_profiles():
    ec = c.EnergyConsumer(mrid="ec", name="load")
    assert not find(validate_profile([ec], cgmes3.EQ), prop="EnergyConsumer.p")
    ssh = validate_profile([ec], cgmes3.SSH)
    errors = find(ssh, severity="error")
    assert {"EnergyConsumer.p", "EnergyConsumer.q"} <= {i.property for i in errors}
    assert all(i.profile == "SSH" for i in errors)
    ec.p, ec.q = 1.0, 2.0
    left = {i.property for i in find(validate_profile([ec], cgmes3.SSH), severity="error")}
    assert not left & {"EnergyConsumer.p", "EnergyConsumer.q"}


def test_required_association_missing():
    sub = c.Substation(mrid="s", name="s")
    sub_issues = validate_profile([sub], cgmes3.EQ)
    assert find(sub_issues, severity="error", prop="Substation.Region")


def test_max_cardinality_exceeded():
    loc = c.Location(mrid="loc", name="loc")
    a = c.Substation(mrid="a", name="a")
    b = c.Substation(mrid="b", name="b")
    loc.add_power_system_resource(a)
    ok = validate_profile([loc], cgmes3.GL, include_reachable=False)
    assert not find(ok, prop="Location.PowerSystemResources")
    loc.add_power_system_resource(b)
    issues = validate_profile([loc], cgmes3.GL, include_reachable=False)
    (e,) = find(issues, prop="Location.PowerSystemResources")
    assert (
        e.severity == "error" and e.profile == "GL" and "2 item(s), allows at most 1" in e.message
    )


def _narrowed_op() -> ProfileSet:
    # the CGMES 3.0 vocabularies list every literal; narrow OP's UnitSymbol to test the check
    snap = json.loads(
        resources.files("cim_python_sdk.profiles").joinpath("data/cgmes_3_0.json").read_text("utf-8")
    )
    snap["profiles"]["OP"]["classes"]["UnitSymbol"]["literals"] = ["V", "A", "W"]
    return ProfileSet.from_snapshot(snap, "narrowed")


def test_enum_value_not_allowed():
    op = _narrowed_op().OP
    an = c.Analog(
        mrid="an", name="an", unit_symbol=c.UnitSymbol.V, unit_multiplier=c.UnitMultiplier.k
    )
    assert not find(validate_profile([an], op), prop="Measurement.unitSymbol")
    an.unit_symbol = c.UnitSymbol.kg
    (e,) = find(validate_profile([an], op), prop="Measurement.unitSymbol")
    assert e.severity == "error" and e.profile == "OP" and "'kg' is not allowed" in e.message
    assert not find(validate_profile([an], cgmes3.OP), prop="Measurement.unitSymbol")
    # unrestricted in EQ: any literal passes
    ok = c.SynchronousMachineOperatingMode.motor
    sm = c.SynchronousMachine(mrid="sm", name="sm", operating_mode=ok)
    assert not find(validate_profile([sm], cgmes3.SSH), prop="SynchronousMachine.operatingMode")


def test_known_gap_properties_are_skipped():
    vs = c.VsConverter(mrid="vs", name="vs")
    issues = validate_profile([vs], cgmes3.SV)
    assert not find(issues, prop="VsConverter.uf")


def test_issue_str_and_input_handling():
    net = build_eq(1)
    net["line0"].r = None
    (i,) = validate_profile(net["line0"], cgmes3.EQ, include_reachable=False)
    assert isinstance(i, ProfileIssue)
    assert str(i) == (
        "error: ACLineSegment(mrid='line0') [EQ]: required property ACLineSegment.r is not set"
    )
    with pytest.raises(ValueError):
        validate_profile([], [])
    with pytest.raises(TypeError):
        validate_profile([], ["EQ"])  # type: ignore[list-item]
    with pytest.raises(TypeError):
        validate_profile(["x"], cgmes3.EQ)  # type: ignore[list-item]


def test_does_not_change_object_validate():
    net = build_eq(1)
    before = net["line0"].validate()
    validate_profile(net.values(), cgmes3.EQ)
    assert net["line0"].validate() == before


def test_performance_smoke():
    net = build_eq(2000, topology=True)  # about 14 000 objects
    t = time.perf_counter()
    issues = validate_profile(net.values(), [cgmes3.EQ, cgmes3.TP])
    elapsed = time.perf_counter() - t
    assert issues == []
    assert elapsed < 5.0, elapsed
