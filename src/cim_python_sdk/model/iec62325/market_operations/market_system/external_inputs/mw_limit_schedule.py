"""CIM class MWLimitSchedule (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.contingency_constraint_limit import (
        ContingencyConstraintLimit,
    )


class MWLimitSchedule(CimObject):
    """Maximum MW and optionally Minimum MW (Y1 and Y2, respectively)."""

    __slots__ = ("_security_constraint_limit",)

    security_constraint_limit: One[ContingencyConstraintLimit] = One(
        EndMeta(
            name="security_constraint_limit",
            cim_role="SecurityConstraintLimit",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.contingency_constraint_limit:ContingencyConstraintLimit",
            many=False,
            lower=1,
            upper=1,
            inverse="mw_limit_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MWLimitSchedule",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{40FDD18B-50C8-4ddc-A1C4-DFC133B178E3}",
        ends=(security_constraint_limit.meta,),
    )

    def __init__(
        self,
        *,
        security_constraint_limit: ContingencyConstraintLimit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if security_constraint_limit is not None:
            self.security_constraint_limit = security_constraint_limit
