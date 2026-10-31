"""CIM enumeration OilTemperatureSource (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilTemperatureSource(CimEnum):
    """Sources for oil temperature."""

    topOilTemperatureGauge = "topOilTemperatureGauge"
    infraredGun = "infraredGun"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilTemperatureSource",
            package="TC57CIM/IEC61968/Assets",
            guid="{EBCB5BFC-C0B7-4c82-83BE-26B0AAD47DCF}",
            kind="enumeration",
        )
    )
