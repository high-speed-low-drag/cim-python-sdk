"""CIM class TurbineGovernorDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics import (
        AsynchronousMachineDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
        SynchronousMachineDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_load_controller_dynamics.turbine_load_controller_dynamics import (
        TurbineLoadControllerDynamics,
    )


class TurbineGovernorDynamics(DynamicsFunctionBlock):
    """Turbine-governor function block whose behaviour is described by reference to a standard
    model or by definition of a user-defined model."""

    __slots__ = (
        "_asynchronous_machine_dynamics",
        "_synchronous_machine_dynamics",
        "_turbine_load_controller_dynamics",
    )

    turbine_load_controller_dynamics: One[TurbineLoadControllerDynamics] = One(
        EndMeta(
            name="turbine_load_controller_dynamics",
            cim_role="TurbineLoadControllerDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_load_controller_dynamics.turbine_load_controller_dynamics:TurbineLoadControllerDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="turbine_governor_dynamics",
            aggregation="none",
        )
    )
    asynchronous_machine_dynamics: One[AsynchronousMachineDynamics] = One(
        EndMeta(
            name="asynchronous_machine_dynamics",
            cim_role="AsynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics:AsynchronousMachineDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="turbine_governor_dynamics",
            aggregation="none",
        )
    )
    synchronous_machine_dynamics: One[SynchronousMachineDynamics] = One(
        EndMeta(
            name="synchronous_machine_dynamics",
            cim_role="SynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics:SynchronousMachineDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="turbine_governor_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TurbineGovernorDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{C759C48A-48F3-4038-8572-625367012530}",
        ends=(
            turbine_load_controller_dynamics.meta,
            asynchronous_machine_dynamics.meta,
            synchronous_machine_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        turbine_load_controller_dynamics: TurbineLoadControllerDynamics | None = None,
        asynchronous_machine_dynamics: AsynchronousMachineDynamics | None = None,
        synchronous_machine_dynamics: SynchronousMachineDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if turbine_load_controller_dynamics is not None:
            self.turbine_load_controller_dynamics = turbine_load_controller_dynamics
        if asynchronous_machine_dynamics is not None:
            self.asynchronous_machine_dynamics = asynchronous_machine_dynamics
        if synchronous_machine_dynamics is not None:
            self.synchronous_machine_dynamics = synchronous_machine_dynamics
