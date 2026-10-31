"""CIM class LandProperty (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset_container import AssetContainer
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.person_property_role import (
        PersonPropertyRole,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.property_organisation_role import (
        PropertyOrganisationRole,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_site_level_data import (
        ErpSiteLevelData,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.demographic_kind import (
        DemographicKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property_kind import (
        LandPropertyKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.location_grant import (
        LocationGrant,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.right_of_way import RightOfWay


class LandProperty(IdentifiedObject):
    """Information about a particular piece of (land) property such as its use. Ownership of
    the property may be determined through associations to Organisations and/or ErpPersons."""

    __slots__ = (
        "_asset_containers",
        "_erp_organisation_roles",
        "_erp_person_roles",
        "_erp_site_level_datas",
        "_location_grants",
        "_locations",
        "_right_of_ways",
        "demographic_kind",
        "external_record_reference",
        "kind",
        "status",
    )

    kind: LandPropertyKind | None
    demographic_kind: DemographicKind | None
    external_record_reference: str | None
    status: Status | None

    erp_organisation_roles: Many[PropertyOrganisationRole] = Many(
        EndMeta(
            name="erp_organisation_roles",
            cim_role="ErpOrganisationRoles",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.property_organisation_role:PropertyOrganisationRole",
            many=True,
            lower=0,
            upper=None,
            inverse="land_property",
            aggregation="none",
        )
    )
    asset_containers: Many[AssetContainer] = Many(
        EndMeta(
            name="asset_containers",
            cim_role="AssetContainers",
            target="cim_python_sdk.model.iec61968.assets.asset_container:AssetContainer",
            many=True,
            lower=0,
            upper=None,
            inverse="land_properties",
            aggregation="none",
        )
    )
    erp_site_level_datas: Many[ErpSiteLevelData] = Many(
        EndMeta(
            name="erp_site_level_datas",
            cim_role="ErpSiteLevelDatas",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_site_level_data:ErpSiteLevelData",
            many=True,
            lower=0,
            upper=None,
            inverse="land_property",
            aggregation="none",
        )
    )
    locations: Many[Location] = Many(
        EndMeta(
            name="locations",
            cim_role="Locations",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=True,
            lower=0,
            upper=None,
            inverse="land_properties",
            aggregation="none",
        )
    )
    location_grants: Many[LocationGrant] = Many(
        EndMeta(
            name="location_grants",
            cim_role="LocationGrants",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.location_grant:LocationGrant",
            many=True,
            lower=0,
            upper=None,
            inverse="land_property",
            aggregation="none",
        )
    )
    erp_person_roles: Many[PersonPropertyRole] = Many(
        EndMeta(
            name="erp_person_roles",
            cim_role="ErpPersonRoles",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.person_property_role:PersonPropertyRole",
            many=True,
            lower=0,
            upper=None,
            inverse="land_property",
            aggregation="none",
        )
    )
    right_of_ways: Many[RightOfWay] = Many(
        EndMeta(
            name="right_of_ways",
            cim_role="RightOfWays",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.right_of_way:RightOfWay",
            many=True,
            lower=0,
            upper=None,
            inverse="land_properties",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LandProperty",
        package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
        guid="{B793B5F9-0EB8-4854-92EC-0D26B22AFAF1}",
        attributes=(
            AttrMeta("kind", "kind", "LandPropertyKind", 0, 1, "enumeration"),
            AttrMeta("demographic_kind", "demographicKind", "DemographicKind", 0, 1, "enumeration"),
            AttrMeta(
                "external_record_reference", "externalRecordReference", "str", 0, 1, "primitive"
            ),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            erp_organisation_roles.meta,
            asset_containers.meta,
            erp_site_level_datas.meta,
            locations.meta,
            location_grants.meta,
            erp_person_roles.meta,
            right_of_ways.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: LandPropertyKind | None = None,
        demographic_kind: DemographicKind | None = None,
        external_record_reference: str | None = None,
        status: Status | None = None,
        erp_organisation_roles: Iterable[PropertyOrganisationRole] | None = None,
        asset_containers: Iterable[AssetContainer] | None = None,
        erp_site_level_datas: Iterable[ErpSiteLevelData] | None = None,
        locations: Iterable[Location] | None = None,
        location_grants: Iterable[LocationGrant] | None = None,
        erp_person_roles: Iterable[PersonPropertyRole] | None = None,
        right_of_ways: Iterable[RightOfWay] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.demographic_kind = demographic_kind
        self.external_record_reference = external_record_reference
        self.status = status
        if erp_organisation_roles is not None:
            LandProperty.erp_organisation_roles.extend(self, erp_organisation_roles)
        if asset_containers is not None:
            LandProperty.asset_containers.extend(self, asset_containers)
        if erp_site_level_datas is not None:
            LandProperty.erp_site_level_datas.extend(self, erp_site_level_datas)
        if locations is not None:
            LandProperty.locations.extend(self, locations)
        if location_grants is not None:
            LandProperty.location_grants.extend(self, location_grants)
        if erp_person_roles is not None:
            LandProperty.erp_person_roles.extend(self, erp_person_roles)
        if right_of_ways is not None:
            LandProperty.right_of_ways.extend(self, right_of_ways)

    def add_erp_organisation_role(self, erp_organisation_role: PropertyOrganisationRole) -> Self:
        return LandProperty.erp_organisation_roles.add(self, erp_organisation_role)

    def remove_erp_organisation_role(self, erp_organisation_role: PropertyOrganisationRole) -> Self:
        return LandProperty.erp_organisation_roles.remove(self, erp_organisation_role)

    def clear_erp_organisation_roles(self) -> Self:
        return LandProperty.erp_organisation_roles.clear(self)

    def num_erp_organisation_role(self) -> int:
        return LandProperty.erp_organisation_roles.count(self)

    def get_erp_organisation_role_by_mrid(self, mrid: str) -> PropertyOrganisationRole | None:
        return LandProperty.erp_organisation_roles.get_by_mrid(self, mrid)

    def add_asset_container(self, asset_container: AssetContainer) -> Self:
        return LandProperty.asset_containers.add(self, asset_container)

    def remove_asset_container(self, asset_container: AssetContainer) -> Self:
        return LandProperty.asset_containers.remove(self, asset_container)

    def clear_asset_containers(self) -> Self:
        return LandProperty.asset_containers.clear(self)

    def num_asset_container(self) -> int:
        return LandProperty.asset_containers.count(self)

    def get_asset_container_by_mrid(self, mrid: str) -> AssetContainer | None:
        return LandProperty.asset_containers.get_by_mrid(self, mrid)

    def add_erp_site_level_data(self, erp_site_level_data: ErpSiteLevelData) -> Self:
        return LandProperty.erp_site_level_datas.add(self, erp_site_level_data)

    def remove_erp_site_level_data(self, erp_site_level_data: ErpSiteLevelData) -> Self:
        return LandProperty.erp_site_level_datas.remove(self, erp_site_level_data)

    def clear_erp_site_level_datas(self) -> Self:
        return LandProperty.erp_site_level_datas.clear(self)

    def num_erp_site_level_data(self) -> int:
        return LandProperty.erp_site_level_datas.count(self)

    def get_erp_site_level_data_by_mrid(self, mrid: str) -> ErpSiteLevelData | None:
        return LandProperty.erp_site_level_datas.get_by_mrid(self, mrid)

    def add_location(self, location: Location) -> Self:
        return LandProperty.locations.add(self, location)

    def remove_location(self, location: Location) -> Self:
        return LandProperty.locations.remove(self, location)

    def clear_locations(self) -> Self:
        return LandProperty.locations.clear(self)

    def num_location(self) -> int:
        return LandProperty.locations.count(self)

    def get_location_by_mrid(self, mrid: str) -> Location | None:
        return LandProperty.locations.get_by_mrid(self, mrid)

    def add_location_grant(self, location_grant: LocationGrant) -> Self:
        return LandProperty.location_grants.add(self, location_grant)

    def remove_location_grant(self, location_grant: LocationGrant) -> Self:
        return LandProperty.location_grants.remove(self, location_grant)

    def clear_location_grants(self) -> Self:
        return LandProperty.location_grants.clear(self)

    def num_location_grant(self) -> int:
        return LandProperty.location_grants.count(self)

    def get_location_grant_by_mrid(self, mrid: str) -> LocationGrant | None:
        return LandProperty.location_grants.get_by_mrid(self, mrid)

    def add_erp_person_role(self, erp_person_role: PersonPropertyRole) -> Self:
        return LandProperty.erp_person_roles.add(self, erp_person_role)

    def remove_erp_person_role(self, erp_person_role: PersonPropertyRole) -> Self:
        return LandProperty.erp_person_roles.remove(self, erp_person_role)

    def clear_erp_person_roles(self) -> Self:
        return LandProperty.erp_person_roles.clear(self)

    def num_erp_person_role(self) -> int:
        return LandProperty.erp_person_roles.count(self)

    def get_erp_person_role_by_mrid(self, mrid: str) -> PersonPropertyRole | None:
        return LandProperty.erp_person_roles.get_by_mrid(self, mrid)

    def add_right_of_way(self, right_of_way: RightOfWay) -> Self:
        return LandProperty.right_of_ways.add(self, right_of_way)

    def remove_right_of_way(self, right_of_way: RightOfWay) -> Self:
        return LandProperty.right_of_ways.remove(self, right_of_way)

    def clear_right_of_ways(self) -> Self:
        return LandProperty.right_of_ways.clear(self)

    def num_right_of_way(self) -> int:
        return LandProperty.right_of_ways.count(self)

    def get_right_of_way_by_mrid(self, mrid: str) -> RightOfWay | None:
        return LandProperty.right_of_ways.get_by_mrid(self, mrid)
