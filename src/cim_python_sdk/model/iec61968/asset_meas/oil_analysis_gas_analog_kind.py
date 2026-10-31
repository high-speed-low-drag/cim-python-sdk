"""CIM enumeration OilAnalysisGasAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisGasAnalogKind(CimEnum):
    """Analogs representing oil dissolved gas analysis result."""

    hydrogen = "hydrogen"
    methane = "methane"
    ethane = "ethane"
    ethylene = "ethylene"
    acetylene = "acetylene"
    carbonMonoxide = "carbonMonoxide"
    propane = "propane"
    propene = "propene"
    carbonDioxide = "carbonDioxide"
    oxygen = "oxygen"
    nitrogen = "nitrogen"
    totalDissolvedGasPercent = "totalDissolvedGasPercent"
    totalCombustibleGasPercent = "totalCombustibleGasPercent"
    butane = "butane"
    carbon = "carbon"
    carbon3 = "carbon3"
    carbon4 = "carbon4"
    isobutane = "isobutane"
    equivalentTCGPercent = "equivalentTCGPercent"
    totalHeatGas = "totalHeatGas"
    totalDissolvedCombustibleGas = "totalDissolvedCombustibleGas"
    totalPartialPressure = "totalPartialPressure"
    estimatedSafeHandlingLimit = "estimatedSafeHandlingLimit"
    hydran = "hydran"
    hydranPredicted = "hydranPredicted"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisGasAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{FB38FFF8-8B26-4438-A8B9-DDB8EA475FEB}",
            kind="enumeration",
        )
    )
