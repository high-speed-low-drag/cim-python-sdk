"""CIM enumeration InspectionAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class InspectionAnalogKind(CimEnum):
    """Analogs typically recorded during a field inspection."""

    sF6PressureReading = "sF6PressureReading"
    airPressureReading = "airPressureReading"
    airPressureHPSystemReading = "airPressureHPSystemReading"
    compressorHourMeterReading = "compressorHourMeterReading"
    airPressureLPSystemReading = "airPressureLPSystemReading"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="InspectionAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{838A2C66-9B01-4e76-9527-6981B5BE49FB}",
            kind="enumeration",
        )
    )
