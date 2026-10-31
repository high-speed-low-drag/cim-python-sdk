"""CIM class PFVArControllerType1Dynamics (TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType1Dynamics). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_adjuster_dynamics.voltage_adjuster_dynamics import (
        VoltageAdjusterDynamics,
    )


class PFVArControllerType1Dynamics(DynamicsFunctionBlock):
    """Power factor or VAr controller type 1 function block whose behaviour is described by
    reference to a standard model or by definition of a user-defined model."""

    __slots__ = (
        "_excitation_system_dynamics",
        "_remote_input_signal",
        "_voltage_adjuster_dynamics",
    )

    remote_input_signal: One[RemoteInputSignal] = One(
        EndMeta(
            name="remote_input_signal",
            cim_role="RemoteInputSignal",
            target="cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal:RemoteInputSignal",
            many=False,
            lower=0,
            upper=1,
            inverse="pfv_ar_controller_type1_dynamics",
            aggregation="none",
        )
    )
    voltage_adjuster_dynamics: One[VoltageAdjusterDynamics] = One(
        EndMeta(
            name="voltage_adjuster_dynamics",
            cim_role="VoltageAdjusterDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_adjuster_dynamics.voltage_adjuster_dynamics:VoltageAdjusterDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="pfv_ar_controller_type1_dynamics",
            aggregation="none",
        )
    )
    excitation_system_dynamics: One[ExcitationSystemDynamics] = One(
        EndMeta(
            name="excitation_system_dynamics",
            cim_role="ExcitationSystemDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics:ExcitationSystemDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="pfv_ar_controller_type1_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PFVArControllerType1Dynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType1Dynamics",
        guid="{1880F77A-765D-4759-AE22-1E43ED912C81}",
        ends=(
            remote_input_signal.meta,
            voltage_adjuster_dynamics.meta,
            excitation_system_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        remote_input_signal: RemoteInputSignal | None = None,
        voltage_adjuster_dynamics: VoltageAdjusterDynamics | None = None,
        excitation_system_dynamics: ExcitationSystemDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if remote_input_signal is not None:
            self.remote_input_signal = remote_input_signal
        if voltage_adjuster_dynamics is not None:
            self.voltage_adjuster_dynamics = voltage_adjuster_dynamics
        if excitation_system_dynamics is not None:
            self.excitation_system_dynamics = excitation_system_dynamics
