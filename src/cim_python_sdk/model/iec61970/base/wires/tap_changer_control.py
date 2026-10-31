"""CIM class TapChangerControl (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.regulating_control import RegulatingControl

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.tap_changer import TapChanger


class TapChangerControl(RegulatingControl):
    """Describes behaviour specific to tap changers, e.g. how the voltage at the end of a line
    varies with the load level and compensation of the voltage drop by tap adjustment."""

    __slots__ = (
        "_tap_changer",
        "limit_voltage",
        "line_drop_compensation",
        "line_drop_r",
        "line_drop_x",
        "reverse_line_drop_r",
        "reverse_line_drop_x",
    )

    limit_voltage: float | None  # Voltage
    line_drop_compensation: bool | None
    line_drop_r: float | None  # Resistance
    line_drop_x: float | None  # Reactance
    reverse_line_drop_r: float | None  # Resistance
    reverse_line_drop_x: float | None  # Reactance

    tap_changer: Many[TapChanger] = Many(
        EndMeta(
            name="tap_changer",
            cim_role="TapChanger",
            target="cim_python_sdk.model.iec61970.base.wires.tap_changer:TapChanger",
            many=True,
            lower=1,
            upper=None,
            inverse="tap_changer_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TapChangerControl",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{32D5C39A-ABB5-4ac8-8B3F-FBDC00DB19BB}",
        attributes=(
            AttrMeta("limit_voltage", "limitVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("line_drop_compensation", "lineDropCompensation", "bool", 0, 1, "primitive"),
            AttrMeta("line_drop_r", "lineDropR", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("line_drop_x", "lineDropX", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("reverse_line_drop_r", "reverseLineDropR", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("reverse_line_drop_x", "reverseLineDropX", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(tap_changer.meta,),
    )

    def __init__(
        self,
        *,
        limit_voltage: float | None = None,
        line_drop_compensation: bool | None = None,
        line_drop_r: float | None = None,
        line_drop_x: float | None = None,
        reverse_line_drop_r: float | None = None,
        reverse_line_drop_x: float | None = None,
        tap_changer: Iterable[TapChanger] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.limit_voltage = limit_voltage
        self.line_drop_compensation = line_drop_compensation
        self.line_drop_r = line_drop_r
        self.line_drop_x = line_drop_x
        self.reverse_line_drop_r = reverse_line_drop_r
        self.reverse_line_drop_x = reverse_line_drop_x
        if tap_changer is not None:
            TapChangerControl.tap_changer.extend(self, tap_changer)

    def add_tap_changer(self, tap_changer: TapChanger) -> Self:
        return TapChangerControl.tap_changer.add(self, tap_changer)

    def remove_tap_changer(self, tap_changer: TapChanger) -> Self:
        return TapChangerControl.tap_changer.remove(self, tap_changer)

    def clear_tap_changer(self) -> Self:
        return TapChangerControl.tap_changer.clear(self)

    def num_tap_changer(self) -> int:
        return TapChangerControl.tap_changer.count(self)

    def get_tap_changer_by_mrid(self, mrid: str) -> TapChanger | None:
        return TapChangerControl.tap_changer.get_by_mrid(self, mrid)
