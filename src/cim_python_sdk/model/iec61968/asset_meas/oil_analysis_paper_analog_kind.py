"""CIM enumeration OilAnalysisPaperAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisPaperAnalogKind(CimEnum):
    """Analogs representing oil paper degradation analysis result."""

    hydroxymethylfurfural = "hydroxymethylfurfural"
    furfurylAlcohol = "furfurylAlcohol"
    furfural = "furfural"
    methylfurfural = "methylfurfural"
    totalFuran = "totalFuran"
    degreeOfPolymerization = "degreeOfPolymerization"
    degreeOfPolymerizationCalculated = "degreeOfPolymerizationCalculated"
    methanol = "methanol"
    ethanol = "ethanol"
    tensileStrength = "tensileStrength"
    solidInsulationDielectricStrength = "solidInsulationDielectricStrength"
    acetylfuran = "acetylfuran"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisPaperAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{C1AB95B9-A09A-466c-BEE0-CDF175C30E70}",
            kind="enumeration",
        )
    )
