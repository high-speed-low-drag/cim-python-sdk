"""CIM class TurbineLoadControllerDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineLoadControllerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
        TurbineGovernorDynamics,
    )


class TurbineLoadControllerDynamics(DynamicsFunctionBlock):
    """Turbine load controller function block whose behaviour is described by reference to a
    standard model or by definition of a user-defined model."""

    __slots__ = ("_turbine_governor_dynamics",)

    turbine_governor_dynamics: One[TurbineGovernorDynamics] = One(
        EndMeta(
            name="turbine_governor_dynamics",
            cim_role="TurbineGovernorDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics:TurbineGovernorDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="turbine_load_controller_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TurbineLoadControllerDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineLoadControllerDynamics",
        guid="{7BB91FE6-FE5C-4ee6-B5BD-B2D092F8AFD9}",
        ends=(turbine_governor_dynamics.meta,),
    )

    def __init__(
        self,
        *,
        turbine_governor_dynamics: TurbineGovernorDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if turbine_governor_dynamics is not None:
            self.turbine_governor_dynamics = turbine_governor_dynamics
