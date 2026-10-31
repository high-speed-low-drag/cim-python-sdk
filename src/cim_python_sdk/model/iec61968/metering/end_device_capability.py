"""CIM compound EndDeviceCapability (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class EndDeviceCapability(CimCompound):
    """Inherent capabilities of an end device (i.e., the functions it supports)."""

    __slots__ = (
        "autonomous_dst",
        "communication",
        "connect_disconnect",
        "demand_response",
        "electric_metering",
        "gas_metering",
        "metrology",
        "on_request_read",
        "outage_history",
        "pressure_compensation",
        "pricing_info",
        "pulse_output",
        "relays_programming",
        "reverse_flow",
        "super_compressibility_compensation",
        "temperature_compensation",
        "text_message",
        "water_metering",
    )

    reverse_flow: bool | None
    demand_response: bool | None
    metrology: bool | None
    outage_history: bool | None
    relays_programming: bool | None
    on_request_read: bool | None
    autonomous_dst: bool | None
    communication: bool | None
    connect_disconnect: bool | None
    electric_metering: bool | None
    gas_metering: bool | None
    water_metering: bool | None
    text_message: bool | None
    pricing_info: bool | None
    pulse_output: bool | None
    pressure_compensation: bool | None
    temperature_compensation: bool | None
    super_compressibility_compensation: bool | None

    _cim_meta = ClassMeta(
        cim_name="EndDeviceCapability",
        package="TC57CIM/IEC61968/Metering",
        guid="{27FAE402-A373-4580-83D4-4EF96A4F374D}",
        kind="compound",
        attributes=(
            AttrMeta("reverse_flow", "reverseFlow", "bool", 0, 1, "primitive"),
            AttrMeta("demand_response", "demandResponse", "bool", 0, 1, "primitive"),
            AttrMeta("metrology", "metrology", "bool", 0, 1, "primitive"),
            AttrMeta("outage_history", "outageHistory", "bool", 0, 1, "primitive"),
            AttrMeta("relays_programming", "relaysProgramming", "bool", 0, 1, "primitive"),
            AttrMeta("on_request_read", "onRequestRead", "bool", 0, 1, "primitive"),
            AttrMeta("autonomous_dst", "autonomousDst", "bool", 0, 1, "primitive"),
            AttrMeta("communication", "communication", "bool", 0, 1, "primitive"),
            AttrMeta("connect_disconnect", "connectDisconnect", "bool", 0, 1, "primitive"),
            AttrMeta("electric_metering", "electricMetering", "bool", 0, 1, "primitive"),
            AttrMeta("gas_metering", "gasMetering", "bool", 0, 1, "primitive"),
            AttrMeta("water_metering", "waterMetering", "bool", 0, 1, "primitive"),
            AttrMeta("text_message", "textMessage", "bool", 0, 1, "primitive"),
            AttrMeta("pricing_info", "pricingInfo", "bool", 0, 1, "primitive"),
            AttrMeta("pulse_output", "pulseOutput", "bool", 0, 1, "primitive"),
            AttrMeta("pressure_compensation", "pressureCompensation", "bool", 0, 1, "primitive"),
            AttrMeta(
                "temperature_compensation", "temperatureCompensation", "bool", 0, 1, "primitive"
            ),
            AttrMeta(
                "super_compressibility_compensation",
                "superCompressibilityCompensation",
                "bool",
                0,
                1,
                "primitive",
            ),
        ),
    )
