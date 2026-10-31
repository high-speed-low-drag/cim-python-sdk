"""CIM class DERFunction (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup


class DERFunction(CimObject):
    """Specifies the list of functions that are supported."""

    __slots__ = (
        "_end_device_group",
        "_end_device_group_der_function",
        "connect_disconnect",
        "frequency_watt_curve_function",
        "max_real_power_limiting",
        "ramp_rate_control",
        "reactive_power_dispatch",
        "real_power_dispatch",
        "volt_var_curve_function",
        "volt_watt_curve_function",
        "voltage_regulation",
    )

    real_power_dispatch: bool | None
    reactive_power_dispatch: bool | None
    max_real_power_limiting: bool | None
    ramp_rate_control: bool | None
    voltage_regulation: bool | None
    volt_var_curve_function: bool | None
    volt_watt_curve_function: bool | None
    frequency_watt_curve_function: bool | None
    connect_disconnect: bool | None

    end_device_group: Many[EndDeviceGroup] = Many(
        EndMeta(
            name="end_device_group",
            cim_role="EndDeviceGroup",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="der_function",
            aggregation="none",
        )
    )
    end_device_group_der_function: One[EndDeviceGroup] = One(
        EndMeta(
            name="end_device_group_der_function",
            cim_role="EndDeviceGroup",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="der_function_end_device_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DERFunction",
        package="TC57CIM/IEC61968/DER",
        guid="{247CC932-35C1-4d1d-8085-29AE0CEBD920}",
        attributes=(
            AttrMeta("real_power_dispatch", "realPowerDispatch", "bool", 0, 1, "primitive"),
            AttrMeta("reactive_power_dispatch", "reactivePowerDispatch", "bool", 0, 1, "primitive"),
            AttrMeta("max_real_power_limiting", "maxRealPowerLimiting", "bool", 0, 1, "primitive"),
            AttrMeta("ramp_rate_control", "rampRateControl", "bool", 0, 1, "primitive"),
            AttrMeta("voltage_regulation", "voltageRegulation", "bool", 0, 1, "primitive"),
            AttrMeta("volt_var_curve_function", "voltVarCurveFunction", "bool", 0, 1, "primitive"),
            AttrMeta(
                "volt_watt_curve_function", "voltWattCurveFunction", "bool", 0, 1, "primitive"
            ),
            AttrMeta(
                "frequency_watt_curve_function",
                "frequencyWattCurveFunction",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta("connect_disconnect", "connectDisconnect", "bool", 0, 1, "primitive"),
        ),
        ends=(
            end_device_group.meta,
            end_device_group_der_function.meta,
        ),
    )

    def __init__(
        self,
        *,
        real_power_dispatch: bool | None = None,
        reactive_power_dispatch: bool | None = None,
        max_real_power_limiting: bool | None = None,
        ramp_rate_control: bool | None = None,
        voltage_regulation: bool | None = None,
        volt_var_curve_function: bool | None = None,
        volt_watt_curve_function: bool | None = None,
        frequency_watt_curve_function: bool | None = None,
        connect_disconnect: bool | None = None,
        end_device_group: Iterable[EndDeviceGroup] | None = None,
        end_device_group_der_function: EndDeviceGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.real_power_dispatch = real_power_dispatch
        self.reactive_power_dispatch = reactive_power_dispatch
        self.max_real_power_limiting = max_real_power_limiting
        self.ramp_rate_control = ramp_rate_control
        self.voltage_regulation = voltage_regulation
        self.volt_var_curve_function = volt_var_curve_function
        self.volt_watt_curve_function = volt_watt_curve_function
        self.frequency_watt_curve_function = frequency_watt_curve_function
        self.connect_disconnect = connect_disconnect
        if end_device_group is not None:
            DERFunction.end_device_group.extend(self, end_device_group)
        if end_device_group_der_function is not None:
            self.end_device_group_der_function = end_device_group_der_function

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERFunction.end_device_group.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERFunction.end_device_group.remove(self, end_device_group)

    def clear_end_device_group(self) -> Self:
        return DERFunction.end_device_group.clear(self)

    def num_end_device_group(self) -> int:
        return DERFunction.end_device_group.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return DERFunction.end_device_group.get_by_mrid(self, mrid)
