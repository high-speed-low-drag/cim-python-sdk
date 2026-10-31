"""CIM enumeration TimeZoneType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TimeZoneType(CimEnum):
    """CIM enumeration TimeZoneType."""

    PPT = "PPT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TimeZoneType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{C823AFC3-EADA-4bc7-B6B1-BDA5F6BB257B}",
            kind="enumeration",
        )
    )
