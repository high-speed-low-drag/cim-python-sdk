"""CIM class MktContingency (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.contingency.contingency import Contingency

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.contingency_constraint_limit import (
        ContingencyConstraintLimit,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface_solution import (
        TransferInterfaceSolution,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_results import (
        ConstraintResults,
    )


class MktContingency(Contingency):
    """Subclass of IEC 61970:Contingency."""

    __slots__ = (
        "_constraint_results",
        "_contingency_constraint_limit",
        "_transfer_interface_solution_a",
        "_transfer_interface_solution_b",
        "load_rollover_flag",
        "ltc_control_flag",
        "participation_factor_set",
        "screening_flag",
    )

    load_rollover_flag: bool | None
    ltc_control_flag: bool | None
    participation_factor_set: str | None
    screening_flag: bool | None

    constraint_results: Many[ConstraintResults] = Many(
        EndMeta(
            name="constraint_results",
            cim_role="ConstraintResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_results:ConstraintResults",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_contingency",
            aggregation="none",
        )
    )
    contingency_constraint_limit: Many[ContingencyConstraintLimit] = Many(
        EndMeta(
            name="contingency_constraint_limit",
            cim_role="ContingencyConstraintLimit",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.contingency_constraint_limit:ContingencyConstraintLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_contingency",
            aggregation="none",
        )
    )
    transfer_interface_solution_b: One[TransferInterfaceSolution] = One(
        EndMeta(
            name="transfer_interface_solution_b",
            cim_role="TransferInterfaceSolutionB",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface_solution:TransferInterfaceSolution",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_contingency_b",
            aggregation="none",
        )
    )
    transfer_interface_solution_a: One[TransferInterfaceSolution] = One(
        EndMeta(
            name="transfer_interface_solution_a",
            cim_role="TransferInterfaceSolutionA",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface_solution:TransferInterfaceSolution",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_contingency_a",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktContingency",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{836AD0B6-1B52-46ea-8BF0-C210A74EDB3D}",
        attributes=(
            AttrMeta("load_rollover_flag", "loadRolloverFlag", "bool", 0, 1, "primitive"),
            AttrMeta("ltc_control_flag", "ltcControlFlag", "bool", 0, 1, "primitive"),
            AttrMeta(
                "participation_factor_set", "participationFactorSet", "str", 0, 1, "primitive"
            ),
            AttrMeta("screening_flag", "screeningFlag", "bool", 0, 1, "primitive"),
        ),
        ends=(
            constraint_results.meta,
            contingency_constraint_limit.meta,
            transfer_interface_solution_b.meta,
            transfer_interface_solution_a.meta,
        ),
    )

    def __init__(
        self,
        *,
        load_rollover_flag: bool | None = None,
        ltc_control_flag: bool | None = None,
        participation_factor_set: str | None = None,
        screening_flag: bool | None = None,
        constraint_results: Iterable[ConstraintResults] | None = None,
        contingency_constraint_limit: Iterable[ContingencyConstraintLimit] | None = None,
        transfer_interface_solution_b: TransferInterfaceSolution | None = None,
        transfer_interface_solution_a: TransferInterfaceSolution | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.load_rollover_flag = load_rollover_flag
        self.ltc_control_flag = ltc_control_flag
        self.participation_factor_set = participation_factor_set
        self.screening_flag = screening_flag
        if constraint_results is not None:
            MktContingency.constraint_results.extend(self, constraint_results)
        if contingency_constraint_limit is not None:
            MktContingency.contingency_constraint_limit.extend(self, contingency_constraint_limit)
        if transfer_interface_solution_b is not None:
            self.transfer_interface_solution_b = transfer_interface_solution_b
        if transfer_interface_solution_a is not None:
            self.transfer_interface_solution_a = transfer_interface_solution_a

    def add_constraint_result(self, constraint_result: ConstraintResults) -> Self:
        return MktContingency.constraint_results.add(self, constraint_result)

    def remove_constraint_result(self, constraint_result: ConstraintResults) -> Self:
        return MktContingency.constraint_results.remove(self, constraint_result)

    def clear_constraint_results(self) -> Self:
        return MktContingency.constraint_results.clear(self)

    def num_constraint_result(self) -> int:
        return MktContingency.constraint_results.count(self)

    def get_constraint_result_by_mrid(self, mrid: str) -> ConstraintResults | None:
        return MktContingency.constraint_results.get_by_mrid(self, mrid)

    def add_contingency_constraint_limit(
        self, contingency_constraint_limit: ContingencyConstraintLimit
    ) -> Self:
        return MktContingency.contingency_constraint_limit.add(self, contingency_constraint_limit)

    def remove_contingency_constraint_limit(
        self, contingency_constraint_limit: ContingencyConstraintLimit
    ) -> Self:
        return MktContingency.contingency_constraint_limit.remove(
            self, contingency_constraint_limit
        )

    def clear_contingency_constraint_limit(self) -> Self:
        return MktContingency.contingency_constraint_limit.clear(self)

    def num_contingency_constraint_limit(self) -> int:
        return MktContingency.contingency_constraint_limit.count(self)

    def get_contingency_constraint_limit_by_mrid(
        self, mrid: str
    ) -> ContingencyConstraintLimit | None:
        return MktContingency.contingency_constraint_limit.get_by_mrid(self, mrid)
