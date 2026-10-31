"""CIM class UnderexcitationLimiterDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
        ExcitationSystemDynamics,
    )


class UnderexcitationLimiterDynamics(DynamicsFunctionBlock):
    """Underexcitation limiter function block whose behaviour is described by reference to a
    standard model or by definition of a user-defined model."""

    __slots__ = ("_excitation_system_dynamics", "_remote_input_signal")

    excitation_system_dynamics: One[ExcitationSystemDynamics] = One(
        EndMeta(
            name="excitation_system_dynamics",
            cim_role="ExcitationSystemDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics:ExcitationSystemDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="underexcitation_limiter_dynamics",
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
            inverse="underexcitation_limiter_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UnderexcitationLimiterDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/UnderexcitationLimiterDynamics",
        guid="{C765F8F2-EACC-46ac-8EC1-62B38E9A38FF}",
        ends=(
            excitation_system_dynamics.meta,
            remote_input_signal.meta,
        ),
    )

    def __init__(
        self,
        *,
        excitation_system_dynamics: ExcitationSystemDynamics | None = None,
        remote_input_signal: RemoteInputSignal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if excitation_system_dynamics is not None:
            self.excitation_system_dynamics = excitation_system_dynamics
        if remote_input_signal is not None:
            self.remote_input_signal = remote_input_signal
