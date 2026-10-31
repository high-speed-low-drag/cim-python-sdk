"""CIM class ProportionalDistributionComponent (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_component import EnergyComponent

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ProportionalDistributionComponent(EnergyComponent):
    """CIM class ProportionalDistributionComponent."""

    __slots__ = ("distribution_factor",)

    distribution_factor: float | None  # ActivePower

    _cim_meta = ClassMeta(
        cim_name="ProportionalDistributionComponent",
        package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
        guid="{29EE59D5-E1CE-4420-9A89-7C93996DBBA2}",
        attributes=(
            AttrMeta(
                "distribution_factor", "distributionFactor", "ActivePower", 0, 1, "cimdatatype"
            ),
        ),
    )

    def __init__(
        self,
        *,
        distribution_factor: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.distribution_factor = distribution_factor
