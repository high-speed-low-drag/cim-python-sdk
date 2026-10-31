"""CIM enumeration WindingInsulationKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WindingInsulationKind(CimEnum):
    """Insulation kind for windings."""

    paper = "paper"
    thermallyUpgradedPaper = "thermallyUpgradedPaper"
    nomex = "nomex"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WindingInsulationKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{7EC6DA40-F14F-446d-8BFD-CCA4C712C76D}",
            kind="enumeration",
        )
    )
