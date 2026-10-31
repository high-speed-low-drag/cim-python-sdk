"""CIM enumeration OutageStatusKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OutageStatusKind(CimEnum):
    """This defines if the outage have been predicted or confirmed"""

    confirmed = "confirmed"
    predicted = "predicted"
    partiallyRestored = "partiallyRestored"
    restored = "restored"
    closed = "closed"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OutageStatusKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{EEA30D3B-F1FD-4289-BD60-81C91AEB7886}",
            kind="enumeration",
        )
    )
