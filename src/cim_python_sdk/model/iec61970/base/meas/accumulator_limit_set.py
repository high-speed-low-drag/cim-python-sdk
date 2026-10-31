"""CIM class AccumulatorLimitSet (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.meas.limit_set import LimitSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.accumulator import Accumulator
    from cim_python_sdk.model.iec61970.base.meas.accumulator_limit import AccumulatorLimit


class AccumulatorLimitSet(LimitSet):
    """An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator
    measurement."""

    __slots__ = ("_limits", "_measurements")

    limits: Many[AccumulatorLimit] = Many(
        EndMeta(
            name="limits",
            cim_role="Limits",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator_limit:AccumulatorLimit",
            many=True,
            lower=1,
            upper=None,
            inverse="limit_set",
            aggregation="shared",
        )
    )
    measurements: Many[Accumulator] = Many(
        EndMeta(
            name="measurements",
            cim_role="Measurements",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator:Accumulator",
            many=True,
            lower=0,
            upper=None,
            inverse="limit_sets",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AccumulatorLimitSet",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{25F6012B-0434-4c9b-8E77-E64E5897923B}",
        ends=(
            limits.meta,
            measurements.meta,
        ),
    )

    def __init__(
        self,
        *,
        limits: Iterable[AccumulatorLimit] | None = None,
        measurements: Iterable[Accumulator] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if limits is not None:
            AccumulatorLimitSet.limits.extend(self, limits)
        if measurements is not None:
            AccumulatorLimitSet.measurements.extend(self, measurements)

    def add_limit(self, limit: AccumulatorLimit) -> Self:
        return AccumulatorLimitSet.limits.add(self, limit)

    def remove_limit(self, limit: AccumulatorLimit) -> Self:
        return AccumulatorLimitSet.limits.remove(self, limit)

    def clear_limits(self) -> Self:
        return AccumulatorLimitSet.limits.clear(self)

    def num_limit(self) -> int:
        return AccumulatorLimitSet.limits.count(self)

    def get_limit_by_mrid(self, mrid: str) -> AccumulatorLimit | None:
        return AccumulatorLimitSet.limits.get_by_mrid(self, mrid)

    def add_measurement(self, measurement: Accumulator) -> Self:
        return AccumulatorLimitSet.measurements.add(self, measurement)

    def remove_measurement(self, measurement: Accumulator) -> Self:
        return AccumulatorLimitSet.measurements.remove(self, measurement)

    def clear_measurements(self) -> Self:
        return AccumulatorLimitSet.measurements.clear(self)

    def num_measurement(self) -> int:
        return AccumulatorLimitSet.measurements.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Accumulator | None:
        return AccumulatorLimitSet.measurements.get_by_mrid(self, mrid)
