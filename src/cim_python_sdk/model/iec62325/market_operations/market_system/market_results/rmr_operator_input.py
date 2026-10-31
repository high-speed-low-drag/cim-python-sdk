"""CIM class RMROperatorInput (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType


class RMROperatorInput(MarketFactors):
    """RMR Operator's entry of the RMR requirement per market interval."""

    __slots__ = (
        "_registered_resource",
        "manually_sched_rmr_mw",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    manually_sched_rmr_mw: float | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="rmr_operator_input",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RMROperatorInput",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{FB23ACBA-4D15-4196-9926-30AFFE7D6701}",
        attributes=(
            AttrMeta("manually_sched_rmr_mw", "manuallySchedRMRMw", "float", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        manually_sched_rmr_mw: float | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.manually_sched_rmr_mw = manually_sched_rmr_mw
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        if registered_resource is not None:
            self.registered_resource = registered_resource
