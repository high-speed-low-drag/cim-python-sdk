"""CIM enumeration StreetlightLampKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class StreetlightLampKind(CimEnum):
    """Kind of lamp for the streetlight."""

    highPressureSodium = "highPressureSodium"
    mercuryVapor = "mercuryVapor"
    metalHalide = "metalHalide"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="StreetlightLampKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{F0B6B07C-FC15-4ec6-92E8-96EA94AC530F}",
            kind="enumeration",
        )
    )
