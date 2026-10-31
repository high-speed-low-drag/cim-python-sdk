"""CIM class AnalogLimitSet (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.meas.limit_set import LimitSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.analog import Analog
    from cim_python_sdk.model.iec61970.base.meas.analog_limit import AnalogLimit


class AnalogLimitSet(LimitSet):
    """An AnalogLimitSet specifies a set of Limits that are associated with an Analog
    measurement."""

    __slots__ = ("_limits", "_measurements")

    measurements: Many[Analog] = Many(
        EndMeta(
            name="measurements",
            cim_role="Measurements",
            target="cim_python_sdk.model.iec61970.base.meas.analog:Analog",
            many=True,
            lower=0,
            upper=None,
            inverse="limit_sets",
            aggregation="none",
        )
    )
    limits: Many[AnalogLimit] = Many(
        EndMeta(
            name="limits",
            cim_role="Limits",
            target="cim_python_sdk.model.iec61970.base.meas.analog_limit:AnalogLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="limit_set",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AnalogLimitSet",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{629BA1E7-A3FB-480f-93A6-0AE81750CC57}",
        ends=(
            measurements.meta,
            limits.meta,
        ),
    )

    def __init__(
        self,
        *,
        measurements: Iterable[Analog] | None = None,
        limits: Iterable[AnalogLimit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if measurements is not None:
            AnalogLimitSet.measurements.extend(self, measurements)
        if limits is not None:
            AnalogLimitSet.limits.extend(self, limits)

    def add_measurement(self, measurement: Analog) -> Self:
        return AnalogLimitSet.measurements.add(self, measurement)

    def remove_measurement(self, measurement: Analog) -> Self:
        return AnalogLimitSet.measurements.remove(self, measurement)

    def clear_measurements(self) -> Self:
        return AnalogLimitSet.measurements.clear(self)

    def num_measurement(self) -> int:
        return AnalogLimitSet.measurements.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Analog | None:
        return AnalogLimitSet.measurements.get_by_mrid(self, mrid)

    def add_limit(self, limit: AnalogLimit) -> Self:
        return AnalogLimitSet.limits.add(self, limit)

    def remove_limit(self, limit: AnalogLimit) -> Self:
        return AnalogLimitSet.limits.remove(self, limit)

    def clear_limits(self) -> Self:
        return AnalogLimitSet.limits.clear(self)

    def num_limit(self) -> int:
        return AnalogLimitSet.limits.count(self)

    def get_limit_by_mrid(self, mrid: str) -> AnalogLimit | None:
        return AnalogLimitSet.limits.get_by_mrid(self, mrid)
