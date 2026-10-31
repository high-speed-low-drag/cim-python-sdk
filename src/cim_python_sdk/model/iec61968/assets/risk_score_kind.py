"""CIM enumeration RiskScoreKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RiskScoreKind(CimEnum):
    """Types of risk scores."""

    customerRisk = "customerRisk"
    financialRisk = "financialRisk"
    safetyRisk = "safetyRisk"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RiskScoreKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{0A7A6DC8-E106-4f1f-B10C-106ADDA343FF}",
            kind="enumeration",
        )
    )
