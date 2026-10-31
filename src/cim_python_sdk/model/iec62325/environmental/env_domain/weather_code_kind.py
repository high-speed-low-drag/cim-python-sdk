"""CIM enumeration WeatherCodeKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WeatherCodeKind(CimEnum):
    """Kinds of weather conditions."""

    hail = "hail"
    blowingDust = "blowingDust"
    blowingSand = "blowingSand"
    mist = "mist"
    blowingSnow = "blowingSnow"
    fog = "fog"
    frost = "frost"
    haze = "haze"
    iceCrystals = "iceCrystals"
    iceFog = "iceFog"
    sleet = "sleet"
    smoke = "smoke"
    drizzle = "drizzle"
    rain = "rain"
    rainShowers = "rainShowers"
    rainSnowMix = "rainSnowMix"
    snowSleetMix = "snowSleetMix"
    wintryMix = "wintryMix"
    snow = "snow"
    snowShowers = "snowShowers"
    thunderStorms = "thunderStorms"
    volcanicAsh = "volcanicAsh"
    waterSpouts = "waterSpouts"
    freezingSpray = "freezingSpray"
    freezingDrizzle = "freezingDrizzle"
    freezingRain = "freezingRain"
    cloudy = "cloudy"
    sunny = "sunny"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WeatherCodeKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{3EC746A3-C1F6-4e58-9967-D7CF8177C57A}",
            kind="enumeration",
        )
    )
