"""Light checks of the generated package (M6 adds the exhaustive suite)."""

from __future__ import annotations

import importlib
import re
import subprocess
import sys
import time
from pathlib import Path

import pytest

from cim_python_sdk import _registry
from cim_python_sdk._runtime import CimCompound, CimDatatype, CimEnum, CimObject, resolve

ROOT = Path(__file__).resolve().parents[2]


def _load(ref: str) -> type:
    module, _, name = ref.partition(":")
    return getattr(importlib.import_module(module), name)


@pytest.fixture(scope="module")
def classes() -> dict[str, type]:
    return {guid: _load(ref) for guid, ref in _registry.BY_GUID.items()}


def test_registry_shape(classes):
    assert len(_registry.BY_GUID) == 1937 + 4  # CIM100 + eu (3 classes, LimitKind)
    assert sum(".model.european." in r for r in _registry.BY_GUID.values()) == 4
    assert set(_registry.BY_NAME.values()) <= set(_registry.BY_GUID.values())
    assert _registry.MODEL_VERSIONS["IEC61970CIMVersion"] == "IEC61970CIM17v40"
    assert _registry.MODEL_VERSIONS["ExtIEC61970Version"] == "3.0"
    for guid, cls in classes.items():
        assert cls._cim_meta.guid == guid


def test_every_class_instantiates(classes):
    for cls in classes.values():
        if issubclass(cls, CimEnum):
            for m in cls:
                assert cls(m.value) is m
        elif issubclass(cls, CimDatatype):
            assert cls(1.0).value == 1.0
        elif issubclass(cls, CimCompound):
            cls()
        else:
            assert issubclass(cls, CimObject)
            assert isinstance(cls(), cls)


def test_all_end_targets_resolve(classes):
    for cls in classes.values():
        for end in cls._cim_meta.ends:
            assert resolve(end.target)


def test_terminal_and_conducting_equipment_in_sync():
    from cim_python_sdk import ACLineSegment, Terminal

    ce = ACLineSegment()
    t = Terminal(conducting_equipment=ce)
    assert ce.num_terminal() == 1
    assert ce.terminals == (t,)
    assert t.conducting_equipment is ce
    ce.remove_terminal(t)
    assert t.conducting_equipment is None


def test_attribute_enum_uuid_and_keyword_names():
    import cim_python_sdk
    from cim_python_sdk import FTR, ACLineSegment, Facility, IdentifiedObject, UnitSymbol

    assert ACLineSegment(r=1.0).r == 1.0
    assert UnitSymbol("W") is UnitSymbol.W
    assert re.fullmatch(
        r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}",
        IdentifiedObject().mrid,
    )
    assert FTR(class_="x").class_ == "x"
    assert Facility(kind="warehouse").kind == "warehouse"
    assert "ACLineSegment" in dir(cim_python_sdk)
    with pytest.raises(AttributeError):
        cim_python_sdk.__getattr__("NoSuchClass")


def test_self_association_and_many_to_many():
    from cim_python_sdk import CostType

    parent, child = CostType(), CostType()
    parent.add_child_cost_type(child)
    assert child.parent_cost_type is parent
    assert parent.num_child_cost_type() == 1

    # an N:M pair in the real model: Asset.power_system_resources <-> PowerSystemResource.assets
    from cim_python_sdk import Asset, PowerSystemResource

    a, p = Asset(), PowerSystemResource()
    a.add_power_system_resource(p)
    assert p.assets == (a,)
    assert a.power_system_resources == (p,)
    p.remove_asset(a)
    assert a.num_power_system_resource() == 0


def test_regen_check_is_clean():
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "regen.py"), "--check"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_import_cim_python_sdk_is_fast_and_lazy():
    code = (
        "import time, sys; t = time.perf_counter(); import cim_python_sdk; "
        "ms = (time.perf_counter() - t) * 1000; "
        "print(ms, any(m.startswith('cim_python_sdk.model') or m == 'cim_python_sdk._registry' for m in sys.modules))"
    )
    best = None
    for _ in range(3):
        out = subprocess.run(
            [sys.executable, "-c", code], capture_output=True, text=True, check=True
        )
        ms, loaded = out.stdout.split()
        assert loaded == "False"
        best = float(ms) if best is None else min(best, float(ms))
    assert best < 50


def test_import_all_modules_timing(classes, capsys):
    code = (
        "import time, importlib; from cim_python_sdk import _registry; "
        "t = time.perf_counter(); "
        "[importlib.import_module(r.partition(':')[0]) for r in _registry.BY_GUID.values()]; "
        "print(time.perf_counter() - t)"
    )
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    secs = float(out.stdout)
    with capsys.disabled():
        print(f"\nimport of all {len(_registry.BY_GUID)} modules: {secs:.2f} s")
    assert secs < 10
    assert time.perf_counter() > 0
