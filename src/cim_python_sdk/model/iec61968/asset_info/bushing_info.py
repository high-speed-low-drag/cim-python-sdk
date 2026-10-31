"""CIM class BushingInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.bushing_insulation_kind import (
        BushingInsulationKind,
    )


class BushingInfo(AssetInfo):
    """Bushing datasheet information."""

    __slots__ = (
        "c1_capacitance",
        "c1_power_factor",
        "c2_capacitance",
        "c2_power_factor",
        "insulation_kind",
        "rated_current",
        "rated_impulse_withstand_voltage",
        "rated_line_to_ground_voltage",
        "rated_voltage",
    )

    insulation_kind: BushingInsulationKind | None
    c1_power_factor: float | None  # PerCent
    c2_power_factor: float | None  # PerCent
    c1_capacitance: float | None  # Capacitance
    c2_capacitance: float | None  # Capacitance
    rated_voltage: float | None  # Voltage
    rated_impulse_withstand_voltage: float | None  # Voltage
    rated_line_to_ground_voltage: float | None  # Voltage
    rated_current: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="BushingInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{4DC01EF0-CC32-4ffd-AB7B-3FA7B8ADAFD9}",
        attributes=(
            AttrMeta(
                "insulation_kind", "insulationKind", "BushingInsulationKind", 0, 1, "enumeration"
            ),
            AttrMeta("c1_power_factor", "c1PowerFactor", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("c2_power_factor", "c2PowerFactor", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("c1_capacitance", "c1Capacitance", "Capacitance", 0, 1, "cimdatatype"),
            AttrMeta("c2_capacitance", "c2Capacitance", "Capacitance", 0, 1, "cimdatatype"),
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta(
                "rated_impulse_withstand_voltage",
                "ratedImpulseWithstandVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "rated_line_to_ground_voltage",
                "ratedLineToGroundVoltage",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        insulation_kind: BushingInsulationKind | None = None,
        c1_power_factor: float | None = None,
        c2_power_factor: float | None = None,
        c1_capacitance: float | None = None,
        c2_capacitance: float | None = None,
        rated_voltage: float | None = None,
        rated_impulse_withstand_voltage: float | None = None,
        rated_line_to_ground_voltage: float | None = None,
        rated_current: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.insulation_kind = insulation_kind
        self.c1_power_factor = c1_power_factor
        self.c2_power_factor = c2_power_factor
        self.c1_capacitance = c1_capacitance
        self.c2_capacitance = c2_capacitance
        self.rated_voltage = rated_voltage
        self.rated_impulse_withstand_voltage = rated_impulse_withstand_voltage
        self.rated_line_to_ground_voltage = rated_line_to_ground_voltage
        self.rated_current = rated_current
