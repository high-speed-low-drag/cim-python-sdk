"""CIM enumeration CommodityKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CommodityKind(CimEnum):
    """Kind of commodity being measured."""

    none = "none"
    electricitySecondaryMetered = "electricitySecondaryMetered"
    electricityPrimaryMetered = "electricityPrimaryMetered"
    communication = "communication"
    air = "air"
    insulativeGas = "insulativeGas"
    insulativeOil = "insulativeOil"
    naturalGas = "naturalGas"
    propane = "propane"
    potableWater = "potableWater"
    steam = "steam"
    wasteWater = "wasteWater"
    heatingFluid = "heatingFluid"
    coolingFluid = "coolingFluid"
    nonpotableWater = "nonpotableWater"
    nox = "nox"
    so2 = "so2"
    ch4 = "ch4"
    co2 = "co2"
    carbon = "carbon"
    hch = "hch"
    pfc = "pfc"
    sf6 = "sf6"
    tvLicence = "tvLicence"
    internet = "internet"
    refuse = "refuse"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CommodityKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{A2E31B03-2F48-48e5-A761-4C372BE29E12}",
            kind="enumeration",
        )
    )
