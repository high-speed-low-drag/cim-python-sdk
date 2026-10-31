"""CIM100 Python SDK.

Every generated class and enumeration is available lazily by its canonical name::

    from cim_python_sdk import ACLineSegment, Terminal, UnitSymbol

Nothing from ``cim_python_sdk.model`` is imported until a name is first used (PEP 562).
"""

from importlib import import_module as _import_module

__version__ = "0.1.0"


def __getattr__(name: str) -> object:
    if name.startswith("_"):  # dunder / private probes (__path__, _registry, ...) are never CIM names
        raise AttributeError(f"module 'cim_python_sdk' has no attribute {name!r}")
    ref = _import_module("cim_python_sdk._registry").BY_NAME.get(name)
    if ref is None:
        raise AttributeError(f"module 'cim_python_sdk' has no attribute {name!r}")
    module, _, cls_name = ref.partition(":")
    obj = getattr(_import_module(module), cls_name)
    globals()[name] = obj
    return obj


def __dir__() -> list[str]:
    names = set(globals()) | set(_import_module("cim_python_sdk._registry").BY_NAME)
    return sorted(n for n in names if not n.startswith("_") or n.endswith("__"))
