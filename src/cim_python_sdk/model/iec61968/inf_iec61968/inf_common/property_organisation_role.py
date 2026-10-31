"""CIM class PropertyOrganisationRole (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property import LandProperty


class PropertyOrganisationRole(OrganisationRole):
    """Role an organisation plays with respect to property (for example, the organisation may
    be the owner, renter, occupier, taxiing authority, etc.)."""

    __slots__ = ("_land_property",)

    land_property: Many[LandProperty] = Many(
        EndMeta(
            name="land_property",
            cim_role="LandProperty",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property:LandProperty",
            many=True,
            lower=1,
            upper=None,
            inverse="erp_organisation_roles",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PropertyOrganisationRole",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{932B12D0-870B-4599-A9F1-735101651947}",
        ends=(land_property.meta,),
    )

    def __init__(
        self,
        *,
        land_property: Iterable[LandProperty] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if land_property is not None:
            PropertyOrganisationRole.land_property.extend(self, land_property)

    def add_land_property(self, land_property: LandProperty) -> Self:
        return PropertyOrganisationRole.land_property.add(self, land_property)

    def remove_land_property(self, land_property: LandProperty) -> Self:
        return PropertyOrganisationRole.land_property.remove(self, land_property)

    def clear_land_property(self) -> Self:
        return PropertyOrganisationRole.land_property.clear(self)

    def num_land_property(self) -> int:
        return PropertyOrganisationRole.land_property.count(self)

    def get_land_property_by_mrid(self, mrid: str) -> LandProperty | None:
        return PropertyOrganisationRole.land_property.get_by_mrid(self, mrid)
