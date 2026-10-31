"""CIM class Analog (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.analog_limit_set import AnalogLimitSet
    from cim_python_sdk.model.iec61970.base.meas.analog_value import AnalogValue


class Analog(Measurement):
    """Analog represents an analog Measurement."""

    __slots__ = (
        "_analog_values",
        "_limit_sets",
        "max_value",
        "min_value",
        "normal_value",
        "positive_flow_in",
    )

    max_value: float | None
    min_value: float | None
    normal_value: float | None
    positive_flow_in: bool | None

    limit_sets: Many[AnalogLimitSet] = Many(
        EndMeta(
            name="limit_sets",
            cim_role="LimitSets",
            target="cim_python_sdk.model.iec61970.base.meas.analog_limit_set:AnalogLimitSet",
            many=True,
            lower=0,
            upper=None,
            inverse="measurements",
            aggregation="none",
        )
    )
    analog_values: Many[AnalogValue] = Many(
        EndMeta(
            name="analog_values",
            cim_role="AnalogValues",
            target="cim_python_sdk.model.iec61970.base.meas.analog_value:AnalogValue",
            many=True,
            lower=0,
            upper=None,
            inverse="analog",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Analog",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{BBCB109C-256C-42ee-9B78-8B17B54C9668}",
        attributes=(
            AttrMeta("max_value", "maxValue", "float", 0, 1, "primitive"),
            AttrMeta("min_value", "minValue", "float", 0, 1, "primitive"),
            AttrMeta("normal_value", "normalValue", "float", 0, 1, "primitive"),
            AttrMeta("positive_flow_in", "positiveFlowIn", "bool", 0, 1, "primitive"),
        ),
        ends=(
            limit_sets.meta,
            analog_values.meta,
        ),
    )

    def __init__(
        self,
        *,
        max_value: float | None = None,
        min_value: float | None = None,
        normal_value: float | None = None,
        positive_flow_in: bool | None = None,
        limit_sets: Iterable[AnalogLimitSet] | None = None,
        analog_values: Iterable[AnalogValue] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_value = max_value
        self.min_value = min_value
        self.normal_value = normal_value
        self.positive_flow_in = positive_flow_in
        if limit_sets is not None:
            Analog.limit_sets.extend(self, limit_sets)
        if analog_values is not None:
            Analog.analog_values.extend(self, analog_values)

    def add_limit_set(self, limit_set: AnalogLimitSet) -> Self:
        return Analog.limit_sets.add(self, limit_set)

    def remove_limit_set(self, limit_set: AnalogLimitSet) -> Self:
        return Analog.limit_sets.remove(self, limit_set)

    def clear_limit_sets(self) -> Self:
        return Analog.limit_sets.clear(self)

    def num_limit_set(self) -> int:
        return Analog.limit_sets.count(self)

    def get_limit_set_by_mrid(self, mrid: str) -> AnalogLimitSet | None:
        return Analog.limit_sets.get_by_mrid(self, mrid)

    def add_analog_value(self, analog_value: AnalogValue) -> Self:
        return Analog.analog_values.add(self, analog_value)

    def remove_analog_value(self, analog_value: AnalogValue) -> Self:
        return Analog.analog_values.remove(self, analog_value)

    def clear_analog_values(self) -> Self:
        return Analog.analog_values.clear(self)

    def num_analog_value(self) -> int:
        return Analog.analog_values.count(self)

    def get_analog_value_by_mrid(self, mrid: str) -> AnalogValue | None:
        return Analog.analog_values.get_by_mrid(self, mrid)
