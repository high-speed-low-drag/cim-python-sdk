"""CIM class MechanicalLoadDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/MechanicalLoadDynamics). Generated code: do not edit."""

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


class MechanicalLoadDynamics(DynamicsFunctionBlock):
    """Mechanical load function block whose behaviour is described by reference to a standard
    model or by definition of a user-defined model."""

    __slots__ = ("_asynchronous_machine_dynamics", "_synchronous_machine_dynamics")

    synchronous_machine_dynamics: One[SynchronousMachineDynamics] = One(
        EndMeta(
            name="synchronous_machine_dynamics",
            cim_role="SynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics:SynchronousMachineDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="mechanical_load_dynamics",
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
            inverse="mechanical_load_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MechanicalLoadDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/MechanicalLoadDynamics",
        guid="{3C5B6644-5E53-4330-8E77-595A2B1335DD}",
        ends=(
            synchronous_machine_dynamics.meta,
            asynchronous_machine_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        synchronous_machine_dynamics: SynchronousMachineDynamics | None = None,
        asynchronous_machine_dynamics: AsynchronousMachineDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if synchronous_machine_dynamics is not None:
            self.synchronous_machine_dynamics = synchronous_machine_dynamics
        if asynchronous_machine_dynamics is not None:
            self.asynchronous_machine_dynamics = asynchronous_machine_dynamics
