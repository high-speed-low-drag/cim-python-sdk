"""CIM class ConfigurationEvent (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.common.document import Document
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole
    from cim_python_sdk.model.iec61968.common.person_role import PersonRole
    from cim_python_sdk.model.iec61968.customers.service_category import ServiceCategory
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource
    from cim_python_sdk.model.iec61970.base.faults.fault_cause_type import FaultCauseType


class ConfigurationEvent(ActivityRecord):
    """Used to report details on creation, change or deletion of an entity or its
    configuration."""

    __slots__ = (
        "_changed_asset",
        "_changed_document",
        "_changed_location",
        "_changed_organisation_role",
        "_changed_person_role",
        "_changed_service_category",
        "_changed_usage_point",
        "_fault_cause_type",
        "_power_system_resource",
        "effective_date_time",
        "modified_by",
        "remark",
    )

    effective_date_time: _dt.datetime | None
    modified_by: str | None
    remark: str | None

    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_event",
            aggregation="none",
        )
    )
    changed_service_category: One[ServiceCategory] = One(
        EndMeta(
            name="changed_service_category",
            cim_role="ChangedServiceCategory",
            target="cim_python_sdk.model.iec61968.customers.service_category:ServiceCategory",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_events",
            aggregation="none",
        )
    )
    changed_person_role: One[PersonRole] = One(
        EndMeta(
            name="changed_person_role",
            cim_role="ChangedPersonRole",
            target="cim_python_sdk.model.iec61968.common.person_role:PersonRole",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_events",
            aggregation="none",
        )
    )
    changed_location: One[Location] = One(
        EndMeta(
            name="changed_location",
            cim_role="ChangedLocation",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_events",
            aggregation="none",
        )
    )
    changed_asset: One[Asset] = One(
        EndMeta(
            name="changed_asset",
            cim_role="ChangedAsset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_events",
            aggregation="none",
        )
    )
    changed_organisation_role: One[OrganisationRole] = One(
        EndMeta(
            name="changed_organisation_role",
            cim_role="ChangedOrganisationRole",
            target="cim_python_sdk.model.iec61968.common.organisation_role:OrganisationRole",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_events",
            aggregation="none",
        )
    )
    fault_cause_type: One[FaultCauseType] = One(
        EndMeta(
            name="fault_cause_type",
            cim_role="FaultCauseType",
            target="cim_python_sdk.model.iec61970.base.faults.fault_cause_type:FaultCauseType",
            many=False,
            lower=1,
            upper=1,
            inverse="configuration_event",
            aggregation="none",
        )
    )
    changed_usage_point: One[UsagePoint] = One(
        EndMeta(
            name="changed_usage_point",
            cim_role="ChangedUsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_events",
            aggregation="none",
        )
    )
    changed_document: One[Document] = One(
        EndMeta(
            name="changed_document",
            cim_role="ChangedDocument",
            target="cim_python_sdk.model.iec61968.common.document:Document",
            many=False,
            lower=0,
            upper=1,
            inverse="configuration_events",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConfigurationEvent",
        package="TC57CIM/IEC61968/Common",
        guid="{6CAAAEB2-8624-419d-A80B-3E553C3CE444}",
        attributes=(
            AttrMeta("effective_date_time", "effectiveDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("modified_by", "modifiedBy", "str", 0, 1, "primitive"),
            AttrMeta("remark", "remark", "str", 0, 1, "primitive"),
        ),
        ends=(
            power_system_resource.meta,
            changed_service_category.meta,
            changed_person_role.meta,
            changed_location.meta,
            changed_asset.meta,
            changed_organisation_role.meta,
            fault_cause_type.meta,
            changed_usage_point.meta,
            changed_document.meta,
        ),
    )

    def __init__(
        self,
        *,
        effective_date_time: _dt.datetime | None = None,
        modified_by: str | None = None,
        remark: str | None = None,
        power_system_resource: PowerSystemResource | None = None,
        changed_service_category: ServiceCategory | None = None,
        changed_person_role: PersonRole | None = None,
        changed_location: Location | None = None,
        changed_asset: Asset | None = None,
        changed_organisation_role: OrganisationRole | None = None,
        fault_cause_type: FaultCauseType | None = None,
        changed_usage_point: UsagePoint | None = None,
        changed_document: Document | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.effective_date_time = effective_date_time
        self.modified_by = modified_by
        self.remark = remark
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
        if changed_service_category is not None:
            self.changed_service_category = changed_service_category
        if changed_person_role is not None:
            self.changed_person_role = changed_person_role
        if changed_location is not None:
            self.changed_location = changed_location
        if changed_asset is not None:
            self.changed_asset = changed_asset
        if changed_organisation_role is not None:
            self.changed_organisation_role = changed_organisation_role
        if fault_cause_type is not None:
            self.fault_cause_type = fault_cause_type
        if changed_usage_point is not None:
            self.changed_usage_point = changed_usage_point
        if changed_document is not None:
            self.changed_document = changed_document
