"""CIM class LimitSet (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class LimitSet(IdentifiedObject):
    """Specifies a set of Limits that are associated with a Measurement. A Measurement may have
    several LimitSets corresponding to seasonal or other changing conditions. The condition
    is captured in the name and description attributes. The same LimitSet may be used for
    several Measurements. In particular percentage limits are used this way."""

    __slots__ = ("is_percentage_limits",)

    is_percentage_limits: bool | None

    _cim_meta = ClassMeta(
        cim_name="LimitSet",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{D0F989DA-F598-4d05-98C6-4148DE43F7AB}",
        attributes=(
            AttrMeta("is_percentage_limits", "isPercentageLimits", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        is_percentage_limits: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_percentage_limits = is_percentage_limits
