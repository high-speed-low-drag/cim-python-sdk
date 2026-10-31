"""CIM class WindTurbineType3or4IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_dynamics import (
    WindTurbineType3or4Dynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_curr_lim_iec import (
        WindContCurrLimIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_q_lim_iec import (
        WindContQLimIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_qiec import (
        WindContQIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_qpqu_lim_iec import (
        WindContQPQULimIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_protection_iec import (
        WindProtectionIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_ref_frame_rot_iec import (
        WindRefFrameRotIEC,
    )


class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """Parent class supporting relationships to IEC wind turbines type 3 and type 4 including
    their control models."""

    __slots__ = (
        "_w_ind_cont_qiec",
        "_wind_cont_curr_lim_iec",
        "_wind_cont_q_lim_iec",
        "_wind_cont_qpqu_lim_iec",
        "_wind_protection_iec",
        "_wind_ref_frame_rot_iec",
    )

    wind_cont_q_lim_iec: One[WindContQLimIEC] = One(
        EndMeta(
            name="wind_cont_q_lim_iec",
            cim_role="WindContQLimIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_q_lim_iec:WindContQLimIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type3or4_iec",
            aggregation="none",
        )
    )
    wind_ref_frame_rot_iec: One[WindRefFrameRotIEC] = One(
        EndMeta(
            name="wind_ref_frame_rot_iec",
            cim_role="WindRefFrameRotIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_ref_frame_rot_iec:WindRefFrameRotIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3or4_iec",
            aggregation="none",
        )
    )
    w_ind_cont_qiec: One[WindContQIEC] = One(
        EndMeta(
            name="w_ind_cont_qiec",
            cim_role="WIndContQIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_qiec:WindContQIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3or4_iec",
            aggregation="none",
        )
    )
    wind_protection_iec: One[WindProtectionIEC] = One(
        EndMeta(
            name="wind_protection_iec",
            cim_role="WindProtectionIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_protection_iec:WindProtectionIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3or4_iec",
            aggregation="none",
        )
    )
    wind_cont_curr_lim_iec: One[WindContCurrLimIEC] = One(
        EndMeta(
            name="wind_cont_curr_lim_iec",
            cim_role="WindContCurrLimIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_curr_lim_iec:WindContCurrLimIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3or4_iec",
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
            inverse="wind_turbine_type3or4_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType3or4IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{BF659CC1-2596-4e28-AF74-C5177DDE557E}",
        ends=(
            wind_cont_q_lim_iec.meta,
            wind_ref_frame_rot_iec.meta,
            w_ind_cont_qiec.meta,
            wind_protection_iec.meta,
            wind_cont_curr_lim_iec.meta,
            wind_cont_qpqu_lim_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_cont_q_lim_iec: WindContQLimIEC | None = None,
        wind_ref_frame_rot_iec: WindRefFrameRotIEC | None = None,
        w_ind_cont_qiec: WindContQIEC | None = None,
        wind_protection_iec: WindProtectionIEC | None = None,
        wind_cont_curr_lim_iec: WindContCurrLimIEC | None = None,
        wind_cont_qpqu_lim_iec: WindContQPQULimIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_cont_q_lim_iec is not None:
            self.wind_cont_q_lim_iec = wind_cont_q_lim_iec
        if wind_ref_frame_rot_iec is not None:
            self.wind_ref_frame_rot_iec = wind_ref_frame_rot_iec
        if w_ind_cont_qiec is not None:
            self.w_ind_cont_qiec = w_ind_cont_qiec
        if wind_protection_iec is not None:
            self.wind_protection_iec = wind_protection_iec
        if wind_cont_curr_lim_iec is not None:
            self.wind_cont_curr_lim_iec = wind_cont_curr_lim_iec
        if wind_cont_qpqu_lim_iec is not None:
            self.wind_cont_qpqu_lim_iec = wind_cont_qpqu_lim_iec
