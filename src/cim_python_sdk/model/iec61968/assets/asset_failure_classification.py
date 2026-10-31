"""CIM enumeration AssetFailureClassification (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetFailureClassification(CimEnum):
    """Classifications of asset failures."""

    major = "major"
    minor = "minor"
    defect = "defect"
    majorNeedsReplacement = "majorNeedsReplacement"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetFailureClassification",
            package="TC57CIM/IEC61968/Assets",
            guid="{01057CD3-8D73-4ef5-A952-DBFB54C079E5}",
            kind="enumeration",
        )
    )
