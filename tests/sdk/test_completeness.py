"""The generated SDK is complete and correct against the IR, keyed by GUID."""

from __future__ import annotations

import datetime
import decimal

from cim_python_sdk._runtime import CimCompound, CimDatatype, CimEnum, CimObject, resolve

KIND_BASE = {"class": CimObject, "cimdatatype": CimDatatype, "compound": CimCompound, "enumeration": CimEnum}
PRIM_PY = {
    "Float": "float",
    "String": "str",
    "Boolean": "bool",
    "DateTime": "datetime",
    "Integer": "int",
    "Date": "date",
    "Decimal": "Decimal",
    "Time": "time",
    "MonthDay": "str",
    "Duration": "str",
}


def check(failures: list[str], limit: int = 40) -> None:
    assert not failures, f"{len(failures)} failures:\n" + "\n".join(failures[:limit])


# (CIM100, eu) counts: non-enum classes, enums, attributes, literals, associations
TOTALS = {"cim": (1532, 405, 6334, 3211, 1374), "eu": (3, 1, 11, 11, 3)}


def test_totals(ir, by_guid):
    for ns, (n_cls, n_enum, n_attr, n_lit, n_assoc) in TOTALS.items():
        cls = [c for c in ir.classifiers if c.namespace == ns]
        kinds = [c.kind for c in cls]
        assert kinds.count("class") + kinds.count("cimdatatype") + kinds.count("compound") == n_cls
        assert kinds.count("enumeration") == n_enum
        attrs = [a for c in ir.classifiers if c.kind != "enumeration" for a in c.attributes]
        assert sum(a.namespace == ns for a in attrs) == n_attr
        assert sum(len(c.literals) for c in cls) == n_lit
        assert sum(a.namespace == ns for a in ir.associations) == n_assoc
        gen = [c for c in by_guid.values() if c._cim_meta.namespace == ns]
        assert sum(1 for c in gen if issubclass(c, CimEnum)) == n_enum
        assert sum(1 for c in gen if not issubclass(c, CimEnum)) == n_cls
        assert sum(len(list(c.__members__)) for c in gen if issubclass(c, CimEnum)) == n_lit
        metas = [m for c in by_guid.values() for m in c._cim_meta.attributes]
        assert sum(m.namespace == ns for m in metas) == n_attr
        ends = [e for c in by_guid.values() for e in c._cim_meta.ends]
        assert sum(e.namespace == ns for e in ends) == 2 * n_assoc
    assert {c.namespace for c in ir.classifiers} == set(TOTALS)


def test_classifier_identity(ir, by_guid):
    f = []
    expected = {c.guid: c for c in ir.classifiers if c.kind != "primitive"}
    if set(expected) != set(by_guid):
        f.append(f"guid sets differ: missing={sorted(set(expected) - set(by_guid))[:5]} extra={sorted(set(by_guid) - set(expected))[:5]}")
    for guid, c in expected.items():
        cls = by_guid.get(guid)
        if cls is None:
            continue
        meta = cls.__dict__.get("_cim_meta")
        if meta is None:
            f.append(f"{c.name}: no own _cim_meta")
            continue
        got = (meta.guid, meta.cim_name, meta.package, meta.kind, meta.namespace)
        if got != (guid, c.name, c.package, c.kind, c.namespace):
            f.append(f"{c.name}: meta {got} != IR {(guid, c.name, c.package, c.kind, c.namespace)}")
        if not issubclass(cls, KIND_BASE[c.kind]):
            f.append(f"{c.name}: {cls.__mro__} lacks base for kind {c.kind}")
        if cls.__module__.rsplit(".", 1)[0] != cls.__module__.rsplit(".", 1)[0]:
            f.append(c.name)
    check(f)


def test_superclasses(ir, by_guid):
    f = []
    for c in ir.classifiers:
        if c.kind in ("primitive", "enumeration"):
            continue
        cls = by_guid[c.guid]
        base = cls.__bases__[0]
        if c.superclass is None:
            if base not in (CimObject, CimDatatype, CimCompound):
                f.append(f"{c.name}: expected runtime root base, got {base}")
        elif by_guid.get(c.superclass) is not base:
            f.append(f"{c.name}: base {base.__name__} != IR superclass guid {c.superclass}")
        if len(cls.__bases__) != 1:
            f.append(f"{c.name}: multiple bases {cls.__bases__}")
    check(f)


# IR defaults that cannot be represented in the SDK because the model itself is inconsistent.
# Each entry is (class CIM name, attribute CIM name) and the SDK default must then be None.
KNOWN_MODEL_QUIRKS = {
    # IR default is 'g' but the UnitSymbol enumeration has no 'g' literal (only 'kg').
    ("Mass", "unit"),
}
USED_QUIRKS: set[tuple[str, str]] = set()


def _default_ok(cname, meta, ir_attr, by_guid) -> bool:
    if ir_attr.default is None:
        return meta.default is None
    if (cname, ir_attr.name) in KNOWN_MODEL_QUIRKS:
        USED_QUIRKS.add((cname, ir_attr.name))
        return meta.default is None
    if meta.kind == "enumeration":
        return isinstance(meta.default, CimEnum) and meta.default.value == ir_attr.default and (
            type(meta.default) is by_guid[ir_attr.type_guid]
        )
    if meta.py_type == "date":
        return (
            type(meta.default) is datetime.date and meta.default == datetime.date.fromisoformat(ir_attr.default)
        )
    return str(meta.default) == ir_attr.default or repr(meta.default).strip("'\"") == ir_attr.default.strip("'\"")


def test_attributes(ir, by_guid, ir_classifiers):
    f = []
    for c in ir.classifiers:
        if c.kind in ("primitive", "enumeration"):
            continue
        metas = {a.cim_name: a for a in by_guid[c.guid]._cim_meta.attributes}
        if len(metas) != len(c.attributes):
            f.append(f"{c.name}: {len(metas)} attributes != IR {len(c.attributes)}")
        if [a.cim_name for a in by_guid[c.guid]._cim_meta.attributes] != [a.name for a in c.attributes]:
            f.append(f"{c.name}: attribute order/names differ")
        for a in c.attributes:
            m = metas.get(a.name)
            if m is None:
                f.append(f"{c.name}.{a.name}: missing")
                continue
            t = ir_classifiers[a.type_guid]
            want_type = PRIM_PY[t.name] if t.kind == "primitive" else t.name
            got = (m.lower, m.upper, m.py_type, m.kind, m.static, m.deprecated, m.namespace)
            want = (a.lower, a.upper, want_type, t.kind, a.is_static, a.deprecated, a.namespace)
            if got != want:
                f.append(f"{c.name}.{a.name}: {got} != {want}")
            if not _default_ok(c.name, m, a, by_guid):
                f.append(f"{c.name}.{a.name}: default {m.default!r} != IR {a.default!r}")
    assert USED_QUIRKS == KNOWN_MODEL_QUIRKS, "stale entries in KNOWN_MODEL_QUIRKS"
    check(f)


def test_enums(ir, by_guid, resolved):
    f = []
    total = 0
    py_names = {e.guid: [(l.cim_value, l.py_name) for l in e.literals] for e in resolved.enums}
    for c in ir.classifiers:
        if c.kind != "enumeration":
            continue
        cls = by_guid[c.guid]
        members = list(cls.__members__.values())
        total += len(members)
        if [m.value for m in members] != [l.name for l in c.literals]:
            f.append(f"{c.name}: values differ from IR literals")
        if [(m.value, m.name) for m in members] != py_names[c.guid]:
            f.append(f"{c.name}: member names differ from resolved model")
        if len(list(cls)) != len(members):
            f.append(f"{c.name}: aliased members")
        for m in members:
            if cls(m.value) is not m:
                f.append(f"{c.name}.{m.name}: lookup by value fails")
                break
    assert total == 3211 + 11  # CIM100 + eu (LimitKind)
    check(f)


def test_associations_produce_two_ends(ir, by_guid, resolved):
    f = []
    rend = {(e.association_guid, e.end_index): e for c in resolved.classes for e in c.ends}
    expected_keys = set()
    n = 0
    for assoc in ir.associations:
        for idx, end in enumerate(assoc.ends):
            n += 1
            r = rend.get((assoc.guid, idx))
            if r is None:
                f.append(f"{assoc.guid}[{idx}]: no resolved end")
                continue
            owner = by_guid[end.owner]
            key = (end.owner, r.py_name)
            if key in expected_keys:
                f.append(f"duplicate end {key}")
            expected_keys.add(key)
            m = next((e for e in owner._cim_meta.ends if e.name == r.py_name), None)
            if m is None:
                f.append(f"{owner.__name__}.{r.py_name}: end not generated on owner")
                continue
            if end.role is not None and m.cim_role != end.role:
                f.append(f"{owner.__name__}.{m.name}: cim_role {m.cim_role!r} != {end.role!r}")
            if end.role is None and m.cim_role not in (None, r.py_name) and not r.generated_role:
                f.append(f"{owner.__name__}.{m.name}: unexpected role {m.cim_role!r}")
            if resolve(m.target)._cim_meta.guid != end.target:
                f.append(f"{owner.__name__}.{m.name}: target {m.target} != IR {end.target}")
            many = end.upper is None or end.upper > 1
            if (m.lower, m.upper, m.many) != (end.lower, end.upper, many):
                f.append(f"{owner.__name__}.{m.name}: card {(m.lower, m.upper, m.many)} != {(end.lower, end.upper, many)}")
            if m.namespace != assoc.namespace:
                f.append(f"{owner.__name__}.{m.name}: namespace {m.namespace} != {assoc.namespace}")
    assert n == 2748 + 6  # CIM100 + eu
    actual = {(cls._cim_meta.guid, e.name) for cls in by_guid.values() for e in cls._cim_meta.ends}
    if actual != expected_keys:
        f.append(f"extra/missing ends: {sorted(actual ^ expected_keys)[:5]}")
    check(f)


def test_datatype_value_types(by_guid):
    expected = {"float": float, "int": int, "str": str, "bool": bool, "datetime": datetime.datetime,
                "date": datetime.date, "time": datetime.time, "Decimal": decimal.Decimal}
    f = []
    for cls in by_guid.values():
        if issubclass(cls, CimDatatype):
            vt = getattr(cls, "value_type", None)
            if vt not in expected.values():
                f.append(f"{cls.__name__}: value_type {vt!r}")
    check(f)
