"""CIM class CrossCompoundTurbineGovernorDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
        SynchronousMachineDynamics,
    )


class CrossCompoundTurbineGovernorDynamics(DynamicsFunctionBlock):
    """Turbine-governor cross-compound function block whose behaviour is described by reference
    to a standard model or by definition of a user-defined model."""

    __slots__ = (
        "_high_pressure_synchronous_machine_dynamics",
        "_low_pressure_synchronous_machine_dynamics",
    )

    high_pressure_synchronous_machine_dynamics: One[SynchronousMachineDynamics] = One(
        EndMeta(
            name="high_pressure_synchronous_machine_dynamics",
            cim_role="HighPressureSynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics:SynchronousMachineDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="cross_compound_turbine_governor_dyanmics",
            aggregation="none",
        )
    )
    low_pressure_synchronous_machine_dynamics: One[SynchronousMachineDynamics] = One(
        EndMeta(
            name="low_pressure_synchronous_machine_dynamics",
            cim_role="LowPressureSynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics:SynchronousMachineDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="cross_compound_turbine_governor_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CrossCompoundTurbineGovernorDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{9C543894-7669-4bd9-B389-C68E4C167F6E}",
        ends=(
            high_pressure_synchronous_machine_dynamics.meta,
            low_pressure_synchronous_machine_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        high_pressure_synchronous_machine_dynamics: SynchronousMachineDynamics | None = None,
        low_pressure_synchronous_machine_dynamics: SynchronousMachineDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if high_pressure_synchronous_machine_dynamics is not None:
            self.high_pressure_synchronous_machine_dynamics = (
                high_pressure_synchronous_machine_dynamics
            )
        if low_pressure_synchronous_machine_dynamics is not None:
            self.low_pressure_synchronous_machine_dynamics = (
                low_pressure_synchronous_machine_dynamics
            )
