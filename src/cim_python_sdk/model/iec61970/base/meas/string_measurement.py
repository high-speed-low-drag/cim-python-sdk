"""CIM class StringMeasurement (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.meas.string_measurement_value import (
        StringMeasurementValue,
    )


class StringMeasurement(Measurement):
    """StringMeasurement represents a measurement with values of type string."""

    __slots__ = ("_string_measurement_values",)

    string_measurement_values: Many[StringMeasurementValue] = Many(
        EndMeta(
            name="string_measurement_values",
            cim_role="StringMeasurementValues",
            target="cim_python_sdk.model.iec61970.base.meas.string_measurement_value:StringMeasurementValue",
            many=True,
            lower=0,
            upper=None,
            inverse="string_measurement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StringMeasurement",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{3EC705BA-D494-4102-AD0B-8CD7A9EECE3B}",
        ends=(string_measurement_values.meta,),
    )

    def __init__(
        self,
        *,
        string_measurement_values: Iterable[StringMeasurementValue] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if string_measurement_values is not None:
            StringMeasurement.string_measurement_values.extend(self, string_measurement_values)

    def add_string_measurement_value(
        self, string_measurement_value: StringMeasurementValue
    ) -> Self:
        return StringMeasurement.string_measurement_values.add(self, string_measurement_value)

    def remove_string_measurement_value(
        self, string_measurement_value: StringMeasurementValue
    ) -> Self:
        return StringMeasurement.string_measurement_values.remove(self, string_measurement_value)

    def clear_string_measurement_values(self) -> Self:
        return StringMeasurement.string_measurement_values.clear(self)

    def num_string_measurement_value(self) -> int:
        return StringMeasurement.string_measurement_values.count(self)

    def get_string_measurement_value_by_mrid(self, mrid: str) -> StringMeasurementValue | None:
        return StringMeasurement.string_measurement_values.get_by_mrid(self, mrid)
