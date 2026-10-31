"""CIM class DopInstruction (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing_dop import (
        InstructionClearingDOP,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class DopInstruction(CimObject):
    """Provides the necessary information (on a resource basis) to capture the Dispatch
    Operating Point (DOP) results on a Dispatch interval. This information is only relevant
    to the RT interval market."""

    __slots__ = (
        "_instruction_clearing_dop",
        "_registered_resouce",
        "mw_dop",
        "plot_priority",
        "run_indicator_dop",
        "timestamp_dop",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    mw_dop: float | None  # ActivePower
    timestamp_dop: _dt.datetime | None
    plot_priority: int | None
    run_indicator_dop: YesNo | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None

    registered_resouce: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resouce",
            cim_role="RegisteredResouce",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="dop_instruction",
            aggregation="none",
        )
    )
    instruction_clearing_dop: Many[InstructionClearingDOP] = Many(
        EndMeta(
            name="instruction_clearing_dop",
            cim_role="InstructionClearingDOP",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing_dop:InstructionClearingDOP",
            many=True,
            lower=1,
            upper=None,
            inverse="dop_instruction",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DopInstruction",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{B6174126-E8E3-48d8-9573-FE95E1ABCED1}",
        attributes=(
            AttrMeta("mw_dop", "mwDOP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("timestamp_dop", "timestampDOP", "datetime", 0, 1, "primitive"),
            AttrMeta("plot_priority", "plotPriority", "int", 0, 1, "primitive"),
            AttrMeta("run_indicator_dop", "runIndicatorDOP", "YesNo", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
        ),
        ends=(
            registered_resouce.meta,
            instruction_clearing_dop.meta,
        ),
    )

    def __init__(
        self,
        *,
        mw_dop: float | None = None,
        timestamp_dop: _dt.datetime | None = None,
        plot_priority: int | None = None,
        run_indicator_dop: YesNo | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        registered_resouce: RegisteredResource | None = None,
        instruction_clearing_dop: Iterable[InstructionClearingDOP] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mw_dop = mw_dop
        self.timestamp_dop = timestamp_dop
        self.plot_priority = plot_priority
        self.run_indicator_dop = run_indicator_dop
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        if registered_resouce is not None:
            self.registered_resouce = registered_resouce
        if instruction_clearing_dop is not None:
            DopInstruction.instruction_clearing_dop.extend(self, instruction_clearing_dop)

    def add_instruction_clearing_dop(
        self, instruction_clearing_dop: InstructionClearingDOP
    ) -> Self:
        return DopInstruction.instruction_clearing_dop.add(self, instruction_clearing_dop)

    def remove_instruction_clearing_dop(
        self, instruction_clearing_dop: InstructionClearingDOP
    ) -> Self:
        return DopInstruction.instruction_clearing_dop.remove(self, instruction_clearing_dop)

    def clear_instruction_clearing_dop(self) -> Self:
        return DopInstruction.instruction_clearing_dop.clear(self)

    def num_instruction_clearing_dop(self) -> int:
        return DopInstruction.instruction_clearing_dop.count(self)

    def get_instruction_clearing_dop_by_mrid(self, mrid: str) -> InstructionClearingDOP | None:
        return DopInstruction.instruction_clearing_dop.get_by_mrid(self, mrid)
