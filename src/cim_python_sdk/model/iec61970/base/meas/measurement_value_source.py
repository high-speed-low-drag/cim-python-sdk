"""CIM class MeasurementValueSource (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue


class MeasurementValueSource(IdentifiedObject):
    """MeasurementValueSource describes the alternative sources updating a MeasurementValue.
    User conventions for how to use the MeasurementValueSource attributes are defined in IEC
    61970-301."""

    __slots__ = ("_measurement_values",)

    measurement_values: Many[MeasurementValue] = Many(
        EndMeta(
            name="measurement_values",
            cim_role="MeasurementValues",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value:MeasurementValue",
            many=True,
            lower=0,
            upper=None,
            inverse="measurement_value_source",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeasurementValueSource",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{9A0BEA87-6F15-4c48-A102-9DA595DD7B0A}",
        ends=(measurement_values.meta,),
    )

    def __init__(
        self,
        *,
        measurement_values: Iterable[MeasurementValue] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if measurement_values is not None:
            MeasurementValueSource.measurement_values.extend(self, measurement_values)

    def add_measurement_value(self, measurement_value: MeasurementValue) -> Self:
        return MeasurementValueSource.measurement_values.add(self, measurement_value)

    def remove_measurement_value(self, measurement_value: MeasurementValue) -> Self:
        return MeasurementValueSource.measurement_values.remove(self, measurement_value)

    def clear_measurement_values(self) -> Self:
        return MeasurementValueSource.measurement_values.clear(self)

    def num_measurement_value(self) -> int:
        return MeasurementValueSource.measurement_values.count(self)

    def get_measurement_value_by_mrid(self, mrid: str) -> MeasurementValue | None:
        return MeasurementValueSource.measurement_values.get_by_mrid(self, mrid)
