"""CIM class SetPoint (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.meas.analog_control import AnalogControl

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class SetPoint(AnalogControl):
    """An analog control that issues a set point value."""

    __slots__ = ("normal_value", "value")

    normal_value: float | None
    value: float | None

    _cim_meta = ClassMeta(
        cim_name="SetPoint",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{34230D45-F881-4938-9104-22653DEFE6A2}",
        attributes=(
            AttrMeta("normal_value", "normalValue", "float", 0, 1, "primitive"),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        normal_value: float | None = None,
        value: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.normal_value = normal_value
        self.value = value
