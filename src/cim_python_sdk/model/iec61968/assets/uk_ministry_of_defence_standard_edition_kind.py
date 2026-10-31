"""CIM enumeration UKMinistryOfDefenceStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UKMinistryOfDefenceStandardEditionKind(CimEnum):
    """List of editions for UK Ministry of Defence standards."""

    Issue_1 = "Issue 1"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UKMinistryOfDefenceStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{6C7BC949-58D1-43e0-9935-E3FB228569E3}",
            kind="enumeration",
        )
    )
