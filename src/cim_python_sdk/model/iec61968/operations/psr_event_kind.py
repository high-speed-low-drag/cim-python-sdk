"""CIM enumeration PSREventKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PSREventKind(CimEnum):
    """Kind of power system resource (PSR) event."""

    inService = "inService"
    outOfService = "outOfService"
    pendingAdd = "pendingAdd"
    pendingRemove = "pendingRemove"
    pendingReplace = "pendingReplace"
    other = "other"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PSREventKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{ACC00459-6F3B-4c7a-8BCA-3A885E34C9AB}",
            kind="enumeration",
        )
    )
