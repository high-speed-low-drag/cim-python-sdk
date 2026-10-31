"""CIM class PowerQualityPricing (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PowerQualityPricing(Document):
    """Pricing can be based on power quality."""

    __slots__ = (
        "emergency_high_volt_limit",
        "emergency_low_volt_limit",
        "normal_high_volt_limit",
        "normal_low_volt_limit",
        "power_factor_min",
        "value_uninterrupted_service_energy",
        "value_uninterrupted_service_p",
        "volt_imbalance_viol_cost",
        "volt_limit_viol_cost",
    )

    emergency_high_volt_limit: float | None  # Voltage
    emergency_low_volt_limit: float | None  # Voltage
    normal_high_volt_limit: float | None  # Voltage
    normal_low_volt_limit: float | None  # Voltage
    power_factor_min: float | None
    value_uninterrupted_service_energy: float | None  # CostPerEnergyUnit
    value_uninterrupted_service_p: float | None
    volt_imbalance_viol_cost: float | None
    volt_limit_viol_cost: float | None

    _cim_meta = ClassMeta(
        cim_name="PowerQualityPricing",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{90C89F99-E6E7-4b81-8D3C-3070C9E7853D}",
        attributes=(
            AttrMeta(
                "emergency_high_volt_limit",
                "emergencyHighVoltLimit",
                "Voltage",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "emergency_low_volt_limit", "emergencyLowVoltLimit", "Voltage", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "normal_high_volt_limit", "normalHighVoltLimit", "Voltage", 0, 1, "cimdatatype"
            ),
            AttrMeta("normal_low_volt_limit", "normalLowVoltLimit", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("power_factor_min", "powerFactorMin", "float", 0, 1, "primitive"),
            AttrMeta(
                "value_uninterrupted_service_energy",
                "valueUninterruptedServiceEnergy",
                "CostPerEnergyUnit",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "value_uninterrupted_service_p",
                "valueUninterruptedServiceP",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta(
                "volt_imbalance_viol_cost", "voltImbalanceViolCost", "float", 0, 1, "primitive"
            ),
            AttrMeta("volt_limit_viol_cost", "voltLimitViolCost", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        emergency_high_volt_limit: float | None = None,
        emergency_low_volt_limit: float | None = None,
        normal_high_volt_limit: float | None = None,
        normal_low_volt_limit: float | None = None,
        power_factor_min: float | None = None,
        value_uninterrupted_service_energy: float | None = None,
        value_uninterrupted_service_p: float | None = None,
        volt_imbalance_viol_cost: float | None = None,
        volt_limit_viol_cost: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.emergency_high_volt_limit = emergency_high_volt_limit
        self.emergency_low_volt_limit = emergency_low_volt_limit
        self.normal_high_volt_limit = normal_high_volt_limit
        self.normal_low_volt_limit = normal_low_volt_limit
        self.power_factor_min = power_factor_min
        self.value_uninterrupted_service_energy = value_uninterrupted_service_energy
        self.value_uninterrupted_service_p = value_uninterrupted_service_p
        self.volt_imbalance_viol_cost = volt_imbalance_viol_cost
        self.volt_limit_viol_cost = volt_limit_viol_cost
