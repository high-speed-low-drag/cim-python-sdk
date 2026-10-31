"""CIM class TapChanger (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.state_variables.sv_tap_step import SvTapStep
    from cim_python_sdk.model.iec61970.base.wires.tap_changer_control import TapChangerControl
    from cim_python_sdk.model.iec61970.base.wires.tap_schedule import TapSchedule


class TapChanger(PowerSystemResource):
    """Mechanism for changing transformer winding tap positions."""

    __slots__ = (
        "_sv_tap_step",
        "_tap_changer_control",
        "_tap_schedules",
        "control_enabled",
        "high_step",
        "initial_delay",
        "low_step",
        "ltc_flag",
        "neutral_step",
        "neutral_u",
        "normal_step",
        "step",
        "subsequent_delay",
    )

    control_enabled: bool | None
    high_step: int | None
    initial_delay: float | None  # Seconds
    low_step: int | None
    ltc_flag: bool | None
    neutral_step: int | None
    neutral_u: float | None  # Voltage
    normal_step: int | None
    subsequent_delay: float | None  # Seconds
    step: float | None

    tap_schedules: Many[TapSchedule] = Many(
        EndMeta(
            name="tap_schedules",
            cim_role="TapSchedules",
            target="cim_python_sdk.model.iec61970.base.wires.tap_schedule:TapSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="tap_changer",
            aggregation="none",
        )
    )
    tap_changer_control: One[TapChangerControl] = One(
        EndMeta(
            name="tap_changer_control",
            cim_role="TapChangerControl",
            target="cim_python_sdk.model.iec61970.base.wires.tap_changer_control:TapChangerControl",
            many=False,
            lower=0,
            upper=1,
            inverse="tap_changer",
            aggregation="none",
        )
    )
    sv_tap_step: One[SvTapStep] = One(
        EndMeta(
            name="sv_tap_step",
            cim_role="SvTapStep",
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_tap_step:SvTapStep",
            many=False,
            lower=0,
            upper=1,
            inverse="tap_changer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TapChanger",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{F43099C0-90EA-47f1-B038-EDE831744C07}",
        attributes=(
            AttrMeta("control_enabled", "controlEnabled", "bool", 0, 1, "primitive"),
            AttrMeta("high_step", "highStep", "int", 0, 1, "primitive"),
            AttrMeta("initial_delay", "initialDelay", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("low_step", "lowStep", "int", 0, 1, "primitive"),
            AttrMeta("ltc_flag", "ltcFlag", "bool", 0, 1, "primitive"),
            AttrMeta("neutral_step", "neutralStep", "int", 0, 1, "primitive"),
            AttrMeta("neutral_u", "neutralU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("normal_step", "normalStep", "int", 0, 1, "primitive"),
            AttrMeta("subsequent_delay", "subsequentDelay", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("step", "step", "float", 0, 1, "primitive"),
        ),
        ends=(
            tap_schedules.meta,
            tap_changer_control.meta,
            sv_tap_step.meta,
        ),
    )

    def __init__(
        self,
        *,
        control_enabled: bool | None = None,
        high_step: int | None = None,
        initial_delay: float | None = None,
        low_step: int | None = None,
        ltc_flag: bool | None = None,
        neutral_step: int | None = None,
        neutral_u: float | None = None,
        normal_step: int | None = None,
        subsequent_delay: float | None = None,
        step: float | None = None,
        tap_schedules: Iterable[TapSchedule] | None = None,
        tap_changer_control: TapChangerControl | None = None,
        sv_tap_step: SvTapStep | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.control_enabled = control_enabled
        self.high_step = high_step
        self.initial_delay = initial_delay
        self.low_step = low_step
        self.ltc_flag = ltc_flag
        self.neutral_step = neutral_step
        self.neutral_u = neutral_u
        self.normal_step = normal_step
        self.subsequent_delay = subsequent_delay
        self.step = step
        if tap_schedules is not None:
            TapChanger.tap_schedules.extend(self, tap_schedules)
        if tap_changer_control is not None:
            self.tap_changer_control = tap_changer_control
        if sv_tap_step is not None:
            self.sv_tap_step = sv_tap_step

    def add_tap_schedule(self, tap_schedule: TapSchedule) -> Self:
        return TapChanger.tap_schedules.add(self, tap_schedule)

    def remove_tap_schedule(self, tap_schedule: TapSchedule) -> Self:
        return TapChanger.tap_schedules.remove(self, tap_schedule)

    def clear_tap_schedules(self) -> Self:
        return TapChanger.tap_schedules.clear(self)

    def num_tap_schedule(self) -> int:
        return TapChanger.tap_schedules.count(self)

    def get_tap_schedule_by_mrid(self, mrid: str) -> TapSchedule | None:
        return TapChanger.tap_schedules.get_by_mrid(self, mrid)
