"""CIM class ExPostPricingResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_pricing import (
        ExPostPricing,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode


class ExPostPricingResults(CimObject):
    """Model of ex-post pricing of nodes. Includes LMP information, pnode based."""

    __slots__ = ("_ex_post_pricing", "_pnode", "congest_lmp", "lmp", "loss_lmp")

    congest_lmp: float | None
    lmp: float | None
    loss_lmp: float | None

    ex_post_pricing: One[ExPostPricing] = One(
        EndMeta(
            name="ex_post_pricing",
            cim_role="ExPostPricing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_pricing:ExPostPricing",
            many=False,
            lower=1,
            upper=1,
            inverse="ex_post_results",
            aggregation="none",
        )
    )
    pnode: One[Pnode] = One(
        EndMeta(
            name="pnode",
            cim_role="Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=1,
            upper=1,
            inverse="ex_post_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostPricingResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{A0C86A9F-25C5-4904-AF0B-4F9312CAD08E}",
        attributes=(
            AttrMeta("congest_lmp", "congestLMP", "float", 0, 1, "primitive"),
            AttrMeta("lmp", "lmp", "float", 0, 1, "primitive"),
            AttrMeta("loss_lmp", "lossLMP", "float", 0, 1, "primitive"),
        ),
        ends=(
            ex_post_pricing.meta,
            pnode.meta,
        ),
    )

    def __init__(
        self,
        *,
        congest_lmp: float | None = None,
        lmp: float | None = None,
        loss_lmp: float | None = None,
        ex_post_pricing: ExPostPricing | None = None,
        pnode: Pnode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.congest_lmp = congest_lmp
        self.lmp = lmp
        self.loss_lmp = loss_lmp
        if ex_post_pricing is not None:
            self.ex_post_pricing = ex_post_pricing
        if pnode is not None:
            self.pnode = pnode
