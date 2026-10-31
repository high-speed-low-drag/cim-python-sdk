"""CIM class Crew (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.crew_member import CrewMember
    from cim_python_sdk.model.iec61968.common.crew_type import CrewType
    from cim_python_sdk.model.iec61968.common.field_dispatch_history import FieldDispatchHistory
    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.operations.outage import Outage
    from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction
    from cim_python_sdk.model.iec61968.work.work_asset import WorkAsset
    from cim_python_sdk.model.iec61968.work.work_task import WorkTask


class Crew(IdentifiedObject):
    """Group of people with specific skills, tools, and vehicles."""

    __slots__ = (
        "_crew_members",
        "_crew_type",
        "_field_dispatch_history",
        "_location",
        "_outage",
        "_switching_action",
        "_work_assets",
        "_work_tasks",
        "status",
    )

    status: Status | None

    field_dispatch_history: Many[FieldDispatchHistory] = Many(
        EndMeta(
            name="field_dispatch_history",
            cim_role="FieldDispatchHistory",
            target="cim_python_sdk.model.iec61968.common.field_dispatch_history:FieldDispatchHistory",
            many=True,
            lower=0,
            upper=None,
            inverse="crew",
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
            inverse="crew",
            aggregation="none",
        )
    )
    crew_type: One[CrewType] = One(
        EndMeta(
            name="crew_type",
            cim_role="CrewType",
            target="cim_python_sdk.model.iec61968.common.crew_type:CrewType",
            many=False,
            lower=0,
            upper=1,
            inverse="crews",
            aggregation="none",
        )
    )
    work_assets: Many[WorkAsset] = Many(
        EndMeta(
            name="work_assets",
            cim_role="WorkAssets",
            target="cim_python_sdk.model.iec61968.work.work_asset:WorkAsset",
            many=True,
            lower=0,
            upper=None,
            inverse="crew",
            aggregation="none",
        )
    )
    crew_members: Many[CrewMember] = Many(
        EndMeta(
            name="crew_members",
            cim_role="CrewMembers",
            target="cim_python_sdk.model.iec61968.common.crew_member:CrewMember",
            many=True,
            lower=0,
            upper=None,
            inverse="crew",
            aggregation="none",
        )
    )
    switching_action: One[SwitchingAction] = One(
        EndMeta(
            name="switching_action",
            cim_role="SwitchingAction",
            target="cim_python_sdk.model.iec61968.operations.switching_action:SwitchingAction",
            many=False,
            lower=1,
            upper=1,
            inverse="crew",
            aggregation="none",
        )
    )
    outage: Many[Outage] = Many(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=True,
            lower=0,
            upper=None,
            inverse="crew",
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
            inverse="crews",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Crew",
        package="TC57CIM/IEC61968/Common",
        guid="{C9FE3505-80D0-4126-85C4-1218FCC4A61D}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            field_dispatch_history.meta,
            location.meta,
            crew_type.meta,
            work_assets.meta,
            crew_members.meta,
            switching_action.meta,
            outage.meta,
            work_tasks.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        field_dispatch_history: Iterable[FieldDispatchHistory] | None = None,
        location: Location | None = None,
        crew_type: CrewType | None = None,
        work_assets: Iterable[WorkAsset] | None = None,
        crew_members: Iterable[CrewMember] | None = None,
        switching_action: SwitchingAction | None = None,
        outage: Iterable[Outage] | None = None,
        work_tasks: Iterable[WorkTask] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if field_dispatch_history is not None:
            Crew.field_dispatch_history.extend(self, field_dispatch_history)
        if location is not None:
            self.location = location
        if crew_type is not None:
            self.crew_type = crew_type
        if work_assets is not None:
            Crew.work_assets.extend(self, work_assets)
        if crew_members is not None:
            Crew.crew_members.extend(self, crew_members)
        if switching_action is not None:
            self.switching_action = switching_action
        if outage is not None:
            Crew.outage.extend(self, outage)
        if work_tasks is not None:
            Crew.work_tasks.extend(self, work_tasks)

    def add_field_dispatch_history(self, field_dispatch_history: FieldDispatchHistory) -> Self:
        return Crew.field_dispatch_history.add(self, field_dispatch_history)

    def remove_field_dispatch_history(self, field_dispatch_history: FieldDispatchHistory) -> Self:
        return Crew.field_dispatch_history.remove(self, field_dispatch_history)

    def clear_field_dispatch_history(self) -> Self:
        return Crew.field_dispatch_history.clear(self)

    def num_field_dispatch_history(self) -> int:
        return Crew.field_dispatch_history.count(self)

    def get_field_dispatch_history_by_mrid(self, mrid: str) -> FieldDispatchHistory | None:
        return Crew.field_dispatch_history.get_by_mrid(self, mrid)

    def add_work_asset(self, work_asset: WorkAsset) -> Self:
        return Crew.work_assets.add(self, work_asset)

    def remove_work_asset(self, work_asset: WorkAsset) -> Self:
        return Crew.work_assets.remove(self, work_asset)

    def clear_work_assets(self) -> Self:
        return Crew.work_assets.clear(self)

    def num_work_asset(self) -> int:
        return Crew.work_assets.count(self)

    def get_work_asset_by_mrid(self, mrid: str) -> WorkAsset | None:
        return Crew.work_assets.get_by_mrid(self, mrid)

    def add_crew_member(self, crew_member: CrewMember) -> Self:
        return Crew.crew_members.add(self, crew_member)

    def remove_crew_member(self, crew_member: CrewMember) -> Self:
        return Crew.crew_members.remove(self, crew_member)

    def clear_crew_members(self) -> Self:
        return Crew.crew_members.clear(self)

    def num_crew_member(self) -> int:
        return Crew.crew_members.count(self)

    def get_crew_member_by_mrid(self, mrid: str) -> CrewMember | None:
        return Crew.crew_members.get_by_mrid(self, mrid)

    def add_outage(self, outage: Outage) -> Self:
        return Crew.outage.add(self, outage)

    def remove_outage(self, outage: Outage) -> Self:
        return Crew.outage.remove(self, outage)

    def clear_outage(self) -> Self:
        return Crew.outage.clear(self)

    def num_outage(self) -> int:
        return Crew.outage.count(self)

    def get_outage_by_mrid(self, mrid: str) -> Outage | None:
        return Crew.outage.get_by_mrid(self, mrid)

    def add_work_task(self, work_task: WorkTask) -> Self:
        return Crew.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: WorkTask) -> Self:
        return Crew.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return Crew.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return Crew.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> WorkTask | None:
        return Crew.work_tasks.get_by_mrid(self, mrid)
