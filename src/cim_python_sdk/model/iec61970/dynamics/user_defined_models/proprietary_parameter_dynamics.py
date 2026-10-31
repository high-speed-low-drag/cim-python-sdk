"""CIM class ProprietaryParameterDynamics (TC57CIM/IEC61970/Dynamics/UserDefinedModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.asynchronous_machine_user_defined import (
        AsynchronousMachineUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.csc_user_defined import (
        CSCUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.discontinuous_excitation_control_user_defined import (
        DiscontinuousExcitationControlUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.excitation_system_user_defined import (
        ExcitationSystemUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.load_user_defined import (
        LoadUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.mechanical_load_user_defined import (
        MechanicalLoadUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.overexcitation_limiter_user_defined import (
        OverexcitationLimiterUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.pfv_ar_controller_type1_user_defined import (
        PFVArControllerType1UserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.pfv_ar_controller_type2_user_defined import (
        PFVArControllerType2UserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.power_system_stabilizer_user_defined import (
        PowerSystemStabilizerUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.svc_user_defined import (
        SVCUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.synchronous_machine_user_defined import (
        SynchronousMachineUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.turbine_governor_user_defined import (
        TurbineGovernorUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.turbine_load_controller_user_defined import (
        TurbineLoadControllerUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.underexcitation_limiter_user_defined import (
        UnderexcitationLimiterUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.voltage_adjuster_user_defined import (
        VoltageAdjusterUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.voltage_compensator_user_defined import (
        VoltageCompensatorUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.vsc_user_defined import (
        VSCUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.wind_plant_user_defined import (
        WindPlantUserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.wind_type1or2_user_defined import (
        WindType1or2UserDefined,
    )
    from cim_python_sdk.model.iec61970.dynamics.user_defined_models.wind_type3or4_user_defined import (
        WindType3or4UserDefined,
    )


class ProprietaryParameterDynamics(CimObject):
    """Supports definition of one or more parameters of several different datatypes for use by
    proprietary user-defined models.

    This class does not inherit from IdentifiedObject since it is not intended that a single
    instance of it be referenced by more than one proprietary user-defined model instance."""

    __slots__ = (
        "_asynchronous_machine_user_defined",
        "_csc_user_defined",
        "_discontinuous_excitation_control_user_defined",
        "_excitation_system_user_defined",
        "_load_user_defined",
        "_mechanical_load_user_defined",
        "_overexcitation_limiter_user_defined",
        "_pfv_ar_controller_type1_user_defined",
        "_pfv_ar_controller_type2_user_defined",
        "_power_system_stabilizer_user_defined",
        "_svc_user_defined",
        "_synchronous_machine_user_defined",
        "_turbine_governor_user_defined",
        "_turbine_load_controller_user_defined",
        "_underexcitation_limiter_user_defined",
        "_voltage_adjuster_user_defined",
        "_voltage_compensator_user_defined",
        "_vsc_user_defined",
        "_wind_plant_user_defined",
        "_wind_type1or2_user_defined",
        "_wind_type3or4_user_defined",
        "boolean_parameter_value",
        "float_parameter_value",
        "integer_parameter_value",
        "parameter_number",
    )

    parameter_number: int | None
    boolean_parameter_value: bool | None
    integer_parameter_value: int | None
    float_parameter_value: float | None

    svc_user_defined: One[SVCUserDefined] = One(
        EndMeta(
            name="svc_user_defined",
            cim_role="SVCUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.svc_user_defined:SVCUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    mechanical_load_user_defined: One[MechanicalLoadUserDefined] = One(
        EndMeta(
            name="mechanical_load_user_defined",
            cim_role="MechanicalLoadUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.mechanical_load_user_defined:MechanicalLoadUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    pfv_ar_controller_type2_user_defined: One[PFVArControllerType2UserDefined] = One(
        EndMeta(
            name="pfv_ar_controller_type2_user_defined",
            cim_role="PFVArControllerType2UserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.pfv_ar_controller_type2_user_defined:PFVArControllerType2UserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    discontinuous_excitation_control_user_defined: One[
        DiscontinuousExcitationControlUserDefined
    ] = One(
        EndMeta(
            name="discontinuous_excitation_control_user_defined",
            cim_role="DiscontinuousExcitationControlUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.discontinuous_excitation_control_user_defined:DiscontinuousExcitationControlUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    load_user_defined: One[LoadUserDefined] = One(
        EndMeta(
            name="load_user_defined",
            cim_role="LoadUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.load_user_defined:LoadUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    excitation_system_user_defined: One[ExcitationSystemUserDefined] = One(
        EndMeta(
            name="excitation_system_user_defined",
            cim_role="ExcitationSystemUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.excitation_system_user_defined:ExcitationSystemUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    power_system_stabilizer_user_defined: One[PowerSystemStabilizerUserDefined] = One(
        EndMeta(
            name="power_system_stabilizer_user_defined",
            cim_role="PowerSystemStabilizerUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.power_system_stabilizer_user_defined:PowerSystemStabilizerUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    wind_type3or4_user_defined: One[WindType3or4UserDefined] = One(
        EndMeta(
            name="wind_type3or4_user_defined",
            cim_role="WindType3or4UserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.wind_type3or4_user_defined:WindType3or4UserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    overexcitation_limiter_user_defined: One[OverexcitationLimiterUserDefined] = One(
        EndMeta(
            name="overexcitation_limiter_user_defined",
            cim_role="OverexcitationLimiterUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.overexcitation_limiter_user_defined:OverexcitationLimiterUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    pfv_ar_controller_type1_user_defined: One[PFVArControllerType1UserDefined] = One(
        EndMeta(
            name="pfv_ar_controller_type1_user_defined",
            cim_role="PFVArControllerType1UserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.pfv_ar_controller_type1_user_defined:PFVArControllerType1UserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    wind_type1or2_user_defined: One[WindType1or2UserDefined] = One(
        EndMeta(
            name="wind_type1or2_user_defined",
            cim_role="WindType1or2UserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.wind_type1or2_user_defined:WindType1or2UserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    voltage_compensator_user_defined: One[VoltageCompensatorUserDefined] = One(
        EndMeta(
            name="voltage_compensator_user_defined",
            cim_role="VoltageCompensatorUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.voltage_compensator_user_defined:VoltageCompensatorUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    wind_plant_user_defined: One[WindPlantUserDefined] = One(
        EndMeta(
            name="wind_plant_user_defined",
            cim_role="WindPlantUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.wind_plant_user_defined:WindPlantUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    synchronous_machine_user_defined: One[SynchronousMachineUserDefined] = One(
        EndMeta(
            name="synchronous_machine_user_defined",
            cim_role="SynchronousMachineUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.synchronous_machine_user_defined:SynchronousMachineUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    vsc_user_defined: One[VSCUserDefined] = One(
        EndMeta(
            name="vsc_user_defined",
            cim_role="VSCUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.vsc_user_defined:VSCUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    turbine_load_controller_user_defined: One[TurbineLoadControllerUserDefined] = One(
        EndMeta(
            name="turbine_load_controller_user_defined",
            cim_role="TurbineLoadControllerUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.turbine_load_controller_user_defined:TurbineLoadControllerUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    underexcitation_limiter_user_defined: One[UnderexcitationLimiterUserDefined] = One(
        EndMeta(
            name="underexcitation_limiter_user_defined",
            cim_role="UnderexcitationLimiterUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.underexcitation_limiter_user_defined:UnderexcitationLimiterUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    csc_user_defined: One[CSCUserDefined] = One(
        EndMeta(
            name="csc_user_defined",
            cim_role="CSCUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.csc_user_defined:CSCUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    asynchronous_machine_user_defined: One[AsynchronousMachineUserDefined] = One(
        EndMeta(
            name="asynchronous_machine_user_defined",
            cim_role="AsynchronousMachineUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.asynchronous_machine_user_defined:AsynchronousMachineUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    voltage_adjuster_user_defined: One[VoltageAdjusterUserDefined] = One(
        EndMeta(
            name="voltage_adjuster_user_defined",
            cim_role="VoltageAdjusterUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.voltage_adjuster_user_defined:VoltageAdjusterUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )
    turbine_governor_user_defined: One[TurbineGovernorUserDefined] = One(
        EndMeta(
            name="turbine_governor_user_defined",
            cim_role="TurbineGovernorUserDefined",
            target="cim_python_sdk.model.iec61970.dynamics.user_defined_models.turbine_governor_user_defined:TurbineGovernorUserDefined",
            many=False,
            lower=0,
            upper=1,
            inverse="proprietary_parameter_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProprietaryParameterDynamics",
        package="TC57CIM/IEC61970/Dynamics/UserDefinedModels",
        guid="{511A476A-15FF-4c1e-A02D-348B2843D4D5}",
        attributes=(
            AttrMeta("parameter_number", "parameterNumber", "int", 0, 1, "primitive"),
            AttrMeta("boolean_parameter_value", "booleanParameterValue", "bool", 0, 1, "primitive"),
            AttrMeta("integer_parameter_value", "integerParameterValue", "int", 0, 1, "primitive"),
            AttrMeta("float_parameter_value", "floatParameterValue", "float", 0, 1, "primitive"),
        ),
        ends=(
            svc_user_defined.meta,
            mechanical_load_user_defined.meta,
            pfv_ar_controller_type2_user_defined.meta,
            discontinuous_excitation_control_user_defined.meta,
            load_user_defined.meta,
            excitation_system_user_defined.meta,
            power_system_stabilizer_user_defined.meta,
            wind_type3or4_user_defined.meta,
            overexcitation_limiter_user_defined.meta,
            pfv_ar_controller_type1_user_defined.meta,
            wind_type1or2_user_defined.meta,
            voltage_compensator_user_defined.meta,
            wind_plant_user_defined.meta,
            synchronous_machine_user_defined.meta,
            vsc_user_defined.meta,
            turbine_load_controller_user_defined.meta,
            underexcitation_limiter_user_defined.meta,
            csc_user_defined.meta,
            asynchronous_machine_user_defined.meta,
            voltage_adjuster_user_defined.meta,
            turbine_governor_user_defined.meta,
        ),
    )

    def __init__(
        self,
        *,
        parameter_number: int | None = None,
        boolean_parameter_value: bool | None = None,
        integer_parameter_value: int | None = None,
        float_parameter_value: float | None = None,
        svc_user_defined: SVCUserDefined | None = None,
        mechanical_load_user_defined: MechanicalLoadUserDefined | None = None,
        pfv_ar_controller_type2_user_defined: PFVArControllerType2UserDefined | None = None,
        discontinuous_excitation_control_user_defined: DiscontinuousExcitationControlUserDefined
        | None = None,
        load_user_defined: LoadUserDefined | None = None,
        excitation_system_user_defined: ExcitationSystemUserDefined | None = None,
        power_system_stabilizer_user_defined: PowerSystemStabilizerUserDefined | None = None,
        wind_type3or4_user_defined: WindType3or4UserDefined | None = None,
        overexcitation_limiter_user_defined: OverexcitationLimiterUserDefined | None = None,
        pfv_ar_controller_type1_user_defined: PFVArControllerType1UserDefined | None = None,
        wind_type1or2_user_defined: WindType1or2UserDefined | None = None,
        voltage_compensator_user_defined: VoltageCompensatorUserDefined | None = None,
        wind_plant_user_defined: WindPlantUserDefined | None = None,
        synchronous_machine_user_defined: SynchronousMachineUserDefined | None = None,
        vsc_user_defined: VSCUserDefined | None = None,
        turbine_load_controller_user_defined: TurbineLoadControllerUserDefined | None = None,
        underexcitation_limiter_user_defined: UnderexcitationLimiterUserDefined | None = None,
        csc_user_defined: CSCUserDefined | None = None,
        asynchronous_machine_user_defined: AsynchronousMachineUserDefined | None = None,
        voltage_adjuster_user_defined: VoltageAdjusterUserDefined | None = None,
        turbine_governor_user_defined: TurbineGovernorUserDefined | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.parameter_number = parameter_number
        self.boolean_parameter_value = boolean_parameter_value
        self.integer_parameter_value = integer_parameter_value
        self.float_parameter_value = float_parameter_value
        if svc_user_defined is not None:
            self.svc_user_defined = svc_user_defined
        if mechanical_load_user_defined is not None:
            self.mechanical_load_user_defined = mechanical_load_user_defined
        if pfv_ar_controller_type2_user_defined is not None:
            self.pfv_ar_controller_type2_user_defined = pfv_ar_controller_type2_user_defined
        if discontinuous_excitation_control_user_defined is not None:
            self.discontinuous_excitation_control_user_defined = (
                discontinuous_excitation_control_user_defined
            )
        if load_user_defined is not None:
            self.load_user_defined = load_user_defined
        if excitation_system_user_defined is not None:
            self.excitation_system_user_defined = excitation_system_user_defined
        if power_system_stabilizer_user_defined is not None:
            self.power_system_stabilizer_user_defined = power_system_stabilizer_user_defined
        if wind_type3or4_user_defined is not None:
            self.wind_type3or4_user_defined = wind_type3or4_user_defined
        if overexcitation_limiter_user_defined is not None:
            self.overexcitation_limiter_user_defined = overexcitation_limiter_user_defined
        if pfv_ar_controller_type1_user_defined is not None:
            self.pfv_ar_controller_type1_user_defined = pfv_ar_controller_type1_user_defined
        if wind_type1or2_user_defined is not None:
            self.wind_type1or2_user_defined = wind_type1or2_user_defined
        if voltage_compensator_user_defined is not None:
            self.voltage_compensator_user_defined = voltage_compensator_user_defined
        if wind_plant_user_defined is not None:
            self.wind_plant_user_defined = wind_plant_user_defined
        if synchronous_machine_user_defined is not None:
            self.synchronous_machine_user_defined = synchronous_machine_user_defined
        if vsc_user_defined is not None:
            self.vsc_user_defined = vsc_user_defined
        if turbine_load_controller_user_defined is not None:
            self.turbine_load_controller_user_defined = turbine_load_controller_user_defined
        if underexcitation_limiter_user_defined is not None:
            self.underexcitation_limiter_user_defined = underexcitation_limiter_user_defined
        if csc_user_defined is not None:
            self.csc_user_defined = csc_user_defined
        if asynchronous_machine_user_defined is not None:
            self.asynchronous_machine_user_defined = asynchronous_machine_user_defined
        if voltage_adjuster_user_defined is not None:
            self.voltage_adjuster_user_defined = voltage_adjuster_user_defined
        if turbine_governor_user_defined is not None:
            self.turbine_governor_user_defined = turbine_governor_user_defined
