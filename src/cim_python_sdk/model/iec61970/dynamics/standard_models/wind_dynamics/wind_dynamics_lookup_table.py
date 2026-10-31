"""CIM class WindDynamicsLookupTable (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_curr_lim_iec import (
        WindContCurrLimIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type3_iec import (
        WindContPType3IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_qpqu_lim_iec import (
        WindContQPQULimIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_rotor_riec import (
        WindContRotorRIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3b_iec import (
        WindGenType3bIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_lookup_table_function_kind import (
        WindLookupTableFunctionKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_pitch_cont_power_iec import (
        WindPitchContPowerIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_freq_pcontrol_iec import (
        WindPlantFreqPcontrolIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_reactive_control_iec import (
        WindPlantReactiveControlIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_protection_iec import (
        WindProtectionIEC,
    )


class WindDynamicsLookupTable(IdentifiedObject):
    """Look up table for the purpose of wind standard models."""

    __slots__ = (
        "_wind_cont_curr_lim_iec",
        "_wind_cont_p_type3_iec",
        "_wind_cont_qpqu_lim_iec",
        "_wind_cont_rotor_riec",
        "_wind_gen_type3b_iec",
        "_wind_pitch_cont_power_iec",
        "_wind_plant_freq_pcontrol_iec",
        "_wind_plant_reactive_control_iec",
        "_wind_protection_iec",
        "input",
        "lookup_table_function_type",
        "output",
        "sequence",
    )

    input: float | None
    lookup_table_function_type: WindLookupTableFunctionKind | None
    output: float | None
    sequence: int | None

    wind_gen_type3b_iec: One[WindGenType3bIEC] = One(
        EndMeta(
            name="wind_gen_type3b_iec",
            cim_role="WindGenType3bIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3b_iec:WindGenType3bIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_plant_freq_pcontrol_iec: One[WindPlantFreqPcontrolIEC] = One(
        EndMeta(
            name="wind_plant_freq_pcontrol_iec",
            cim_role="WindPlantFreqPcontrolIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_freq_pcontrol_iec:WindPlantFreqPcontrolIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_plant_reactive_control_iec: One[WindPlantReactiveControlIEC] = One(
        EndMeta(
            name="wind_plant_reactive_control_iec",
            cim_role="WindPlantReactiveControlIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_reactive_control_iec:WindPlantReactiveControlIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_cont_p_type3_iec: One[WindContPType3IEC] = One(
        EndMeta(
            name="wind_cont_p_type3_iec",
            cim_role="WindContPType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type3_iec:WindContPType3IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_pitch_cont_power_iec: One[WindPitchContPowerIEC] = One(
        EndMeta(
            name="wind_pitch_cont_power_iec",
            cim_role="WindPitchContPowerIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_pitch_cont_power_iec:WindPitchContPowerIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_cont_curr_lim_iec: One[WindContCurrLimIEC] = One(
        EndMeta(
            name="wind_cont_curr_lim_iec",
            cim_role="WindContCurrLimIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_curr_lim_iec:WindContCurrLimIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_cont_qpqu_lim_iec: One[WindContQPQULimIEC] = One(
        EndMeta(
            name="wind_cont_qpqu_lim_iec",
            cim_role="WindContQPQULimIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_qpqu_lim_iec:WindContQPQULimIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_protection_iec: One[WindProtectionIEC] = One(
        EndMeta(
            name="wind_protection_iec",
            cim_role="WindProtectionIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_protection_iec:WindProtectionIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )
    wind_cont_rotor_riec: One[WindContRotorRIEC] = One(
        EndMeta(
            name="wind_cont_rotor_riec",
            cim_role="WindContRotorRIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_rotor_riec:WindContRotorRIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_dynamics_lookup_table",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindDynamicsLookupTable",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{E76DF2A3-865B-4280-9AA3-FCE228118FE8}",
        attributes=(
            AttrMeta("input", "input", "float", 0, 1, "primitive"),
            AttrMeta(
                "lookup_table_function_type",
                "lookupTableFunctionType",
                "WindLookupTableFunctionKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("output", "output", "float", 0, 1, "primitive"),
            AttrMeta("sequence", "sequence", "int", 0, 1, "primitive"),
        ),
        ends=(
            wind_gen_type3b_iec.meta,
            wind_plant_freq_pcontrol_iec.meta,
            wind_plant_reactive_control_iec.meta,
            wind_cont_p_type3_iec.meta,
            wind_pitch_cont_power_iec.meta,
            wind_cont_curr_lim_iec.meta,
            wind_cont_qpqu_lim_iec.meta,
            wind_protection_iec.meta,
            wind_cont_rotor_riec.meta,
        ),
    )

    def __init__(
        self,
        *,
        input: float | None = None,
        lookup_table_function_type: WindLookupTableFunctionKind | None = None,
        output: float | None = None,
        sequence: int | None = None,
        wind_gen_type3b_iec: WindGenType3bIEC | None = None,
        wind_plant_freq_pcontrol_iec: WindPlantFreqPcontrolIEC | None = None,
        wind_plant_reactive_control_iec: WindPlantReactiveControlIEC | None = None,
        wind_cont_p_type3_iec: WindContPType3IEC | None = None,
        wind_pitch_cont_power_iec: WindPitchContPowerIEC | None = None,
        wind_cont_curr_lim_iec: WindContCurrLimIEC | None = None,
        wind_cont_qpqu_lim_iec: WindContQPQULimIEC | None = None,
        wind_protection_iec: WindProtectionIEC | None = None,
        wind_cont_rotor_riec: WindContRotorRIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.input = input
        self.lookup_table_function_type = lookup_table_function_type
        self.output = output
        self.sequence = sequence
        if wind_gen_type3b_iec is not None:
            self.wind_gen_type3b_iec = wind_gen_type3b_iec
        if wind_plant_freq_pcontrol_iec is not None:
            self.wind_plant_freq_pcontrol_iec = wind_plant_freq_pcontrol_iec
        if wind_plant_reactive_control_iec is not None:
            self.wind_plant_reactive_control_iec = wind_plant_reactive_control_iec
        if wind_cont_p_type3_iec is not None:
            self.wind_cont_p_type3_iec = wind_cont_p_type3_iec
        if wind_pitch_cont_power_iec is not None:
            self.wind_pitch_cont_power_iec = wind_pitch_cont_power_iec
        if wind_cont_curr_lim_iec is not None:
            self.wind_cont_curr_lim_iec = wind_cont_curr_lim_iec
        if wind_cont_qpqu_lim_iec is not None:
            self.wind_cont_qpqu_lim_iec = wind_cont_qpqu_lim_iec
        if wind_protection_iec is not None:
            self.wind_protection_iec = wind_protection_iec
        if wind_cont_rotor_riec is not None:
            self.wind_cont_rotor_riec = wind_cont_rotor_riec
