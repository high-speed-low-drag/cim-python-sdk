"""CGMES European extensions (namespace eu) as members of the generated model."""

from __future__ import annotations

import cim_python_sdk
from cim_python_sdk import (
    ACLineSegment,
    BoundaryPoint,
    ConnectivityNode,
    LimitKind,
    OperationalLimitType,
    PowerSystemResource,
    SolarGeneratingUnit,
    SolarPowerPlant,
    WindGeneratingUnit,
    WindPowerPlant,
    _registry,
)
from cim_python_sdk._runtime import (
    NAMESPACES,
    AttrMeta,
    ClassMeta,
    EndMeta,
    cim_attributes,
    cim_ends,
)

EU = "http://iec.ch/TC57/CIM100-European#"


def _attr(cls, cim_name):
    return next(a for a in cim_attributes(cls) if a.cim_name == cim_name)


def _end(cls, role):
    return next(e for e in cim_ends(cls) if e.cim_role == role)


def test_namespaces_and_defaults():
    assert NAMESPACES == {"cim": "http://iec.ch/TC57/CIM100#", "eu": EU}
    # existing callers that build metas without a namespace get cim
    assert ClassMeta("X", "P", "{G}").namespace == "cim"
    assert AttrMeta("x", "x", "str", 0, 1, "primitive").namespace == "cim"
    assert EndMeta("e", "E", "m:C", False, 0, 1, "i").namespace == "cim"
    assert ACLineSegment._cim_meta.namespace == "cim"


def test_classes_and_enum():
    for cls in (BoundaryPoint, SolarPowerPlant, WindPowerPlant, LimitKind):
        assert cls._cim_meta.namespace == "eu"
        assert cls.__module__.startswith("cim_python_sdk.model.european.")
        assert getattr(cim_python_sdk, cls.__name__) is cls
    for cls in (BoundaryPoint, SolarPowerPlant, WindPowerPlant):
        assert cls.__mro__[1] is PowerSystemResource
    assert [m.value for m in LimitKind] == [
        "patl",
        "patlt",
        "tatl",
        "tc",
        "tct",
        "highVoltage",
        "lowVoltage",
        "operationalVoltageLimit",
        "alarmVoltage",
        "warningVoltage",
        "stability",
    ]
    assert _registry.MODEL_VERSIONS["ExtIEC61970Version"] == "3.0"


def test_boundary_point_attributes():
    names = [a.cim_name for a in BoundaryPoint._cim_meta.attributes]
    assert names == [
        "fromEndIsoCode",
        "fromEndName",
        "fromEndNameTso",
        "toEndIsoCode",
        "toEndName",
        "toEndNameTso",
        "isDirectCurrent",
        "isExcludedFromAreaInterchange",
    ]
    assert all(a.namespace == "eu" for a in BoundaryPoint._cim_meta.attributes)
    assert _attr(BoundaryPoint, "isDirectCurrent").py_type == "bool"
    assert _attr(BoundaryPoint, "name").namespace == "cim"  # inherited CIM member
    bp = BoundaryPoint(from_end_iso_code="NO", to_end_iso_code="SE", is_direct_current=False)
    assert (bp.from_end_iso_code, bp.to_end_iso_code, bp.is_direct_current) == ("NO", "SE", False)


def test_extension_attributes_on_cim_classes():
    line = ACLineSegment(name="L1", short_name="L1s", energy_ident_code_eic="10T-NO-SE-00001")
    assert (line.short_name, line.energy_ident_code_eic) == ("L1s", "10T-NO-SE-00001")
    short = _attr(ACLineSegment, "shortName")
    assert (short.name, short.py_type, short.lower, short.upper) == ("short_name", "str", 0, 1)
    assert short.namespace == "eu" and _attr(ACLineSegment, "energyIdentCodeEic").namespace == "eu"
    kind = _attr(OperationalLimitType, "kind")
    assert (kind.py_type, kind.kind, kind.namespace) == ("LimitKind", "enumeration", "eu")
    olt = OperationalLimitType(kind=LimitKind.patl)
    assert olt.kind is LimitKind.patl


def test_links_both_ways():
    cn = ConnectivityNode()
    bp = BoundaryPoint(connectivity_node=cn)
    assert cn.boundary_point is bp
    cn.boundary_point = None
    assert bp.connectivity_node is None
    end = _end(BoundaryPoint, "ConnectivityNode")
    assert (end.lower, end.upper, end.inverse, end.namespace) == (1, 1, "boundary_point", "eu")
    assert _end(ConnectivityNode, "BoundaryPoint").namespace == "eu"

    wpp = WindPowerPlant()
    w1, w2 = WindGeneratingUnit(), WindGeneratingUnit(wind_power_plant=wpp)
    wpp.add_wind_generating_unit(w1)
    assert set(wpp.wind_generating_units) == {w1, w2} and w1.wind_power_plant is wpp
    w2.wind_power_plant = None
    assert wpp.wind_generating_units == (w1,) and wpp.num_wind_generating_unit() == 1
    assert _end(WindGeneratingUnit, "WindPowerPlant").namespace == "eu"

    spp = SolarPowerPlant(solar_generating_units=[SolarGeneratingUnit()])
    (s,) = spp.solar_generating_units
    assert s.solar_power_plant is spp
    spp.clear_solar_generating_units()
    assert s.solar_power_plant is None
