"""CIM enumeration WorkTimeScheduleKind (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WorkTimeScheduleKind(CimEnum):
    """Kind of work schedule."""

    estimate = "estimate"
    request = "request"
    actual = "actual"
    earliest = "earliest"
    latest = "latest"
    immediate = "immediate"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WorkTimeScheduleKind",
            package="TC57CIM/IEC61968/Work",
            guid="{0265E52A-D5D6-43bf-8ABA-854FECBB9692}",
            kind="enumeration",
        )
    )
