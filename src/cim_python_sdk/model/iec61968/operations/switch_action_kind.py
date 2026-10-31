"""CIM enumeration SwitchActionKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SwitchActionKind(CimEnum):
    """Kind of action on switch."""

    open = "open"
    close = "close"
    disableReclosing = "disableReclosing"
    enableReclosing = "enableReclosing"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SwitchActionKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{4B2B08CF-4F3C-4dba-871B-CC48F7241111}",
            kind="enumeration",
        )
    )
