"""CIM enumeration InputSignalKind (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class InputSignalKind(CimEnum):
    """Types of input signals. In dynamics modelling, commonly represented by the j parameter."""

    rotorSpeed = "rotorSpeed"
    rotorAngularFrequencyDeviation = "rotorAngularFrequencyDeviation"
    busFrequency = "busFrequency"
    busFrequencyDeviation = "busFrequencyDeviation"
    generatorElectricalPower = "generatorElectricalPower"
    generatorAcceleratingPower = "generatorAcceleratingPower"
    busVoltage = "busVoltage"
    busVoltageDerivative = "busVoltageDerivative"
    branchCurrent = "branchCurrent"
    fieldCurrent = "fieldCurrent"
    generatorMechanicalPower = "generatorMechanicalPower"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="InputSignalKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
            guid="{FF87046C-0F52-4924-8269-7F7E9E719673}",
            kind="enumeration",
        )
    )
