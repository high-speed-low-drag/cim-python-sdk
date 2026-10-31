"""CIM class HydroGeneratingUnit (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import GeneratingUnit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.hydro_turbine_kind import (
        HydroTurbineKind,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.hydro_energy_conversion_kind import (
        HydroEnergyConversionKind,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_efficiency_curve import (
        HydroGeneratingEfficiencyCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.hydro_power_plant import (
        HydroPowerPlant,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.penstock_loss_curve import (
        PenstockLossCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.tailbay_loss_curve import (
        TailbayLossCurve,
    )


class HydroGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton,
    Kaplan)."""

    __slots__ = (
        "_hydro_generating_efficiency_curves",
        "_hydro_power_plant",
        "_penstock_loss_curve",
        "_tailbay_loss_curve",
        "drop_height",
        "energy_conversion_capability",
        "hydro_unit_water_cost",
        "turbine_type",
    )

    energy_conversion_capability: HydroEnergyConversionKind | None
    hydro_unit_water_cost: float | None  # CostPerVolume
    drop_height: float | None  # Length
    turbine_type: HydroTurbineKind | None

    penstock_loss_curve: One[PenstockLossCurve] = One(
        EndMeta(
            name="penstock_loss_curve",
            cim_role="PenstockLossCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.penstock_loss_curve:PenstockLossCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="hydro_generating_unit",
            aggregation="shared",
        )
    )
    hydro_generating_efficiency_curves: Many[HydroGeneratingEfficiencyCurve] = Many(
        EndMeta(
            name="hydro_generating_efficiency_curves",
            cim_role="HydroGeneratingEfficiencyCurves",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_generating_efficiency_curve:HydroGeneratingEfficiencyCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="hydro_generating_unit",
            aggregation="shared",
        )
    )
    hydro_power_plant: One[HydroPowerPlant] = One(
        EndMeta(
            name="hydro_power_plant",
            cim_role="HydroPowerPlant",
            target="cim_python_sdk.model.iec61970.base.generation.production.hydro_power_plant:HydroPowerPlant",
            many=False,
            lower=0,
            upper=1,
            inverse="hydro_generating_units",
            aggregation="none",
        )
    )
    tailbay_loss_curve: Many[TailbayLossCurve] = Many(
        EndMeta(
            name="tailbay_loss_curve",
            cim_role="TailbayLossCurve",
            target="cim_python_sdk.model.iec61970.base.generation.production.tailbay_loss_curve:TailbayLossCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="hydro_generating_unit",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HydroGeneratingUnit",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{2B8CC296-5CEF-4662-9FB2-48F968B7C3D9}",
        attributes=(
            AttrMeta(
                "energy_conversion_capability",
                "energyConversionCapability",
                "HydroEnergyConversionKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "hydro_unit_water_cost", "hydroUnitWaterCost", "CostPerVolume", 0, 1, "cimdatatype"
            ),
            AttrMeta("drop_height", "dropHeight", "Length", 0, 1, "cimdatatype"),
            AttrMeta("turbine_type", "turbineType", "HydroTurbineKind", 0, 1, "enumeration"),
        ),
        ends=(
            penstock_loss_curve.meta,
            hydro_generating_efficiency_curves.meta,
            hydro_power_plant.meta,
            tailbay_loss_curve.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_conversion_capability: HydroEnergyConversionKind | None = None,
        hydro_unit_water_cost: float | None = None,
        drop_height: float | None = None,
        turbine_type: HydroTurbineKind | None = None,
        penstock_loss_curve: PenstockLossCurve | None = None,
        hydro_generating_efficiency_curves: Iterable[HydroGeneratingEfficiencyCurve] | None = None,
        hydro_power_plant: HydroPowerPlant | None = None,
        tailbay_loss_curve: Iterable[TailbayLossCurve] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.energy_conversion_capability = energy_conversion_capability
        self.hydro_unit_water_cost = hydro_unit_water_cost
        self.drop_height = drop_height
        self.turbine_type = turbine_type
        if penstock_loss_curve is not None:
            self.penstock_loss_curve = penstock_loss_curve
        if hydro_generating_efficiency_curves is not None:
            HydroGeneratingUnit.hydro_generating_efficiency_curves.extend(
                self, hydro_generating_efficiency_curves
            )
        if hydro_power_plant is not None:
            self.hydro_power_plant = hydro_power_plant
        if tailbay_loss_curve is not None:
            HydroGeneratingUnit.tailbay_loss_curve.extend(self, tailbay_loss_curve)

    def add_hydro_generating_efficiency_curve(
        self, hydro_generating_efficiency_curve: HydroGeneratingEfficiencyCurve
    ) -> Self:
        return HydroGeneratingUnit.hydro_generating_efficiency_curves.add(
            self, hydro_generating_efficiency_curve
        )

    def remove_hydro_generating_efficiency_curve(
        self, hydro_generating_efficiency_curve: HydroGeneratingEfficiencyCurve
    ) -> Self:
        return HydroGeneratingUnit.hydro_generating_efficiency_curves.remove(
            self, hydro_generating_efficiency_curve
        )

    def clear_hydro_generating_efficiency_curves(self) -> Self:
        return HydroGeneratingUnit.hydro_generating_efficiency_curves.clear(self)

    def num_hydro_generating_efficiency_curve(self) -> int:
        return HydroGeneratingUnit.hydro_generating_efficiency_curves.count(self)

    def get_hydro_generating_efficiency_curve_by_mrid(
        self, mrid: str
    ) -> HydroGeneratingEfficiencyCurve | None:
        return HydroGeneratingUnit.hydro_generating_efficiency_curves.get_by_mrid(self, mrid)

    def add_tailbay_loss_curve(self, tailbay_loss_curve: TailbayLossCurve) -> Self:
        return HydroGeneratingUnit.tailbay_loss_curve.add(self, tailbay_loss_curve)

    def remove_tailbay_loss_curve(self, tailbay_loss_curve: TailbayLossCurve) -> Self:
        return HydroGeneratingUnit.tailbay_loss_curve.remove(self, tailbay_loss_curve)

    def clear_tailbay_loss_curve(self) -> Self:
        return HydroGeneratingUnit.tailbay_loss_curve.clear(self)

    def num_tailbay_loss_curve(self) -> int:
        return HydroGeneratingUnit.tailbay_loss_curve.count(self)

    def get_tailbay_loss_curve_by_mrid(self, mrid: str) -> TailbayLossCurve | None:
        return HydroGeneratingUnit.tailbay_loss_curve.get_by_mrid(self, mrid)
