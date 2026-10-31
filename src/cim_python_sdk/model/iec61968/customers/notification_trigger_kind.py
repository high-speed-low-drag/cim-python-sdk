"""CIM enumeration NotificationTriggerKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class NotificationTriggerKind(CimEnum):
    """Kind of trigger to notify customer."""

    initialEtr = "initialEtr"
    etrChange = "etrChange"
    powerRestored = "powerRestored"
    powerOut = "powerOut"
    informDispatched = "informDispatched"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="NotificationTriggerKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{A52701A8-85CB-4fe2-9DC7-F5EDCF562D95}",
            kind="enumeration",
        )
    )
