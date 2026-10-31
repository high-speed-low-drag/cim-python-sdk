"""deepcopy / pickle / copy semantics, atomic extend, resolution errors, weakref, deprecated."""

from __future__ import annotations

import copy
import gc
import pickle
import weakref

import pytest

from cim_python_sdk._runtime import (
    AttrMeta,
    CimObject,
    ClassMeta,
    EndMeta,
    One,
    cim_attributes,
    cim_ends,
)
from tests.runtime.minimodel.asset import Asset
from tests.runtime.minimodel.conducting_equipment import ConductingEquipment
from tests.runtime.minimodel.conductor import Conductor
from tests.runtime.minimodel.power_system_resource import PowerSystemResource
from tests.runtime.minimodel.terminal import Terminal


def _roundtrip_deep(x):
    return copy.deepcopy(x)


def _roundtrip_pickle(x):
    return pickle.loads(pickle.dumps(x, protocol=pickle.HIGHEST_PROTOCOL))


@pytest.fixture(params=[_roundtrip_deep, _roundtrip_pickle], ids=["deepcopy", "pickle"])
def clone(request):
    return request.param


def _graph():
    ce = ConductingEquipment(mrid="ce", nominal_voltage=11.0)
    t1, t2 = Terminal(mrid="t1", sequence_number=1), Terminal(mrid="t2", sequence_number=2)
    ce.add_terminal(t1).add_terminal(t2)  # N:1
    a1, a2 = Asset(mrid="a1"), Asset(mrid="a2")
    a1.add_power_system_resource(ce).add_power_system_resource(PowerSystemResource(mrid="p"))
    a2.add_power_system_resource(ce)  # N:M
    root, c1, c2 = (PowerSystemResource(mrid=m) for m in ("root", "c1", "c2"))
    root.add_child(c1).add_child(c2)  # self-association
    return {"ce": ce, "t": (t1, t2), "a": (a1, a2), "tree": (root, c1, c2)}


def test_roundtrip_graph_consistent_and_original_untouched(clone):
    g = _graph()
    ce, (t1, t2), (root, c1, c2) = g["ce"], g["t"], g["tree"]
    ce2, ts2, as2, tree2 = clone((ce, g["t"], g["a"], g["tree"]))
    t1b, t2b = ts2
    a1b, a2b = as2
    rootb, c1b, c2b = tree2

    assert ce2 is not ce and ce2.terminals == (t1b, t2b)
    assert t1b.conducting_equipment is ce2 and t2b.conducting_equipment is ce2
    assert ce2.nominal_voltage == 11.0 and ce2.mrid == "ce"
    assert a1b.power_system_resources[0] is ce2 and ce2 in a2b.power_system_resources
    assert set(ce2.assets) == {a1b, a2b}
    assert rootb.children == (c1b, c2b) and c1b.parent is rootb
    # no object is shared with the original
    assert not ({id(t1), id(t2), id(ce)} & {id(x) for x in ce2.terminals + (ce2,)})
    # original untouched
    assert ce.terminals == (t1, t2) and t1.conducting_equipment is ce
    assert root.children == (c1, c2) and c1.parent is root


def test_restored_many_ends_remove_and_add(clone):
    g = _graph()
    ce = g["ce"]
    ce2, (t1b, t2b) = clone((ce, g["t"]))

    ce2.remove_terminal(t1b)  # would raise ValueError with stale id keys
    assert ce2.terminals == (t2b,) and t1b.conducting_equipment is None
    ce2.add_terminal(t1b)
    assert ce2.terminals == (t2b, t1b) and t1b.conducting_equipment is ce2
    ce2.add_terminal(t1b)  # idempotent: id keys are fresh
    assert ce2.num_terminal() == 2
    new = Terminal()
    ce2.add_terminal(new)
    ce2.clear_terminals()
    assert ce2.terminals == () and new.conducting_equipment is None
    # original unaffected by all of the above
    assert len(ce.terminals) == 2 and all(t.conducting_equipment is ce for t in ce.terminals)


def test_restored_self_association_and_nm(clone):
    g = _graph()
    rootb, c1b, c2b = clone(g["tree"])
    rootb.remove_child(c1b)
    assert c1b.parent is None and rootb.children == (c2b,)
    c1b.parent = rootb
    assert rootb.children == (c2b, c1b)
    ce_b, (a1b, a2b) = clone((g["ce"], g["a"]))
    a1b.remove_power_system_resource(ce_b)
    assert ce_b not in a1b.power_system_resources and a1b not in ce_b.assets
    assert a2b in ce_b.assets


def test_roundtrip_subclass_and_unset_slots(clone):
    c = Conductor(mrid="c")
    c2 = clone(c)
    assert type(c2) is Conductor and c2.mrid == "c" and c2.terminals == ()
    c2.add_terminal(Terminal())
    assert c.terminals == ()
    lone = ConductingEquipment.__new__(ConductingEquipment)  # nothing set at all
    assert clone(lone).terminals == ()


def test_shallow_copy_raises_with_hint():
    ce = ConductingEquipment(terminals=[Terminal()])
    with pytest.raises(TypeError, match="deepcopy"):
        copy.copy(ce)
    assert len(ce.terminals) == 1 and ce.terminals[0].conducting_equipment is ce


# ------------------------------------------------------------------ atomic extend


def test_failed_construction_leaves_no_links():
    t = Terminal()
    with pytest.raises(TypeError):
        ConductingEquipment(terminals=[t, 5])
    assert t.conducting_equipment is None

    ce = ConductingEquipment()
    t2 = Terminal()
    with pytest.raises(TypeError):
        ConductingEquipment.terminals.extend(ce, (x for x in (t2, "bad")))  # generator input
    assert t2.conducting_equipment is None and ce.terminals == ()


# ------------------------------------------------------------------ resolution errors


class _Bad(CimObject):
    __slots__ = ("_x", "_y")

    x = One(EndMeta("x", None, "no.such.module:Foo", False, 0, 1, "z"))
    y = One(EndMeta("y", None, "tests.runtime.minimodel.terminal:Nope", False, 0, 1, "z"))
    _cim_meta = ClassMeta("Bad", "p", "g")


def test_unresolvable_target_message_and_chain():
    with pytest.raises(RuntimeError, match=r"_Bad\.x: cannot resolve target 'no\.such\.module:Foo'") as ei:
        _Bad().x = object()
    assert isinstance(ei.value.__cause__, ImportError)
    with pytest.raises(RuntimeError, match=r"_Bad\.y: cannot resolve target .*Nope") as ei:
        _Bad().y = object()
    assert isinstance(ei.value.__cause__, AttributeError)


# ------------------------------------------------------------------ weakref / deprecated


def test_weakref_and_gc():
    ce = ConductingEquipment(terminals=[Terminal()])
    r = weakref.ref(ce)
    assert r() is ce
    del ce
    gc.collect()  # links are strong both ways: only the cyclic GC frees the graph
    assert r() is None


def test_deprecated_flags():
    a = AttrMeta("n", "n", "str", 0, 1, "primitive")
    e = EndMeta("e", None, "m:C", False, 0, 1, "i")
    assert a.deprecated is False and e.deprecated is False
    assert AttrMeta("n", "n", "str", 0, 1, "primitive", deprecated=True).deprecated
    assert EndMeta("e", None, "m:C", False, 0, 1, "i", deprecated=True).deprecated
    assert ClassMeta("C", "p", "g", deprecated=True).deprecated
    assert a != AttrMeta("n", "n", "str", 0, 1, "primitive", deprecated=True)
    assert cim_attributes(Conductor) == cim_attributes(ConductingEquipment)
    assert cim_ends(Conductor) == cim_ends(ConductingEquipment)
