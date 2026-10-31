"""Randomized operations on a small pool, checked against an independent shadow model."""

from __future__ import annotations

import random

import pytest

from cim_python_sdk._runtime import Many, One, cim_ends
from tests.runtime.minimodel.asset import Asset
from tests.runtime.minimodel.conducting_equipment import ConductingEquipment
from tests.runtime.minimodel.facility import Facility
from tests.runtime.minimodel.location import Location
from tests.runtime.minimodel.power_system_resource import PowerSystemResource
from tests.runtime.minimodel.terminal import Terminal


def _end(obj, name):
    return getattr(type(obj), name)


def _canonical(end):
    """(association key, True if `end` is the canonical side)."""
    a = (end.owner.__name__, end.name)
    b = (end.inverse.owner.__name__, end.inverse.name)
    return (min(a, b), max(a, b)), a <= b


class Shadow:
    """Expected link state: per association, a set of (holder, item) pairs on the canonical end."""

    def __init__(self):
        self.pairs: dict[tuple, set[tuple[int, int]]] = {}

    def _view(self, end):
        key, canon = _canonical(end)
        return self.pairs.setdefault(key, set()), canon

    def targets(self, end, obj) -> set[int]:
        pairs, canon = self._view(end)
        if canon:
            return {b for a, b in pairs if a == id(obj)}
        return {a for a, b in pairs if b == id(obj)}

    def _drop(self, end, obj):
        """Drop every pair where `obj` holds something through `end`."""
        pairs, canon = self._view(end)
        idx = 0 if canon else 1
        for p in [p for p in pairs if p[idx] == id(obj)]:
            pairs.discard(p)

    def link(self, end, a, b):
        pairs, canon = self._view(end)
        if (id(a), id(b)) in pairs if canon else (id(b), id(a)) in pairs:
            return
        if isinstance(end, One):
            self._drop(end, a)
        if isinstance(end.inverse, One):
            self._drop(end.inverse, b)
        pairs.add((id(a), id(b)) if canon else (id(b), id(a)))

    def unlink(self, end, a, b):
        pairs, canon = self._view(end)
        pairs.discard((id(a), id(b)) if canon else (id(b), id(a)))


def check_invariant(pool, shadow):
    for obj in pool:
        for meta in cim_ends(type(obj)):
            end = _end(obj, meta.name)
            value = getattr(obj, meta.name)
            items = (value,) if isinstance(end, One) else value
            items = tuple(x for x in items if x is not None)
            if isinstance(end, Many):
                assert len({id(x) for x in items}) == len(items)
                store = getattr(obj, "_" + meta.name, {})
                assert all(k == id(v) for k, v in store.items())
            for other in items:  # global two-way invariant
                back = getattr(other, end.inverse.name)
                assert (back is obj) if isinstance(end.inverse, One) else (obj in back)
            assert {id(x) for x in items} == shadow.targets(end, obj), (obj, meta.name)


@pytest.mark.parametrize("seed", range(6))
def test_random_operations(seed):
    rng = random.Random(seed)
    pool = (
        [ConductingEquipment() for _ in range(4)]
        + [Terminal() for _ in range(6)]
        + [PowerSystemResource() for _ in range(3)]
        + [Asset() for _ in range(3)]
        + [Facility()]
        + [Location() for _ in range(3)]
    )
    shadow = Shadow()
    counts = {"set": 0, "none": 0, "add": 0, "remove": 0, "clear": 0, "type": 0, "absent": 0}
    for _ in range(2500):
        obj = rng.choice(pool)
        meta = rng.choice(cim_ends(type(obj)))
        end = _end(obj, meta.name)
        candidate = rng.choice(pool)
        ok_type = isinstance(candidate, end.target)
        if isinstance(end, One):
            if rng.random() < 0.2:
                setattr(obj, meta.name, None)
                current = getattr(obj, meta.name)
                assert current is None
                for b in [x for x in pool if id(x) in shadow.targets(end, obj)]:
                    shadow.unlink(end, obj, b)
                counts["none"] += 1
            elif not ok_type:
                with pytest.raises(TypeError):
                    setattr(obj, meta.name, candidate)
                counts["type"] += 1
            else:
                setattr(obj, meta.name, candidate)
                shadow.link(end, obj, candidate)
                counts["set"] += 1
        else:
            r = rng.random()
            if r < 0.1:
                end.clear(obj)
                for b in [x for x in pool if id(x) in shadow.targets(end, obj)]:
                    shadow.unlink(end, obj, b)
                counts["clear"] += 1
            elif r < 0.45:
                linked = getattr(obj, meta.name)
                if linked and rng.random() < 0.7:
                    candidate = rng.choice(linked)
                if id(candidate) in shadow.targets(end, obj):
                    end.remove(obj, candidate)
                    shadow.unlink(end, obj, candidate)
                    counts["remove"] += 1
                else:
                    with pytest.raises(ValueError):
                        end.remove(obj, candidate)
                    counts["absent"] += 1
            elif not ok_type:
                with pytest.raises(TypeError):
                    end.add(obj, candidate)
                counts["type"] += 1
            else:
                assert end.add(obj, candidate) is obj
                shadow.link(end, obj, candidate)
                counts["add"] += 1
        check_invariant(pool, shadow)
    assert all(v > 20 for v in counts.values()), counts
