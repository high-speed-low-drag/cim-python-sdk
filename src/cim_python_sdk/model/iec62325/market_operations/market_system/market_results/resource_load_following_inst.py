"""CIM class ResourceLoadFollowingInst (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_clearing import (
        ResourceClearing,
    )


class ResourceLoadFollowingInst(CimObject):
    """Model of market clearing results for resources that bid to follow load."""

    __slots__ = (
        "_registered_resource",
        "_resource_clearing",
        "calc_load_following_mw",
        "disp_window_high_limt",
        "disp_window_low_limt",
        "instruction_id",
        "interval_start_time",
    )

    instruction_id: str | None
    interval_start_time: _dt.datetime | None
    calc_load_following_mw: float | None
    disp_window_low_limt: float | None
    disp_window_high_limt: float | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="resource_load_following_inst",
            aggregation="none",
        )
    )
    resource_clearing: One[ResourceClearing] = One(
        EndMeta(
            name="resource_clearing",
            cim_role="ResourceClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_clearing:ResourceClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="resource_load_following_inst",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceLoadFollowingInst",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{1874CDEF-F92E-449f-A0B1-0FF929793AAB}",
        attributes=(
            AttrMeta("instruction_id", "instructionID", "str", 0, 1, "primitive"),
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("calc_load_following_mw", "calcLoadFollowingMW", "float", 0, 1, "primitive"),
            AttrMeta("disp_window_low_limt", "dispWindowLowLimt", "float", 0, 1, "primitive"),
            AttrMeta("disp_window_high_limt", "dispWindowHighLimt", "float", 0, 1, "primitive"),
        ),
        ends=(
            registered_resource.meta,
            resource_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        instruction_id: str | None = None,
        interval_start_time: _dt.datetime | None = None,
        calc_load_following_mw: float | None = None,
        disp_window_low_limt: float | None = None,
        disp_window_high_limt: float | None = None,
        registered_resource: RegisteredResource | None = None,
        resource_clearing: ResourceClearing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.instruction_id = instruction_id
        self.interval_start_time = interval_start_time
        self.calc_load_following_mw = calc_load_following_mw
        self.disp_window_low_limt = disp_window_low_limt
        self.disp_window_high_limt = disp_window_high_limt
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if resource_clearing is not None:
            self.resource_clearing = resource_clearing
