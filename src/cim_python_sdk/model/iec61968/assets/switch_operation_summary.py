"""CIM class SwitchOperationSummary (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset


class SwitchOperationSummary(IdentifiedObject):
    """Up-to-date, of-record summary of switch operation information, distilled from a variety
    of sources (real-time data or real-time data historian, field inspections, etc.) of use
    to asset health analytics."""

    __slots__ = (
        "_breaker",
        "lifetime_fault_operations",
        "lifetime_motor_starts",
        "lifetime_total_operations",
        "most_recent_fault_operation_date",
        "most_recent_motor_start_date",
        "most_recent_operation_date",
    )

    lifetime_total_operations: int | None
    lifetime_fault_operations: int | None
    lifetime_motor_starts: int | None
    most_recent_operation_date: _dt.date | None
    most_recent_fault_operation_date: _dt.date | None
    most_recent_motor_start_date: _dt.date | None

    breaker: One[Asset] = One(
        EndMeta(
            name="breaker",
            cim_role="Breaker",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=1,
            upper=1,
            inverse="breaker_operation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchOperationSummary",
        package="TC57CIM/IEC61968/Assets",
        guid="{FA56C86D-F988-404a-AE34-CDAEAC52A3E7}",
        attributes=(
            AttrMeta(
                "lifetime_total_operations", "lifetimeTotalOperations", "int", 0, 1, "primitive"
            ),
            AttrMeta(
                "lifetime_fault_operations", "lifetimeFaultOperations", "int", 0, 1, "primitive"
            ),
            AttrMeta("lifetime_motor_starts", "lifetimeMotorStarts", "int", 0, 1, "primitive"),
            AttrMeta(
                "most_recent_operation_date", "mostRecentOperationDate", "date", 0, 1, "primitive"
            ),
            AttrMeta(
                "most_recent_fault_operation_date",
                "mostRecentFaultOperationDate",
                "date",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "most_recent_motor_start_date",
                "mostRecentMotorStartDate",
                "date",
                0,
                1,
                "primitive",
            ),
        ),
        ends=(breaker.meta,),
    )

    def __init__(
        self,
        *,
        lifetime_total_operations: int | None = None,
        lifetime_fault_operations: int | None = None,
        lifetime_motor_starts: int | None = None,
        most_recent_operation_date: _dt.date | None = None,
        most_recent_fault_operation_date: _dt.date | None = None,
        most_recent_motor_start_date: _dt.date | None = None,
        breaker: Asset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.lifetime_total_operations = lifetime_total_operations
        self.lifetime_fault_operations = lifetime_fault_operations
        self.lifetime_motor_starts = lifetime_motor_starts
        self.most_recent_operation_date = most_recent_operation_date
        self.most_recent_fault_operation_date = most_recent_fault_operation_date
        self.most_recent_motor_start_date = most_recent_motor_start_date
        if breaker is not None:
            self.breaker = breaker
