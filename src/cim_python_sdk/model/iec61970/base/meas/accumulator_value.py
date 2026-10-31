"""CIM class AccumulatorValue (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.accumulator import Accumulator
    from cim_python_sdk.model.iec61970.base.meas.accumulator_reset import AccumulatorReset


class AccumulatorValue(MeasurementValue):
    """AccumulatorValue represents an accumulated (counted) MeasurementValue."""

    __slots__ = ("_accumulator", "_accumulator_reset", "value")

    value: int | None

    accumulator_reset: One[AccumulatorReset] = One(
        EndMeta(
            name="accumulator_reset",
            cim_role="AccumulatorReset",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator_reset:AccumulatorReset",
            many=False,
            lower=0,
            upper=1,
            inverse="accumulator_value",
            aggregation="none",
        )
    )
    accumulator: One[Accumulator] = One(
        EndMeta(
            name="accumulator",
            cim_role="Accumulator",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator:Accumulator",
            many=False,
            lower=1,
            upper=1,
            inverse="accumulator_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AccumulatorValue",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{EBC302E8-45FB-4cb3-8F17-3CC7387EE297}",
        attributes=(AttrMeta("value", "value", "int", 0, 1, "primitive"),),
        ends=(
            accumulator_reset.meta,
            accumulator.meta,
        ),
    )

    def __init__(
        self,
        *,
        value: int | None = None,
        accumulator_reset: AccumulatorReset | None = None,
        accumulator: Accumulator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        if accumulator_reset is not None:
            self.accumulator_reset = accumulator_reset
        if accumulator is not None:
            self.accumulator = accumulator
