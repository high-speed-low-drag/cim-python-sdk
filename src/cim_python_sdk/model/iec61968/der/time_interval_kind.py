"""CIM enumeration TimeIntervalKind (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TimeIntervalKind(CimEnum):
    """Specifies the unit of time for the intervals in the schedule."""

    Y = "Y"
    M = "M"
    D = "D"
    h = "h"
    m = "m"
    s = "s"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TimeIntervalKind",
            package="TC57CIM/IEC61968/DER",
            guid="{BAD15303-A2BD-4e5f-86B7-30D9CD344146}",
            kind="enumeration",
        )
    )
