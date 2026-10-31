"""CIM class Accumulator (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.accumulator_limit_set import AccumulatorLimitSet
    from cim_python_sdk.model.iec61970.base.meas.accumulator_value import AccumulatorValue


class Accumulator(Measurement):
    """Accumulator represents an accumulated (counted) Measurement, e.g. an energy value."""

    __slots__ = ("_accumulator_values", "_limit_sets", "max_value")

    max_value: int | None

    limit_sets: Many[AccumulatorLimitSet] = Many(
        EndMeta(
            name="limit_sets",
            cim_role="LimitSets",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator_limit_set:AccumulatorLimitSet",
            many=True,
            lower=0,
            upper=None,
            inverse="measurements",
            aggregation="none",
        )
    )
    accumulator_values: Many[AccumulatorValue] = Many(
        EndMeta(
            name="accumulator_values",
            cim_role="AccumulatorValues",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator_value:AccumulatorValue",
            many=True,
            lower=0,
            upper=None,
            inverse="accumulator",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Accumulator",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{4A66104E-BA5F-446e-A5B6-C9BBAF00E0F3}",
        attributes=(AttrMeta("max_value", "maxValue", "int", 0, 1, "primitive"),),
        ends=(
            limit_sets.meta,
            accumulator_values.meta,
        ),
    )

    def __init__(
        self,
        *,
        max_value: int | None = None,
        limit_sets: Iterable[AccumulatorLimitSet] | None = None,
        accumulator_values: Iterable[AccumulatorValue] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_value = max_value
        if limit_sets is not None:
            Accumulator.limit_sets.extend(self, limit_sets)
        if accumulator_values is not None:
            Accumulator.accumulator_values.extend(self, accumulator_values)

    def add_limit_set(self, limit_set: AccumulatorLimitSet) -> Self:
        return Accumulator.limit_sets.add(self, limit_set)

    def remove_limit_set(self, limit_set: AccumulatorLimitSet) -> Self:
        return Accumulator.limit_sets.remove(self, limit_set)

    def clear_limit_sets(self) -> Self:
        return Accumulator.limit_sets.clear(self)

    def num_limit_set(self) -> int:
        return Accumulator.limit_sets.count(self)

    def get_limit_set_by_mrid(self, mrid: str) -> AccumulatorLimitSet | None:
        return Accumulator.limit_sets.get_by_mrid(self, mrid)

    def add_accumulator_value(self, accumulator_value: AccumulatorValue) -> Self:
        return Accumulator.accumulator_values.add(self, accumulator_value)

    def remove_accumulator_value(self, accumulator_value: AccumulatorValue) -> Self:
        return Accumulator.accumulator_values.remove(self, accumulator_value)

    def clear_accumulator_values(self) -> Self:
        return Accumulator.accumulator_values.clear(self)

    def num_accumulator_value(self) -> int:
        return Accumulator.accumulator_values.count(self)

    def get_accumulator_value_by_mrid(self, mrid: str) -> AccumulatorValue | None:
        return Accumulator.accumulator_values.get_by_mrid(self, mrid)
