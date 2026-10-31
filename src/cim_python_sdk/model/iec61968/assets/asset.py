"""CIM class Asset (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.acceptance_test import AcceptanceTest
    from cim_python_sdk.model.iec61968.assets.analytic import Analytic
    from cim_python_sdk.model.iec61968.assets.analytic_score import AnalyticScore
    from cim_python_sdk.model.iec61968.assets.asset_container import AssetContainer
    from cim_python_sdk.model.iec61968.assets.asset_deployment import AssetDeployment
    from cim_python_sdk.model.iec61968.assets.asset_function import AssetFunction
    from cim_python_sdk.model.iec61968.assets.asset_group import AssetGroup
    from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo
    from cim_python_sdk.model.iec61968.assets.asset_kind import AssetKind
    from cim_python_sdk.model.iec61968.assets.asset_lifecycle_state_kind import (
        AssetLifecycleStateKind,
    )
    from cim_python_sdk.model.iec61968.assets.asset_organisation_role import AssetOrganisationRole
    from cim_python_sdk.model.iec61968.assets.financial_info import FinancialInfo
    from cim_python_sdk.model.iec61968.assets.in_use_date import InUseDate
    from cim_python_sdk.model.iec61968.assets.in_use_state_kind import InUseStateKind
    from cim_python_sdk.model.iec61968.assets.lifecycle_date import LifecycleDate
    from cim_python_sdk.model.iec61968.assets.medium import Medium
    from cim_python_sdk.model.iec61968.assets.procedure import Procedure
    from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet
    from cim_python_sdk.model.iec61968.assets.product_asset_model import ProductAssetModel
    from cim_python_sdk.model.iec61968.assets.retired_reason_kind import RetiredReasonKind
    from cim_python_sdk.model.iec61968.assets.switch_operation_summary import SwitchOperationSummary
    from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord
    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.common.electronic_address import ElectronicAddress
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.common.ownership import Ownership
    from cim_python_sdk.model.iec61968.common.scheduled_event import ScheduledEvent
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.customers.service_location import ServiceLocation
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.asset_property_curve import (
        AssetPropertyCurve,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reconditioning import Reconditioning
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reliability_info import (
        ReliabilityInfo,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_inventory import (
        ErpInventory,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_item_master import (
        ErpItemMaster,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item import (
        ErpRecDelvLineItem,
    )
    from cim_python_sdk.model.iec61968.operations.incident import Incident
    from cim_python_sdk.model.iec61968.operations.operational_tag import OperationalTag
    from cim_python_sdk.model.iec61968.work.work_task import WorkTask
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource
    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement


class Asset(IdentifiedObject):
    """Tangible resource of the utility, including power system equipment, various end devices,
    cabinets, buildings, etc. For electrical network equipment, the role of the asset is
    defined through PowerSystemResource and its subclasses, defined mainly in the Wires
    model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description
    places emphasis on the physical characteristics of the equipment fulfilling that role."""

    __slots__ = (
        "_activity_records",
        "_analytic",
        "_analytic_score",
        "_asset_container",
        "_asset_deployment",
        "_asset_function",
        "_asset_group",
        "_asset_info",
        "_asset_property_curves",
        "_breaker_operation",
        "_configuration_events",
        "_erp_inventory",
        "_erp_item_master",
        "_erp_rec_delivery_items",
        "_financial_info",
        "_incident",
        "_location",
        "_measurements",
        "_medium",
        "_operational_tags",
        "_organisation_roles",
        "_ownerships",
        "_power_system_resources",
        "_procedure_data_set",
        "_procedures",
        "_product_asset_model",
        "_reconditionings",
        "_reliability_infos",
        "_replacement_work_tasks",
        "_scheduled_events",
        "_service_location",
        "_work_tasks",
        "acceptance_test",
        "critical",
        "electronic_address",
        "in_use_date",
        "in_use_state",
        "initial_condition",
        "initial_loss_of_life",
        "kind",
        "lifecycle_date",
        "lifecycle_state",
        "lot_number",
        "position",
        "purchase_price",
        "retired_reason",
        "serial_number",
        "status",
        "type",
        "utc_number",
    )

    kind: AssetKind | None
    type: str | None
    utc_number: str | None
    serial_number: str | None
    lot_number: str | None
    purchase_price: _decimal.Decimal | None  # Money
    critical: bool | None
    position: str | None
    electronic_address: ElectronicAddress | None
    lifecycle_state: AssetLifecycleStateKind | None
    lifecycle_date: LifecycleDate | None
    in_use_state: InUseStateKind | None
    in_use_date: InUseDate | None
    acceptance_test: AcceptanceTest | None
    initial_condition: str | None
    initial_loss_of_life: float | None  # PerCent
    status: Status | None
    retired_reason: RetiredReasonKind | None

    measurements: Many[Measurement] = Many(
        EndMeta(
            name="measurements",
            cim_role="Measurements",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    incident: Many[Incident] = Many(
        EndMeta(
            name="incident",
            cim_role="Incident",
            target="cim_python_sdk.model.iec61968.operations.incident:Incident",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    asset_info: One[AssetInfo] = One(
        EndMeta(
            name="asset_info",
            cim_role="AssetInfo",
            target="cim_python_sdk.model.iec61968.assets.asset_info:AssetInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="assets",
            aggregation="none",
        )
    )
    reconditionings: Many[Reconditioning] = Many(
        EndMeta(
            name="reconditionings",
            cim_role="Reconditionings",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reconditioning:Reconditioning",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="assets",
            aggregation="none",
        )
    )
    financial_info: One[FinancialInfo] = One(
        EndMeta(
            name="financial_info",
            cim_role="FinancialInfo",
            target="cim_python_sdk.model.iec61968.assets.financial_info:FinancialInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="asset",
            aggregation="none",
        )
    )
    product_asset_model: One[ProductAssetModel] = One(
        EndMeta(
            name="product_asset_model",
            cim_role="ProductAssetModel",
            target="cim_python_sdk.model.iec61968.assets.product_asset_model:ProductAssetModel",
            many=False,
            lower=0,
            upper=1,
            inverse="asset",
            aggregation="none",
        )
    )
    reliability_infos: Many[ReliabilityInfo] = Many(
        EndMeta(
            name="reliability_infos",
            cim_role="ReliabilityInfos",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reliability_info:ReliabilityInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    procedures: Many[Procedure] = Many(
        EndMeta(
            name="procedures",
            cim_role="Procedures",
            target="cim_python_sdk.model.iec61968.assets.procedure:Procedure",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    asset_deployment: One[AssetDeployment] = One(
        EndMeta(
            name="asset_deployment",
            cim_role="AssetDeployment",
            target="cim_python_sdk.model.iec61968.assets.asset_deployment:AssetDeployment",
            many=False,
            lower=0,
            upper=1,
            inverse="asset",
            aggregation="none",
        )
    )
    analytic_score: Many[AnalyticScore] = Many(
        EndMeta(
            name="analytic_score",
            cim_role="AnalyticScore",
            target="cim_python_sdk.model.iec61968.assets.analytic_score:AnalyticScore",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    service_location: One[ServiceLocation] = One(
        EndMeta(
            name="service_location",
            cim_role="ServiceLocation",
            target="cim_python_sdk.model.iec61968.customers.service_location:ServiceLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_service_location",
            aggregation="none",
        )
    )
    analytic: Many[Analytic] = Many(
        EndMeta(
            name="analytic",
            cim_role="Analytic",
            target="cim_python_sdk.model.iec61968.assets.analytic:Analytic",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    erp_rec_delivery_items: Many[ErpRecDelvLineItem] = Many(
        EndMeta(
            name="erp_rec_delivery_items",
            cim_role="ErpRecDeliveryItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_delv_line_item:ErpRecDelvLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    operational_tags: Many[OperationalTag] = Many(
        EndMeta(
            name="operational_tags",
            cim_role="OperationalTags",
            target="cim_python_sdk.model.iec61968.operations.operational_tag:OperationalTag",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    configuration_events: Many[ConfigurationEvent] = Many(
        EndMeta(
            name="configuration_events",
            cim_role="ConfigurationEvents",
            target="cim_python_sdk.model.iec61968.common.configuration_event:ConfigurationEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="changed_asset",
            aggregation="none",
        )
    )
    ownerships: Many[Ownership] = Many(
        EndMeta(
            name="ownerships",
            cim_role="Ownerships",
            target="cim_python_sdk.model.iec61968.common.ownership:Ownership",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    asset_property_curves: Many[AssetPropertyCurve] = Many(
        EndMeta(
            name="asset_property_curves",
            cim_role="AssetPropertyCurves",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.asset_property_curve:AssetPropertyCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    work_tasks: Many[WorkTask] = Many(
        EndMeta(
            name="work_tasks",
            cim_role="WorkTasks",
            target="cim_python_sdk.model.iec61968.work.work_task:WorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    asset_container: One[AssetContainer] = One(
        EndMeta(
            name="asset_container",
            cim_role="AssetContainer",
            target="cim_python_sdk.model.iec61968.assets.asset_container:AssetContainer",
            many=False,
            lower=0,
            upper=1,
            inverse="assets",
            aggregation="none",
        )
    )
    erp_item_master: One[ErpItemMaster] = One(
        EndMeta(
            name="erp_item_master",
            cim_role="ErpItemMaster",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_item_master:ErpItemMaster",
            many=False,
            lower=0,
            upper=1,
            inverse="asset",
            aggregation="none",
        )
    )
    power_system_resources: Many[PowerSystemResource] = Many(
        EndMeta(
            name="power_system_resources",
            cim_role="PowerSystemResources",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    asset_function: Many[AssetFunction] = Many(
        EndMeta(
            name="asset_function",
            cim_role="AssetFunction",
            target="cim_python_sdk.model.iec61968.assets.asset_function:AssetFunction",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    medium: Many[Medium] = Many(
        EndMeta(
            name="medium",
            cim_role="Medium",
            target="cim_python_sdk.model.iec61968.assets.medium:Medium",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    activity_records: Many[ActivityRecord] = Many(
        EndMeta(
            name="activity_records",
            cim_role="ActivityRecords",
            target="cim_python_sdk.model.iec61968.common.activity_record:ActivityRecord",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    breaker_operation: One[SwitchOperationSummary] = One(
        EndMeta(
            name="breaker_operation",
            cim_role="BreakerOperation",
            target="cim_python_sdk.model.iec61968.assets.switch_operation_summary:SwitchOperationSummary",
            many=False,
            lower=0,
            upper=1,
            inverse="breaker",
            aggregation="none",
        )
    )
    organisation_roles: Many[AssetOrganisationRole] = Many(
        EndMeta(
            name="organisation_roles",
            cim_role="OrganisationRoles",
            target="cim_python_sdk.model.iec61968.assets.asset_organisation_role:AssetOrganisationRole",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    asset_group: Many[AssetGroup] = Many(
        EndMeta(
            name="asset_group",
            cim_role="AssetGroup",
            target="cim_python_sdk.model.iec61968.assets.asset_group:AssetGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )
    replacement_work_tasks: Many[WorkTask] = Many(
        EndMeta(
            name="replacement_work_tasks",
            cim_role="ReplacementWorkTasks",
            target="cim_python_sdk.model.iec61968.work.work_task:WorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="old_asset",
            aggregation="none",
        )
    )
    scheduled_events: Many[ScheduledEvent] = Many(
        EndMeta(
            name="scheduled_events",
            cim_role="ScheduledEvents",
            target="cim_python_sdk.model.iec61968.common.scheduled_event:ScheduledEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="assets",
            aggregation="none",
        )
    )
    erp_inventory: One[ErpInventory] = One(
        EndMeta(
            name="erp_inventory",
            cim_role="ErpInventory",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_inventory:ErpInventory",
            many=False,
            lower=0,
            upper=1,
            inverse="asset",
            aggregation="none",
        )
    )
    procedure_data_set: Many[ProcedureDataSet] = Many(
        EndMeta(
            name="procedure_data_set",
            cim_role="ProcedureDataSet",
            target="cim_python_sdk.model.iec61968.assets.procedure_data_set:ProcedureDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="asset",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Asset",
        package="TC57CIM/IEC61968/Assets",
        guid="{4F4AE641-1576-4f64-BE09-A19143D580F7}",
        attributes=(
            AttrMeta("kind", "kind", "AssetKind", 0, 1, "enumeration"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("utc_number", "utcNumber", "str", 0, 1, "primitive"),
            AttrMeta("serial_number", "serialNumber", "str", 0, 1, "primitive"),
            AttrMeta("lot_number", "lotNumber", "str", 0, 1, "primitive"),
            AttrMeta("purchase_price", "purchasePrice", "Money", 0, 1, "cimdatatype"),
            AttrMeta("critical", "critical", "bool", 0, 1, "primitive"),
            AttrMeta("position", "position", "str", 0, 1, "primitive"),
            AttrMeta(
                "electronic_address", "electronicAddress", "ElectronicAddress", 0, 1, "compound"
            ),
            AttrMeta(
                "lifecycle_state", "lifecycleState", "AssetLifecycleStateKind", 0, 1, "enumeration"
            ),
            AttrMeta("lifecycle_date", "lifecycleDate", "LifecycleDate", 0, 1, "compound"),
            AttrMeta("in_use_state", "inUseState", "InUseStateKind", 0, 1, "enumeration"),
            AttrMeta("in_use_date", "inUseDate", "InUseDate", 0, 1, "compound"),
            AttrMeta("acceptance_test", "acceptanceTest", "AcceptanceTest", 0, 1, "compound"),
            AttrMeta("initial_condition", "initialCondition", "str", 0, 1, "primitive"),
            AttrMeta("initial_loss_of_life", "initialLossOfLife", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
            AttrMeta("retired_reason", "retiredReason", "RetiredReasonKind", 0, 1, "enumeration"),
        ),
        ends=(
            measurements.meta,
            incident.meta,
            asset_info.meta,
            reconditionings.meta,
            location.meta,
            financial_info.meta,
            product_asset_model.meta,
            reliability_infos.meta,
            procedures.meta,
            asset_deployment.meta,
            analytic_score.meta,
            service_location.meta,
            analytic.meta,
            erp_rec_delivery_items.meta,
            operational_tags.meta,
            configuration_events.meta,
            ownerships.meta,
            asset_property_curves.meta,
            work_tasks.meta,
            asset_container.meta,
            erp_item_master.meta,
            power_system_resources.meta,
            asset_function.meta,
            medium.meta,
            activity_records.meta,
            breaker_operation.meta,
            organisation_roles.meta,
            asset_group.meta,
            replacement_work_tasks.meta,
            scheduled_events.meta,
            erp_inventory.meta,
            procedure_data_set.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: AssetKind | None = None,
        type: str | None = None,
        utc_number: str | None = None,
        serial_number: str | None = None,
        lot_number: str | None = None,
        purchase_price: _decimal.Decimal | None = None,
        critical: bool | None = None,
        position: str | None = None,
        electronic_address: ElectronicAddress | None = None,
        lifecycle_state: AssetLifecycleStateKind | None = None,
        lifecycle_date: LifecycleDate | None = None,
        in_use_state: InUseStateKind | None = None,
        in_use_date: InUseDate | None = None,
        acceptance_test: AcceptanceTest | None = None,
        initial_condition: str | None = None,
        initial_loss_of_life: float | None = None,
        status: Status | None = None,
        retired_reason: RetiredReasonKind | None = None,
        measurements: Iterable[Measurement] | None = None,
        incident: Iterable[Incident] | None = None,
        asset_info: AssetInfo | None = None,
        reconditionings: Iterable[Reconditioning] | None = None,
        location: Location | None = None,
        financial_info: FinancialInfo | None = None,
        product_asset_model: ProductAssetModel | None = None,
        reliability_infos: Iterable[ReliabilityInfo] | None = None,
        procedures: Iterable[Procedure] | None = None,
        asset_deployment: AssetDeployment | None = None,
        analytic_score: Iterable[AnalyticScore] | None = None,
        service_location: ServiceLocation | None = None,
        analytic: Iterable[Analytic] | None = None,
        erp_rec_delivery_items: Iterable[ErpRecDelvLineItem] | None = None,
        operational_tags: Iterable[OperationalTag] | None = None,
        configuration_events: Iterable[ConfigurationEvent] | None = None,
        ownerships: Iterable[Ownership] | None = None,
        asset_property_curves: Iterable[AssetPropertyCurve] | None = None,
        work_tasks: Iterable[WorkTask] | None = None,
        asset_container: AssetContainer | None = None,
        erp_item_master: ErpItemMaster | None = None,
        power_system_resources: Iterable[PowerSystemResource] | None = None,
        asset_function: Iterable[AssetFunction] | None = None,
        medium: Iterable[Medium] | None = None,
        activity_records: Iterable[ActivityRecord] | None = None,
        breaker_operation: SwitchOperationSummary | None = None,
        organisation_roles: Iterable[AssetOrganisationRole] | None = None,
        asset_group: Iterable[AssetGroup] | None = None,
        replacement_work_tasks: Iterable[WorkTask] | None = None,
        scheduled_events: Iterable[ScheduledEvent] | None = None,
        erp_inventory: ErpInventory | None = None,
        procedure_data_set: Iterable[ProcedureDataSet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.type = type
        self.utc_number = utc_number
        self.serial_number = serial_number
        self.lot_number = lot_number
        self.purchase_price = purchase_price
        self.critical = critical
        self.position = position
        self.electronic_address = electronic_address
        self.lifecycle_state = lifecycle_state
        self.lifecycle_date = lifecycle_date
        self.in_use_state = in_use_state
        self.in_use_date = in_use_date
        self.acceptance_test = acceptance_test
        self.initial_condition = initial_condition
        self.initial_loss_of_life = initial_loss_of_life
        self.status = status
        self.retired_reason = retired_reason
        if measurements is not None:
            Asset.measurements.extend(self, measurements)
        if incident is not None:
            Asset.incident.extend(self, incident)
        if asset_info is not None:
            self.asset_info = asset_info
        if reconditionings is not None:
            Asset.reconditionings.extend(self, reconditionings)
        if location is not None:
            self.location = location
        if financial_info is not None:
            self.financial_info = financial_info
        if product_asset_model is not None:
            self.product_asset_model = product_asset_model
        if reliability_infos is not None:
            Asset.reliability_infos.extend(self, reliability_infos)
        if procedures is not None:
            Asset.procedures.extend(self, procedures)
        if asset_deployment is not None:
            self.asset_deployment = asset_deployment
        if analytic_score is not None:
            Asset.analytic_score.extend(self, analytic_score)
        if service_location is not None:
            self.service_location = service_location
        if analytic is not None:
            Asset.analytic.extend(self, analytic)
        if erp_rec_delivery_items is not None:
            Asset.erp_rec_delivery_items.extend(self, erp_rec_delivery_items)
        if operational_tags is not None:
            Asset.operational_tags.extend(self, operational_tags)
        if configuration_events is not None:
            Asset.configuration_events.extend(self, configuration_events)
        if ownerships is not None:
            Asset.ownerships.extend(self, ownerships)
        if asset_property_curves is not None:
            Asset.asset_property_curves.extend(self, asset_property_curves)
        if work_tasks is not None:
            Asset.work_tasks.extend(self, work_tasks)
        if asset_container is not None:
            self.asset_container = asset_container
        if erp_item_master is not None:
            self.erp_item_master = erp_item_master
        if power_system_resources is not None:
            Asset.power_system_resources.extend(self, power_system_resources)
        if asset_function is not None:
            Asset.asset_function.extend(self, asset_function)
        if medium is not None:
            Asset.medium.extend(self, medium)
        if activity_records is not None:
            Asset.activity_records.extend(self, activity_records)
        if breaker_operation is not None:
            self.breaker_operation = breaker_operation
        if organisation_roles is not None:
            Asset.organisation_roles.extend(self, organisation_roles)
        if asset_group is not None:
            Asset.asset_group.extend(self, asset_group)
        if replacement_work_tasks is not None:
            Asset.replacement_work_tasks.extend(self, replacement_work_tasks)
        if scheduled_events is not None:
            Asset.scheduled_events.extend(self, scheduled_events)
        if erp_inventory is not None:
            self.erp_inventory = erp_inventory
        if procedure_data_set is not None:
            Asset.procedure_data_set.extend(self, procedure_data_set)

    def add_measurement(self, measurement: Measurement) -> Self:
        return Asset.measurements.add(self, measurement)

    def remove_measurement(self, measurement: Measurement) -> Self:
        return Asset.measurements.remove(self, measurement)

    def clear_measurements(self) -> Self:
        return Asset.measurements.clear(self)

    def num_measurement(self) -> int:
        return Asset.measurements.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Measurement | None:
        return Asset.measurements.get_by_mrid(self, mrid)

    def add_incident(self, incident: Incident) -> Self:
        return Asset.incident.add(self, incident)

    def remove_incident(self, incident: Incident) -> Self:
        return Asset.incident.remove(self, incident)

    def clear_incident(self) -> Self:
        return Asset.incident.clear(self)

    def num_incident(self) -> int:
        return Asset.incident.count(self)

    def get_incident_by_mrid(self, mrid: str) -> Incident | None:
        return Asset.incident.get_by_mrid(self, mrid)

    def add_reconditioning(self, reconditioning: Reconditioning) -> Self:
        return Asset.reconditionings.add(self, reconditioning)

    def remove_reconditioning(self, reconditioning: Reconditioning) -> Self:
        return Asset.reconditionings.remove(self, reconditioning)

    def clear_reconditionings(self) -> Self:
        return Asset.reconditionings.clear(self)

    def num_reconditioning(self) -> int:
        return Asset.reconditionings.count(self)

    def get_reconditioning_by_mrid(self, mrid: str) -> Reconditioning | None:
        return Asset.reconditionings.get_by_mrid(self, mrid)

    def add_reliability_info(self, reliability_info: ReliabilityInfo) -> Self:
        return Asset.reliability_infos.add(self, reliability_info)

    def remove_reliability_info(self, reliability_info: ReliabilityInfo) -> Self:
        return Asset.reliability_infos.remove(self, reliability_info)

    def clear_reliability_infos(self) -> Self:
        return Asset.reliability_infos.clear(self)

    def num_reliability_info(self) -> int:
        return Asset.reliability_infos.count(self)

    def get_reliability_info_by_mrid(self, mrid: str) -> ReliabilityInfo | None:
        return Asset.reliability_infos.get_by_mrid(self, mrid)

    def add_procedure(self, procedure: Procedure) -> Self:
        return Asset.procedures.add(self, procedure)

    def remove_procedure(self, procedure: Procedure) -> Self:
        return Asset.procedures.remove(self, procedure)

    def clear_procedures(self) -> Self:
        return Asset.procedures.clear(self)

    def num_procedure(self) -> int:
        return Asset.procedures.count(self)

    def get_procedure_by_mrid(self, mrid: str) -> Procedure | None:
        return Asset.procedures.get_by_mrid(self, mrid)

    def add_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return Asset.analytic_score.add(self, analytic_score)

    def remove_analytic_score(self, analytic_score: AnalyticScore) -> Self:
        return Asset.analytic_score.remove(self, analytic_score)

    def clear_analytic_score(self) -> Self:
        return Asset.analytic_score.clear(self)

    def num_analytic_score(self) -> int:
        return Asset.analytic_score.count(self)

    def get_analytic_score_by_mrid(self, mrid: str) -> AnalyticScore | None:
        return Asset.analytic_score.get_by_mrid(self, mrid)

    def add_analytic(self, analytic: Analytic) -> Self:
        return Asset.analytic.add(self, analytic)

    def remove_analytic(self, analytic: Analytic) -> Self:
        return Asset.analytic.remove(self, analytic)

    def clear_analytic(self) -> Self:
        return Asset.analytic.clear(self)

    def num_analytic(self) -> int:
        return Asset.analytic.count(self)

    def get_analytic_by_mrid(self, mrid: str) -> Analytic | None:
        return Asset.analytic.get_by_mrid(self, mrid)

    def add_erp_rec_delivery_item(self, erp_rec_delivery_item: ErpRecDelvLineItem) -> Self:
        return Asset.erp_rec_delivery_items.add(self, erp_rec_delivery_item)

    def remove_erp_rec_delivery_item(self, erp_rec_delivery_item: ErpRecDelvLineItem) -> Self:
        return Asset.erp_rec_delivery_items.remove(self, erp_rec_delivery_item)

    def clear_erp_rec_delivery_items(self) -> Self:
        return Asset.erp_rec_delivery_items.clear(self)

    def num_erp_rec_delivery_item(self) -> int:
        return Asset.erp_rec_delivery_items.count(self)

    def get_erp_rec_delivery_item_by_mrid(self, mrid: str) -> ErpRecDelvLineItem | None:
        return Asset.erp_rec_delivery_items.get_by_mrid(self, mrid)

    def add_operational_tag(self, operational_tag: OperationalTag) -> Self:
        return Asset.operational_tags.add(self, operational_tag)

    def remove_operational_tag(self, operational_tag: OperationalTag) -> Self:
        return Asset.operational_tags.remove(self, operational_tag)

    def clear_operational_tags(self) -> Self:
        return Asset.operational_tags.clear(self)

    def num_operational_tag(self) -> int:
        return Asset.operational_tags.count(self)

    def get_operational_tag_by_mrid(self, mrid: str) -> OperationalTag | None:
        return Asset.operational_tags.get_by_mrid(self, mrid)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return Asset.configuration_events.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return Asset.configuration_events.remove(self, configuration_event)

    def clear_configuration_events(self) -> Self:
        return Asset.configuration_events.clear(self)

    def num_configuration_event(self) -> int:
        return Asset.configuration_events.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return Asset.configuration_events.get_by_mrid(self, mrid)

    def add_ownership(self, ownership: Ownership) -> Self:
        return Asset.ownerships.add(self, ownership)

    def remove_ownership(self, ownership: Ownership) -> Self:
        return Asset.ownerships.remove(self, ownership)

    def clear_ownerships(self) -> Self:
        return Asset.ownerships.clear(self)

    def num_ownership(self) -> int:
        return Asset.ownerships.count(self)

    def get_ownership_by_mrid(self, mrid: str) -> Ownership | None:
        return Asset.ownerships.get_by_mrid(self, mrid)

    def add_asset_property_curve(self, asset_property_curve: AssetPropertyCurve) -> Self:
        return Asset.asset_property_curves.add(self, asset_property_curve)

    def remove_asset_property_curve(self, asset_property_curve: AssetPropertyCurve) -> Self:
        return Asset.asset_property_curves.remove(self, asset_property_curve)

    def clear_asset_property_curves(self) -> Self:
        return Asset.asset_property_curves.clear(self)

    def num_asset_property_curve(self) -> int:
        return Asset.asset_property_curves.count(self)

    def get_asset_property_curve_by_mrid(self, mrid: str) -> AssetPropertyCurve | None:
        return Asset.asset_property_curves.get_by_mrid(self, mrid)

    def add_work_task(self, work_task: WorkTask) -> Self:
        return Asset.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: WorkTask) -> Self:
        return Asset.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return Asset.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return Asset.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> WorkTask | None:
        return Asset.work_tasks.get_by_mrid(self, mrid)

    def add_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return Asset.power_system_resources.add(self, power_system_resource)

    def remove_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return Asset.power_system_resources.remove(self, power_system_resource)

    def clear_power_system_resources(self) -> Self:
        return Asset.power_system_resources.clear(self)

    def num_power_system_resource(self) -> int:
        return Asset.power_system_resources.count(self)

    def get_power_system_resource_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return Asset.power_system_resources.get_by_mrid(self, mrid)

    def add_asset_function(self, asset_function: AssetFunction) -> Self:
        return Asset.asset_function.add(self, asset_function)

    def remove_asset_function(self, asset_function: AssetFunction) -> Self:
        return Asset.asset_function.remove(self, asset_function)

    def clear_asset_function(self) -> Self:
        return Asset.asset_function.clear(self)

    def num_asset_function(self) -> int:
        return Asset.asset_function.count(self)

    def get_asset_function_by_mrid(self, mrid: str) -> AssetFunction | None:
        return Asset.asset_function.get_by_mrid(self, mrid)

    def add_medium(self, medium: Medium) -> Self:
        return Asset.medium.add(self, medium)

    def remove_medium(self, medium: Medium) -> Self:
        return Asset.medium.remove(self, medium)

    def clear_medium(self) -> Self:
        return Asset.medium.clear(self)

    def num_medium(self) -> int:
        return Asset.medium.count(self)

    def get_medium_by_mrid(self, mrid: str) -> Medium | None:
        return Asset.medium.get_by_mrid(self, mrid)

    def add_activity_record(self, activity_record: ActivityRecord) -> Self:
        return Asset.activity_records.add(self, activity_record)

    def remove_activity_record(self, activity_record: ActivityRecord) -> Self:
        return Asset.activity_records.remove(self, activity_record)

    def clear_activity_records(self) -> Self:
        return Asset.activity_records.clear(self)

    def num_activity_record(self) -> int:
        return Asset.activity_records.count(self)

    def get_activity_record_by_mrid(self, mrid: str) -> ActivityRecord | None:
        return Asset.activity_records.get_by_mrid(self, mrid)

    def add_organisation_role(self, organisation_role: AssetOrganisationRole) -> Self:
        return Asset.organisation_roles.add(self, organisation_role)

    def remove_organisation_role(self, organisation_role: AssetOrganisationRole) -> Self:
        return Asset.organisation_roles.remove(self, organisation_role)

    def clear_organisation_roles(self) -> Self:
        return Asset.organisation_roles.clear(self)

    def num_organisation_role(self) -> int:
        return Asset.organisation_roles.count(self)

    def get_organisation_role_by_mrid(self, mrid: str) -> AssetOrganisationRole | None:
        return Asset.organisation_roles.get_by_mrid(self, mrid)

    def add_asset_group(self, asset_group: AssetGroup) -> Self:
        return Asset.asset_group.add(self, asset_group)

    def remove_asset_group(self, asset_group: AssetGroup) -> Self:
        return Asset.asset_group.remove(self, asset_group)

    def clear_asset_group(self) -> Self:
        return Asset.asset_group.clear(self)

    def num_asset_group(self) -> int:
        return Asset.asset_group.count(self)

    def get_asset_group_by_mrid(self, mrid: str) -> AssetGroup | None:
        return Asset.asset_group.get_by_mrid(self, mrid)

    def add_replacement_work_task(self, replacement_work_task: WorkTask) -> Self:
        return Asset.replacement_work_tasks.add(self, replacement_work_task)

    def remove_replacement_work_task(self, replacement_work_task: WorkTask) -> Self:
        return Asset.replacement_work_tasks.remove(self, replacement_work_task)

    def clear_replacement_work_tasks(self) -> Self:
        return Asset.replacement_work_tasks.clear(self)

    def num_replacement_work_task(self) -> int:
        return Asset.replacement_work_tasks.count(self)

    def get_replacement_work_task_by_mrid(self, mrid: str) -> WorkTask | None:
        return Asset.replacement_work_tasks.get_by_mrid(self, mrid)

    def add_scheduled_event(self, scheduled_event: ScheduledEvent) -> Self:
        return Asset.scheduled_events.add(self, scheduled_event)

    def remove_scheduled_event(self, scheduled_event: ScheduledEvent) -> Self:
        return Asset.scheduled_events.remove(self, scheduled_event)

    def clear_scheduled_events(self) -> Self:
        return Asset.scheduled_events.clear(self)

    def num_scheduled_event(self) -> int:
        return Asset.scheduled_events.count(self)

    def get_scheduled_event_by_mrid(self, mrid: str) -> ScheduledEvent | None:
        return Asset.scheduled_events.get_by_mrid(self, mrid)

    def add_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return Asset.procedure_data_set.add(self, procedure_data_set)

    def remove_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return Asset.procedure_data_set.remove(self, procedure_data_set)

    def clear_procedure_data_set(self) -> Self:
        return Asset.procedure_data_set.clear(self)

    def num_procedure_data_set(self) -> int:
        return Asset.procedure_data_set.count(self)

    def get_procedure_data_set_by_mrid(self, mrid: str) -> ProcedureDataSet | None:
        return Asset.procedure_data_set.get_by_mrid(self, mrid)
