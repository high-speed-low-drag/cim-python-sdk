"""CIM class Trade (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.action_request import (
        ActionRequest,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade_error import (
        TradeError,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade_product import (
        TradeProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator import (
        SchedulingCoordinator,
    )


class Trade(IdentifiedObject):
    """Inter Scheduling Coordinator Trades to model financial trades which may impact
    settlement."""

    __slots__ = (
        "_action_request",
        "_from_sc",
        "_pnode",
        "_registered_generator",
        "_submit_from_scheduling_coordinator",
        "_submit_to_scheduling_coordinator",
        "_to_sc",
        "_trade_error",
        "_trade_product",
        "adjusted_trade_quantity",
        "counter_trade_quantity",
        "depend_on_trade_name",
        "last_modified",
        "market_type",
        "start_time",
        "stop_time",
        "submit_from_time_stamp",
        "submit_from_user",
        "submit_to_time_stamp",
        "submit_to_user",
        "trade_quantity",
        "trade_status",
        "update_time_stamp",
        "update_user",
    )

    adjusted_trade_quantity: float | None
    counter_trade_quantity: float | None
    depend_on_trade_name: str | None
    last_modified: _dt.datetime | None
    market_type: MarketType | None
    start_time: _dt.datetime | None
    stop_time: _dt.datetime | None
    submit_from_time_stamp: _dt.datetime | None
    submit_from_user: str | None
    submit_to_time_stamp: _dt.datetime | None
    submit_to_user: str | None
    trade_quantity: float | None
    trade_status: str | None
    update_time_stamp: _dt.datetime | None
    update_user: str | None

    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="trade",
            aggregation="none",
        )
    )
    action_request: One[ActionRequest] = One(
        EndMeta(
            name="action_request",
            cim_role="ActionRequest",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.action_request:ActionRequest",
            many=False,
            lower=1,
            upper=1,
            inverse="trade",
            aggregation="none",
        )
    )
    submit_from_scheduling_coordinator: One[SchedulingCoordinator] = One(
        EndMeta(
            name="submit_from_scheduling_coordinator",
            cim_role="submitFromSchedulingCoordinator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=False,
            lower=0,
            upper=1,
            inverse="submit_from_sc_trade",
            aggregation="none",
        )
    )
    from_sc: One[SchedulingCoordinator] = One(
        EndMeta(
            name="from_sc",
            cim_role="From_SC",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=False,
            lower=1,
            upper=1,
            inverse="from_sc_trade",
            aggregation="none",
        )
    )
    to_sc: One[SchedulingCoordinator] = One(
        EndMeta(
            name="to_sc",
            cim_role="To_SC",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=False,
            lower=1,
            upper=1,
            inverse="to_sc_trade",
            aggregation="none",
        )
    )
    trade_product: One[TradeProduct] = One(
        EndMeta(
            name="trade_product",
            cim_role="TradeProduct",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade_product:TradeProduct",
            many=False,
            lower=1,
            upper=1,
            inverse="trade",
            aggregation="none",
        )
    )
    submit_to_scheduling_coordinator: One[SchedulingCoordinator] = One(
        EndMeta(
            name="submit_to_scheduling_coordinator",
            cim_role="submitToSchedulingCoordinator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator:SchedulingCoordinator",
            many=False,
            lower=0,
            upper=1,
            inverse="submit_to_sc_trade",
            aggregation="none",
        )
    )
    trade_error: Many[TradeError] = Many(
        EndMeta(
            name="trade_error",
            cim_role="TradeError",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade_error:TradeError",
            many=True,
            lower=0,
            upper=None,
            inverse="trade",
            aggregation="none",
        )
    )
    pnode: One[Pnode] = One(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=0,
            upper=1,
            inverse="trade",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Trade",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{BC568130-E2FD-4938-8D44-2749731BC734}",
        attributes=(
            AttrMeta(
                "adjusted_trade_quantity", "adjustedTradeQuantity", "float", 0, 1, "primitive"
            ),
            AttrMeta("counter_trade_quantity", "counterTradeQuantity", "float", 0, 1, "primitive"),
            AttrMeta("depend_on_trade_name", "dependOnTradeName", "str", 0, 1, "primitive"),
            AttrMeta("last_modified", "lastModified", "datetime", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta("stop_time", "stopTime", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "submit_from_time_stamp", "submitFromTimeStamp", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("submit_from_user", "submitFromUser", "str", 0, 1, "primitive"),
            AttrMeta("submit_to_time_stamp", "submitToTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("submit_to_user", "submitToUser", "str", 0, 1, "primitive"),
            AttrMeta("trade_quantity", "tradeQuantity", "float", 0, 1, "primitive"),
            AttrMeta("trade_status", "tradeStatus", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
        ),
        ends=(
            registered_generator.meta,
            action_request.meta,
            submit_from_scheduling_coordinator.meta,
            from_sc.meta,
            to_sc.meta,
            trade_product.meta,
            submit_to_scheduling_coordinator.meta,
            trade_error.meta,
            pnode.meta,
        ),
    )

    def __init__(
        self,
        *,
        adjusted_trade_quantity: float | None = None,
        counter_trade_quantity: float | None = None,
        depend_on_trade_name: str | None = None,
        last_modified: _dt.datetime | None = None,
        market_type: MarketType | None = None,
        start_time: _dt.datetime | None = None,
        stop_time: _dt.datetime | None = None,
        submit_from_time_stamp: _dt.datetime | None = None,
        submit_from_user: str | None = None,
        submit_to_time_stamp: _dt.datetime | None = None,
        submit_to_user: str | None = None,
        trade_quantity: float | None = None,
        trade_status: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_user: str | None = None,
        registered_generator: RegisteredGenerator | None = None,
        action_request: ActionRequest | None = None,
        submit_from_scheduling_coordinator: SchedulingCoordinator | None = None,
        from_sc: SchedulingCoordinator | None = None,
        to_sc: SchedulingCoordinator | None = None,
        trade_product: TradeProduct | None = None,
        submit_to_scheduling_coordinator: SchedulingCoordinator | None = None,
        trade_error: Iterable[TradeError] | None = None,
        pnode: Pnode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.adjusted_trade_quantity = adjusted_trade_quantity
        self.counter_trade_quantity = counter_trade_quantity
        self.depend_on_trade_name = depend_on_trade_name
        self.last_modified = last_modified
        self.market_type = market_type
        self.start_time = start_time
        self.stop_time = stop_time
        self.submit_from_time_stamp = submit_from_time_stamp
        self.submit_from_user = submit_from_user
        self.submit_to_time_stamp = submit_to_time_stamp
        self.submit_to_user = submit_to_user
        self.trade_quantity = trade_quantity
        self.trade_status = trade_status
        self.update_time_stamp = update_time_stamp
        self.update_user = update_user
        if registered_generator is not None:
            self.registered_generator = registered_generator
        if action_request is not None:
            self.action_request = action_request
        if submit_from_scheduling_coordinator is not None:
            self.submit_from_scheduling_coordinator = submit_from_scheduling_coordinator
        if from_sc is not None:
            self.from_sc = from_sc
        if to_sc is not None:
            self.to_sc = to_sc
        if trade_product is not None:
            self.trade_product = trade_product
        if submit_to_scheduling_coordinator is not None:
            self.submit_to_scheduling_coordinator = submit_to_scheduling_coordinator
        if trade_error is not None:
            Trade.trade_error.extend(self, trade_error)
        if pnode is not None:
            self.pnode = pnode

    def add_trade_error(self, trade_error: TradeError) -> Self:
        return Trade.trade_error.add(self, trade_error)

    def remove_trade_error(self, trade_error: TradeError) -> Self:
        return Trade.trade_error.remove(self, trade_error)

    def clear_trade_error(self) -> Self:
        return Trade.trade_error.clear(self)

    def num_trade_error(self) -> int:
        return Trade.trade_error.count(self)

    def get_trade_error_by_mrid(self, mrid: str) -> TradeError | None:
        return Trade.trade_error.get_by_mrid(self, mrid)
