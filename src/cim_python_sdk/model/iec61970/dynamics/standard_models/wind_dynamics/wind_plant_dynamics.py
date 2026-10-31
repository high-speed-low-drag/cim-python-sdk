"""CIM class WindPlantDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal import (
        RemoteInputSignal,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_dynamics import (
        WindTurbineType3or4Dynamics,
    )


class WindPlantDynamics(DynamicsFunctionBlock):
    """Parent class supporting relationships to wind turbines type 3 and type 4 and wind plant
    IEC and user-defined wind plants including their control models."""

    __slots__ = ("_remote_input_signal", "_wind_turbine_type3or4_dynamics")

    remote_input_signal: One[RemoteInputSignal] = One(
        EndMeta(
            name="remote_input_signal",
            cim_role="RemoteInputSignal",
            target="cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal:RemoteInputSignal",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_plant_dynamics",
            aggregation="none",
        )
    )
    wind_turbine_type3or4_dynamics: Many[WindTurbineType3or4Dynamics] = Many(
        EndMeta(
            name="wind_turbine_type3or4_dynamics",
            cim_role="WindTurbineType3or4Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_dynamics:WindTurbineType3or4Dynamics",
            many=True,
            lower=1,
            upper=None,
            inverse="wind_plant_dynamics",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindPlantDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{B60295F4-04E6-43e9-BC0E-F91F22664A67}",
        ends=(
            remote_input_signal.meta,
            wind_turbine_type3or4_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        remote_input_signal: RemoteInputSignal | None = None,
        wind_turbine_type3or4_dynamics: Iterable[WindTurbineType3or4Dynamics] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if remote_input_signal is not None:
            self.remote_input_signal = remote_input_signal
        if wind_turbine_type3or4_dynamics is not None:
            WindPlantDynamics.wind_turbine_type3or4_dynamics.extend(
                self, wind_turbine_type3or4_dynamics
            )

    def add_wind_turbine_type3or4_dynamics(
        self, wind_turbine_type3or4_dynamics: WindTurbineType3or4Dynamics
    ) -> Self:
        return WindPlantDynamics.wind_turbine_type3or4_dynamics.add(
            self, wind_turbine_type3or4_dynamics
        )

    def remove_wind_turbine_type3or4_dynamics(
        self, wind_turbine_type3or4_dynamics: WindTurbineType3or4Dynamics
    ) -> Self:
        return WindPlantDynamics.wind_turbine_type3or4_dynamics.remove(
            self, wind_turbine_type3or4_dynamics
        )

    def clear_wind_turbine_type3or4_dynamics(self) -> Self:
        return WindPlantDynamics.wind_turbine_type3or4_dynamics.clear(self)

    def num_wind_turbine_type3or4_dynamics(self) -> int:
        return WindPlantDynamics.wind_turbine_type3or4_dynamics.count(self)

    def get_wind_turbine_type3or4_dynamics_by_mrid(
        self, mrid: str
    ) -> WindTurbineType3or4Dynamics | None:
        return WindPlantDynamics.wind_turbine_type3or4_dynamics.get_by_mrid(self, mrid)
