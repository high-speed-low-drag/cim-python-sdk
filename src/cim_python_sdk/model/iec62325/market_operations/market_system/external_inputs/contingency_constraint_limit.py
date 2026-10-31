"""CIM class ContingencyConstraintLimit (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mw_limit_schedule import (
        MWLimitSchedule,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum import (
        SecurityConstraintSum,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_contingency import (
        MktContingency,
    )


class ContingencyConstraintLimit(Curve):
    """Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2,
    respectively) assigned to a constraint for a specific contingency. Use CurveSchedule
    XAxisUnits to specify MW or MVA."""

    __slots__ = ("_mkt_contingency", "_mw_limit_schedules", "_security_constraint_sum")

    mkt_contingency: One[MktContingency] = One(
        EndMeta(
            name="mkt_contingency",
            cim_role="MktContingency",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_contingency:MktContingency",
            many=False,
            lower=1,
            upper=1,
            inverse="contingency_constraint_limit",
            aggregation="none",
        )
    )
    mw_limit_schedules: One[MWLimitSchedule] = One(
        EndMeta(
            name="mw_limit_schedules",
            cim_role="MWLimitSchedules",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mw_limit_schedule:MWLimitSchedule",
            many=False,
            lower=1,
            upper=1,
            inverse="security_constraint_limit",
            aggregation="none",
        )
    )
    security_constraint_sum: One[SecurityConstraintSum] = One(
        EndMeta(
            name="security_constraint_sum",
            cim_role="SecurityConstraintSum",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum:SecurityConstraintSum",
            many=False,
            lower=1,
            upper=1,
            inverse="contingency_constraint_limits",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ContingencyConstraintLimit",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{E1D7E102-8A3F-45de-A1C8-E6971CA32DD9}",
        ends=(
            mkt_contingency.meta,
            mw_limit_schedules.meta,
            security_constraint_sum.meta,
        ),
    )

    def __init__(
        self,
        *,
        mkt_contingency: MktContingency | None = None,
        mw_limit_schedules: MWLimitSchedule | None = None,
        security_constraint_sum: SecurityConstraintSum | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if mkt_contingency is not None:
            self.mkt_contingency = mkt_contingency
        if mw_limit_schedules is not None:
            self.mw_limit_schedules = mw_limit_schedules
        if security_constraint_sum is not None:
            self.security_constraint_sum = security_constraint_sum
