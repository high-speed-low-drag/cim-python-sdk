"""CIM enumeration MediumKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MediumKind(CimEnum):
    """Kind of medium."""

    air = "air"
    gas = "gas"
    liquid = "liquid"
    mineralOil = "mineralOil"
    SF6 = "SF6"
    SF6CF4 = "SF6CF4"
    SF6N2 = "SF6N2"
    solid = "solid"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MediumKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{F7D95C04-FBC0-490a-8587-6B50CE99B307}",
            kind="enumeration",
        )
    )
