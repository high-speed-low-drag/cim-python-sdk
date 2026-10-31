"""CIM class SchedulingCoordinatorUser (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator import (
        SchedulingCoordinator,
    )


class SchedulingCoordinatorUser(CimObject):
    """Describing users of a Scheduling Coordinator."""

    __slots__ = ("_scheduling_coordinator", "login_id", "login_role")

    login_id: str | None
    login_role: str | None

    scheduling_coordinator: One[SchedulingCoordinator] = One(
        EndMeta(
            name="scheduling_coordinator",
            cim_role=None,
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=False,
            lower=1,
            upper=1,
            inverse="scheduling_coordinator_users",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SchedulingCoordinatorUser",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{FE8B191F-0122-4f90-968A-81D44B223005}",
        attributes=(
            AttrMeta("login_id", "loginID", "str", 0, 1, "primitive"),
            AttrMeta("login_role", "loginRole", "str", 0, 1, "primitive"),
        ),
        ends=(scheduling_coordinator.meta,),
    )

    def __init__(
        self,
        *,
        login_id: str | None = None,
        login_role: str | None = None,
        scheduling_coordinator: SchedulingCoordinator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.login_id = login_id
        self.login_role = login_role
        if scheduling_coordinator is not None:
            self.scheduling_coordinator = scheduling_coordinator
