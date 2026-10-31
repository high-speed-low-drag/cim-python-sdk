"""CIM enumeration FailureIsolationMethodKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FailureIsolationMethodKind(CimEnum):
    """How the failure has been isolated."""

    breakerOperation = "breakerOperation"
    fuse = "fuse"
    burnedInTheClear = "burnedInTheClear"
    manuallyIsolated = "manuallyIsolated"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FailureIsolationMethodKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{02D24517-FD1D-4225-AE36-A1FF7BCE5E08}",
            kind="enumeration",
        )
    )
