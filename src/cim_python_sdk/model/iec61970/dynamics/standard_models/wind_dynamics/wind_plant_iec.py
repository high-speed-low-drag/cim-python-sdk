"""CIM class WindPlantIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_dynamics import (
    WindPlantDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_freq_pcontrol_iec import (
        WindPlantFreqPcontrolIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_reactive_control_iec import (
        WindPlantReactiveControlIEC,
    )


class WindPlantIEC(WindPlantDynamics):
    """Simplified IEC type plant level model.

    Reference: IEC 61400-27-1:2015, Annex D."""

    __slots__ = ("_wind_plant_freq_pcontrol_iec", "_wind_plant_reactive_control_iec")

    wind_plant_reactive_control_iec: One[WindPlantReactiveControlIEC] = One(
        EndMeta(
            name="wind_plant_reactive_control_iec",
            cim_role="WindPlantReactiveControlIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_reactive_control_iec:WindPlantReactiveControlIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_plant_iec",
            aggregation="none",
        )
    )
    wind_plant_freq_pcontrol_iec: One[WindPlantFreqPcontrolIEC] = One(
        EndMeta(
            name="wind_plant_freq_pcontrol_iec",
            cim_role="WindPlantFreqPcontrolIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_freq_pcontrol_iec:WindPlantFreqPcontrolIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_plant_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindPlantIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{0DBB7A33-19DB-41a4-952D-ECB797036597}",
        ends=(
            wind_plant_reactive_control_iec.meta,
            wind_plant_freq_pcontrol_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_plant_reactive_control_iec: WindPlantReactiveControlIEC | None = None,
        wind_plant_freq_pcontrol_iec: WindPlantFreqPcontrolIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_plant_reactive_control_iec is not None:
            self.wind_plant_reactive_control_iec = wind_plant_reactive_control_iec
        if wind_plant_freq_pcontrol_iec is not None:
            self.wind_plant_freq_pcontrol_iec = wind_plant_freq_pcontrol_iec
