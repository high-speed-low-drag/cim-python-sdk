"""CIM enumeration LoadForecastType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LoadForecastType(CimEnum):
    """Load forecast zone types."""

    LFZ = "LFZ"
    LZMS = "LZMS"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LoadForecastType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{5FC3A4F6-B913-4e9d-BA33-E253363199A6}",
            kind="enumeration",
        )
    )
