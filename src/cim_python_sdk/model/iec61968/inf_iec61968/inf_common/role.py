"""CIM class Role (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status


class Role(IdentifiedObject):
    """Enumeration of potential roles that might be played by one object relative to another."""

    __slots__ = ("status", "type")

    type: str | None
    status: Status | None

    _cim_meta = ClassMeta(
        cim_name="Role",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{9A4F58D3-9532-4488-AC87-867473F3EC06}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        status: Status | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.status = status
