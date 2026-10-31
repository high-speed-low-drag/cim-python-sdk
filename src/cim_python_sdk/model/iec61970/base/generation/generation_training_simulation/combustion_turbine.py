"""CIM class CombustionTurbine (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.prime_mover import (
    PrimeMover,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.ct_temp_active_power_curve import (
        CTTempActivePowerCurve,
    )
    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.heat_recovery_boiler import (
        HeatRecoveryBoiler,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.air_compressor import (
        AirCompressor,
    )


class CombustionTurbine(PrimeMover):
    """A prime mover that is typically fuelled by gas or light oil."""

    __slots__ = (
        "_air_compressor",
        "_ct_temp_active_power_curve",
        "_heat_recovery_boiler",
        "ambient_temp",
        "aux_power_versus_frequency",
        "aux_power_versus_voltage",
        "capability_versus_frequency",
        "heat_recovery_flag",
        "power_variation_by_temp",
        "reference_temp",
        "time_constant",
    )

    ambient_temp: float | None  # Temperature
    aux_power_versus_frequency: float | None  # PU
    aux_power_versus_voltage: float | None  # PU
    capability_versus_frequency: float | None  # PU
    heat_recovery_flag: bool | None
    power_variation_by_temp: float | None  # PU
    reference_temp: float | None  # Temperature
    time_constant: float | None  # Seconds

    ct_temp_active_power_curve: One[CTTempActivePowerCurve] = One(
        EndMeta(
            name="ct_temp_active_power_curve",
            cim_role="CTTempActivePowerCurve",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.ct_temp_active_power_curve:CTTempActivePowerCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="combustion_turbine",
            aggregation="shared",
        )
    )
    heat_recovery_boiler: One[HeatRecoveryBoiler] = One(
        EndMeta(
            name="heat_recovery_boiler",
            cim_role="HeatRecoveryBoiler",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.heat_recovery_boiler:HeatRecoveryBoiler",
            many=False,
            lower=0,
            upper=1,
            inverse="combustion_turbines",
            aggregation="none",
        )
    )
    air_compressor: One[AirCompressor] = One(
        EndMeta(
            name="air_compressor",
            cim_role="AirCompressor",
            target="cim_python_sdk.model.iec61970.base.generation.production.air_compressor:AirCompressor",
            many=False,
            lower=0,
            upper=1,
            inverse="combustion_turbine",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CombustionTurbine",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{9BCFB807-2761-4db7-A0E1-66D834951CB1}",
        attributes=(
            AttrMeta("ambient_temp", "ambientTemp", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta(
                "aux_power_versus_frequency", "auxPowerVersusFrequency", "PU", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "aux_power_versus_voltage", "auxPowerVersusVoltage", "PU", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "capability_versus_frequency",
                "capabilityVersusFrequency",
                "PU",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("heat_recovery_flag", "heatRecoveryFlag", "bool", 0, 1, "primitive"),
            AttrMeta("power_variation_by_temp", "powerVariationByTemp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("reference_temp", "referenceTemp", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("time_constant", "timeConstant", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(
            ct_temp_active_power_curve.meta,
            heat_recovery_boiler.meta,
            air_compressor.meta,
        ),
    )

    def __init__(
        self,
        *,
        ambient_temp: float | None = None,
        aux_power_versus_frequency: float | None = None,
        aux_power_versus_voltage: float | None = None,
        capability_versus_frequency: float | None = None,
        heat_recovery_flag: bool | None = None,
        power_variation_by_temp: float | None = None,
        reference_temp: float | None = None,
        time_constant: float | None = None,
        ct_temp_active_power_curve: CTTempActivePowerCurve | None = None,
        heat_recovery_boiler: HeatRecoveryBoiler | None = None,
        air_compressor: AirCompressor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ambient_temp = ambient_temp
        self.aux_power_versus_frequency = aux_power_versus_frequency
        self.aux_power_versus_voltage = aux_power_versus_voltage
        self.capability_versus_frequency = capability_versus_frequency
        self.heat_recovery_flag = heat_recovery_flag
        self.power_variation_by_temp = power_variation_by_temp
        self.reference_temp = reference_temp
        self.time_constant = time_constant
        if ct_temp_active_power_curve is not None:
            self.ct_temp_active_power_curve = ct_temp_active_power_curve
        if heat_recovery_boiler is not None:
            self.heat_recovery_boiler = heat_recovery_boiler
        if air_compressor is not None:
            self.air_compressor = air_compressor
