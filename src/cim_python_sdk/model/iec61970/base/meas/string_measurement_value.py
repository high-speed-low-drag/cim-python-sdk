"""CIM class StringMeasurementValue (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.string_measurement import StringMeasurement


class StringMeasurementValue(MeasurementValue):
    """StringMeasurementValue represents a measurement value of type string."""

    __slots__ = ("_string_measurement", "value")

    value: str | None

    string_measurement: One[StringMeasurement] = One(
        EndMeta(
            name="string_measurement",
            cim_role="StringMeasurement",
            target="cim_python_sdk.model.iec61970.base.meas.string_measurement:StringMeasurement",
            many=False,
            lower=1,
            upper=1,
            inverse="string_measurement_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StringMeasurementValue",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{76C03FC7-3DB4-46ec-977E-7C00BF90B881}",
        attributes=(AttrMeta("value", "value", "str", 0, 1, "primitive"),),
        ends=(string_measurement.meta,),
    )

    def __init__(
        self,
        *,
        value: str | None = None,
        string_measurement: StringMeasurement | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        if string_measurement is not None:
            self.string_measurement = string_measurement
