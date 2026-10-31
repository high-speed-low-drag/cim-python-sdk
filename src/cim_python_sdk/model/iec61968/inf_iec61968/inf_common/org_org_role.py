"""CIM class OrgOrgRole (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class OrgOrgRole(OrganisationRole):
    """Roles played between Organisations and other Organisations. This includes role ups for
    ogranisations, cost centers, profit centers, regulatory reporting, etc.

    Note that the parent and child relationship is indicated by the name on each end of the
    association."""

    __slots__ = ("client_id",)

    client_id: str | None

    _cim_meta = ClassMeta(
        cim_name="OrgOrgRole",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{BC155F06-3541-48cf-A84A-B1E6A3BFFF0A}",
        attributes=(AttrMeta("client_id", "clientID", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        client_id: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.client_id = client_id
