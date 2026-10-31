"""CIM class ScheduledActivePowerLimitValue (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value import (
    ScheduledLimitValue,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ScheduledActivePowerLimitValue(ScheduledLimitValue):
    """CIM class ScheduledActivePowerLimitValue."""

    __slots__ = ("value",)

    value: float | None  # ActivePower

    _cim_meta = ClassMeta(
        cim_name="ScheduledActivePowerLimitValue",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{D03914BB-F02B-4722-BF53-1C09B5A994D0}",
        attributes=(AttrMeta("value", "value", "ActivePower", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
