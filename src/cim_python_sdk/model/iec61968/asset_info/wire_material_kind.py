"""CIM enumeration WireMaterialKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WireMaterialKind(CimEnum):
    """Kind of wire material."""

    copper = "copper"
    steel = "steel"
    aluminum = "aluminum"
    aluminumSteel = "aluminumSteel"
    acsr = "acsr"
    aluminumAlloy = "aluminumAlloy"
    aluminumAlloySteel = "aluminumAlloySteel"
    aaac = "aaac"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WireMaterialKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{79C6A256-4E46-4717-9E2F-BBB1984DB9D5}",
            kind="enumeration",
        )
    )
