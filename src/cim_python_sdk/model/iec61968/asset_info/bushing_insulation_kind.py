"""CIM enumeration BushingInsulationKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BushingInsulationKind(CimEnum):
    """Insulation kind for bushings."""

    oilImpregnatedPaper = "oilImpregnatedPaper"
    compound = "compound"
    resinBondedPaper = "resinBondedPaper"
    resinImpregnatedPaper = "resinImpregnatedPaper"
    solidPorcelain = "solidPorcelain"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BushingInsulationKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{486A794A-2B6E-4226-A5CE-60F8BAE9F395}",
            kind="enumeration",
        )
    )
