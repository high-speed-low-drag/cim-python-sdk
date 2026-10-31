"""CIM class TapChangerInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TapChangerInfo(AssetInfo):
    """Tap changer data."""

    __slots__ = (
        "bil",
        "ct_rating",
        "ct_ratio",
        "frequency",
        "high_step",
        "is_tcul",
        "low_step",
        "neutral_step",
        "neutral_u",
        "pt_ratio",
        "rated_apparent_power",
        "rated_current",
        "rated_voltage",
        "step_phase_increment",
        "step_voltage_increment",
    )

    is_tcul: bool | None
    pt_ratio: float | None
    ct_ratio: float | None
    ct_rating: float | None  # CurrentFlow
    neutral_u: float | None  # Voltage
    neutral_step: int | None
    high_step: int | None
    low_step: int | None
    step_voltage_increment: float | None  # PerCent
    step_phase_increment: float | None  # AngleDegrees
    rated_voltage: float | None  # Voltage
    rated_apparent_power: float | None  # ApparentPower
    rated_current: float | None  # CurrentFlow
    bil: float | None  # Voltage
    frequency: float | None  # Frequency

    _cim_meta = ClassMeta(
        cim_name="TapChangerInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{72DDFFCD-3592-413c-AAFA-E3834EB67086}",
        attributes=(
            AttrMeta("is_tcul", "isTcul", "bool", 0, 1, "primitive"),
            AttrMeta("pt_ratio", "ptRatio", "float", 0, 1, "primitive"),
            AttrMeta("ct_ratio", "ctRatio", "float", 0, 1, "primitive"),
            AttrMeta("ct_rating", "ctRating", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("neutral_u", "neutralU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("neutral_step", "neutralStep", "int", 0, 1, "primitive"),
            AttrMeta("high_step", "highStep", "int", 0, 1, "primitive"),
            AttrMeta("low_step", "lowStep", "int", 0, 1, "primitive"),
            AttrMeta(
                "step_voltage_increment", "stepVoltageIncrement", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "step_phase_increment", "stepPhaseIncrement", "AngleDegrees", 0, 1, "cimdatatype"
            ),
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta(
                "rated_apparent_power", "ratedApparentPower", "ApparentPower", 0, 1, "cimdatatype"
            ),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("bil", "bil", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("frequency", "frequency", "Frequency", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        is_tcul: bool | None = None,
        pt_ratio: float | None = None,
        ct_ratio: float | None = None,
        ct_rating: float | None = None,
        neutral_u: float | None = None,
        neutral_step: int | None = None,
        high_step: int | None = None,
        low_step: int | None = None,
        step_voltage_increment: float | None = None,
        step_phase_increment: float | None = None,
        rated_voltage: float | None = None,
        rated_apparent_power: float | None = None,
        rated_current: float | None = None,
        bil: float | None = None,
        frequency: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_tcul = is_tcul
        self.pt_ratio = pt_ratio
        self.ct_ratio = ct_ratio
        self.ct_rating = ct_rating
        self.neutral_u = neutral_u
        self.neutral_step = neutral_step
        self.high_step = high_step
        self.low_step = low_step
        self.step_voltage_increment = step_voltage_increment
        self.step_phase_increment = step_phase_increment
        self.rated_voltage = rated_voltage
        self.rated_apparent_power = rated_apparent_power
        self.rated_current = rated_current
        self.bil = bil
        self.frequency = frequency
