"""CIM class LoadFollowingInst (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource


class LoadFollowingInst(CimObject):
    """Metered SubSystem Load Following Instruction."""

    __slots__ = (
        "_registered_resource",
        "end_time",
        "load_following_mw",
        "mss_instruction_id",
        "start_time",
    )

    mss_instruction_id: str | None
    start_time: _dt.datetime | None
    end_time: _dt.datetime | None
    load_following_mw: float | None

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="load_following_inst",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadFollowingInst",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{A366CFF5-28B3-4052-9EA2-A228FA053F62}",
        attributes=(
            AttrMeta("mss_instruction_id", "mssInstructionID", "str", 0, 1, "primitive"),
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta("end_time", "endTime", "datetime", 0, 1, "primitive"),
            AttrMeta("load_following_mw", "loadFollowingMW", "float", 0, 1, "primitive"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        mss_instruction_id: str | None = None,
        start_time: _dt.datetime | None = None,
        end_time: _dt.datetime | None = None,
        load_following_mw: float | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mss_instruction_id = mss_instruction_id
        self.start_time = start_time
        self.end_time = end_time
        self.load_following_mw = load_following_mw
        if registered_resource is not None:
            self.registered_resource = registered_resource
