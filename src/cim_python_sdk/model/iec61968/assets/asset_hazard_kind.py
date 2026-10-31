"""CIM enumeration AssetHazardKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetHazardKind(CimEnum):
    """Type of hazard that is posed to asset in this location.

    Note: This enumeration provides essential information to asset health analytics. The
    existing list is a starting point and is anticipated to be fleshed out further as
    requirements are better understood (PAB 2016/01/09)."""

    ambientTempBelowMinus12 = "ambientTempBelowMinus12"
    ambientTempAbove38 = "ambientTempAbove38"
    vegetation = "vegetation"
    childrenAtPlay = "childrenAtPlay"
    fishingArea = "fishingArea"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetHazardKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{C1FC4F91-3E73-4782-8B0D-4BB7BDA876B0}",
            kind="enumeration",
        )
    )
