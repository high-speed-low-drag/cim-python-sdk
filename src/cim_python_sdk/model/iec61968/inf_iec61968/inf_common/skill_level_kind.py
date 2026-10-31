"""CIM enumeration SkillLevelKind (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SkillLevelKind(CimEnum):
    """Kind of skill level."""

    master = "master"
    standard = "standard"
    apprentice = "apprentice"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SkillLevelKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
            guid="{159907A1-CFDD-4260-91BB-B8F48D276230}",
            kind="enumeration",
        )
    )
