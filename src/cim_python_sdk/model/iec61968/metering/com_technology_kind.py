"""CIM enumeration ComTechnologyKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ComTechnologyKind(CimEnum):
    """Kind of communication technology."""

    cellular = "cellular"
    ethernet = "ethernet"
    homePlug = "homePlug"
    pager = "pager"
    phone = "phone"
    plc = "plc"
    rf = "rf"
    rfMesh = "rfMesh"
    zigbee = "zigbee"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ComTechnologyKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{3A4B0E91-7AA6-42cc-BC26-416A68711ED9}",
            kind="enumeration",
        )
    )
