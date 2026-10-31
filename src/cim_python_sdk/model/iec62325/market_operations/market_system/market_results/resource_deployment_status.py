"""CIM class ResourceDeploymentStatus (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing import (
        InstructionClearing,
    )


class ResourceDeploymentStatus(CimObject):
    """CIM class ResourceDeploymentStatus."""

    __slots__ = (
        "_instruction_clearing",
        "accept_comments",
        "accept_status",
        "resource_response_mw",
    )

    accept_comments: str | None
    accept_status: str | None
    resource_response_mw: float | None

    instruction_clearing: One[InstructionClearing] = One(
        EndMeta(
            name="instruction_clearing",
            cim_role="InstructionClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.instruction_clearing:InstructionClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="resource_deployment_status",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceDeploymentStatus",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{3C11781A-95A7-4d39-9DF2-77AE0C86FFD0}",
        attributes=(
            AttrMeta("accept_comments", "acceptComments", "str", 0, 1, "primitive"),
            AttrMeta("accept_status", "acceptStatus", "str", 0, 1, "primitive"),
            AttrMeta("resource_response_mw", "resourceResponseMW", "float", 0, 1, "primitive"),
        ),
        ends=(instruction_clearing.meta,),
    )

    def __init__(
        self,
        *,
        accept_comments: str | None = None,
        accept_status: str | None = None,
        resource_response_mw: float | None = None,
        instruction_clearing: InstructionClearing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.accept_comments = accept_comments
        self.accept_status = accept_status
        self.resource_response_mw = resource_response_mw
        if instruction_clearing is not None:
            self.instruction_clearing = instruction_clearing
