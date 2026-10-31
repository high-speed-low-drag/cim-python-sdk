"""CIM enumeration OilAnalysisMoistureAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisMoistureAnalogKind(CimEnum):
    """Analogs representing oil moisture analysis result."""

    waterContent = "waterContent"
    waterContentMonitoredViaInfrared = "waterContentMonitoredViaInfrared"
    waterContentMonitoredViaCapacitance = "waterContentMonitoredViaCapacitance"
    waterContentMonitoredViaAluminumOxide = "waterContentMonitoredViaAluminumOxide"
    waterContentMonitoredViaOther = "waterContentMonitoredViaOther"
    relativeSaturation = "relativeSaturation"
    relativeSaturationCalculated = "relativeSaturationCalculated"
    dewPoint = "dewPoint"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisMoistureAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{FC1F4947-3F1A-49e4-8572-8FB4B7B1136C}",
            kind="enumeration",
        )
    )
