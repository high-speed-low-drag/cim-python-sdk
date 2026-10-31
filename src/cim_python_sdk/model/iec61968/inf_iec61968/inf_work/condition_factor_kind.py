"""CIM enumeration ConditionFactorKind (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ConditionFactorKind(CimEnum):
    """Kind of condition factor."""

    labor = "labor"
    accountAllocation = "accountAllocation"
    material = "material"
    travel = "travel"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ConditionFactorKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfWork",
            guid="{89182E41-81F8-4c11-A5D4-6B68220A8B7E}",
            kind="enumeration",
        )
    )
