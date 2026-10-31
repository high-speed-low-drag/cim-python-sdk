"""CIM enumeration AnchorKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AnchorKind(CimEnum):
    """Kind of anchor."""

    concrete = "concrete"
    helix = "helix"
    multiHelix = "multiHelix"
    rod = "rod"
    screw = "screw"
    unknown = "unknown"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AnchorKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{C8058D3C-2D3F-4036-8D55-14C034FADE2A}",
            kind="enumeration",
        )
    )
