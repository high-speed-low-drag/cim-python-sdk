"""CIM class StaticVarCompensatorDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/StaticVarCompensatorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.static_var_compensator import StaticVarCompensator


class StaticVarCompensatorDynamics(DynamicsFunctionBlock):
    """Static var compensator whose behaviour is described by reference to a standard model or
    by definition of a user-defined model."""

    __slots__ = ("_static_var_compensator",)

    static_var_compensator: One[StaticVarCompensator] = One(
        EndMeta(
            name="static_var_compensator",
            cim_role="StaticVarCompensator",
            target="cim_python_sdk.model.iec61970.base.wires.static_var_compensator:StaticVarCompensator",
            many=False,
            lower=1,
            upper=1,
            inverse="static_var_compensator_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StaticVarCompensatorDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/StaticVarCompensatorDynamics",
        guid="{B979A376-AE67-4798-8E61-A1745649B242}",
        ends=(static_var_compensator.meta,),
    )

    def __init__(
        self,
        *,
        static_var_compensator: StaticVarCompensator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if static_var_compensator is not None:
            self.static_var_compensator = static_var_compensator
