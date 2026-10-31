"""CIM class SurgeArresterInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class SurgeArresterInfo(AssetInfo):
    """Properties of surge arrester."""

    __slots__ = (
        "continuous_operating_voltage",
        "is_polymer",
        "lightning_impulse_discharge_voltage",
        "line_discharge_class",
        "nominal_discharge_current",
        "pressure_relief_class",
        "rated_voltage",
        "steep_front_discharge_voltage",
        "switching_impulse_discharge_voltage",
    )

    rated_voltage: float | None  # Voltage
    continuous_operating_voltage: float | None  # Voltage
    nominal_discharge_current: float | None  # CurrentFlow
    line_discharge_class: int | None
    steep_front_discharge_voltage: float | None  # Voltage
    lightning_impulse_discharge_voltage: float | None  # Voltage
    switching_impulse_discharge_voltage: float | None  # Voltage
    pressure_relief_class: float | None  # CurrentFlow
    is_polymer: bool | None

    _cim_meta = ClassMeta(
        cim_name="SurgeArresterInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{370B4FF9-5E0B-471b-84E3-8CA9185651CD}",
        attributes=(
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta(
                "continuous_operating_voltage",
                "continuousOperatingVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "nominal_discharge_current",
                "nominalDischargeCurrent",
                "CurrentFlow",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("line_discharge_class", "lineDischargeClass", "int", 0, 1, "primitive"),
            AttrMeta(
                "steep_front_discharge_voltage",
                "steepFrontDischargeVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "lightning_impulse_discharge_voltage",
                "lightningImpulseDischargeVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "switching_impulse_discharge_voltage",
                "switchingImpulseDischargeVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "pressure_relief_class", "pressureReliefClass", "CurrentFlow", 0, 1, "cimdatatype"
            ),
            AttrMeta("is_polymer", "isPolymer", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        rated_voltage: float | None = None,
        continuous_operating_voltage: float | None = None,
        nominal_discharge_current: float | None = None,
        line_discharge_class: int | None = None,
        steep_front_discharge_voltage: float | None = None,
        lightning_impulse_discharge_voltage: float | None = None,
        switching_impulse_discharge_voltage: float | None = None,
        pressure_relief_class: float | None = None,
        is_polymer: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_voltage = rated_voltage
        self.continuous_operating_voltage = continuous_operating_voltage
        self.nominal_discharge_current = nominal_discharge_current
        self.line_discharge_class = line_discharge_class
        self.steep_front_discharge_voltage = steep_front_discharge_voltage
        self.lightning_impulse_discharge_voltage = lightning_impulse_discharge_voltage
        self.switching_impulse_discharge_voltage = switching_impulse_discharge_voltage
        self.pressure_relief_class = pressure_relief_class
        self.is_polymer = is_polymer
