"""CIM class CAESPlant (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.air_compressor import (
        AirCompressor,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class CAESPlant(PowerSystemResource):
    """Compressed air energy storage plant."""

    __slots__ = (
        "_air_compressor",
        "_thermal_generating_unit",
        "energy_storage_capacity",
        "rated_capacity_p",
    )

    energy_storage_capacity: float | None  # RealEnergy
    rated_capacity_p: float | None  # ActivePower

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=0,
            upper=1,
            inverse="caes_plant",
            aggregation="none",
        )
    )
    air_compressor: One[AirCompressor] = One(
        EndMeta(
            name="air_compressor",
            cim_role="AirCompressor",
            target="cim_python_sdk.model.iec61970.base.generation.production.air_compressor:AirCompressor",
            many=False,
            lower=1,
            upper=1,
            inverse="caes_plant",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CAESPlant",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{9B56B51B-E15A-4439-8F43-CBA3D7D29587}",
        attributes=(
            AttrMeta(
                "energy_storage_capacity",
                "energyStorageCapacity",
                "RealEnergy",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("rated_capacity_p", "ratedCapacityP", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            thermal_generating_unit.meta,
            air_compressor.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_storage_capacity: float | None = None,
        rated_capacity_p: float | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        air_compressor: AirCompressor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.energy_storage_capacity = energy_storage_capacity
        self.rated_capacity_p = rated_capacity_p
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit
        if air_compressor is not None:
            self.air_compressor = air_compressor
