"""CIM class DefaultConstraintLimit (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum import (
        SecurityConstraintSum,
    )


class DefaultConstraintLimit(Curve):
    """Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2,
    respectively) applied as a default value if no specific constraint limits are specified
    for a contingency analysis. Use CurveSchedule XAxisUnits to specify MW or MVA."""

    __slots__ = ("_security_constraint_sum",)

    security_constraint_sum: One[SecurityConstraintSum] = One(
        EndMeta(
            name="security_constraint_sum",
            cim_role="SecurityConstraintSum",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum:SecurityConstraintSum",
            many=False,
            lower=1,
            upper=1,
            inverse="default_constraint_limit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DefaultConstraintLimit",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{40FB4806-7F6D-470d-9F6E-92F7A857A11B}",
        ends=(security_constraint_sum.meta,),
    )

    def __init__(
        self,
        *,
        security_constraint_sum: SecurityConstraintSum | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if security_constraint_sum is not None:
            self.security_constraint_sum = security_constraint_sum
