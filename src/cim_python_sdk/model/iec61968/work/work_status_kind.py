"""CIM enumeration WorkStatusKind (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WorkStatusKind(CimEnum):
    """Kind of status, specific to work."""

    waitingOnApproval = "waitingOnApproval"
    approved = "approved"
    cancelled = "cancelled"
    waitingToBeScheduled = "waitingToBeScheduled"
    scheduled = "scheduled"
    waitingOnMaterial = "waitingOnMaterial"
    inProgress = "inProgress"
    completed = "completed"
    closed = "closed"
    dispatched = "dispatched"
    enroute = "enroute"
    onSite = "onSite"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WorkStatusKind",
            package="TC57CIM/IEC61968/Work",
            guid="{AA715820-3F71-45a6-9E21-B8F331C03999}",
            kind="enumeration",
        )
    )
