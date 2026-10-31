"""CIM class MktACLineSegment (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.ac_line_segment import ACLineSegment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.branch_end_flow import (
        BranchEndFlow,
    )


class MktACLineSegment(ACLineSegment):
    """Subclass of IEC 61970:Wires:ACLineSegment."""

    __slots__ = ("_end_a_flow", "_end_b_flow")

    end_b_flow: One[BranchEndFlow] = One(
        EndMeta(
            name="end_b_flow",
            cim_role="EndBFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.branch_end_flow:BranchEndFlow",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_ac_line_segment_end_b_flow",
            aggregation="none",
        )
    )
    end_a_flow: One[BranchEndFlow] = One(
        EndMeta(
            name="end_a_flow",
            cim_role="EndAFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.branch_end_flow:BranchEndFlow",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_ac_line_segment_end_a_flow",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktACLineSegment",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{5D97034C-EE14-4ec9-B92A-E90EE3C3AC9F}",
        ends=(
            end_b_flow.meta,
            end_a_flow.meta,
        ),
    )

    def __init__(
        self,
        *,
        end_b_flow: BranchEndFlow | None = None,
        end_a_flow: BranchEndFlow | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if end_b_flow is not None:
            self.end_b_flow = end_b_flow
        if end_a_flow is not None:
            self.end_a_flow = end_a_flow
