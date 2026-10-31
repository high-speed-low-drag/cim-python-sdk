"""Metadata, validate(), value types, resolution and import cost of `cim_python_sdk._runtime`."""

from __future__ import annotations

import datetime as _dt
import subprocess
import sys
import time

import pytest

from cim_python_sdk._runtime import (
    AttrMeta,
    CimObject,
    ClassMeta,
    EndMeta,
    Many,
    One,
    all_metas,
    cim_attributes,
    cim_ends,
    resolve,
)
from tests.runtime.minimodel import asset as asset_module
from tests.runtime.minimodel._registry import REGISTRY
from tests.runtime.minimodel.asset import Asset
from tests.runtime.minimodel.asset_kind import AssetKind
from tests.runtime.minimodel.conducting_equipment import ConductingEquipment
from tests.runtime.minimodel.facility import Facility
from tests.runtime.minimodel.identified_object import IdentifiedObject
from tests.runtime.minimodel.location import Location
from tests.runtime.minimodel.power_system_resource import PowerSystemResource
from tests.runtime.minimodel.street_address import StreetAddress
from tests.runtime.minimodel.terminal import Terminal
from tests.runtime.minimodel.unit_symbol import UnitSymbol
from tests.runtime.minimodel.voltage import Voltage

# --------------------------------------------------------------------------- metas


def test_class_meta_and_mro_helpers():
    m = ConductingEquipment._cim_meta
    assert m.cim_name == "ConductingEquipment" and m.kind == "class" and not m.deprecated
    assert [x.cim_name for x in all_metas(ConductingEquipment)] == [
        "IdentifiedObject",
        "PowerSystemResource",
        "ConductingEquipment",
    ]
    assert [a.name for a in cim_attributes(ConductingEquipment)] == [
        "description",
        "mrid",
        "name",
        "nominal_voltage",
    ]
    assert [e.name for e in cim_ends(ConductingEquipment)] == [
        "assets",
        "children",
        "parent",
        "terminals",
    ]
    end = cim_ends(Terminal)[0]
    assert (end.target, end.many, end.lower, end.upper, end.inverse) == (
        "tests.runtime.minimodel.conducting_equipment:ConductingEquipment",
        False,
        1,
        1,
        "terminals",
    )
    assert Terminal.conducting_equipment.meta is end


def test_override_replaces_inherited_attribute_meta():
    kinds = [a for a in cim_attributes(Facility) if a.name == "kind"]
    assert len(kinds) == 1 and kinds[0].py_type == "str"
    assert [a.name for a in cim_attributes(Facility)] == [a.name for a in cim_attributes(Asset)]
    assert "kind" not in Facility.__slots__ and Facility.__slots__ == ()
    assert next(a for a in cim_attributes(Asset) if a.name == "kind").default is AssetKind.other


def test_metas_are_frozen_values():
    a = AttrMeta("x", "X", "str", 0, 1, "primitive")
    assert a == AttrMeta("x", "X", "str", 0, 1, "primitive") and hash(a) == hash(
        AttrMeta("x", "X", "str", 0, 1, "primitive")
    )
    with pytest.raises(AttributeError):
        a.name = "y"  # type: ignore[misc]
    with pytest.raises(AttributeError):
        del a.lower
    assert "cim_name='X'" in repr(a)
    assert ClassMeta("C", "p", "g", ends=[EndMeta("e", None, "m:C", True, 0, None, "f")]).ends[0].name


def test_registry_resolves_to_classes_with_matching_guid():
    for guid, ref in REGISTRY.items():
        cls = resolve(ref)
        assert cls._cim_meta.guid == guid, ref
        assert resolve(ref) is cls  # cached
    assert resolve(Terminal) is Terminal
    with pytest.raises(ValueError):
        resolve("no_colon")
    with pytest.raises(ModuleNotFoundError):
        resolve("tests.runtime.minimodel.nope:X")
    with pytest.raises(AttributeError):
        resolve("tests.runtime.minimodel.terminal:Nope")
    with pytest.raises(TypeError):
        resolve("tests.runtime.minimodel.terminal:TYPE_CHECKING")


def test_end_descriptor_contract_errors():
    with pytest.raises(TypeError, match="__slots__ must contain '_x'"):

        class Bad(CimObject):
            __slots__ = ()
            x = One(EndMeta("x", None, "m:C", False, 0, 1, "y"))

    with pytest.raises(TypeError, match="named 'y'"):

        class Bad2(CimObject):
            __slots__ = ("_x",)
            x = One(EndMeta("y", None, "m:C", False, 0, 1, "y"))

    with pytest.raises(TypeError, match="many"):
        One(EndMeta("x", None, "m:C", True, 0, None, "y"))
    with pytest.raises(TypeError, match="many"):
        Many(EndMeta("x", None, "m:C", False, 0, 1, "y"))


def test_bad_inverse_detected_on_first_use():
    class Lonely(CimObject):
        __slots__ = ("_terminal",)
        terminal = One(
            EndMeta(
                "terminal", None, "tests.runtime.minimodel.terminal:Terminal", False, 0, 1, "nope"
            )
        )

    with pytest.raises(TypeError, match="not an association end"):
        Lonely().terminal = Terminal()

    class Impostor(CimObject):  # claims Terminal.conducting_equipment as its inverse
        __slots__ = ("_terminals",)
        terminals = Many(
            EndMeta(
                "terminals",
                None,
                "tests.runtime.minimodel.terminal:Terminal",
                True,
                0,
                None,
                "conducting_equipment",
            )
        )

    with pytest.raises(TypeError, match="not inverses"):
        Impostor.terminals.add(Impostor(), Terminal())


# --------------------------------------------------------------------------- object protocol


def test_slots_only_no_instance_dict():
    for cls in (Terminal, ConductingEquipment, Asset, Facility, Location, PowerSystemResource):
        obj = cls()
        assert not hasattr(obj, "__dict__"), cls
        with pytest.raises(AttributeError):
            obj.not_an_attribute = 1  # type: ignore[attr-defined]
    with pytest.raises(AttributeError):
        StreetAddress().x = 1  # type: ignore[attr-defined]


def test_repr_eq_hash_identity():
    t = Terminal(mrid="abc")
    assert repr(t) == "Terminal(mrid='abc')"
    t.mrid = None
    assert repr(t).startswith("Terminal(id=0x")
    a, b = Terminal(mrid="same"), Terminal(mrid="same")
    assert a != b and len({a, b, a}) == 2
    assert hash(a) == object.__hash__(a)


def test_attribute_named_like_an_import_resolves_in_class_namespace():
    """`date: _dt.date` stays correct even though `date` is also a slot name."""
    ns = {**vars(asset_module), "_dt": _dt}  # module globals as a type checker sees them
    ann = Asset.__annotations__["date"]
    assert eval(ann, ns, dict(vars(Asset))) == _dt.date | None
    assert eval("date", ns, dict(vars(Asset))) is Asset.__dict__["date"]  # what a bare name would hit
    a = Asset(date=_dt.date(2026, 1, 2))
    assert a.date == _dt.date(2026, 1, 2)


# --------------------------------------------------------------------------- validate


def test_validate_reports_lower_and_upper_bounds():
    t = Terminal()
    issues = t.validate()
    assert any("'sequence_number'" in i and "required attribute" in i for i in issues)
    assert any("'conducting_equipment'" in i and "not set" in i for i in issues)
    t.sequence_number = 1
    t.conducting_equipment = ConductingEquipment()
    assert t.validate() == []

    a = Asset()
    assert a.validate() == [f"{a!r}: 'power_system_resources' has 0 item(s), needs at least 1"]
    a.add_power_system_resource(PowerSystemResource())
    assert a.validate() == []

    p = PowerSystemResource(children=[PowerSystemResource() for _ in range(3)])
    assert p.validate() == [f"{p!r}: 'children' has 3 item(s), allows at most 2"]
    assert IdentifiedObject().validate() == []


def test_validate_never_raises():
    t = Terminal(sequence_number=1)
    del t.mrid
    del t.sequence_number  # an unset slot counts as missing
    assert any("sequence_number" in i for i in t.validate())

    class Broken(CimObject):
        __slots__ = ()
        _cim_meta = ClassMeta("Broken", "p", "g", ends=(EndMeta("ghost", None, "m:C", True, 1, None, "x"),))

    issues = Broken().validate()
    assert len(issues) == 1 and "validate() failed" in issues[0]


# --------------------------------------------------------------------------- value types


def test_enum():
    assert str(AssetKind.v3phase_transformer) == "3phaseTransformer"
    assert AssetKind("3phaseTransformer") is AssetKind.v3phase_transformer
    assert [m.name for m in AssetKind] == ["breaker", "other", "v3phase_transformer"]
    assert AssetKind._cim_meta.kind == "enumeration"
    assert all_metas(AssetKind) == (AssetKind._cim_meta,)


def test_compound():
    s = StreetAddress(town="Arnhem", street="Main 1")
    assert s.postal_code is None and s.town == "Arnhem"
    assert s == StreetAddress(street="Main 1", town="Arnhem")
    assert s != StreetAddress(town="Arnhem")
    assert repr(s) == "StreetAddress(street='Main 1', town='Arnhem')"
    with pytest.raises(TypeError, match="'country'"):
        StreetAddress(country="NL")
    with pytest.raises(TypeError):
        hash(s)
    loc = Location(main_address=s)
    assert loc.main_address is s


def test_datatype():
    assert Voltage.value_type is float and Voltage.unit is UnitSymbol.V
    assert Voltage.multiplier is None and Voltage._cim_meta.kind == "cimdatatype"
    assert Voltage(1.5) == Voltage(1.5) and Voltage(1.5) != Voltage(2.0)
    assert repr(Voltage(1.5)) == "Voltage(1.5)"
    unit = next(a for a in cim_attributes(Voltage) if a.name == "unit")
    assert unit.static and unit.default is UnitSymbol.V
    # attributes typed by a datatype hold the plain value
    ce = ConductingEquipment(nominal_voltage=11.0)
    assert ce.nominal_voltage == 11.0
    nv = next(a for a in cim_attributes(ConductingEquipment) if a.name == "nominal_voltage")
    assert (nv.kind, nv.py_type) == ("cimdatatype", "Voltage")


# --------------------------------------------------------------------------- import cost


def test_runtime_import_is_light_and_does_not_load_generated_code():
    code = (
        "import sys, cim_python_sdk._runtime; "
        "bad = [m for m in sys.modules if m.startswith(('cim_python_sdk.model', 'cim_python_sdk._registry'))]; "
        "assert not bad, bad; assert 'typing' not in sys.modules"
    )
    subprocess.run([sys.executable, "-c", code], check=True)

    def wall(c: str) -> float:
        t = time.perf_counter()
        subprocess.run([sys.executable, "-c", c], check=True)
        return time.perf_counter() - t

    deltas = [wall("import cim_python_sdk._runtime") - wall("pass") for _ in range(5)]
    assert min(deltas) < 0.020, deltas


def test_new_mrid_is_uuid4_and_unique():
    import uuid

    from cim_python_sdk._runtime import new_mrid

    ids = {new_mrid() for _ in range(20_000)}
    assert len(ids) == 20_000
    u = uuid.UUID(next(iter(ids)))
    assert u.version == 4 and u.variant == uuid.RFC_4122 and str(u) in ids
