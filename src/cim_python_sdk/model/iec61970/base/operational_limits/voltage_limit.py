"""CIM class VoltageLimit (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import OperationalLimit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class VoltageLimit(OperationalLimit):
    """Operational limit applied to voltage.

    The use of operational VoltageLimit is preferred instead of limits defined at
    VoltageLevel. The operational VoltageLimits are used, if present."""

    __slots__ = ("normal_value", "value")

    normal_value: float | None  # Voltage
    value: float | None  # Voltage

    _cim_meta = ClassMeta(
        cim_name="VoltageLimit",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{9D49B294-C5CA-4145-BE42-437419517604}",
        attributes=(
            AttrMeta("normal_value", "normalValue", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("value", "value", "Voltage", 0, 1, "cimdatatype"),
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
