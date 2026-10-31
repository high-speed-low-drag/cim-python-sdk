"""CIM enumeration OnOff (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OnOff(CimEnum):
    """ON

    OFF"""

    ON = "ON"
    OFF = "OFF"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OnOff",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{78428A4F-29E8-4d9c-BB8C-E92CB3114B93}",
            kind="enumeration",
        )
    )
