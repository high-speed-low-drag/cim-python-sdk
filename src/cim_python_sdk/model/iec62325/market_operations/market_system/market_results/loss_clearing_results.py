"""CIM class LossClearingResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing import (
        LossClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.ruc_zone import RUCZone
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class LossClearingResults(CimObject):
    """Provides the MW loss for RUC Zones, subcontrol areas, and the total loss."""

    __slots__ = (
        "_host_control_area",
        "_loss_clearing",
        "_ruc_zone",
        "_sub_control_area",
        "loss_mw",
    )

    loss_mw: float | None

    ruc_zone: One[RUCZone] = One(
        EndMeta(
            name="ruc_zone",
            cim_role="RUCZone",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.ruc_zone:RUCZone",
            many=False,
            lower=0,
            upper=1,
            inverse="loss_clearing_results",
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
            inverse="loss_clearing_results",
            aggregation="none",
        )
    )
    loss_clearing: One[LossClearing] = One(
        EndMeta(
            name="loss_clearing",
            cim_role="LossClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.loss_clearing:LossClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="loss_clearing_results",
            aggregation="none",
        )
    )
    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="loss_clearing_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LossClearingResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{13E4D24D-E662-436f-98DA-EB56DD64E571}",
        attributes=(AttrMeta("loss_mw", "lossMW", "float", 0, 1, "primitive"),),
        ends=(
            ruc_zone.meta,
            sub_control_area.meta,
            loss_clearing.meta,
            host_control_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        loss_mw: float | None = None,
        ruc_zone: RUCZone | None = None,
        sub_control_area: SubControlArea | None = None,
        loss_clearing: LossClearing | None = None,
        host_control_area: HostControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.loss_mw = loss_mw
        if ruc_zone is not None:
            self.ruc_zone = ruc_zone
        if sub_control_area is not None:
            self.sub_control_area = sub_control_area
        if loss_clearing is not None:
            self.loss_clearing = loss_clearing
        if host_control_area is not None:
            self.host_control_area = host_control_area
