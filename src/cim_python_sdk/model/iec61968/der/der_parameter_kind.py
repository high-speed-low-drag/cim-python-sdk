"""CIM enumeration DERParameterKind (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DERParameterKind(CimEnum):
    """Specifies the DER parameters related to the unit of power, ramp rate and regulation
    flows."""

    apparentPower = "apparentPower"
    activePower = "activePower"
    reactivePower = "reactivePower"
    highFilterBiDirectionalRegulation = "highFilterBiDirectionalRegulation"
    lowFilterBiDirectionalRegulation = "lowFilterBiDirectionalRegulation"
    highFilterUpRegulation = "highFilterUpRegulation"
    lowFilterUpRegulation = "lowFilterUpRegulation"
    highFilterDownRegulation = "highFilterDownRegulation"
    lowFilterDownRegulation = "lowFilterDownRegulation"
    increasingRampRate = "increasingRampRate"
    decreasingRampRate = "decreasingRampRate"
    voltage = "voltage"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DERParameterKind",
            package="TC57CIM/IEC61968/DER",
            guid="{1D5BD9FF-A03A-4271-A8E4-73BF5431FF8C}",
            kind="enumeration",
        )
    )
