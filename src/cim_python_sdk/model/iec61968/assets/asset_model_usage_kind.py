"""CIM enumeration AssetModelUsageKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetModelUsageKind(CimEnum):
    """Usage for an asset model."""

    distributionOverhead = "distributionOverhead"
    distributionUnderground = "distributionUnderground"
    transmission = "transmission"
    substation = "substation"
    streetlight = "streetlight"
    customerSubstation = "customerSubstation"
    unknown = "unknown"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetModelUsageKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{A72BDDB7-03B4-4754-8F5E-C1930D7F7923}",
            kind="enumeration",
        )
    )
