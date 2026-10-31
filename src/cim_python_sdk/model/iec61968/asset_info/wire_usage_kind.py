"""CIM enumeration WireUsageKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WireUsageKind(CimEnum):
    """Kind of wire usage."""

    transmission = "transmission"
    distribution = "distribution"
    secondary = "secondary"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WireUsageKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{670B1BC7-ED86-4b0a-99A9-5233357BB560}",
            kind="enumeration",
        )
    )
