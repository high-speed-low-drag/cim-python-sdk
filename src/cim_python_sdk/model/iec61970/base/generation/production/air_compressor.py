"""CIM class AirCompressor (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.combustion_turbine import (
        CombustionTurbine,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.caes_plant import CAESPlant


class AirCompressor(PowerSystemResource):
    """Combustion turbine air compressor which is an integral part of a compressed air energy
    storage (CAES) plant."""

    __slots__ = ("_caes_plant", "_combustion_turbine", "air_compressor_rating")

    air_compressor_rating: float | None

    caes_plant: One[CAESPlant] = One(
        EndMeta(
            name="caes_plant",
            cim_role="CAESPlant",
            target="cim_python_sdk.model.iec61970.base.generation.production.caes_plant:CAESPlant",
            many=False,
            lower=1,
            upper=1,
            inverse="air_compressor",
            aggregation="none",
        )
    )
    combustion_turbine: One[CombustionTurbine] = One(
        EndMeta(
            name="combustion_turbine",
            cim_role="CombustionTurbine",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.combustion_turbine:CombustionTurbine",
            many=False,
            lower=1,
            upper=1,
            inverse="air_compressor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AirCompressor",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{3620E654-094D-4422-8417-E50ADEF99CAB}",
        attributes=(
            AttrMeta("air_compressor_rating", "airCompressorRating", "float", 0, 1, "primitive"),
        ),
        ends=(
            caes_plant.meta,
            combustion_turbine.meta,
        ),
    )

    def __init__(
        self,
        *,
        air_compressor_rating: float | None = None,
        caes_plant: CAESPlant | None = None,
        combustion_turbine: CombustionTurbine | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.air_compressor_rating = air_compressor_rating
        if caes_plant is not None:
            self.caes_plant = caes_plant
        if combustion_turbine is not None:
            self.combustion_turbine = combustion_turbine
