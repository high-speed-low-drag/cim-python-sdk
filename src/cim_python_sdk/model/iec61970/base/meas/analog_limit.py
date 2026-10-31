"""CIM class AnalogLimit (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.limit import Limit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.analog_limit_set import AnalogLimitSet


class AnalogLimit(Limit):
    """Limit values for Analog measurements."""

    __slots__ = ("_limit_set", "value")

    value: float | None

    limit_set: One[AnalogLimitSet] = One(
        EndMeta(
            name="limit_set",
            cim_role="LimitSet",
            target="cim_python_sdk.model.iec61970.base.meas.analog_limit_set:AnalogLimitSet",
            many=False,
            lower=1,
            upper=1,
            inverse="limits",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AnalogLimit",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{7B8D1296-E9A1-4d2c-87AF-C3DED5FD9463}",
        attributes=(AttrMeta("value", "value", "float", 0, 1, "primitive"),),
        ends=(limit_set.meta,),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        limit_set: AnalogLimitSet | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        if limit_set is not None:
            self.limit_set = limit_set
