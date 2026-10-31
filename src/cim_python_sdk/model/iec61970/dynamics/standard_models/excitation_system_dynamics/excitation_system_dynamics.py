"""CIM class ExcitationSystemDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.discontinuous_excitation_control_dynamics.discontinuous_excitation_control_dynamics import (
        DiscontinuousExcitationControlDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.overexcitation_limiter_dynamics.overexcitation_limiter_dynamics import (
        OverexcitationLimiterDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics import (
        PFVArControllerType1Dynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type2_dynamics.pfv_ar_controller_type2_dynamics import (
        PFVArControllerType2Dynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
        PowerSystemStabilizerDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
        SynchronousMachineDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics import (
        UnderexcitationLimiterDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.voltage_compensator_dynamics import (
        VoltageCompensatorDynamics,
    )


class ExcitationSystemDynamics(DynamicsFunctionBlock):
    """Excitation system function block whose behaviour is described by reference to a standard
    model or by definition of a user-defined model."""

    __slots__ = (
        "_discontinuous_excitation_control_dynamics",
        "_overexcitation_limiter_dynamics",
        "_pfv_ar_controller_type1_dynamics",
        "_pfv_ar_controller_type2_dynamics",
        "_power_system_stabilizer_dynamics",
        "_synchronous_machine_dynamics",
        "_underexcitation_limiter_dynamics",
        "_voltage_compensator_dynamics",
    )

    voltage_compensator_dynamics: One[VoltageCompensatorDynamics] = One(
        EndMeta(
            name="voltage_compensator_dynamics",
            cim_role="VoltageCompensatorDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.voltage_compensator_dynamics:VoltageCompensatorDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )
    underexcitation_limiter_dynamics: One[UnderexcitationLimiterDynamics] = One(
        EndMeta(
            name="underexcitation_limiter_dynamics",
            cim_role="UnderexcitationLimiterDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics:UnderexcitationLimiterDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )
    pfv_ar_controller_type2_dynamics: One[PFVArControllerType2Dynamics] = One(
        EndMeta(
            name="pfv_ar_controller_type2_dynamics",
            cim_role="PFVArControllerType2Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type2_dynamics.pfv_ar_controller_type2_dynamics:PFVArControllerType2Dynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )
    discontinuous_excitation_control_dynamics: One[DiscontinuousExcitationControlDynamics] = One(
        EndMeta(
            name="discontinuous_excitation_control_dynamics",
            cim_role="DiscontinuousExcitationControlDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.discontinuous_excitation_control_dynamics.discontinuous_excitation_control_dynamics:DiscontinuousExcitationControlDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )
    overexcitation_limiter_dynamics: One[OverexcitationLimiterDynamics] = One(
        EndMeta(
            name="overexcitation_limiter_dynamics",
            cim_role="OverexcitationLimiterDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.overexcitation_limiter_dynamics.overexcitation_limiter_dynamics:OverexcitationLimiterDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )
    pfv_ar_controller_type1_dynamics: One[PFVArControllerType1Dynamics] = One(
        EndMeta(
            name="pfv_ar_controller_type1_dynamics",
            cim_role="PFVArControllerType1Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics:PFVArControllerType1Dynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )
    synchronous_machine_dynamics: One[SynchronousMachineDynamics] = One(
        EndMeta(
            name="synchronous_machine_dynamics",
            cim_role="SynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics:SynchronousMachineDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )
    power_system_stabilizer_dynamics: One[PowerSystemStabilizerDynamics] = One(
        EndMeta(
            name="power_system_stabilizer_dynamics",
            cim_role="PowerSystemStabilizerDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics:PowerSystemStabilizerDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="excitation_system_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ExcitationSystemDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{F119E4EC-2DC8-4801-B68B-A282AF621324}",
        ends=(
            voltage_compensator_dynamics.meta,
            underexcitation_limiter_dynamics.meta,
            pfv_ar_controller_type2_dynamics.meta,
            discontinuous_excitation_control_dynamics.meta,
            overexcitation_limiter_dynamics.meta,
            pfv_ar_controller_type1_dynamics.meta,
            synchronous_machine_dynamics.meta,
            power_system_stabilizer_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        voltage_compensator_dynamics: VoltageCompensatorDynamics | None = None,
        underexcitation_limiter_dynamics: UnderexcitationLimiterDynamics | None = None,
        pfv_ar_controller_type2_dynamics: PFVArControllerType2Dynamics | None = None,
        discontinuous_excitation_control_dynamics: DiscontinuousExcitationControlDynamics
        | None = None,
        overexcitation_limiter_dynamics: OverexcitationLimiterDynamics | None = None,
        pfv_ar_controller_type1_dynamics: PFVArControllerType1Dynamics | None = None,
        synchronous_machine_dynamics: SynchronousMachineDynamics | None = None,
        power_system_stabilizer_dynamics: PowerSystemStabilizerDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if voltage_compensator_dynamics is not None:
            self.voltage_compensator_dynamics = voltage_compensator_dynamics
        if underexcitation_limiter_dynamics is not None:
            self.underexcitation_limiter_dynamics = underexcitation_limiter_dynamics
        if pfv_ar_controller_type2_dynamics is not None:
            self.pfv_ar_controller_type2_dynamics = pfv_ar_controller_type2_dynamics
        if discontinuous_excitation_control_dynamics is not None:
            self.discontinuous_excitation_control_dynamics = (
                discontinuous_excitation_control_dynamics
            )
        if overexcitation_limiter_dynamics is not None:
            self.overexcitation_limiter_dynamics = overexcitation_limiter_dynamics
        if pfv_ar_controller_type1_dynamics is not None:
            self.pfv_ar_controller_type1_dynamics = pfv_ar_controller_type1_dynamics
        if synchronous_machine_dynamics is not None:
            self.synchronous_machine_dynamics = synchronous_machine_dynamics
        if power_system_stabilizer_dynamics is not None:
            self.power_system_stabilizer_dynamics = power_system_stabilizer_dynamics
