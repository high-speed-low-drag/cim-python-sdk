"""Two-way association maintenance on the mini model (1:1, N:1, N:M, self)."""

from __future__ import annotations

import itertools

import pytest

from cim_python_sdk._runtime import Many, One
from tests.runtime.minimodel.asset import Asset
from tests.runtime.minimodel.conducting_equipment import ConductingEquipment
from tests.runtime.minimodel.facility import Facility
from tests.runtime.minimodel.location import Location
from tests.runtime.minimodel.power_system_resource import PowerSystemResource
from tests.runtime.minimodel.terminal import Terminal

# --------------------------------------------------------------------------- N:1 / 1:N


def test_one_side_set_replace_none():
    ce1, ce2 = ConductingEquipment(), ConductingEquipment()
    t = Terminal()
    assert t.conducting_equipment is None and ce1.terminals == ()

    t.conducting_equipment = ce1
    assert t.conducting_equipment is ce1
    assert ce1.terminals == (t,)

    t.conducting_equipment = ce2  # replace: removed from the old collection
    assert t.conducting_equipment is ce2
    assert ce1.terminals == () and ce2.terminals == (t,)

    t.conducting_equipment = None
    assert t.conducting_equipment is None
    assert ce2.terminals == ()


def test_many_side_add_remove_clear():
    ce1, ce2 = ConductingEquipment(), ConductingEquipment()
    t1, t2, t3 = Terminal(), Terminal(), Terminal()

    assert ce1.add_terminal(t1).add_terminal(t2) is ce1  # chaining
    assert ce1.terminals == (t1, t2)  # insertion order
    assert t1.conducting_equipment is ce1 and t2.conducting_equipment is ce1
    assert ce1.num_terminal() == 2

    ce2.add_terminal(t1)  # steals t1 from ce1
    assert t1.conducting_equipment is ce2
    assert ce1.terminals == (t2,) and ce2.terminals == (t1,)

    ce1.remove_terminal(t2)
    assert t2.conducting_equipment is None and ce1.terminals == ()
    with pytest.raises(ValueError):
        ce1.remove_terminal(t2)
    with pytest.raises(ValueError):
        ce1.remove_terminal(t3)

    ce2.add_terminal(t2).add_terminal(t3)
    assert ce2.clear_terminals() is ce2
    assert ce2.terminals == () and ce2.num_terminal() == 0
    assert all(t.conducting_equipment is None for t in (t1, t2, t3))


def test_get_by_mrid():
    ce = ConductingEquipment()
    t = Terminal(mrid="T1", conducting_equipment=ce)
    assert ce.get_terminal_by_mrid("T1") is t
    assert ce.get_terminal_by_mrid("nope") is None
    assert ConductingEquipment().get_terminal_by_mrid("T1") is None


def test_idempotent():
    ce = ConductingEquipment()
    t = Terminal()
    ce.add_terminal(t)
    ce.add_terminal(t)
    t.conducting_equipment = ce
    assert ce.terminals == (t,) and t.conducting_equipment is ce
    a, loc = Asset(), Location()
    a.location = loc
    a.location = loc
    loc.asset = a
    assert a.location is loc and loc.asset is a
    psr = PowerSystemResource()
    a.add_power_system_resource(psr).add_power_system_resource(psr)
    psr.add_asset(a)
    assert a.power_system_resources == (psr,) and psr.assets == (a,)


# --------------------------------------------------------------------------- 1:1


def test_one_to_one():
    a1, a2 = Asset(), Asset()
    l1, l2 = Location(), Location()
    a1.location = l1
    assert l1.asset is a1
    a2.location = l1  # l1 moves to a2; a1 loses it
    assert a1.location is None and a2.location is l1 and l1.asset is a2
    l2.asset = a2  # a2 switches to l2; l1 is released
    assert a2.location is l2 and l2.asset is a2 and l1.asset is None
    a1.location = l2  # steals l2: a2 and l1 both end up empty
    assert a1.location is l2 and l2.asset is a1 and a2.location is None and l1.asset is None
    del a1.location
    assert a1.location is None and l2.asset is None


# --------------------------------------------------------------------------- N:M


def test_many_to_many():
    a1, a2 = Asset(), Asset()
    p1, p2 = PowerSystemResource(), PowerSystemResource()
    a1.add_power_system_resource(p1).add_power_system_resource(p2)
    p1.add_asset(a2)
    assert a1.power_system_resources == (p1, p2)
    assert p1.assets == (a1, a2) and p2.assets == (a1,)
    p1.remove_asset(a1)
    assert a1.power_system_resources == (p2,) and p1.assets == (a2,)
    p2.clear_assets()
    assert a1.power_system_resources == () and p2.assets == ()
    a2.clear_power_system_resources()
    assert p1.assets == ()


# --------------------------------------------------------------------------- self-associations


def test_self_association():
    root, mid, leaf = PowerSystemResource(), PowerSystemResource(), PowerSystemResource()
    mid.parent = root
    root.add_child(leaf)
    assert root.children == (mid, leaf) and mid.parent is root and leaf.parent is root
    leaf.parent = mid
    assert root.children == (mid,) and mid.children == (leaf,)
    mid.remove_child(leaf)
    assert leaf.parent is None and mid.children == ()


def test_self_link_same_object():
    p = PowerSystemResource()
    p.parent = p
    assert p.parent is p and p.children == (p,)
    p.add_child(p)  # idempotent
    assert p.children == (p,)
    other = PowerSystemResource()
    p.parent = other
    assert p.children == () and other.children == (p,) and p.parent is other
    p.add_child(p)
    assert p.parent is p and other.children == ()
    p.clear_children()
    assert p.parent is None and p.children == ()
    p.add_child(p)
    p.remove_child(p)
    assert p.parent is None and p.children == ()


def test_symmetric_end_is_its_own_inverse():
    """An end whose inverse is itself (not in CIM100, but the runtime must cope)."""
    from cim_python_sdk._runtime import ClassMeta, EndMeta
    from tests.runtime.minimodel.identified_object import IdentifiedObject

    class Peer(IdentifiedObject):
        __slots__ = ("_friends", "_partner")
        partner: One[Peer] = One(EndMeta("partner", "Partner", "x:Peer", False, 0, 1, "partner"))
        friends: Many[Peer] = Many(EndMeta("friends", "Friends", "x:Peer", True, 0, None, "friends"))
        _cim_meta = ClassMeta("Peer", "test", "{peer}", ends=(partner.meta, friends.meta))

    Peer.partner._cls = Peer  # local class: not importable by its string reference
    Peer.friends._cls = Peer
    a, b, c, d = Peer(), Peer(), Peer(), Peer()
    a.partner, c.partner = b, d
    assert b.partner is a and d.partner is c
    a.partner = c  # breaks a-b and c-d
    assert a.partner is c and c.partner is a and b.partner is None and d.partner is None
    a.partner = a
    assert a.partner is a and c.partner is None
    Peer.friends.add(a, b)
    Peer.friends.add(a, a)
    assert a.friends == (b, a) and b.friends == (a,)
    Peer.friends.clear(a)
    assert a.friends == () and b.friends == ()


# --------------------------------------------------------------------------- construction


def test_kwargs_construction_links_both_ends():
    t1, t2 = Terminal(), Terminal()
    ce = ConductingEquipment(name="ce", nominal_voltage=11.0, terminals=[t1, t2])
    assert ce.terminals == (t1, t2) and t1.conducting_equipment is ce
    t3 = Terminal(conducting_equipment=ce, sequence_number=3)
    assert ce.terminals == (t1, t2, t3)
    loc = Location()
    a = Asset(location=loc, power_system_resources=(ce,))
    assert loc.asset is a and ce.assets == (a,)
    child = PowerSystemResource(parent=ce)
    assert ce.children == (child,)
    gen = (t for t in [Terminal()])
    assert len(ConductingEquipment(terminals=gen).terminals) == 1  # any iterable


def test_none_and_missing_kwargs_have_no_side_effects():
    ce = ConductingEquipment(terminals=None)
    t = Terminal(conducting_equipment=None)
    assert ce.terminals == () and t.conducting_equipment is None
    for obj in (ce, t, Asset(), Location(), PowerSystemResource()):
        for name in ("_terminals", "_conducting_equipment", "_location", "_asset", "_parent"):
            if hasattr(type(obj), name):
                assert not hasattr(obj, name), "private end slots stay unset (lazy)"


def test_defaults_and_mrid():
    a = Asset()
    assert a.kind.name == "other" and a.date is None and a.name is None
    assert isinstance(a.mrid, str) and len(a.mrid) == 36
    assert Asset().mrid != a.mrid
    assert Asset(mrid="m1").mrid == "m1"
    f = Facility()
    assert f.kind is None  # the override's default wins over Asset's enum default
    assert Facility(kind="building").kind == "building"


def test_unknown_kwargs():
    with pytest.raises(TypeError, match="'bogus'"):
        Terminal(bogus=1)
    with pytest.raises(TypeError, match="'x', 'y'"):
        ConductingEquipment(name="n", x=1, y=2)
    with pytest.raises(TypeError):
        Terminal("positional")  # type: ignore[misc]


# --------------------------------------------------------------------------- type errors


def test_type_errors():
    t = Terminal()
    with pytest.raises(TypeError, match="expects ConductingEquipment, got Terminal"):
        t.conducting_equipment = Terminal()  # type: ignore[assignment]
    with pytest.raises(TypeError, match="expects Terminal"):
        ConductingEquipment().add_terminal(ConductingEquipment())  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        ConductingEquipment(terminals=[object()])  # type: ignore[list-item]
    with pytest.raises(TypeError):
        Asset(location="nowhere")  # type: ignore[arg-type]
    assert t.conducting_equipment is None
    # subclasses of the target are accepted
    p = PowerSystemResource()
    p.add_child(ConductingEquipment())
    assert p.num_child() == 1


def test_many_end_is_read_only():
    ce = ConductingEquipment()
    with pytest.raises(AttributeError, match="read-only"):
        ce.terminals = ()  # type: ignore[misc]


# --------------------------------------------------------------------------- iteration, recursion


def test_mutation_during_iteration():
    ce = ConductingEquipment(terminals=[Terminal() for _ in range(5)])
    for t in ce.terminals:
        ce.remove_terminal(t)
    assert ce.terminals == ()
    ce2 = ConductingEquipment(terminals=[Terminal() for _ in range(3)])
    seen = 0
    for _ in ce2.terminals:
        ce2.add_terminal(Terminal())
        seen += 1
    assert seen == 3 and ce2.num_terminal() == 6


def test_no_recursion(monkeypatch):
    """Every public operation does a bounded number of one-sided writes, never nested."""
    state = {"calls": 0, "depth": 0, "max_depth": 0}
    for cls in (One, Many):
        for name in ("_raw_add", "_raw_remove"):
            orig = getattr(cls, name)

            def wrapped(self, obj, other, _f=orig):
                state["calls"] += 1
                state["depth"] += 1
                state["max_depth"] = max(state["max_depth"], state["depth"])
                try:
                    return _f(self, obj, other)
                finally:
                    state["depth"] -= 1

            monkeypatch.setattr(cls, name, wrapped)

    def calls(op):
        state["calls"] = 0
        op()
        return state["calls"]

    ce1, ce2, t = ConductingEquipment(), ConductingEquipment(), Terminal()
    assert calls(lambda: setattr(t, "conducting_equipment", ce1)) == 1  # inverse write only
    assert calls(lambda: setattr(t, "conducting_equipment", ce2)) == 2  # + cleanup of ce1
    assert calls(lambda: ce1.add_terminal(t)) == 3  # both sides + cleanup of ce2
    assert calls(lambda: ce1.remove_terminal(t)) == 2
    a, b = Asset(), Location()
    assert calls(lambda: setattr(a, "location", b)) == 1
    assert calls(lambda: a.add_power_system_resource(ce1)) == 2
    assert state["max_depth"] == 1


def test_long_chain_does_not_recurse():
    nodes = [PowerSystemResource() for _ in range(5000)]
    for parent, child in itertools.pairwise(nodes):
        child.parent = parent
    for n in nodes:
        n.parent = None
    assert all(n.children == () for n in nodes)
