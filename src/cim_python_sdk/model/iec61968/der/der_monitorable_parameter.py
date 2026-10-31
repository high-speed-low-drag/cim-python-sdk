"""CIM class DERMonitorableParameter (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.der.der_curve_data import DERCurveData
    from cim_python_sdk.model.iec61968.der.der_parameter_kind import DERParameterKind
    from cim_python_sdk.model.iec61968.der.der_unit_symbol import DERUnitSymbol
    from cim_python_sdk.model.iec61968.der.dispatch_schedule import DispatchSchedule
    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup
    from cim_python_sdk.model.iec61968.metering.flow_direction_kind import FlowDirectionKind
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier


class DERMonitorableParameter(CimObject):
    """To define the DER monitorable parameters that will be forecasted and dispatched for a
    DER Group. Each parameter is represented as a Y Value at a point in time or on a curve
    as a function of time, which is represented on the X axis."""

    __slots__ = (
        "_der_curve_data",
        "_dispatch_schedule",
        "_end_device_group",
        "der_parameter",
        "flow_direction",
        "y_multiplier",
        "y_unit",
        "y_unit_installed_max",
        "y_unit_installed_min",
    )

    der_parameter: DERParameterKind | None
    y_multiplier: UnitMultiplier | None
    y_unit: DERUnitSymbol | None
    y_unit_installed_max: float | None
    y_unit_installed_min: float | None
    flow_direction: FlowDirectionKind | None

    der_curve_data: One[DERCurveData] = One(
        EndMeta(
            name="der_curve_data",
            cim_role="DERCurveData",
            target="cim_python_sdk.model.iec61968.der.der_curve_data:DERCurveData",
            many=False,
            lower=0,
            upper=1,
            inverse="der_monitorable_parameter",
            aggregation="none",
        )
    )
    end_device_group: Many[EndDeviceGroup] = Many(
        EndMeta(
            name="end_device_group",
            cim_role="EndDeviceGroup",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="der_monitorable_parameter",
            aggregation="none",
        )
    )
    dispatch_schedule: Many[DispatchSchedule] = Many(
        EndMeta(
            name="dispatch_schedule",
            cim_role="DispatchSchedule",
            target="cim_python_sdk.model.iec61968.der.dispatch_schedule:DispatchSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="der_monitorable_parameter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DERMonitorableParameter",
        package="TC57CIM/IEC61968/DER",
        guid="{369FEE00-ABA6-424d-B6F7-7C1D777F5D8E}",
        attributes=(
            AttrMeta("der_parameter", "DERParameter", "DERParameterKind", 0, 1, "enumeration"),
            AttrMeta("y_multiplier", "yMultiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("y_unit", "yUnit", "DERUnitSymbol", 0, 1, "enumeration"),
            AttrMeta("y_unit_installed_max", "yUnitInstalledMax", "float", 0, 1, "primitive"),
            AttrMeta("y_unit_installed_min", "yUnitInstalledMin", "float", 0, 1, "primitive"),
            AttrMeta("flow_direction", "flowDirection", "FlowDirectionKind", 1, 1, "enumeration"),
        ),
        ends=(
            der_curve_data.meta,
            end_device_group.meta,
            dispatch_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        der_parameter: DERParameterKind | None = None,
        y_multiplier: UnitMultiplier | None = None,
        y_unit: DERUnitSymbol | None = None,
        y_unit_installed_max: float | None = None,
        y_unit_installed_min: float | None = None,
        flow_direction: FlowDirectionKind | None = None,
        der_curve_data: DERCurveData | None = None,
        end_device_group: Iterable[EndDeviceGroup] | None = None,
        dispatch_schedule: Iterable[DispatchSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.der_parameter = der_parameter
        self.y_multiplier = y_multiplier
        self.y_unit = y_unit
        self.y_unit_installed_max = y_unit_installed_max
        self.y_unit_installed_min = y_unit_installed_min
        self.flow_direction = flow_direction
        if der_curve_data is not None:
            self.der_curve_data = der_curve_data
        if end_device_group is not None:
            DERMonitorableParameter.end_device_group.extend(self, end_device_group)
        if dispatch_schedule is not None:
            DERMonitorableParameter.dispatch_schedule.extend(self, dispatch_schedule)

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERMonitorableParameter.end_device_group.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERMonitorableParameter.end_device_group.remove(self, end_device_group)

    def clear_end_device_group(self) -> Self:
        return DERMonitorableParameter.end_device_group.clear(self)

    def num_end_device_group(self) -> int:
        return DERMonitorableParameter.end_device_group.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return DERMonitorableParameter.end_device_group.get_by_mrid(self, mrid)

    def add_dispatch_schedule(self, dispatch_schedule: DispatchSchedule) -> Self:
        return DERMonitorableParameter.dispatch_schedule.add(self, dispatch_schedule)

    def remove_dispatch_schedule(self, dispatch_schedule: DispatchSchedule) -> Self:
        return DERMonitorableParameter.dispatch_schedule.remove(self, dispatch_schedule)

    def clear_dispatch_schedule(self) -> Self:
        return DERMonitorableParameter.dispatch_schedule.clear(self)

    def num_dispatch_schedule(self) -> int:
        return DERMonitorableParameter.dispatch_schedule.count(self)
