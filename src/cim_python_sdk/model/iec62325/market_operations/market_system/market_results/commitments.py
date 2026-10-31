"""CIM class Commitments (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commitment_clearing import (
        CommitmentClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.automatic_disp_inst_type_commitment import (
        AutomaticDispInstTypeCommitment,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.commitment_type import (
        CommitmentType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType


class Commitments(CimObject):
    """Provides the necessary information (on a resource basis) to capture the Startup/Shutdown
    commitment results. This information is relevant to all markets."""

    __slots__ = (
        "_commitment_clearing",
        "_registered_resource",
        "commitment_type",
        "instruction_cost",
        "instruction_type",
        "interval_end_time",
        "interval_start_time",
        "min_status_change_time",
        "no_load_cost",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    commitment_type: CommitmentType | None
    instruction_cost: float | None
    instruction_type: AutomaticDispInstTypeCommitment | None
    interval_end_time: _dt.datetime | None
    interval_start_time: _dt.datetime | None
    min_status_change_time: int | None
    no_load_cost: float | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None
    update_user: str | None

    commitment_clearing: Many[CommitmentClearing] = Many(
        EndMeta(
            name="commitment_clearing",
            cim_role="CommitmentClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.commitment_clearing:CommitmentClearing",
            many=True,
            lower=1,
            upper=None,
            inverse="commitments",
            aggregation="none",
        )
    )
    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="commitments",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Commitments",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{9132926E-7D92-4cf3-AE39-062BF7ECA914}",
        attributes=(
            AttrMeta("commitment_type", "commitmentType", "CommitmentType", 0, 1, "enumeration"),
            AttrMeta("instruction_cost", "instructionCost", "float", 0, 1, "primitive"),
            AttrMeta(
                "instruction_type",
                "instructionType",
                "AutomaticDispInstTypeCommitment",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("interval_end_time", "intervalEndTime", "datetime", 0, 1, "primitive"),
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("min_status_change_time", "minStatusChangeTime", "int", 0, 1, "primitive"),
            AttrMeta("no_load_cost", "noLoadCost", "float", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
        ),
        ends=(
            commitment_clearing.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        commitment_type: CommitmentType | None = None,
        instruction_cost: float | None = None,
        instruction_type: AutomaticDispInstTypeCommitment | None = None,
        interval_end_time: _dt.datetime | None = None,
        interval_start_time: _dt.datetime | None = None,
        min_status_change_time: int | None = None,
        no_load_cost: float | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        update_user: str | None = None,
        commitment_clearing: Iterable[CommitmentClearing] | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.commitment_type = commitment_type
        self.instruction_cost = instruction_cost
        self.instruction_type = instruction_type
        self.interval_end_time = interval_end_time
        self.interval_start_time = interval_start_time
        self.min_status_change_time = min_status_change_time
        self.no_load_cost = no_load_cost
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        self.update_user = update_user
        if commitment_clearing is not None:
            Commitments.commitment_clearing.extend(self, commitment_clearing)
        if registered_resource is not None:
            self.registered_resource = registered_resource

    def add_commitment_clearing(self, commitment_clearing: CommitmentClearing) -> Self:
        return Commitments.commitment_clearing.add(self, commitment_clearing)

    def remove_commitment_clearing(self, commitment_clearing: CommitmentClearing) -> Self:
        return Commitments.commitment_clearing.remove(self, commitment_clearing)

    def clear_commitment_clearing(self) -> Self:
        return Commitments.commitment_clearing.clear(self)

    def num_commitment_clearing(self) -> int:
        return Commitments.commitment_clearing.count(self)

    def get_commitment_clearing_by_mrid(self, mrid: str) -> CommitmentClearing | None:
        return Commitments.commitment_clearing.get_by_mrid(self, mrid)
