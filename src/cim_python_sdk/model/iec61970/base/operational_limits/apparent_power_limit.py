"""CIM class ApparentPowerLimit (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import OperationalLimit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ApparentPowerLimit(OperationalLimit):
    """Apparent power limit."""

    __slots__ = ("normal_value", "value")

    normal_value: float | None  # ApparentPower
    value: float | None  # ApparentPower

    _cim_meta = ClassMeta(
        cim_name="ApparentPowerLimit",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{4A84BEAD-A18F-4474-B5D6-471216783A07}",
        attributes=(
            AttrMeta("normal_value", "normalValue", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("value", "value", "ApparentPower", 0, 1, "cimdatatype"),
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
