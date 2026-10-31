"""CIM class TapChangerDynamicData (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_tap_changer import (
        MktTapChanger,
    )


class TapChangerDynamicData(CimObject):
    """Optimal Power Flow or State Estimator Phase Shifter Data. This is used for RealTime,
    Study and Maintenance Users. SE Solution Phase Shifter Measurements from the last run of
    SE."""

    __slots__ = (
        "_mkt_tap_changer",
        "angle_regulation_status",
        "desired_mw",
        "desired_voltage",
        "maximum_angle",
        "minimum_angle",
        "solved_angle",
        "tap_position",
        "voltage_regulation_status",
    )

    tap_position: float | None
    desired_voltage: float | None
    voltage_regulation_status: bool | None
    angle_regulation_status: bool | None
    desired_mw: float | None
    solved_angle: float | None
    minimum_angle: float | None
    maximum_angle: float | None

    mkt_tap_changer: One[MktTapChanger] = One(
        EndMeta(
            name="mkt_tap_changer",
            cim_role="MktTapChanger",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_tap_changer:MktTapChanger",
            many=False,
            lower=1,
            upper=1,
            inverse="tap_changer_dynamic_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TapChangerDynamicData",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{7E8D865C-55AD-4ebb-9380-2A1271288F7B}",
        attributes=(
            AttrMeta("tap_position", "tapPosition", "float", 0, 1, "primitive"),
            AttrMeta("desired_voltage", "desiredVoltage", "float", 0, 1, "primitive"),
            AttrMeta(
                "voltage_regulation_status", "voltageRegulationStatus", "bool", 0, 1, "primitive"
            ),
            AttrMeta("angle_regulation_status", "angleRegulationStatus", "bool", 0, 1, "primitive"),
            AttrMeta("desired_mw", "desiredMW", "float", 0, 1, "primitive"),
            AttrMeta("solved_angle", "solvedAngle", "float", 0, 1, "primitive"),
            AttrMeta("minimum_angle", "minimumAngle", "float", 0, 1, "primitive"),
            AttrMeta("maximum_angle", "maximumAngle", "float", 0, 1, "primitive"),
        ),
        ends=(mkt_tap_changer.meta,),
    )

    def __init__(
        self,
        *,
        tap_position: float | None = None,
        desired_voltage: float | None = None,
        voltage_regulation_status: bool | None = None,
        angle_regulation_status: bool | None = None,
        desired_mw: float | None = None,
        solved_angle: float | None = None,
        minimum_angle: float | None = None,
        maximum_angle: float | None = None,
        mkt_tap_changer: MktTapChanger | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tap_position = tap_position
        self.desired_voltage = desired_voltage
        self.voltage_regulation_status = voltage_regulation_status
        self.angle_regulation_status = angle_regulation_status
        self.desired_mw = desired_mw
        self.solved_angle = solved_angle
        self.minimum_angle = minimum_angle
        self.maximum_angle = maximum_angle
        if mkt_tap_changer is not None:
            self.mkt_tap_changer = mkt_tap_changer
