"""Association-end integrity, flags and the public API surface of the generated SDK."""

from __future__ import annotations

import importlib

import pytest

import cim_python_sdk
from cim_python_sdk import _registry
from cim_python_sdk._runtime import CimEnum, Many, One, resolve
from tests.sdk.conftest import load_ref
from tests.sdk.test_completeness import check


def test_end_integrity(owned_ends):
    """The inverse exists on the target (or an ancestor), points back, and targets the owner."""
    f = []
    assert len(owned_ends) == 2748 + 6  # CIM100 + eu
    assert sum(e.namespace == "eu" for _, e in owned_ends) == 6
    for owner, e in owned_ends:
        where = f"{owner.__name__}.{e.name}"
        target = resolve(e.target)
        inv = getattr(target, e.inverse, None)
        if not isinstance(inv, (One, Many)):
            f.append(f"{where}: inverse {target.__name__}.{e.inverse} missing")
            continue
        if inv.meta.inverse != e.name:
            f.append(f"{where}: inverse's inverse is {inv.meta.inverse!r}")
        if inv.meta.namespace != e.namespace:
            f.append(f"{where}: namespace {e.namespace} != inverse's {inv.meta.namespace}")
        if not issubclass(owner, resolve(inv.meta.target)):
            f.append(f"{where}: inverse targets {inv.meta.target}, not the owner or an ancestor")
        if getattr(owner, e.name).meta is not e:
            f.append(f"{where}: descriptor meta is not the declared EndMeta")
        # the inverse's inverse resolves back to this very descriptor
        if getattr(resolve(inv.meta.target), inv.meta.inverse) is not getattr(owner, e.name):
            f.append(f"{where}: inverse of inverse is a different descriptor")
        if isinstance(getattr(owner, e.name), Many) != e.many:
            f.append(f"{where}: descriptor type does not match many={e.many}")
        if e.many != (e.upper is None or e.upper > 1):
            f.append(f"{where}: many flag inconsistent with bounds")
    check(f)


def test_many_ends_expose_exactly_their_methods(resolved, by_guid):
    f = []
    for rc in resolved.classes:
        if rc.kind == "primitive":
            continue
        cls = by_guid[rc.guid]
        expected = set()
        for e in rc.ends:
            if not e.many:
                if e.methods:
                    f.append(f"{rc.cim_name}.{e.py_name}: One end lists methods {e.methods}")
                continue
            expected.update(e.methods)
            for m in e.methods:
                if not callable(cls.__dict__.get(m)):
                    f.append(f"{rc.cim_name}.{e.py_name}: method {m} missing")
        own = {
            n
            for n, v in cls.__dict__.items()
            if callable(v) and not n.startswith("_") and not isinstance(v, (One, Many, type))
        }
        if own != expected:
            f.append(f"{rc.cim_name}: public methods differ, extra={sorted(own - expected)[:3]} missing={sorted(expected - own)[:3]}")
    check(f)


def test_deprecated_flags(ir, resolved, by_guid):
    f = []
    ir_attrs = {a.guid: a for c in ir.classifiers if c.kind != "enumeration" for a in c.attributes}
    assert sum(a.deprecated for a in ir_attrs.values()) == 16
    assert sum(c.deprecated for c in ir.classifiers if c.kind == "enumeration") == 1
    assert sum(c.deprecated for c in ir.classifiers if c.kind != "enumeration") == 0
    for c in ir.classifiers:
        if c.kind == "primitive":
            continue
        meta = by_guid[c.guid]._cim_meta
        if meta.deprecated != c.deprecated:
            f.append(f"{c.name}: class deprecated {meta.deprecated} != IR {c.deprecated}")
        if c.kind == "enumeration":
            continue
        for a, m in zip(c.attributes, meta.attributes, strict=True):
            if m.deprecated != a.deprecated:
                f.append(f"{c.name}.{a.name}: deprecated {m.deprecated} != IR {a.deprecated}")
    # the resolved model never deprecates association ends
    for cls in by_guid.values():
        for e in cls._cim_meta.ends:
            if e.deprecated:
                f.append(f"{cls.__name__}.{e.name}: end unexpectedly deprecated")
    check(f)


def test_canonical_names_import_from_top_level(resolved, by_guid):
    f = []
    canonical = [o for o in (*resolved.classes, *resolved.enums) if o.is_canonical and o.kind != "primitive"]
    assert len(canonical) == len(_registry.BY_NAME)
    for o in canonical:
        try:
            got = getattr(cim_python_sdk, o.py_name)
        except AttributeError:
            f.append(f"{o.py_name}: not importable from cim_python_sdk")
            continue
        if got is not by_guid[o.guid]:
            f.append(f"{o.py_name}: top-level object is not the class with guid {o.guid}")
    check(f)
    names = set(dir(cim_python_sdk))
    assert {o.py_name for o in canonical} <= names


def test_non_canonical_duplicates_import_by_module(resolved, by_guid):
    f = []
    dups = [o for o in (*resolved.classes, *resolved.enums) if not o.is_canonical and o.kind != "primitive"]
    assert dups, "the model has duplicate class names"
    canonical_refs = set(_registry.BY_NAME.values())
    assert {o.guid for o in dups} == {g for g, r in _registry.BY_GUID.items() if r not in canonical_refs}
    for o in dups:
        mod = importlib.import_module(o.module)
        cls = getattr(mod, o.py_name, None)
        if cls is not by_guid[o.guid]:
            f.append(f"{o.module}:{o.py_name} is not the class with guid {o.guid}")
        if cls is getattr(cim_python_sdk, o.py_name, None):
            f.append(f"{o.py_name}: duplicate is also the canonical top-level object")
    check(f)


def test_unknown_names():
    for name in ("NoSuchClass", "acLineSegment", "_NoSuch", "__no_such__"):
        with pytest.raises(AttributeError):
            getattr(cim_python_sdk, name)
    assert all(not n.startswith("_") or n.endswith("__") for n in dir(cim_python_sdk))


def test_registry_refs_load_to_matching_classes(by_guid):
    f = []
    for guid, ref in _registry.BY_GUID.items():
        cls = load_ref(ref)
        if cls._cim_meta.guid != guid:
            f.append(f"{ref}: meta guid {cls._cim_meta.guid} != {guid}")
        if issubclass(cls, CimEnum) != (cls._cim_meta.kind == "enumeration"):
            f.append(f"{ref}: enum base does not match meta kind")
    check(f)
