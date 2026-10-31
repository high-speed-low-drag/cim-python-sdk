"""CIM enumeration AtmosphericAnalogKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AtmosphericAnalogKind(CimEnum):
    """Kinds of analogs (floats) measuring an atmospheric condition."""

    albedo = "albedo"
    ambientTemperature = "ambientTemperature"
    atmosphericPressure = "atmosphericPressure"
    ceiling = "ceiling"
    dewPoint = "dewPoint"
    heatIndex = "heatIndex"
    horizontalVisibility = "horizontalVisibility"
    humidity = "humidity"
    ice = "ice"
    illuminanceDiffuseHorizontal = "illuminanceDiffuseHorizontal"
    illuminanceDirectNormal = "illuminanceDirectNormal"
    illuminanceGlobalHorizontal = "illuminanceGlobalHorizontal"
    irradianceDiffuseHorizonal = "irradianceDiffuseHorizonal"
    irradianceDirectNormal = "irradianceDirectNormal"
    irradianceExtraTerrestrialHorizontal = "irradianceExtraTerrestrialHorizontal"
    irradianceExtraTerrestrialVertical = "irradianceExtraTerrestrialVertical"
    irradianceGlobalHorizontal = "irradianceGlobalHorizontal"
    luminanceZenith = "luminanceZenith"
    precipitation = "precipitation"
    rain = "rain"
    skyCoverageOpaque = "skyCoverageOpaque"
    skyCoverageTotal = "skyCoverageTotal"
    snow = "snow"
    windChill = "windChill"
    windSpeedGust = "windSpeedGust"
    windSpeedInstantaneous = "windSpeedInstantaneous"
    windSpeedPeak = "windSpeedPeak"
    windSpeedSustained = "windSpeedSustained"
    verticalVisibility = "verticalVisibility"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AtmosphericAnalogKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{12972324-2F51-42eb-8281-28F68495D162}",
            kind="enumeration",
        )
    )
