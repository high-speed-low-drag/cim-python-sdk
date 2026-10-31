"""CIM class ExPostLossResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_loss import (
        ExPostLoss,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class ExPostLossResults(CimObject):
    """Model results of ex-post calculation of MW losses. Summarizes loss in two categories
    losses on the the extra high voltage transmission and total losses. Calculated for each
    subcontrol area."""

    __slots__ = ("_ex_post_loss", "_sub_control_area", "ehv_loss_mw", "total_loss_mw")

    total_loss_mw: float | None
    ehv_loss_mw: float | None

    ex_post_loss: One[ExPostLoss] = One(
        EndMeta(
            name="ex_post_loss",
            cim_role="ExPostLoss",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_loss:ExPostLoss",
            many=False,
            lower=1,
            upper=1,
            inverse="ex_post_loss_results",
            aggregation="none",
        )
    )
    sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="ex_post_loss_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostLossResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{03B84153-3A47-4202-8538-6852B96D57E8}",
        attributes=(
            AttrMeta("total_loss_mw", "totalLossMW", "float", 0, 1, "primitive"),
            AttrMeta("ehv_loss_mw", "ehvLossMW", "float", 0, 1, "primitive"),
        ),
        ends=(
            ex_post_loss.meta,
            sub_control_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        total_loss_mw: float | None = None,
        ehv_loss_mw: float | None = None,
        ex_post_loss: ExPostLoss | None = None,
        sub_control_area: SubControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.total_loss_mw = total_loss_mw
        self.ehv_loss_mw = ehv_loss_mw
        if ex_post_loss is not None:
            self.ex_post_loss = ex_post_loss
        if sub_control_area is not None:
            self.sub_control_area = sub_control_area
