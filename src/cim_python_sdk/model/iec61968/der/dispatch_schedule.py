"""CIM class DispatchSchedule (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.der.der_curve_data import DERCurveData
    from cim_python_sdk.model.iec61968.der.der_monitorable_parameter import DERMonitorableParameter
    from cim_python_sdk.model.iec61968.der.time_interval_kind import TimeIntervalKind
    from cim_python_sdk.model.iec61970.base.core.curve_style import CurveStyle


class DispatchSchedule(CimObject):
    """Specifies the characteristics of the time schedule over which DERMonitorableParameters
    are dispatched."""

    __slots__ = (
        "_der_curve_data",
        "_der_monitorable_parameter",
        "confidence",
        "curve_style_kind",
        "number_of_intervals",
        "start_time",
        "time_interval_duration",
        "time_interval_unit",
    )

    confidence: float | None  # PerCent
    curve_style_kind: CurveStyle | None
    start_time: _dt.datetime | None
    number_of_intervals: int | None
    time_interval_unit: TimeIntervalKind | None
    time_interval_duration: int | None

    der_curve_data: Many[DERCurveData] = Many(
        EndMeta(
            name="der_curve_data",
            cim_role="DERCurveData",
            target="cim_python_sdk.model.iec61968.der.der_curve_data:DERCurveData",
            many=True,
            lower=0,
            upper=None,
            inverse="dispatch_schedule",
            aggregation="none",
        )
    )
    der_monitorable_parameter: One[DERMonitorableParameter] = One(
        EndMeta(
            name="der_monitorable_parameter",
            cim_role="DERMonitorableParameter",
            target="cim_python_sdk.model.iec61968.der.der_monitorable_parameter:DERMonitorableParameter",
            many=False,
            lower=1,
            upper=1,
            inverse="dispatch_schedule",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DispatchSchedule",
        package="TC57CIM/IEC61968/DER",
        guid="{AE7805A5-0914-464e-A1BD-C30BB36F0360}",
        attributes=(
            AttrMeta("confidence", "confidence", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("curve_style_kind", "curveStyleKind", "CurveStyle", 0, 1, "enumeration"),
            AttrMeta("start_time", "startTime", "datetime", 0, 1, "primitive"),
            AttrMeta("number_of_intervals", "numberOfIntervals", "int", 0, 1, "primitive"),
            AttrMeta(
                "time_interval_unit", "timeIntervalUnit", "TimeIntervalKind", 0, 1, "enumeration"
            ),
            AttrMeta("time_interval_duration", "timeIntervalDuration", "int", 1, 1, "primitive"),
        ),
        ends=(
            der_curve_data.meta,
            der_monitorable_parameter.meta,
        ),
    )

    def __init__(
        self,
        *,
        confidence: float | None = None,
        curve_style_kind: CurveStyle | None = None,
        start_time: _dt.datetime | None = None,
        number_of_intervals: int | None = None,
        time_interval_unit: TimeIntervalKind | None = None,
        time_interval_duration: int | None = None,
        der_curve_data: Iterable[DERCurveData] | None = None,
        der_monitorable_parameter: DERMonitorableParameter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.confidence = confidence
        self.curve_style_kind = curve_style_kind
        self.start_time = start_time
        self.number_of_intervals = number_of_intervals
        self.time_interval_unit = time_interval_unit
        self.time_interval_duration = time_interval_duration
        if der_curve_data is not None:
            DispatchSchedule.der_curve_data.extend(self, der_curve_data)
        if der_monitorable_parameter is not None:
            self.der_monitorable_parameter = der_monitorable_parameter

    def add_der_curve_data(self, der_curve_data: DERCurveData) -> Self:
        return DispatchSchedule.der_curve_data.add(self, der_curve_data)

    def remove_der_curve_data(self, der_curve_data: DERCurveData) -> Self:
        return DispatchSchedule.der_curve_data.remove(self, der_curve_data)

    def clear_der_curve_data(self) -> Self:
        return DispatchSchedule.der_curve_data.clear(self)

    def num_der_curve_data(self) -> int:
        return DispatchSchedule.der_curve_data.count(self)
