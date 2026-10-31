"""CIM enumeration UsagePointConnectedKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UsagePointConnectedKind(CimEnum):
    """State of the usage point with respect to connection to the network."""

    connected = "connected"
    physicallyDisconnected = "physicallyDisconnected"
    logicallyDisconnected = "logicallyDisconnected"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UsagePointConnectedKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{28D01EAC-4704-4a35-8584-9D85CAAB9128}",
            kind="enumeration",
        )
    )
