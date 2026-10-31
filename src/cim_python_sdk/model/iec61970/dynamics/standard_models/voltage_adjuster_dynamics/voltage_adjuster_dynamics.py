"""CIM class VoltageAdjusterDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/VoltageAdjusterDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics import (
        PFVArControllerType1Dynamics,
    )


class VoltageAdjusterDynamics(DynamicsFunctionBlock):
    """Voltage adjuster function block whose behaviour is described by reference to a standard
    model or by definition of a user-defined model."""

    __slots__ = ("_pfv_ar_controller_type1_dynamics",)

    pfv_ar_controller_type1_dynamics: One[PFVArControllerType1Dynamics] = One(
        EndMeta(
            name="pfv_ar_controller_type1_dynamics",
            cim_role="PFVArControllerType1Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics:PFVArControllerType1Dynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="voltage_adjuster_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VoltageAdjusterDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/VoltageAdjusterDynamics",
        guid="{89A3B646-0C4E-4f77-8B82-4C638EE1A451}",
        ends=(pfv_ar_controller_type1_dynamics.meta,),
    )

    def __init__(
        self,
        *,
        pfv_ar_controller_type1_dynamics: PFVArControllerType1Dynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if pfv_ar_controller_type1_dynamics is not None:
            self.pfv_ar_controller_type1_dynamics = pfv_ar_controller_type1_dynamics
