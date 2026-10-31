"""CIM class PnodeResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_clearing import (
        PnodeClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode


class PnodeResults(CimObject):
    """Provides the total price, the cost component, the loss component, and the congestion
    component for Pnodes for the forward and real time markets. There are several prices
    produced based on the run type (MPM, RUC, Pricing, or Scheduling/Dispatch)."""

    __slots__ = (
        "_pnode",
        "_pnode_clearing",
        "congest_lmp",
        "cost_lmp",
        "loss_lmp",
        "marginal_clearing_price",
        "scheduled_mw",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    marginal_clearing_price: float | None
    cost_lmp: float | None
    loss_lmp: float | None
    congest_lmp: float | None
    scheduled_mw: float | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None

    pnode: One[Pnode] = One(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=0,
            upper=1,
            inverse="pnode_results",
            aggregation="none",
        )
    )
    pnode_clearing: One[PnodeClearing] = One(
        EndMeta(
            name="pnode_clearing",
            cim_role="PnodeClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pnode_clearing:PnodeClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="pnode_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PnodeResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{73FB5C97-DB9B-4153-89F4-4C602A079906}",
        attributes=(
            AttrMeta(
                "marginal_clearing_price", "marginalClearingPrice", "float", 0, 1, "primitive"
            ),
            AttrMeta("cost_lmp", "costLMP", "float", 0, 1, "primitive"),
            AttrMeta("loss_lmp", "lossLMP", "float", 0, 1, "primitive"),
            AttrMeta("congest_lmp", "congestLMP", "float", 0, 1, "primitive"),
            AttrMeta("scheduled_mw", "scheduledMW", "float", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
        ),
        ends=(
            pnode.meta,
            pnode_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        marginal_clearing_price: float | None = None,
        cost_lmp: float | None = None,
        loss_lmp: float | None = None,
        congest_lmp: float | None = None,
        scheduled_mw: float | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        pnode: Pnode | None = None,
        pnode_clearing: PnodeClearing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.marginal_clearing_price = marginal_clearing_price
        self.cost_lmp = cost_lmp
        self.loss_lmp = loss_lmp
        self.congest_lmp = congest_lmp
        self.scheduled_mw = scheduled_mw
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        if pnode is not None:
            self.pnode = pnode
        if pnode_clearing is not None:
            self.pnode_clearing = pnode_clearing
