"""CIM class WindTurbineType3or4Dynamics (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.power_electronics_connection import (
        PowerElectronicsConnection,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal import (
        RemoteInputSignal,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_dynamics import (
        WindPlantDynamics,
    )


class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
    """Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant
    including their control models."""

    __slots__ = ("_power_electronics_connection", "_remote_input_signal", "_wind_plant_dynamics")

    power_electronics_connection: One[PowerElectronicsConnection] = One(
        EndMeta(
            name="power_electronics_connection",
            cim_role="PowerElectronicsConnection",
            target="cim_python_sdk.model.iec61970.base.wires.power_electronics_connection:PowerElectronicsConnection",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3or4_dynamics",
            aggregation="none",
        )
    )
    remote_input_signal: One[RemoteInputSignal] = One(
        EndMeta(
            name="remote_input_signal",
            cim_role="RemoteInputSignal",
            target="cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal:RemoteInputSignal",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type3or4_dynamics",
            aggregation="none",
        )
    )
    wind_plant_dynamics: One[WindPlantDynamics] = One(
        EndMeta(
            name="wind_plant_dynamics",
            cim_role="WindPlantDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_dynamics:WindPlantDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type3or4_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType3or4Dynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{6CF8DB58-B3A5-4e36-994C-F5E48304166C}",
        ends=(
            power_electronics_connection.meta,
            remote_input_signal.meta,
            wind_plant_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        power_electronics_connection: PowerElectronicsConnection | None = None,
        remote_input_signal: RemoteInputSignal | None = None,
        wind_plant_dynamics: WindPlantDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if power_electronics_connection is not None:
            self.power_electronics_connection = power_electronics_connection
        if remote_input_signal is not None:
            self.remote_input_signal = remote_input_signal
        if wind_plant_dynamics is not None:
            self.wind_plant_dynamics = wind_plant_dynamics
