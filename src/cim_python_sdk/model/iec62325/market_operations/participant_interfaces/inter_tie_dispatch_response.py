"""CIM class InterTieDispatchResponse (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.dispatch_response_type import (
        DispatchResponseType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.pass_indicator_type import (
        PassIndicatorType,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie import (
        RegisteredInterTie,
    )


class InterTieDispatchResponse(CimObject):
    """Response from an intertie resource acknowledging receipt of dispatch instructions."""

    __slots__ = (
        "_registered_inter_tie",
        "accept_mw",
        "accept_status",
        "cleared_mw",
        "pass_indicator",
        "start_time",
    )

    accept_status: DispatchResponseType | None
    accept_mw: float | None
    cleared_mw: float | None
    start_time: _dt.datetime | None
    pass_indicator: PassIndicatorType | None

    registered_inter_tie: One[RegisteredInterTie] = One(
        EndMeta(
            name="registered_inter_tie",
            cim_role="RegisteredInterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie:RegisteredInterTie",
            many=False,
            lower=1,
            upper=1,
            inverse="inter_tie_dispatch_response",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InterTieDispatchResponse",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{6EAF0507-95E7-4903-B956-357BB5D0B2F2}",
        attributes=(
            AttrMeta("accept_status", "acceptStatus", "DispatchResponseType", 0, 1, "enumeration"),
            AttrMeta("accept_mw", "acceptMW", "float", 0, 1, "primitive"),
            AttrMeta("cleared_mw", "clearedMW", "float", 0, 1, "primitive"),
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta("pass_indicator", "passIndicator", "PassIndicatorType", 0, 1, "enumeration"),
        ),
        ends=(registered_inter_tie.meta,),
    )

    def __init__(
        self,
        *,
        accept_status: DispatchResponseType | None = None,
        accept_mw: float | None = None,
        cleared_mw: float | None = None,
        start_time: _dt.datetime | None = None,
        pass_indicator: PassIndicatorType | None = None,
        registered_inter_tie: RegisteredInterTie | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.accept_status = accept_status
        self.accept_mw = accept_mw
        self.cleared_mw = cleared_mw
        self.start_time = start_time
        self.pass_indicator = pass_indicator
        if registered_inter_tie is not None:
            self.registered_inter_tie = registered_inter_tie
