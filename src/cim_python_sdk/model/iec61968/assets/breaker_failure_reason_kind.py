"""CIM enumeration BreakerFailureReasonKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BreakerFailureReasonKind(CimEnum):
    """Reason for breaker failure.

    Note: This enumeration provides essential information to asset health analytics. The
    existing list is a starting point and is anticipated to be fleshed out further as
    requirements are better understood (PAB 2016/01/09)."""

    blastValveFailure = "blastValveFailure"
    bushingFailure = "bushingFailure"
    closeCoilOpenShortedFailed = "closeCoilOpenShortedFailed"
    contaminatedAir = "contaminatedAir"
    contaminatedArcChutes = "contaminatedArcChutes"
    contaminatedGas = "contaminatedGas"
    contaminatedGasAir = "contaminatedGasAir"
    controlCircuitFailure = "controlCircuitFailure"
    degradedLubrication = "degradedLubrication"
    externalOrInternalContamination = "externalOrInternalContamination"
    highPressureAirPlant = "highPressureAirPlant"
    highResistanceLoadPath = "highResistanceLoadPath"
    highResistancePath = "highResistancePath"
    interrupterContactFailure = "interrupterContactFailure"
    interrupterFailure = "interrupterFailure"
    linkageFailure = "linkageFailure"
    lossOfOil = "lossOfOil"
    lossOfVacuum = "lossOfVacuum"
    lowGasPressure = "lowGasPressure"
    mechanismFailure = "mechanismFailure"
    mechanismOrLinkageFailure = "mechanismOrLinkageFailure"
    oilRelatedFailure = "oilRelatedFailure"
    poorOilQuality = "poorOilQuality"
    rackingMechanismFailure = "rackingMechanismFailure"
    resistorFailure = "resistorFailure"
    resistorGradingCapacitorFailure = "resistorGradingCapacitorFailure"
    SF6BlastValveFailure = "SF6BlastValveFailure"
    SF6PufferFailure = "SF6PufferFailure"
    solidDielectricFailure = "solidDielectricFailure"
    storedEnergyFailure = "storedEnergyFailure"
    tripCoilOpenShortedFailed = "tripCoilOpenShortedFailed"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BreakerFailureReasonKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{CA4E2E0F-70B3-477e-B506-0B2333FCA021}",
            kind="enumeration",
        )
    )
