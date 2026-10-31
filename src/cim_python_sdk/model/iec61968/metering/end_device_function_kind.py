"""CIM enumeration EndDeviceFunctionKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EndDeviceFunctionKind(CimEnum):
    """Kind of end device function."""

    reverseFlow = "reverseFlow"
    demandResponse = "demandResponse"
    metrology = "metrology"
    outageHistory = "outageHistory"
    relaysProgramming = "relaysProgramming"
    onRequestRead = "onRequestRead"
    autonomousDst = "autonomousDst"
    electricMetering = "electricMetering"
    gasMetering = "gasMetering"
    waterMetering = "waterMetering"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EndDeviceFunctionKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{642E41B6-A2B7-4b81-BDC9-40F67AF173D5}",
            kind="enumeration",
        )
    )
