"""CIM class DynamicSchedule (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.basic_interval_schedule import BasicIntervalSchedule

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement import (
        MktMeasurement,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class DynamicSchedule(BasicIntervalSchedule):
    """A continuously variable component of a control area's MW net interchange schedule.
    Dynamic schedules are sent and received by control areas."""

    __slots__ = (
        "_mkt_measurement",
        "_receive_sub_control_area",
        "_send_sub_control_area",
        "dyn_sched_sign_rev",
        "dyn_sched_status",
    )

    dyn_sched_sign_rev: bool | None
    dyn_sched_status: str | None

    mkt_measurement: One[MktMeasurement] = One(
        EndMeta(
            name="mkt_measurement",
            cim_role="MktMeasurement",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement:MktMeasurement",
            many=False,
            lower=1,
            upper=1,
            inverse="dynamic_schedule",
            aggregation="none",
        )
    )
    receive_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="receive_sub_control_area",
            cim_role="Receive_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="receive_dynamic_schedules",
            aggregation="none",
        )
    )
    send_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="send_sub_control_area",
            cim_role="Send_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="send_dynamic_schedules",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DynamicSchedule",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{C2098222-C39F-4bf7-BCB9-71A9CCD96D0B}",
        attributes=(
            AttrMeta("dyn_sched_sign_rev", "dynSchedSignRev", "bool", 0, 1, "primitive"),
            AttrMeta("dyn_sched_status", "dynSchedStatus", "str", 0, 1, "primitive"),
        ),
        ends=(
            mkt_measurement.meta,
            receive_sub_control_area.meta,
            send_sub_control_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        dyn_sched_sign_rev: bool | None = None,
        dyn_sched_status: str | None = None,
        mkt_measurement: MktMeasurement | None = None,
        receive_sub_control_area: SubControlArea | None = None,
        send_sub_control_area: SubControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dyn_sched_sign_rev = dyn_sched_sign_rev
        self.dyn_sched_status = dyn_sched_status
        if mkt_measurement is not None:
            self.mkt_measurement = mkt_measurement
        if receive_sub_control_area is not None:
            self.receive_sub_control_area = receive_sub_control_area
        if send_sub_control_area is not None:
            self.send_sub_control_area = send_sub_control_area
