"""CIM class AccumulatorReset (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.control import Control

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.accumulator_value import AccumulatorValue


class AccumulatorReset(Control):
    """This command resets the counter value to zero."""

    __slots__ = ("_accumulator_value",)

    accumulator_value: One[AccumulatorValue] = One(
        EndMeta(
            name="accumulator_value",
            cim_role="AccumulatorValue",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator_value:AccumulatorValue",
            many=False,
            lower=1,
            upper=1,
            inverse="accumulator_reset",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AccumulatorReset",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{4B18D989-2A07-447e-B794-898A1DF10DEC}",
        ends=(accumulator_value.meta,),
    )

    def __init__(
        self,
        *,
        accumulator_value: AccumulatorValue | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if accumulator_value is not None:
            self.accumulator_value = accumulator_value
