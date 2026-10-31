"""CIM enumeration CalculationTechniqueKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CalculationTechniqueKind(CimEnum):
    """Possible calculation techniques."""

    trueRMS = "trueRMS"
    minimum = "minimum"
    maximum = "maximum"
    average = "average"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CalculationTechniqueKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{D257257C-1B4A-4a04-8BB4-5A24948089DF}",
            kind="enumeration",
        )
    )
