"""CIM compound ControlledAppliance (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class ControlledAppliance(CimCompound):
    """Appliance controlled with a PAN device control."""

    __slots__ = (
        "is_electric_vehicle",
        "is_exterior_lighting",
        "is_generation_system",
        "is_hvac_compressor_or_furnace",
        "is_interior_lighting",
        "is_irrigation_pump",
        "is_managed_commercial_industrial_load",
        "is_pool_pump_spa_jacuzzi",
        "is_simple_misc_load",
        "is_smart_appliance",
        "is_strip_and_baseboard_heater",
        "is_water_heater",
    )

    is_electric_vehicle: bool | None
    is_exterior_lighting: bool | None
    is_interior_lighting: bool | None
    is_generation_system: bool | None
    is_hvac_compressor_or_furnace: bool | None
    is_irrigation_pump: bool | None
    is_managed_commercial_industrial_load: bool | None
    is_pool_pump_spa_jacuzzi: bool | None
    is_simple_misc_load: bool | None
    is_smart_appliance: bool | None
    is_strip_and_baseboard_heater: bool | None
    is_water_heater: bool | None

    _cim_meta = ClassMeta(
        cim_name="ControlledAppliance",
        package="TC57CIM/IEC61968/Metering",
        guid="{1336F01E-072B-44fd-9D24-EBC9EC60B281}",
        kind="compound",
        attributes=(
            AttrMeta("is_electric_vehicle", "isElectricVehicle", "bool", 0, 1, "primitive"),
            AttrMeta("is_exterior_lighting", "isExteriorLighting", "bool", 0, 1, "primitive"),
            AttrMeta("is_interior_lighting", "isInteriorLighting", "bool", 0, 1, "primitive"),
            AttrMeta("is_generation_system", "isGenerationSystem", "bool", 0, 1, "primitive"),
            AttrMeta(
                "is_hvac_compressor_or_furnace",
                "isHvacCompressorOrFurnace",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta("is_irrigation_pump", "isIrrigationPump", "bool", 0, 1, "primitive"),
            AttrMeta(
                "is_managed_commercial_industrial_load",
                "isManagedCommercialIndustrialLoad",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta("is_pool_pump_spa_jacuzzi", "isPoolPumpSpaJacuzzi", "bool", 0, 1, "primitive"),
            AttrMeta("is_simple_misc_load", "isSimpleMiscLoad", "bool", 0, 1, "primitive"),
            AttrMeta("is_smart_appliance", "isSmartAppliance", "bool", 0, 1, "primitive"),
            AttrMeta(
                "is_strip_and_baseboard_heater",
                "isStripAndBaseboardHeater",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta("is_water_heater", "isWaterHeater", "bool", 0, 1, "primitive"),
        ),
    )
