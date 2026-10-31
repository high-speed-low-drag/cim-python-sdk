"""Every association links and unlinks symmetrically through the public API."""

from __future__ import annotations

from tests.sdk.test_completeness import check


def _link(obj, end, other) -> None:
    if end.many:
        getattr(obj, end.methods[0])(other)  # add_<item>
    else:
        setattr(obj, end.py_name, other)


def _unlink(obj, end, other) -> None:
    if end.many:
        getattr(obj, end.methods[1])(other)  # remove_<item>
    else:
        setattr(obj, end.py_name, None)


def _sees(obj, name: str, many: bool, other) -> bool:
    v = getattr(obj, name)
    return any(x is other for x in v) if many else v is other


def _clean(obj, name: str, many: bool) -> bool:
    v = getattr(obj, name)
    return v == () if many else v is None


def test_link_unlink_every_association(ir, resolved, by_guid):
    ends = {(e.association_guid, e.end_index): e for c in resolved.classes for e in c.ends}
    by_owner_name = {(c.guid, e.py_name): e for c in resolved.classes for e in c.ends}
    f = []
    n_assoc = 0
    n_links = 0
    for assoc in ir.associations:
        n_assoc += 1
        for idx in (0, 1):
            e = ends[(assoc.guid, idx)]
            inv = by_owner_name[e.inverse]
            owner_cls = by_guid[e.owner_guid]
            target_cls = by_guid[e.target_guid]
            where = f"{owner_cls.__name__}.{e.py_name} <-> {target_cls.__name__}.{inv.py_name}"
            if (inv.owner_guid, inv.py_name) == (e.owner_guid, e.py_name):
                f.append(f"{where}: an end is its own inverse")
                continue
            try:
                a, b = owner_cls(), target_cls()
                _link(a, e, b)
                n_links += 1
                if not _sees(a, e.py_name, e.many, b):
                    f.append(f"{where}: owner side does not see the link")
                if not _sees(b, inv.py_name, inv.many, a):
                    f.append(f"{where}: inverse side does not see the link")
                if e.many and getattr(a, e.methods[3])() != 1:  # num_<item>
                    f.append(f"{where}: num_* is not 1 after linking")
                _unlink(a, e, b)
                if not _clean(a, e.py_name, e.many):
                    f.append(f"{where}: owner side not clean after unlink")
                if not _clean(b, inv.py_name, inv.many):
                    f.append(f"{where}: inverse side not clean after unlink")
                # now link from the other side and unlink from this one
                _link(b, inv, a)
                if not (_sees(a, e.py_name, e.many, b) and _sees(b, inv.py_name, inv.many, a)):
                    f.append(f"{where}: link made from the inverse side is not symmetric")
                _unlink(a, e, b)
                if not (_clean(a, e.py_name, e.many) and _clean(b, inv.py_name, inv.many)):
                    f.append(f"{where}: unlink from the owner side after inverse link is not clean")
            except Exception as exc:  # noqa: BLE001 - collect, do not stop at the first failure
                f.append(f"{where}: {type(exc).__name__}: {exc}")
    assert n_assoc == 1374 + 3  # CIM100 + eu
    assert n_links == 2748 + 6
    check(f)


def test_self_associations_use_distinct_instances(ir, resolved, by_guid):
    ends = {(e.association_guid, e.end_index): e for c in resolved.classes for e in c.ends}
    f = []
    n = 0
    for assoc in ir.associations:
        e0, e1 = ends[(assoc.guid, 0)], ends[(assoc.guid, 1)]
        if e0.owner_guid != e0.target_guid or e1.owner_guid != e1.target_guid:
            continue
        n += 1
        cls = by_guid[e0.owner_guid]
        a, b = cls(), cls()
        try:
            _link(a, e0, b)
            if not (_sees(a, e0.py_name, e0.many, b) and _sees(b, e1.py_name, e1.many, a)):
                f.append(f"{cls.__name__}.{e0.py_name}: self-association not symmetric")
            if _sees(a, e1.py_name, e1.many, a) or _sees(b, e0.py_name, e0.many, b):
                f.append(f"{cls.__name__}.{e0.py_name}: link leaked onto the wrong instance")
            _unlink(a, e0, b)
            if not (_clean(a, e0.py_name, e0.many) and _clean(b, e1.py_name, e1.many)):
                f.append(f"{cls.__name__}.{e0.py_name}: not clean after unlink")
        except Exception as exc:  # noqa: BLE001
            f.append(f"{cls.__name__}.{e0.py_name}: {type(exc).__name__}: {exc}")
    assert n >= 14  # M2 review found 14 self-associations
    check(f)


def test_by_mrid_lookup_on_many_ends(resolved, by_guid):
    f = []
    n = 0
    for c in resolved.classes:
        for e in c.ends:
            getter = next((m for m in e.methods if m.endswith("_by_mrid")), None)
            if getter is None:
                continue
            n += 1
            owner, target = by_guid[c.guid](), by_guid[e.target_guid]()
            target.mrid = "m-1"
            getattr(owner, e.methods[0])(target)
            if getattr(owner, getter)("m-1") is not target or getattr(owner, getter)("other") is not None:
                f.append(f"{c.cim_name}.{e.py_name}: {getter} lookup wrong")
    assert n > 0
    check(f)
