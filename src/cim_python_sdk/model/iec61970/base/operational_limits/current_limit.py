"""CIM class CurrentLimit (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import OperationalLimit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class CurrentLimit(OperationalLimit):
    """Operational limit on current."""

    __slots__ = ("normal_value", "value")

    normal_value: float | None  # CurrentFlow
    value: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="CurrentLimit",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{608E420F-FE83-4965-9ED8-F12FF4BCF787}",
        attributes=(
            AttrMeta("normal_value", "normalValue", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("value", "value", "CurrentFlow", 0, 1, "cimdatatype"),
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
