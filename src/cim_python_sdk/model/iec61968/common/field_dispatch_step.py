"""CIM class FieldDispatchStep (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.common.crew_status_kind import CrewStatusKind
    from cim_python_sdk.model.iec61968.common.field_dispatch_history import FieldDispatchHistory


class FieldDispatchStep(CimObject):
    """Details of the step in the field dispatch history."""

    __slots__ = (
        "_field_dispatch_history",
        "dispatch_status",
        "occurred_date_time",
        "remarks",
        "sequence_number",
    )

    dispatch_status: CrewStatusKind | None
    sequence_number: int | None
    occurred_date_time: _dt.datetime | None
    remarks: str | None

    field_dispatch_history: One[FieldDispatchHistory] = One(
        EndMeta(
            name="field_dispatch_history",
            cim_role="FieldDispatchHistory",
            target="cim_python_sdk.model.iec61968.common.field_dispatch_history:FieldDispatchHistory",
            many=False,
            lower=1,
            upper=1,
            inverse="field_dispatch_step",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FieldDispatchStep",
        package="TC57CIM/IEC61968/Common",
        guid="{FD9DBBC8-AE78-4ca9-8E16-2B6906E69D6C}",
        attributes=(
            AttrMeta("dispatch_status", "dispatchStatus", "CrewStatusKind", 1, 1, "enumeration"),
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("occurred_date_time", "occurredDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("remarks", "remarks", "str", 0, 1, "primitive"),
        ),
        ends=(field_dispatch_history.meta,),
    )

    def __init__(
        self,
        *,
        dispatch_status: CrewStatusKind | None = None,
        sequence_number: int | None = None,
        occurred_date_time: _dt.datetime | None = None,
        remarks: str | None = None,
        field_dispatch_history: FieldDispatchHistory | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dispatch_status = dispatch_status
        self.sequence_number = sequence_number
        self.occurred_date_time = occurred_date_time
        self.remarks = remarks
        if field_dispatch_history is not None:
            self.field_dispatch_history = field_dispatch_history
