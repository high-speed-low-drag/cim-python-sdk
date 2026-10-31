"""CIM class ScheduledVoltageLimitValue (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.scheduled_limit_value import (
    ScheduledLimitValue,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ScheduledVoltageLimitValue(ScheduledLimitValue):
    """A voltage limit value for a scheduled time."""

    __slots__ = ("value",)

    value: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="ScheduledVoltageLimitValue",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{9D007556-3FFA-4632-B9FF-719141F5D595}",
        attributes=(AttrMeta("value", "value", "Voltage", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        value: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
