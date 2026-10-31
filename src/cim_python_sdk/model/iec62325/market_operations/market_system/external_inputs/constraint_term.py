"""CIM class ConstraintTerm (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum import (
        SecurityConstraintSum,
    )


class ConstraintTerm(IdentifiedObject):
    """A constraint term is one element of a linear constraint."""

    __slots__ = ("_security_constraint_sum", "factor", "function")

    factor: str | None
    function: str | None

    security_constraint_sum: One[SecurityConstraintSum] = One(
        EndMeta(
            name="security_constraint_sum",
            cim_role="SecurityConstraintSum",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraint_sum:SecurityConstraintSum",
            many=False,
            lower=1,
            upper=1,
            inverse="constraint_terms",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConstraintTerm",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{0888D675-B5E4-464e-A422-E1FC0197BB36}",
        attributes=(
            AttrMeta("factor", "factor", "str", 0, 1, "primitive"),
            AttrMeta("function", "function", "str", 0, 1, "primitive"),
        ),
        ends=(security_constraint_sum.meta,),
    )

    def __init__(
        self,
        *,
        factor: str | None = None,
        function: str | None = None,
        security_constraint_sum: SecurityConstraintSum | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor = factor
        self.function = function
        if security_constraint_sum is not None:
            self.security_constraint_sum = security_constraint_sum
