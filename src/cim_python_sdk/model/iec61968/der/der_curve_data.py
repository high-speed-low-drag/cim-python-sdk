"""CIM class DERCurveData (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.der.der_monitorable_parameter import DERMonitorableParameter
    from cim_python_sdk.model.iec61968.der.dispatch_schedule import DispatchSchedule


class DERCurveData(CimObject):
    """The DER curve data class provides the nominal, maximum and minimum values for a DER
    Monitorable parameter for a series of time intervals defined by the DER
    DispatchSchedule."""

    __slots__ = (
        "_der_monitorable_parameter",
        "_dispatch_schedule",
        "interval_number",
        "max_y_value",
        "min_y_value",
        "nominal_y_value",
        "time_stamp",
    )

    time_stamp: _dt.datetime | None
    nominal_y_value: float | None
    min_y_value: float | None
    max_y_value: float | None
    interval_number: int | None

    der_monitorable_parameter: One[DERMonitorableParameter] = One(
        EndMeta(
            name="der_monitorable_parameter",
            cim_role="DERMonitorableParameter",
            target="cim_python_sdk.model.iec61968.der.der_monitorable_parameter:DERMonitorableParameter",
            many=False,
            lower=1,
            upper=1,
            inverse="der_curve_data",
            aggregation="none",
        )
    )
    dispatch_schedule: One[DispatchSchedule] = One(
        EndMeta(
            name="dispatch_schedule",
            cim_role="DispatchSchedule",
            target="cim_python_sdk.model.iec61968.der.dispatch_schedule:DispatchSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="der_curve_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DERCurveData",
        package="TC57CIM/IEC61968/DER",
        guid="{D94B7227-9399-4e16-BF77-4AA5007B7EEC}",
        attributes=(
            AttrMeta("time_stamp", "timeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("nominal_y_value", "nominalYValue", "float", 0, 1, "primitive"),
            AttrMeta("min_y_value", "minYValue", "float", 0, 1, "primitive"),
            AttrMeta("max_y_value", "maxYValue", "float", 0, 1, "primitive"),
            AttrMeta("interval_number", "intervalNumber", "int", 0, 1, "primitive"),
        ),
        ends=(
            der_monitorable_parameter.meta,
            dispatch_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        time_stamp: _dt.datetime | None = None,
        nominal_y_value: float | None = None,
        min_y_value: float | None = None,
        max_y_value: float | None = None,
        interval_number: int | None = None,
        der_monitorable_parameter: DERMonitorableParameter | None = None,
        dispatch_schedule: DispatchSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_stamp = time_stamp
        self.nominal_y_value = nominal_y_value
        self.min_y_value = min_y_value
        self.max_y_value = max_y_value
        self.interval_number = interval_number
        if der_monitorable_parameter is not None:
            self.der_monitorable_parameter = der_monitorable_parameter
        if dispatch_schedule is not None:
            self.dispatch_schedule = dispatch_schedule
