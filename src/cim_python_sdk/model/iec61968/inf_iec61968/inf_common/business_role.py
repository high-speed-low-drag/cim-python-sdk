"""CIM class BusinessRole (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status


class BusinessRole(OrganisationRole):
    """A business role that this organisation plays. A single organisation typically performs
    many functions, each one described as a role."""

    __slots__ = ("status", "type")

    type: str | None
    status: Status | None

    _cim_meta = ClassMeta(
        cim_name="BusinessRole",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{CC1A0C97-3407-4923-8E44-A38D972175F4}",
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
