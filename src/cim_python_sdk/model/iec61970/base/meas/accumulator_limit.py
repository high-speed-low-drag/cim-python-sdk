"""CIM class AccumulatorLimit (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.limit import Limit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.accumulator_limit_set import AccumulatorLimitSet


class AccumulatorLimit(Limit):
    """Limit values for Accumulator measurements."""

    __slots__ = ("_limit_set", "value")

    value: int | None

    limit_set: One[AccumulatorLimitSet] = One(
        EndMeta(
            name="limit_set",
            cim_role="LimitSet",
            target="cim_python_sdk.model.iec61970.base.meas.accumulator_limit_set:AccumulatorLimitSet",
            many=False,
            lower=1,
            upper=1,
            inverse="limits",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AccumulatorLimit",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{58445F1F-311A-409e-9B07-F05F6BAACE20}",
        attributes=(AttrMeta("value", "value", "int", 0, 1, "primitive"),),
        ends=(limit_set.meta,),
    )

    def __init__(
        self,
        *,
        value: int | None = None,
        limit_set: AccumulatorLimitSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        if limit_set is not None:
            self.limit_set = limit_set
