"""CIM class InterTieResults (TC57CIM/IEC62325/InfIEC62325/InfMarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.inter_tie_clearing import (
        InterTieClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class InterTieResults(CimObject):
    """Provides the tie point specific output from the market applications. Currently, this is
    defined as the loop flow compensation MW value."""

    __slots__ = ("_flowgate", "_inter_tie_clearing", "base_mw", "cleared_value")

    cleared_value: float | None
    base_mw: float | None

    inter_tie_clearing: One[InterTieClearing] = One(
        EndMeta(
            name="inter_tie_clearing",
            cim_role="InterTieClearing",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_market_results.inter_tie_clearing:InterTieClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="inter_tie_results",
            aggregation="none",
        )
    )
    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=1,
            upper=1,
            inverse="inter_tie_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InterTieResults",
        package="TC57CIM/IEC62325/InfIEC62325/InfMarketResults",
        guid="{B7E8BAE0-6817-4352-BFBA-A533508B7DDE}",
        attributes=(
            AttrMeta("cleared_value", "clearedValue", "float", 0, 1, "primitive"),
            AttrMeta("base_mw", "baseMW", "float", 0, 1, "primitive"),
        ),
        ends=(
            inter_tie_clearing.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        cleared_value: float | None = None,
        base_mw: float | None = None,
        inter_tie_clearing: InterTieClearing | None = None,
        flowgate: Flowgate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cleared_value = cleared_value
        self.base_mw = base_mw
        if inter_tie_clearing is not None:
            self.inter_tie_clearing = inter_tie_clearing
        if flowgate is not None:
            self.flowgate = flowgate
