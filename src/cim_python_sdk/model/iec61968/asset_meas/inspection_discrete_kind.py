"""CIM enumeration InspectionDiscreteKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class InspectionDiscreteKind(CimEnum):
    """Discretes representing breaker inspection result."""

    visibleDamageOrLeaks = "visibleDamageOrLeaks"
    controlCabinetHeaterOn = "controlCabinetHeaterOn"
    bushingOilLevelsOK = "bushingOilLevelsOK"
    oilTankLevelsOK = "oilTankLevelsOK"
    springPressureReadingOK = "springPressureReadingOK"
    gasIndicatorNormal = "gasIndicatorNormal"
    hydraulicOilLevelOK = "hydraulicOilLevelOK"
    hydraulicFluidLevelOK = "hydraulicFluidLevelOK"
    checkOilLevelOK = "checkOilLevelOK"
    operationCount = "operationCount"
    motorOperationsCount = "motorOperationsCount"
    pumpMotorOperationCount = "pumpMotorOperationCount"
    lowToHighPressureCount = "lowToHighPressureCount"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="InspectionDiscreteKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{0D9D4668-4B3A-494d-A220-8AAB270616D2}",
            kind="enumeration",
        )
    )
