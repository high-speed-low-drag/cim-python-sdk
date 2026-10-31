"""CIM enumeration CoolingKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CoolingKind(CimEnum):
    """Kind of cooling."""

    selfCooling = "selfCooling"
    forcedAir = "forcedAir"
    forcedOilAndAir = "forcedOilAndAir"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CoolingKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{5F87FD5F-12DA-4fc9-B29C-5D3C5E0874FC}",
            kind="enumeration",
        )
    )
