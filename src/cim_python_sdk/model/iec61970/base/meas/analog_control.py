"""CIM class AnalogControl (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.control import Control

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.analog_value import AnalogValue


class AnalogControl(Control):
    """An analog control used for supervisory control."""

    __slots__ = ("_analog_value", "max_value", "min_value")

    max_value: float | None
    min_value: float | None

    analog_value: One[AnalogValue] = One(
        EndMeta(
            name="analog_value",
            cim_role="AnalogValue",
            target="cim_python_sdk.model.iec61970.base.meas.analog_value:AnalogValue",
            many=False,
            lower=1,
            upper=1,
            inverse="analog_control",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AnalogControl",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{EF5C08B7-CB93-438d-B73A-9F7406694697}",
        attributes=(
            AttrMeta("max_value", "maxValue", "float", 0, 1, "primitive"),
            AttrMeta("min_value", "minValue", "float", 0, 1, "primitive"),
        ),
        ends=(analog_value.meta,),
    )

    def __init__(
        self,
        *,
        max_value: float | None = None,
        min_value: float | None = None,
        analog_value: AnalogValue | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_value = max_value
        self.min_value = min_value
        if analog_value is not None:
            self.analog_value = analog_value
