"""CIM class PowerSystemResource (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo
    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.operations.clearance_document import ClearanceDocument
    from cim_python_sdk.model.iec61968.operations.generic_action import GenericAction
    from cim_python_sdk.model.iec61968.operations.operational_tag import OperationalTag
    from cim_python_sdk.model.iec61968.operations.psr_event import PSREvent
    from cim_python_sdk.model.iec61968.operations.verification_action import VerificationAction
    from cim_python_sdk.model.iec61970.base.core.operating_share import OperatingShare
    from cim_python_sdk.model.iec61970.base.core.psr_type import PSRType
    from cim_python_sdk.model.iec61970.base.core.reporting_group import ReportingGroup
    from cim_python_sdk.model.iec61970.base.meas.control import Control
    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement


class PowerSystemResource(IdentifiedObject):
    """A power system resource (PSR) can be an item of equipment such as a switch, an equipment
    container containing many individual items of equipment such as a substation, or an
    organisational entity such as sub-control area. Power system resources can have
    measurements associated."""

    __slots__ = (
        "_asset_datasheet",
        "_assets",
        "_clearances",
        "_configuration_event",
        "_controls",
        "_generic_action",
        "_location",
        "_measurements",
        "_operating_share",
        "_operational_tags",
        "_psr_events",
        "_psr_type",
        "_reporting_group",
        "_verification_action",
    )

    asset_datasheet: One[AssetInfo] = One(
        EndMeta(
            name="asset_datasheet",
            cim_role="AssetDatasheet",
            target="cim_python_sdk.model.iec61968.assets.asset_info:AssetInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="power_system_resources",
            aggregation="none",
        )
    )
    configuration_event: Many[ConfigurationEvent] = Many(
        EndMeta(
            name="configuration_event",
            cim_role="ConfigurationEvent",
            target="cim_python_sdk.model.iec61968.common.configuration_event:ConfigurationEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
            aggregation="none",
        )
    )
    operating_share: Many[OperatingShare] = Many(
        EndMeta(
            name="operating_share",
            cim_role="OperatingShare",
            target="cim_python_sdk.model.iec61970.base.core.operating_share:OperatingShare",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
            aggregation="none",
        )
    )
    verification_action: Many[VerificationAction] = Many(
        EndMeta(
            name="verification_action",
            cim_role="VerificationAction",
            target="cim_python_sdk.model.iec61968.operations.verification_action:VerificationAction",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
            aggregation="none",
        )
    )
    reporting_group: Many[ReportingGroup] = Many(
        EndMeta(
            name="reporting_group",
            cim_role="ReportingGroup",
            target="cim_python_sdk.model.iec61970.base.core.reporting_group:ReportingGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
            aggregation="none",
        )
    )
    clearances: Many[ClearanceDocument] = Many(
        EndMeta(
            name="clearances",
            cim_role="Clearances",
            target="cim_python_sdk.model.iec61968.operations.clearance_document:ClearanceDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="tagged_psrs",
            aggregation="none",
        )
    )
    psr_type: One[PSRType] = One(
        EndMeta(
            name="psr_type",
            cim_role="PSRType",
            target="cim_python_sdk.model.iec61970.base.core.psr_type:PSRType",
            many=False,
            lower=0,
            upper=1,
            inverse="power_system_resources",
            aggregation="none",
        )
    )
    measurements: Many[Measurement] = Many(
        EndMeta(
            name="measurements",
            cim_role="Measurements",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
            aggregation="shared",
        )
    )
    generic_action: Many[GenericAction] = Many(
        EndMeta(
            name="generic_action",
            cim_role="GenericAction",
            target="cim_python_sdk.model.iec61968.operations.generic_action:GenericAction",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
            aggregation="none",
        )
    )
    psr_events: Many[PSREvent] = Many(
        EndMeta(
            name="psr_events",
            cim_role="PSREvents",
            target="cim_python_sdk.model.iec61968.operations.psr_event:PSREvent",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
            aggregation="none",
        )
    )
    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resources",
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
            inverse="power_system_resources",
            aggregation="none",
        )
    )
    controls: Many[Control] = Many(
        EndMeta(
            name="controls",
            cim_role="Controls",
            target="cim_python_sdk.model.iec61970.base.meas.control:Control",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_resource",
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
            inverse="power_system_resource",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerSystemResource",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{0340C084-3759-40cc-AAF2-386101DE842F}",
        ends=(
            asset_datasheet.meta,
            configuration_event.meta,
            operating_share.meta,
            verification_action.meta,
            reporting_group.meta,
            clearances.meta,
            psr_type.meta,
            measurements.meta,
            generic_action.meta,
            psr_events.meta,
            assets.meta,
            location.meta,
            controls.meta,
            operational_tags.meta,
        ),
    )

    def __init__(
        self,
        *,
        asset_datasheet: AssetInfo | None = None,
        configuration_event: Iterable[ConfigurationEvent] | None = None,
        operating_share: Iterable[OperatingShare] | None = None,
        verification_action: Iterable[VerificationAction] | None = None,
        reporting_group: Iterable[ReportingGroup] | None = None,
        clearances: Iterable[ClearanceDocument] | None = None,
        psr_type: PSRType | None = None,
        measurements: Iterable[Measurement] | None = None,
        generic_action: Iterable[GenericAction] | None = None,
        psr_events: Iterable[PSREvent] | None = None,
        assets: Iterable[Asset] | None = None,
        location: Location | None = None,
        controls: Iterable[Control] | None = None,
        operational_tags: Iterable[OperationalTag] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if asset_datasheet is not None:
            self.asset_datasheet = asset_datasheet
        if configuration_event is not None:
            PowerSystemResource.configuration_event.extend(self, configuration_event)
        if operating_share is not None:
            PowerSystemResource.operating_share.extend(self, operating_share)
        if verification_action is not None:
            PowerSystemResource.verification_action.extend(self, verification_action)
        if reporting_group is not None:
            PowerSystemResource.reporting_group.extend(self, reporting_group)
        if clearances is not None:
            PowerSystemResource.clearances.extend(self, clearances)
        if psr_type is not None:
            self.psr_type = psr_type
        if measurements is not None:
            PowerSystemResource.measurements.extend(self, measurements)
        if generic_action is not None:
            PowerSystemResource.generic_action.extend(self, generic_action)
        if psr_events is not None:
            PowerSystemResource.psr_events.extend(self, psr_events)
        if assets is not None:
            PowerSystemResource.assets.extend(self, assets)
        if location is not None:
            self.location = location
        if controls is not None:
            PowerSystemResource.controls.extend(self, controls)
        if operational_tags is not None:
            PowerSystemResource.operational_tags.extend(self, operational_tags)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return PowerSystemResource.configuration_event.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return PowerSystemResource.configuration_event.remove(self, configuration_event)

    def clear_configuration_event(self) -> Self:
        return PowerSystemResource.configuration_event.clear(self)

    def num_configuration_event(self) -> int:
        return PowerSystemResource.configuration_event.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return PowerSystemResource.configuration_event.get_by_mrid(self, mrid)

    def add_operating_share(self, operating_share: OperatingShare) -> Self:
        return PowerSystemResource.operating_share.add(self, operating_share)

    def remove_operating_share(self, operating_share: OperatingShare) -> Self:
        return PowerSystemResource.operating_share.remove(self, operating_share)

    def clear_operating_share(self) -> Self:
        return PowerSystemResource.operating_share.clear(self)

    def num_operating_share(self) -> int:
        return PowerSystemResource.operating_share.count(self)

    def add_verification_action(self, verification_action: VerificationAction) -> Self:
        return PowerSystemResource.verification_action.add(self, verification_action)

    def remove_verification_action(self, verification_action: VerificationAction) -> Self:
        return PowerSystemResource.verification_action.remove(self, verification_action)

    def clear_verification_action(self) -> Self:
        return PowerSystemResource.verification_action.clear(self)

    def num_verification_action(self) -> int:
        return PowerSystemResource.verification_action.count(self)

    def get_verification_action_by_mrid(self, mrid: str) -> VerificationAction | None:
        return PowerSystemResource.verification_action.get_by_mrid(self, mrid)

    def add_reporting_group(self, reporting_group: ReportingGroup) -> Self:
        return PowerSystemResource.reporting_group.add(self, reporting_group)

    def remove_reporting_group(self, reporting_group: ReportingGroup) -> Self:
        return PowerSystemResource.reporting_group.remove(self, reporting_group)

    def clear_reporting_group(self) -> Self:
        return PowerSystemResource.reporting_group.clear(self)

    def num_reporting_group(self) -> int:
        return PowerSystemResource.reporting_group.count(self)

    def get_reporting_group_by_mrid(self, mrid: str) -> ReportingGroup | None:
        return PowerSystemResource.reporting_group.get_by_mrid(self, mrid)

    def add_clearance(self, clearance: ClearanceDocument) -> Self:
        return PowerSystemResource.clearances.add(self, clearance)

    def remove_clearance(self, clearance: ClearanceDocument) -> Self:
        return PowerSystemResource.clearances.remove(self, clearance)

    def clear_clearances(self) -> Self:
        return PowerSystemResource.clearances.clear(self)

    def num_clearance(self) -> int:
        return PowerSystemResource.clearances.count(self)

    def get_clearance_by_mrid(self, mrid: str) -> ClearanceDocument | None:
        return PowerSystemResource.clearances.get_by_mrid(self, mrid)

    def add_measurement(self, measurement: Measurement) -> Self:
        return PowerSystemResource.measurements.add(self, measurement)

    def remove_measurement(self, measurement: Measurement) -> Self:
        return PowerSystemResource.measurements.remove(self, measurement)

    def clear_measurements(self) -> Self:
        return PowerSystemResource.measurements.clear(self)

    def num_measurement(self) -> int:
        return PowerSystemResource.measurements.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Measurement | None:
        return PowerSystemResource.measurements.get_by_mrid(self, mrid)

    def add_generic_action(self, generic_action: GenericAction) -> Self:
        return PowerSystemResource.generic_action.add(self, generic_action)

    def remove_generic_action(self, generic_action: GenericAction) -> Self:
        return PowerSystemResource.generic_action.remove(self, generic_action)

    def clear_generic_action(self) -> Self:
        return PowerSystemResource.generic_action.clear(self)

    def num_generic_action(self) -> int:
        return PowerSystemResource.generic_action.count(self)

    def get_generic_action_by_mrid(self, mrid: str) -> GenericAction | None:
        return PowerSystemResource.generic_action.get_by_mrid(self, mrid)

    def add_psr_event(self, psr_event: PSREvent) -> Self:
        return PowerSystemResource.psr_events.add(self, psr_event)

    def remove_psr_event(self, psr_event: PSREvent) -> Self:
        return PowerSystemResource.psr_events.remove(self, psr_event)

    def clear_psr_events(self) -> Self:
        return PowerSystemResource.psr_events.clear(self)

    def num_psr_event(self) -> int:
        return PowerSystemResource.psr_events.count(self)

    def get_psr_event_by_mrid(self, mrid: str) -> PSREvent | None:
        return PowerSystemResource.psr_events.get_by_mrid(self, mrid)

    def add_asset(self, asset: Asset) -> Self:
        return PowerSystemResource.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return PowerSystemResource.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return PowerSystemResource.assets.clear(self)

    def num_asset(self) -> int:
        return PowerSystemResource.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return PowerSystemResource.assets.get_by_mrid(self, mrid)

    def add_control(self, control: Control) -> Self:
        return PowerSystemResource.controls.add(self, control)

    def remove_control(self, control: Control) -> Self:
        return PowerSystemResource.controls.remove(self, control)

    def clear_controls(self) -> Self:
        return PowerSystemResource.controls.clear(self)

    def num_control(self) -> int:
        return PowerSystemResource.controls.count(self)

    def get_control_by_mrid(self, mrid: str) -> Control | None:
        return PowerSystemResource.controls.get_by_mrid(self, mrid)

    def add_operational_tag(self, operational_tag: OperationalTag) -> Self:
        return PowerSystemResource.operational_tags.add(self, operational_tag)

    def remove_operational_tag(self, operational_tag: OperationalTag) -> Self:
        return PowerSystemResource.operational_tags.remove(self, operational_tag)

    def clear_operational_tags(self) -> Self:
        return PowerSystemResource.operational_tags.clear(self)

    def num_operational_tag(self) -> int:
        return PowerSystemResource.operational_tags.count(self)

    def get_operational_tag_by_mrid(self, mrid: str) -> OperationalTag | None:
        return PowerSystemResource.operational_tags.get_by_mrid(self, mrid)
