"""CIM class WindTurbineType1or2IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_dynamics import (
    WindTurbineType1or2Dynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_mech_iec import (
        WindMechIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_protection_iec import (
        WindProtectionIEC,
    )


class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """Parent class supporting relationships to IEC wind turbines type 1 and type 2 including
    their control models.

    Generator model for wind turbine of IEC type 1 or type 2 is a standard asynchronous
    generator model.

    Reference: IEC 61400-27-1:2015, 5.5.2 and 5.5.3."""

    __slots__ = ("_wind_mech_iec", "_wind_protection_iec")

    wind_mech_iec: One[WindMechIEC] = One(
        EndMeta(
            name="wind_mech_iec",
            cim_role="WindMechIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_mech_iec:WindMechIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type1or2_iec",
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
            inverse="wind_turbine_type1or2_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType1or2IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{44103F96-CF13-4b64-8875-501A162C4388}",
        ends=(
            wind_mech_iec.meta,
            wind_protection_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_mech_iec: WindMechIEC | None = None,
        wind_protection_iec: WindProtectionIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_mech_iec is not None:
            self.wind_mech_iec = wind_mech_iec
        if wind_protection_iec is not None:
            self.wind_protection_iec = wind_protection_iec
