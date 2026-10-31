"""CIM class ScheduledCurrentLimitValue (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value import (
    ScheduledLimitValue,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ScheduledCurrentLimitValue(ScheduledLimitValue):
    """A current limit that is scheduled."""

    __slots__ = ("value",)

    value: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="ScheduledCurrentLimitValue",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{1DF02F1D-5B29-4ab9-B925-A921AD897A93}",
        attributes=(AttrMeta("value", "value", "CurrentFlow", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
