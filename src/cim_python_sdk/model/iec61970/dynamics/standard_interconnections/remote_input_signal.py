"""CIM class RemoteInputSignal (TC57CIM/IEC61970/Dynamics/StandardInterconnections). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_signal_kind import (
        RemoteSignalKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.discontinuous_excitation_control_dynamics.discontinuous_excitation_control_dynamics import (
        DiscontinuousExcitationControlDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics import (
        PFVArControllerType1Dynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
        PowerSystemStabilizerDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.underexcitation_limiter_dynamics.underexcitation_limiter_dynamics import (
        UnderexcitationLimiterDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.voltage_compensator_dynamics import (
        VoltageCompensatorDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_dynamics import (
        WindPlantDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_dynamics import (
        WindTurbineType1or2Dynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_dynamics import (
        WindTurbineType3or4Dynamics,
    )


class RemoteInputSignal(IdentifiedObject):
    """Supports connection to a terminal associated with a remote bus from which an input
    signal of a specific type is coming."""

    __slots__ = (
        "_discontinuous_excitation_control_dynamics",
        "_pfv_ar_controller_type1_dynamics",
        "_power_system_stabilizer_dynamics",
        "_terminal",
        "_underexcitation_limiter_dynamics",
        "_voltage_compensator_dynamics",
        "_wind_plant_dynamics",
        "_wind_turbine_type1or2_dynamics",
        "_wind_turbine_type3or4_dynamics",
        "remote_signal_type",
    )

    remote_signal_type: RemoteSignalKind | None

    pfv_ar_controller_type1_dynamics: One[PFVArControllerType1Dynamics] = One(
        EndMeta(
            name="pfv_ar_controller_type1_dynamics",
            cim_role="PFVArControllerType1Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics:PFVArControllerType1Dynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="remote_input_signal",
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
            inverse="remote_input_signal",
            aggregation="none",
        )
    )
    wind_turbine_type3or4_dynamics: One[WindTurbineType3or4Dynamics] = One(
        EndMeta(
            name="wind_turbine_type3or4_dynamics",
            cim_role="WindTurbineType3or4Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_dynamics:WindTurbineType3or4Dynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="remote_input_signal",
            aggregation="none",
        )
    )
    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="remote_input_signal",
            aggregation="none",
        )
    )
    wind_turbine_type1or2_dynamics: One[WindTurbineType1or2Dynamics] = One(
        EndMeta(
            name="wind_turbine_type1or2_dynamics",
            cim_role="WindTurbineType1or2Dynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_dynamics:WindTurbineType1or2Dynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="remote_input_signal",
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
            inverse="remote_input_signal",
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
            inverse="remote_input_signal",
            aggregation="none",
        )
    )
    wind_plant_dynamics: One[WindPlantDynamics] = One(
        EndMeta(
            name="wind_plant_dynamics",
            cim_role="WindPlantDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_dynamics:WindPlantDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="remote_input_signal",
            aggregation="none",
        )
    )
    voltage_compensator_dynamics: One[VoltageCompensatorDynamics] = One(
        EndMeta(
            name="voltage_compensator_dynamics",
            cim_role="VoltageCompensatorDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.voltage_compensator_dynamics:VoltageCompensatorDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="remote_input_signal",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RemoteInputSignal",
        package="TC57CIM/IEC61970/Dynamics/StandardInterconnections",
        guid="{4343E844-5BAF-4175-9144-8319CA06EF02}",
        attributes=(
            AttrMeta(
                "remote_signal_type", "remoteSignalType", "RemoteSignalKind", 0, 1, "enumeration"
            ),
        ),
        ends=(
            pfv_ar_controller_type1_dynamics.meta,
            power_system_stabilizer_dynamics.meta,
            wind_turbine_type3or4_dynamics.meta,
            terminal.meta,
            wind_turbine_type1or2_dynamics.meta,
            discontinuous_excitation_control_dynamics.meta,
            underexcitation_limiter_dynamics.meta,
            wind_plant_dynamics.meta,
            voltage_compensator_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        remote_signal_type: RemoteSignalKind | None = None,
        pfv_ar_controller_type1_dynamics: PFVArControllerType1Dynamics | None = None,
        power_system_stabilizer_dynamics: PowerSystemStabilizerDynamics | None = None,
        wind_turbine_type3or4_dynamics: WindTurbineType3or4Dynamics | None = None,
        terminal: Terminal | None = None,
        wind_turbine_type1or2_dynamics: WindTurbineType1or2Dynamics | None = None,
        discontinuous_excitation_control_dynamics: DiscontinuousExcitationControlDynamics
        | None = None,
        underexcitation_limiter_dynamics: UnderexcitationLimiterDynamics | None = None,
        wind_plant_dynamics: WindPlantDynamics | None = None,
        voltage_compensator_dynamics: VoltageCompensatorDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.remote_signal_type = remote_signal_type
        if pfv_ar_controller_type1_dynamics is not None:
            self.pfv_ar_controller_type1_dynamics = pfv_ar_controller_type1_dynamics
        if power_system_stabilizer_dynamics is not None:
            self.power_system_stabilizer_dynamics = power_system_stabilizer_dynamics
        if wind_turbine_type3or4_dynamics is not None:
            self.wind_turbine_type3or4_dynamics = wind_turbine_type3or4_dynamics
        if terminal is not None:
            self.terminal = terminal
        if wind_turbine_type1or2_dynamics is not None:
            self.wind_turbine_type1or2_dynamics = wind_turbine_type1or2_dynamics
        if discontinuous_excitation_control_dynamics is not None:
            self.discontinuous_excitation_control_dynamics = (
                discontinuous_excitation_control_dynamics
            )
        if underexcitation_limiter_dynamics is not None:
            self.underexcitation_limiter_dynamics = underexcitation_limiter_dynamics
        if wind_plant_dynamics is not None:
            self.wind_plant_dynamics = wind_plant_dynamics
        if voltage_compensator_dynamics is not None:
            self.voltage_compensator_dynamics = voltage_compensator_dynamics
