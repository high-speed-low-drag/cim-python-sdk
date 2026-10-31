"""CIM enumeration ServiceRequestKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ServiceRequestKind(CimEnum):
    """Kinds of service requests"""

    construction = "construction"
    inspection = "inspection"
    repair = "repair"
    test = "test"
    disconnect = "disconnect"
    reconnect = "reconnect"
    connect = "connect"
    turn_on = "turn-on"
    other = "other"
    turn_off = "turn-off"
    replace = "replace"
    newservice = "newservice"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ServiceRequestKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{51D116FE-611A-4f90-BA0B-96901E106AE3}",
            kind="enumeration",
        )
    )
