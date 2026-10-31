"""CIM class ExPostResourceResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_resource import (
        ExPostResource,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.equipment_status_type import (
        EquipmentStatusType,
    )


class ExPostResourceResults(CimObject):
    """Model of ex-post pricing of resources contains components of LMPs: energy, congestion,
    loss. Resource based."""

    __slots__ = (
        "_ex_post_resource",
        "_registered_resource",
        "congestion_lmp",
        "desired_mw",
        "dispatch_rate",
        "lmp",
        "loss_lmp",
        "max_economic_mw",
        "min_economic_mw",
        "resource_mw",
        "status",
    )

    congestion_lmp: float | None
    desired_mw: float | None
    dispatch_rate: float | None
    lmp: float | None
    loss_lmp: float | None
    max_economic_mw: float | None
    min_economic_mw: float | None
    resource_mw: float | None
    status: EquipmentStatusType | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="ex_post_resource_results",
            aggregation="none",
        )
    )
    ex_post_resource: One[ExPostResource] = One(
        EndMeta(
            name="ex_post_resource",
            cim_role="ExPostResource",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.ex_post_resource:ExPostResource",
            many=False,
            lower=1,
            upper=1,
            inverse="ex_post_resource_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExPostResourceResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{5784BC07-3A3E-40e0-AD6E-595897F8857D}",
        attributes=(
            AttrMeta("congestion_lmp", "congestionLMP", "float", 0, 1, "primitive"),
            AttrMeta("desired_mw", "desiredMW", "float", 0, 1, "primitive"),
            AttrMeta("dispatch_rate", "dispatchRate", "float", 0, 1, "primitive"),
            AttrMeta("lmp", "lmp", "float", 0, 1, "primitive"),
            AttrMeta("loss_lmp", "lossLMP", "float", 0, 1, "primitive"),
            AttrMeta("max_economic_mw", "maxEconomicMW", "float", 0, 1, "primitive"),
            AttrMeta("min_economic_mw", "minEconomicMW", "float", 0, 1, "primitive"),
            AttrMeta("resource_mw", "resourceMW", "float", 0, 1, "primitive"),
            AttrMeta("status", "status", "EquipmentStatusType", 0, 1, "enumeration"),
        ),
        ends=(
            registered_resource.meta,
            ex_post_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        congestion_lmp: float | None = None,
        desired_mw: float | None = None,
        dispatch_rate: float | None = None,
        lmp: float | None = None,
        loss_lmp: float | None = None,
        max_economic_mw: float | None = None,
        min_economic_mw: float | None = None,
        resource_mw: float | None = None,
        status: EquipmentStatusType | None = None,
        registered_resource: RegisteredResource | None = None,
        ex_post_resource: ExPostResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.congestion_lmp = congestion_lmp
        self.desired_mw = desired_mw
        self.dispatch_rate = dispatch_rate
        self.lmp = lmp
        self.loss_lmp = loss_lmp
        self.max_economic_mw = max_economic_mw
        self.min_economic_mw = min_economic_mw
        self.resource_mw = resource_mw
        self.status = status
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if ex_post_resource is not None:
            self.ex_post_resource = ex_post_resource
