"""CIM enumeration JointFillKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class JointFillKind(CimEnum):
    """Kind of fill for Joint."""

    noFillPrefab = "noFillPrefab"
    airNoFilling = "airNoFilling"
    petrolatum = "petrolatum"
    asphaltic = "asphaltic"
    oil = "oil"
    bluefill254 = "bluefill254"
    noVoid = "noVoid"
    epoxy = "epoxy"
    insoluseal = "insoluseal"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="JointFillKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{21B4CEF2-88B8-4558-9AA0-70669BF06D4D}",
            kind="enumeration",
        )
    )
