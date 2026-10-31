"""CIM class TradeError (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade import Trade


class TradeError(IdentifiedObject):
    """Trade error and warning messages associated with the rule engine processing of the
    submitted trade."""

    __slots__ = (
        "_trade",
        "end_time",
        "err_message",
        "err_priority",
        "log_time_stamp",
        "rule_id",
        "start_time",
    )

    err_priority: int | None
    err_message: str | None
    rule_id: int | None
    start_time: _dt.datetime | None
    end_time: _dt.datetime | None
    log_time_stamp: _dt.datetime | None

    trade: One[Trade] = One(
        EndMeta(
            name="trade",
            cim_role="Trade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=False,
            lower=0,
            upper=1,
            inverse="trade_error",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TradeError",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{D8246ADF-5D06-4955-B17A-F04446F07420}",
        attributes=(
            AttrMeta("err_priority", "errPriority", "int", 0, 1, "primitive"),
            AttrMeta("err_message", "errMessage", "str", 0, 1, "primitive"),
            AttrMeta("rule_id", "ruleID", "int", 0, 1, "primitive"),
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta("end_time", "endTime", "datetime", 0, 1, "primitive"),
            AttrMeta("log_time_stamp", "logTimeStamp", "datetime", 0, 1, "primitive"),
        ),
        ends=(trade.meta,),
    )

    def __init__(
        self,
        *,
        err_priority: int | None = None,
        err_message: str | None = None,
        rule_id: int | None = None,
        start_time: _dt.datetime | None = None,
        end_time: _dt.datetime | None = None,
        log_time_stamp: _dt.datetime | None = None,
        trade: Trade | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.err_priority = err_priority
        self.err_message = err_message
        self.rule_id = rule_id
        self.start_time = start_time
        self.end_time = end_time
        self.log_time_stamp = log_time_stamp
        if trade is not None:
            self.trade = trade
