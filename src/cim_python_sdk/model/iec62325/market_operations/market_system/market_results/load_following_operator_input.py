"""CIM class LoadFollowingOperatorInput (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType


class LoadFollowingOperatorInput(CimObject):
    """Model of load following capabilities that are entered by operators on a temporary basis.
    Related to Registered Resources in Metered Subsystems."""

    __slots__ = (
        "_registered_resource",
        "data_entry_time_stamp",
        "temp_load_following_down_manual_cap",
        "temp_load_following_up_manual_cap",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    data_entry_time_stamp: _dt.datetime | None
    temp_load_following_up_manual_cap: float | None
    temp_load_following_down_manual_cap: float | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="load_following_operator_input",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadFollowingOperatorInput",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{61CFAA82-4719-4897-8251-439FE7ADED7C}",
        attributes=(
            AttrMeta("data_entry_time_stamp", "dataEntryTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "temp_load_following_up_manual_cap",
                "tempLoadFollowingUpManualCap",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "temp_load_following_down_manual_cap",
                "tempLoadFollowingDownManualCap",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        data_entry_time_stamp: _dt.datetime | None = None,
        temp_load_following_up_manual_cap: float | None = None,
        temp_load_following_down_manual_cap: float | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.data_entry_time_stamp = data_entry_time_stamp
        self.temp_load_following_up_manual_cap = temp_load_following_up_manual_cap
        self.temp_load_following_down_manual_cap = temp_load_following_down_manual_cap
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        if registered_resource is not None:
            self.registered_resource = registered_resource
