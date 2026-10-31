"""CIM enumeration CableShieldMaterialKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CableShieldMaterialKind(CimEnum):
    """Kind of cable shield material."""

    lead = "lead"
    copper = "copper"
    steel = "steel"
    aluminum = "aluminum"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CableShieldMaterialKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{5C33DFE0-CE5B-43ce-933A-8579E23D8006}",
            kind="enumeration",
        )
    )
