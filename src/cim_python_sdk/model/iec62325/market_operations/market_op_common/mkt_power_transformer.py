"""CIM class MktPowerTransformer (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.power_transformer import PowerTransformer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.branch_end_flow import (
        BranchEndFlow,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class MktPowerTransformer(PowerTransformer):
    """Subclass of IEC61970:Wires:PowerTransformer."""

    __slots__ = ("_end_a_flow", "_end_b_flow", "_flowgate")

    end_a_flow: One[BranchEndFlow] = One(
        EndMeta(
            name="end_a_flow",
            cim_role="EndAFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.branch_end_flow:BranchEndFlow",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_power_transformer_end_a_flow",
            aggregation="none",
        )
    )
    end_b_flow: One[BranchEndFlow] = One(
        EndMeta(
            name="end_b_flow",
            cim_role="EndBFlow",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.branch_end_flow:BranchEndFlow",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_power_transformer_end_b_flow",
            aggregation="none",
        )
    )
    flowgate: Many[Flowgate] = Many(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_power_transformer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktPowerTransformer",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{234E9796-CB64-4bae-A3EC-C33F3B4F7275}",
        ends=(
            end_a_flow.meta,
            end_b_flow.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        end_a_flow: BranchEndFlow | None = None,
        end_b_flow: BranchEndFlow | None = None,
        flowgate: Iterable[Flowgate] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if end_a_flow is not None:
            self.end_a_flow = end_a_flow
        if end_b_flow is not None:
            self.end_b_flow = end_b_flow
        if flowgate is not None:
            MktPowerTransformer.flowgate.extend(self, flowgate)

    def add_flowgate(self, flowgate: Flowgate) -> Self:
        return MktPowerTransformer.flowgate.add(self, flowgate)

    def remove_flowgate(self, flowgate: Flowgate) -> Self:
        return MktPowerTransformer.flowgate.remove(self, flowgate)

    def clear_flowgate(self) -> Self:
        return MktPowerTransformer.flowgate.clear(self)

    def num_flowgate(self) -> int:
        return MktPowerTransformer.flowgate.count(self)

    def get_flowgate_by_mrid(self, mrid: str) -> Flowgate | None:
        return MktPowerTransformer.flowgate.get_by_mrid(self, mrid)
