"""CIM class ActivePowerLimit (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import OperationalLimit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ActivePowerLimit(OperationalLimit):
    """Limit on active power flow."""

    __slots__ = ("normal_value", "value")

    normal_value: float | None  # ActivePower
    value: float | None  # ActivePower

    _cim_meta = ClassMeta(
        cim_name="ActivePowerLimit",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{37990C74-B64A-4f62-B6ED-FD6133282C42}",
        attributes=(
            AttrMeta("normal_value", "normalValue", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("value", "value", "ActivePower", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        normal_value: float | None = None,
        value: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.normal_value = normal_value
        self.value = value
