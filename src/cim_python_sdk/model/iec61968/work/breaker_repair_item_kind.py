"""CIM enumeration BreakerRepairItemKind (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BreakerRepairItemKind(CimEnum):
    """Breaker components and problem areas which can be the focus of a repair work task."""

    airCompressor = "airCompressor"
    auxiliarySwitchAndLinkage = "auxiliarySwitchAndLinkage"
    busConnection = "busConnection"
    checkValve = "checkValve"
    closeCoil = "closeCoil"
    contactor = "contactor"
    controlCircuit = "controlCircuit"
    corrosion = "corrosion"
    gasDensitySupervision = "gasDensitySupervision"
    heaterOrThermostat = "heaterOrThermostat"
    hydraulicFluidLeak = "hydraulicFluidLeak"
    interrupterAssembly = "interrupterAssembly"
    positionIndicator = "positionIndicator"
    pressureSwitch = "pressureSwitch"
    pumpOrMotor = "pumpOrMotor"
    relay = "relay"
    SF6GasLeak = "SF6GasLeak"
    storedEnergySystem = "storedEnergySystem"
    tripCoil = "tripCoil"
    tripControlValve = "tripControlValve"
    wiring = "wiring"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BreakerRepairItemKind",
            package="TC57CIM/IEC61968/Work",
            guid="{4B0CA5ED-A380-4094-BBEE-6BE0EF12EDBE}",
            kind="enumeration",
        )
    )
