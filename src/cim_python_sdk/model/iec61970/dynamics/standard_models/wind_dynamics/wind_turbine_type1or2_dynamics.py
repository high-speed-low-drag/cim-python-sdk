"""CIM class WindTurbineType1or2Dynamics (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal import (
        RemoteInputSignal,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics import (
        AsynchronousMachineDynamics,
    )


class WindTurbineType1or2Dynamics(DynamicsFunctionBlock):
    """Parent class supporting relationships to wind turbines type 1 and type 2 and their
    control models. Generator model for wind turbine of type 1 or type 2 is a standard
    asynchronous generator model."""

    __slots__ = ("_asynchronous_machine_dynamics", "_remote_input_signal")

    asynchronous_machine_dynamics: One[AsynchronousMachineDynamics] = One(
        EndMeta(
            name="asynchronous_machine_dynamics",
            cim_role="AsynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics:AsynchronousMachineDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type1or2_dynamics",
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
            inverse="wind_turbine_type1or2_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType1or2Dynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{EDAC9109-C756-4d3c-8664-FBA520860E3E}",
        ends=(
            asynchronous_machine_dynamics.meta,
            remote_input_signal.meta,
        ),
    )

    def __init__(
        self,
        *,
        asynchronous_machine_dynamics: AsynchronousMachineDynamics | None = None,
        remote_input_signal: RemoteInputSignal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if asynchronous_machine_dynamics is not None:
            self.asynchronous_machine_dynamics = asynchronous_machine_dynamics
        if remote_input_signal is not None:
            self.remote_input_signal = remote_input_signal
