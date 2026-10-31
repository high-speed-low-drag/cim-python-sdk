"""CIM class ScheduledApparentPowerLimitValue (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value import (
    ScheduledLimitValue,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ScheduledApparentPowerLimitValue(ScheduledLimitValue):
    """A time scheduled value for apparent power limit."""

    __slots__ = ("value",)

    value: float | None  # ApparentPower

    _cim_meta = ClassMeta(
        cim_name="ScheduledApparentPowerLimitValue",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{530D3590-84C8-40bf-A6DF-F36A61F164D2}",
        attributes=(AttrMeta("value", "value", "ApparentPower", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
