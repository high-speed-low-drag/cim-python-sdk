"""CIM compound RemoteConnectDisconnectInfo (TC57CIM/IEC61968/LoadControl). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class RemoteConnectDisconnectInfo(CimCompound):
    """Details of remote connect and disconnect function."""

    __slots__ = (
        "armed_timeout",
        "customer_voltage_limit",
        "energy_limit",
        "energy_usage_start_date_time",
        "energy_usage_warning",
        "is_arm_connect",
        "is_arm_disconnect",
        "is_energy_limiting",
        "needs_power_limit_check",
        "needs_voltage_limit_check",
        "power_limit",
        "use_pushbutton",
    )

    is_arm_connect: bool | None
    is_arm_disconnect: bool | None
    armed_timeout: float | None  # Seconds
    needs_voltage_limit_check: bool | None
    needs_power_limit_check: bool | None
    customer_voltage_limit: float | None  # Voltage
    power_limit: float | None  # ActivePower
    use_pushbutton: bool | None
    is_energy_limiting: bool | None
    energy_limit: float | None  # RealEnergy
    energy_usage_warning: float | None  # RealEnergy
    energy_usage_start_date_time: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="RemoteConnectDisconnectInfo",
        package="TC57CIM/IEC61968/LoadControl",
        guid="{83F01164-7557-4707-A39A-7A840EC61796}",
        kind="compound",
        attributes=(
            AttrMeta("is_arm_connect", "isArmConnect", "bool", 0, 1, "primitive"),
            AttrMeta("is_arm_disconnect", "isArmDisconnect", "bool", 0, 1, "primitive"),
            AttrMeta("armed_timeout", "armedTimeout", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta(
                "needs_voltage_limit_check", "needsVoltageLimitCheck", "bool", 0, 1, "primitive"
            ),
            AttrMeta("needs_power_limit_check", "needsPowerLimitCheck", "bool", 0, 1, "primitive"),
            AttrMeta(
                "customer_voltage_limit", "customerVoltageLimit", "Voltage", 0, 1, "cimdatatype"
            ),
            AttrMeta("power_limit", "powerLimit", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("use_pushbutton", "usePushbutton", "bool", 0, 1, "primitive"),
            AttrMeta("is_energy_limiting", "isEnergyLimiting", "bool", 0, 1, "primitive"),
            AttrMeta("energy_limit", "energyLimit", "RealEnergy", 0, 1, "cimdatatype"),
            AttrMeta(
                "energy_usage_warning", "energyUsageWarning", "RealEnergy", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "energy_usage_start_date_time",
                "energyUsageStartDateTime",
                "datetime",
                0,
                1,
                "primitive",
            ),
        ),
    )
