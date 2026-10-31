"""CIM enumeration AssetTemperaturePressureAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetTemperaturePressureAnalogKind(CimEnum):
    """Analogs representing temperatures or pressures related to assets."""

    oilTemperatureAtValve = "oilTemperatureAtValve"
    oilPressureAtValve = "oilPressureAtValve"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetTemperaturePressureAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{DD05A091-668C-4592-B797-8A7A81D597FA}",
            kind="enumeration",
        )
    )
