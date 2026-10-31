"""CIM class SecurityConstraintSum (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.market_plan.market_factors import MarketFactors

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.base_case_constraint_limit import (
        BaseCaseConstraintLimit,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.constraint_term import (
        ConstraintTerm,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.contingency_constraint_limit import (
        ContingencyConstraintLimit,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_constraint_limit import (
        DefaultConstraintLimit,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class SecurityConstraintSum(MarketFactors):
    """Typically provided by RTO systems, constraints identified in both base case and critical
    contingency cases have to be transferred.

    A constraint has N (>=1) constraint terms. A term is represented by an instance of
    TerminalConstraintTerm.

    The constraint expression is:

    minValue <= c1*x1 + c2*x2 + .... cn*xn + k <= maxValue

    where:

    - cn is ConstraintTerm.factor

    - xn is the flow at the terminal

    Flow into the associated equipment is positive for the purpose of ConnectivityNode
    NodeConstraintTerm.

    k is SecurityConstraintsLinear.resourceMW.

    The units of k are assumed to be same as the units of the flows, xn. The constants, cn,
    are dimensionless.

    With these conventions, cn and k are all positive for a typical constraint such as
    "weighted sum of generation shall be less than limit". Furthermore, cn are all 1.0 for a
    case such as "interface flow shall be less than limit", assuming the terminals are
    chosen on the importing side of the interface."""

    __slots__ = (
        "_base_case_constraint_limit",
        "_constraint_terms",
        "_contingency_constraint_limits",
        "_default_constraint_limit",
        "_rto",
    )

    default_constraint_limit: One[DefaultConstraintLimit] = One(
        EndMeta(
            name="default_constraint_limit",
            cim_role="DefaultConstraintLimit",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.default_constraint_limit:DefaultConstraintLimit",
            many=False,
            lower=0,
            upper=1,
            inverse="security_constraint_sum",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=0,
            upper=1,
            inverse="security_constraints_linear",
            aggregation="none",
        )
    )
    base_case_constraint_limit: One[BaseCaseConstraintLimit] = One(
        EndMeta(
            name="base_case_constraint_limit",
            cim_role="BaseCaseConstraintLimit",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.base_case_constraint_limit:BaseCaseConstraintLimit",
            many=False,
            lower=0,
            upper=1,
            inverse="security_constraint_sum",
            aggregation="none",
        )
    )
    constraint_terms: Many[ConstraintTerm] = Many(
        EndMeta(
            name="constraint_terms",
            cim_role="ConstraintTerms",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.constraint_term:ConstraintTerm",
            many=True,
            lower=0,
            upper=None,
            inverse="security_constraint_sum",
            aggregation="none",
        )
    )
    contingency_constraint_limits: Many[ContingencyConstraintLimit] = Many(
        EndMeta(
            name="contingency_constraint_limits",
            cim_role="ContingencyConstraintLimits",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.contingency_constraint_limit:ContingencyConstraintLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="security_constraint_sum",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SecurityConstraintSum",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{2D47275A-FA55-47a4-BC5E-7A04E8519117}",
        ends=(
            default_constraint_limit.meta,
            rto.meta,
            base_case_constraint_limit.meta,
            constraint_terms.meta,
            contingency_constraint_limits.meta,
        ),
    )

    def __init__(
        self,
        *,
        default_constraint_limit: DefaultConstraintLimit | None = None,
        rto: RTO | None = None,
        base_case_constraint_limit: BaseCaseConstraintLimit | None = None,
        constraint_terms: Iterable[ConstraintTerm] | None = None,
        contingency_constraint_limits: Iterable[ContingencyConstraintLimit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if default_constraint_limit is not None:
            self.default_constraint_limit = default_constraint_limit
        if rto is not None:
            self.rto = rto
        if base_case_constraint_limit is not None:
            self.base_case_constraint_limit = base_case_constraint_limit
        if constraint_terms is not None:
            SecurityConstraintSum.constraint_terms.extend(self, constraint_terms)
        if contingency_constraint_limits is not None:
            SecurityConstraintSum.contingency_constraint_limits.extend(
                self, contingency_constraint_limits
            )

    def add_constraint_term(self, constraint_term: ConstraintTerm) -> Self:
        return SecurityConstraintSum.constraint_terms.add(self, constraint_term)

    def remove_constraint_term(self, constraint_term: ConstraintTerm) -> Self:
        return SecurityConstraintSum.constraint_terms.remove(self, constraint_term)

    def clear_constraint_terms(self) -> Self:
        return SecurityConstraintSum.constraint_terms.clear(self)

    def num_constraint_term(self) -> int:
        return SecurityConstraintSum.constraint_terms.count(self)

    def get_constraint_term_by_mrid(self, mrid: str) -> ConstraintTerm | None:
        return SecurityConstraintSum.constraint_terms.get_by_mrid(self, mrid)

    def add_contingency_constraint_limit(
        self, contingency_constraint_limit: ContingencyConstraintLimit
    ) -> Self:
        return SecurityConstraintSum.contingency_constraint_limits.add(
            self, contingency_constraint_limit
        )

    def remove_contingency_constraint_limit(
        self, contingency_constraint_limit: ContingencyConstraintLimit
    ) -> Self:
        return SecurityConstraintSum.contingency_constraint_limits.remove(
            self, contingency_constraint_limit
        )

    def clear_contingency_constraint_limits(self) -> Self:
        return SecurityConstraintSum.contingency_constraint_limits.clear(self)

    def num_contingency_constraint_limit(self) -> int:
        return SecurityConstraintSum.contingency_constraint_limits.count(self)

    def get_contingency_constraint_limit_by_mrid(
        self, mrid: str
    ) -> ContingencyConstraintLimit | None:
        return SecurityConstraintSum.contingency_constraint_limits.get_by_mrid(self, mrid)
