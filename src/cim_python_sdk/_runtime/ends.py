"""Association-end descriptors that keep both ends of every association in sync.

* `One` (upper bound 1): ``obj.x`` reads the target or None; assigning links, None unlinks.
* `Many` (upper bound > 1): ``obj.xs`` returns a tuple snapshot; generated
  ``add_x / remove_x / clear_xs / num_x / get_x_by_mrid`` methods are one-liners that
  call `Many.add` / `remove` / `clear` / `count` / `get_by_mrid`.

Storage lives in a private slot ``_<name>`` declared by the owning class. An unset
slot means "no target" / "empty"; a Many slot holds a dict ``{id(obj): obj}``
(insertion-ordered identity set), created on the first add.

Two-way maintenance never recurses: `_raw_add` / `_raw_remove` touch one side only and
`_link` / `_unlink` call them once per side. `_raw_add` on a `One` returns the object
it displaced, whose back-reference is then removed, so replacing the target of a 1:1
or N:1 end also cleans the old target.
"""

from __future__ import annotations

from cim_python_sdk._runtime._compat import TYPE_CHECKING, Generic
from cim_python_sdk._runtime.resolve import resolve

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
    from typing import Any, Self, TypeVar, overload

    from cim_python_sdk._runtime.base import CimObject
    from cim_python_sdk._runtime.meta import EndMeta

    T = TypeVar("T")
    O = TypeVar("O", bound=CimObject)
else:
    T = None


class _End(Generic[T]):
    __slots__ = ("_cls", "_get", "_inv", "_set", "meta", "name", "owner")

    meta: EndMeta
    name: str
    owner: type
    _get: Callable[[object], Any]
    _set: Callable[[object, Any], None]
    _cls: type | None
    _inv: _End[Any] | None

    def __init__(self, meta: EndMeta) -> None:
        if meta.many != isinstance(self, Many):
            raise TypeError(f"end {meta.name!r}: EndMeta.many={meta.many} needs the other descriptor")
        self.meta = meta
        self.name = meta.name
        self._cls = None
        self._inv = None

    def __set_name__(self, owner: type, name: str) -> None:
        if name != self.meta.name:
            raise TypeError(f"{owner.__name__}.{name}: descriptor meta is named {self.meta.name!r}")
        member = owner.__dict__.get("_" + name)
        if member is None or not hasattr(member, "__set__"):
            raise TypeError(f"{owner.__name__}.__slots__ must contain '_{name}' for end {name!r}")
        self.owner = owner
        self._get = member.__get__
        self._set = member.__set__

    def __repr__(self) -> str:
        owner = getattr(self, "owner", None)
        return f"<{type(self).__name__} {getattr(owner, '__name__', '?')}.{self.name}>"

    # -- lazy resolution -------------------------------------------------------------

    @property
    def target(self) -> type:
        """The target class, imported on first use."""
        cls = self._cls
        if cls is None:
            ref = self.meta.target
            try:
                cls = self._cls = resolve(ref)
            except Exception as e:
                raise RuntimeError(
                    f"{self.owner.__name__}.{self.name}: cannot resolve target {ref!r}"
                ) from e
        return cls

    @property
    def inverse(self) -> _End[Any]:
        """The descriptor of the opposite end, on the target class."""
        inv = self._inv
        if inv is None:
            target = self.target
            inv = getattr(target, self.meta.inverse, None)
            if not isinstance(inv, _End):
                raise TypeError(
                    f"{self.owner.__name__}.{self.name}: inverse {target.__name__}."
                    f"{self.meta.inverse} is not an association end"
                )
            if inv.meta.inverse != self.name or not issubclass(self.owner, inv.target):
                raise TypeError(f"{self!r} and {inv!r} are not inverses of each other")
            self._inv = inv
        return inv

    def _check(self, other: object) -> None:
        cls = self._cls or self.target
        if not isinstance(other, cls):
            raise TypeError(
                f"{self.owner.__name__}.{self.name} expects {cls.__name__}, "
                f"got {type(other).__name__}"
            )

    # -- one-sided primitives (implemented by One / Many) -----------------------------

    def _raw_add(self, obj: object, other: object) -> object | None:
        raise NotImplementedError

    def _raw_remove(self, obj: object, other: object) -> None:
        raise NotImplementedError

    def count(self, obj: object) -> int:
        raise NotImplementedError


def _link(end: _End[Any], a: object, b: object) -> None:
    """Make ``a.end`` contain `b` and ``b.inverse`` contain `a`."""
    inv = end._inv or end.inverse
    displaced = end._raw_add(a, b)
    if displaced is not None:
        inv._raw_remove(displaced, a)
    displaced = inv._raw_add(b, a)
    if displaced is not None:
        end._raw_remove(displaced, b)


def _unlink(end: _End[Any], a: object, b: object) -> None:
    end._raw_remove(a, b)
    (end._inv or end.inverse)._raw_remove(b, a)


class One(_End[T]):
    """Single-valued end (upper bound 1)."""

    __slots__ = ()

    if TYPE_CHECKING:

        @overload
        def __get__(self, obj: None, objtype: type | None = None) -> Self: ...
        @overload
        def __get__(self, obj: object, objtype: type | None = None) -> T | None: ...

    def __get__(self, obj: object | None, objtype: type | None = None) -> Self | T | None:
        if obj is None:
            return self
        try:
            return self._get(obj)
        except AttributeError:
            return None

    def __set__(self, obj: object, value: T | None) -> None:
        try:
            current = self._get(obj)
        except AttributeError:
            current = None
        if current is value:
            return
        if value is not None:
            self._check(value)
        inv = self._inv or self.inverse
        # same steps as _link/_unlink, reusing `current` (saves a second slot read)
        self._set(obj, value)
        if current is not None:
            inv._raw_remove(current, obj)
        if value is not None:
            displaced = inv._raw_add(value, obj)
            if displaced is not None:
                self._raw_remove(displaced, value)

    def __delete__(self, obj: object) -> None:
        self.__set__(obj, None)

    def _raw_add(self, obj: object, other: object) -> object | None:
        try:
            old = self._get(obj)
        except AttributeError:
            old = None
        self._set(obj, other)
        return None if old is other else old

    def _raw_remove(self, obj: object, other: object) -> None:
        try:
            if self._get(obj) is other:
                self._set(obj, None)
        except AttributeError:
            pass

    def count(self, obj: object) -> int:
        return 0 if self.__get__(obj) is None else 1


class Many(_End[T]):
    """Multi-valued end. Reading returns a tuple snapshot (safe to mutate while iterating)."""

    __slots__ = ()

    if TYPE_CHECKING:

        @overload
        def __get__(self, obj: None, objtype: type | None = None) -> Self: ...
        @overload
        def __get__(self, obj: object, objtype: type | None = None) -> tuple[T, ...]: ...

    def __get__(self, obj: object | None, objtype: type | None = None) -> Self | tuple[T, ...]:
        if obj is None:
            return self
        try:
            return tuple(self._get(obj).values())
        except AttributeError:
            return ()

    def __set__(self, obj: object, value: object) -> None:
        raise AttributeError(
            f"{self.owner.__name__}.{self.name} is read-only; use the add/remove/clear methods"
        )

    def _items(self, obj: object) -> dict[int, T] | None:
        try:
            return self._get(obj)
        except AttributeError:
            return None

    def _raw_add(self, obj: object, other: object) -> None:
        try:
            self._get(obj)[id(other)] = other
        except AttributeError:
            self._set(obj, {id(other): other})

    def _raw_remove(self, obj: object, other: object) -> None:
        try:
            self._get(obj).pop(id(other), None)
        except AttributeError:
            pass

    # -- helpers called by generated methods ------------------------------------------

    def add(self, obj: O, other: T) -> O:
        """Link `other` (idempotent); returns `obj` for chaining."""
        self._check(other)
        items = self._items(obj)
        if items is None or id(other) not in items:
            _link(self, obj, other)
        return obj

    def extend(self, obj: O, others: Iterable[T] | None) -> O:
        """Add every item of `others` (None adds nothing). Used by generated ``__init__``.

        All items are type-checked before any is linked, so a TypeError leaves no links.
        """
        if others is not None:
            items = list(others)
            for other in items:  # validate everything first: a bad item links nothing
                self._check(other)
            for other in items:
                self.add(obj, other)
        return obj

    def remove(self, obj: O, other: T) -> O:
        """Unlink `other`; raises ValueError if it is not linked."""
        items = self._items(obj)
        if items is None or items.get(id(other)) is not other:
            raise ValueError(f"{other!r} is not in {obj!r}.{self.name}")
        _unlink(self, obj, other)
        return obj

    def clear(self, obj: O) -> O:
        """Unlink every item; returns `obj`."""
        items = self._items(obj)
        if items:
            for other in tuple(items.values()):
                _unlink(self, obj, other)
        return obj

    def count(self, obj: object) -> int:
        items = self._items(obj)
        return 0 if items is None else len(items)

    def get_by_mrid(self, obj: object, mrid: str) -> T | None:
        """The linked item whose ``mrid`` equals `mrid`, or None."""
        items = self._items(obj)
        if items:
            for other in items.values():
                if getattr(other, "mrid", None) == mrid:
                    return other
        return None
