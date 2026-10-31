"""Lazy class resolution: a class, or a "module:ClassName" string imported on first use."""

from __future__ import annotations

from importlib import import_module

_cache: dict[str, type] = {}


def resolve(ref: type | str) -> type:
    """Return the class named by `ref`; strings are imported once and cached."""
    if isinstance(ref, type):
        return ref
    cls = _cache.get(ref)
    if cls is None:
        module, sep, name = ref.partition(":")
        if not sep or not module or not name:
            raise ValueError(f"class reference must be 'module:ClassName', got {ref!r}")
        obj = getattr(import_module(module), name)
        if not isinstance(obj, type):
            raise TypeError(f"{ref!r} does not name a class")
        cls = _cache[ref] = obj
    return cls
