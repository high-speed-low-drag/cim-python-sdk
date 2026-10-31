"""Hand-written runtime used by the generated ``cim_python_sdk.model`` package (see docs/RUNTIME.md).

Stdlib only; never imports the generated package at import time.
"""

from cim_python_sdk._runtime.base import CimObject
from cim_python_sdk._runtime.ends import Many, One
from cim_python_sdk._runtime.meta import (
    NAMESPACES,
    AttrMeta,
    ClassMeta,
    EndMeta,
    all_metas,
    cim_attributes,
    cim_ends,
)
from cim_python_sdk._runtime.mrid import new_mrid
from cim_python_sdk._runtime.resolve import resolve
from cim_python_sdk._runtime.values import CimCompound, CimDatatype, CimEnum

__all__ = [
    "NAMESPACES",
    "AttrMeta",
    "CimCompound",
    "CimDatatype",
    "CimEnum",
    "CimObject",
    "ClassMeta",
    "EndMeta",
    "Many",
    "One",
    "all_metas",
    "cim_attributes",
    "cim_ends",
    "new_mrid",
    "resolve",
]
