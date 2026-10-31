"""CIM class DispatchInstReply (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.dispatch_response_type import (
        DispatchResponseType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.pass_indicator_type import (
        PassIndicatorType,
    )


class DispatchInstReply(IdentifiedObject):
    """Response from registered resource acknowledging receipt of dispatch instructions."""

    __slots__ = (
        "_registered_resource",
        "accept_mw",
        "accept_status",
        "certification_name",
        "cleared_mw",
        "instruction_time",
        "instruction_type",
        "pass_indicator",
        "received_time",
        "start_time",
    )

    accept_mw: float | None  # ActivePower
    accept_status: DispatchResponseType | None
    certification_name: str | None
    cleared_mw: float | None  # ActivePower
    instruction_time: _dt.datetime | None
    instruction_type: str | None
    pass_indicator: PassIndicatorType | None
    received_time: _dt.datetime | None
    start_time: _dt.datetime | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="dispatch_inst_reply",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DispatchInstReply",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{7A517BE6-6CC4-4c3a-B95D-700524D10493}",
        attributes=(
            AttrMeta("accept_mw", "acceptMW", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("accept_status", "acceptStatus", "DispatchResponseType", 0, 1, "enumeration"),
            AttrMeta("certification_name", "certificationName", "str", 0, 1, "primitive"),
            AttrMeta("cleared_mw", "clearedMW", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("instruction_time", "instructionTime", "datetime", 0, 1, "primitive"),
            AttrMeta("instruction_type", "instructionType", "str", 0, 1, "primitive"),
            AttrMeta("pass_indicator", "passIndicator", "PassIndicatorType", 0, 1, "enumeration"),
            AttrMeta("received_time", "receivedTime", "datetime", 0, 1, "primitive"),
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        accept_mw: float | None = None,
        accept_status: DispatchResponseType | None = None,
        certification_name: str | None = None,
        cleared_mw: float | None = None,
        instruction_time: _dt.datetime | None = None,
        instruction_type: str | None = None,
        pass_indicator: PassIndicatorType | None = None,
        received_time: _dt.datetime | None = None,
        start_time: _dt.datetime | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.accept_mw = accept_mw
        self.accept_status = accept_status
        self.certification_name = certification_name
        self.cleared_mw = cleared_mw
        self.instruction_time = instruction_time
        self.instruction_type = instruction_type
        self.pass_indicator = pass_indicator
        self.received_time = received_time
        self.start_time = start_time
        if registered_resource is not None:
            self.registered_resource = registered_resource
