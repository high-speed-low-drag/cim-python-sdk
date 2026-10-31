"""CIM class PFVArControllerType2Dynamics (TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType2Dynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
        ExcitationSystemDynamics,
    )


class PFVArControllerType2Dynamics(DynamicsFunctionBlock):
    """Power factor or VAr controller type 2 function block whose behaviour is described by
    reference to a standard model or by definition of a user-defined model."""

    __slots__ = ("_excitation_system_dynamics",)

    excitation_system_dynamics: One[ExcitationSystemDynamics] = One(
        EndMeta(
            name="excitation_system_dynamics",
            cim_role="ExcitationSystemDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics:ExcitationSystemDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="pfv_ar_controller_type2_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PFVArControllerType2Dynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType2Dynamics",
        guid="{D476F3FB-EC19-45d0-99B2-3B218BC1481B}",
        ends=(excitation_system_dynamics.meta,),
    )

    def __init__(
        self,
        *,
        excitation_system_dynamics: ExcitationSystemDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if excitation_system_dynamics is not None:
            self.excitation_system_dynamics = excitation_system_dynamics
