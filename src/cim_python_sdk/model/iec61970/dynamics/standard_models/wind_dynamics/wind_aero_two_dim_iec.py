"""CIM class WindAeroTwoDimIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec import (
        WindTurbineType3IEC,
    )


class WindAeroTwoDimIEC(IdentifiedObject):
    """Two-dimensional aerodynamic model.

    Reference: IEC 61400-27-1:2015, 5.6.1.3."""

    __slots__ = (
        "_wind_turbine_type3_iec",
        "dpomega",
        "dptheta",
        "dpv1",
        "omegazero",
        "pavail",
        "thetav2",
        "thetazero",
    )

    dpomega: float | None  # PU
    dptheta: float | None  # PU
    dpv1: float | None  # PU
    omegazero: float | None  # PU
    pavail: float | None  # PU
    thetav2: float | None  # AngleDegrees
    thetazero: float | None  # AngleDegrees

    wind_turbine_type3_iec: One[WindTurbineType3IEC] = One(
        EndMeta(
            name="wind_turbine_type3_iec",
            cim_role="WindTurbineType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec:WindTurbineType3IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_aero_two_dim_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindAeroTwoDimIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{11B60FC6-8301-4c1a-90A8-2088A2DC11F0}",
        attributes=(
            AttrMeta("dpomega", "dpomega", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dptheta", "dptheta", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dpv1", "dpv1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("omegazero", "omegazero", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pavail", "pavail", "PU", 0, 1, "cimdatatype"),
            AttrMeta("thetav2", "thetav2", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("thetazero", "thetazero", "AngleDegrees", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type3_iec.meta,),
    )

    def __init__(
        self,
        *,
        dpomega: float | None = None,
        dptheta: float | None = None,
        dpv1: float | None = None,
        omegazero: float | None = None,
        pavail: float | None = None,
        thetav2: float | None = None,
        thetazero: float | None = None,
        wind_turbine_type3_iec: WindTurbineType3IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dpomega = dpomega
        self.dptheta = dptheta
        self.dpv1 = dpv1
        self.omegazero = omegazero
        self.pavail = pavail
        self.thetav2 = thetav2
        self.thetazero = thetazero
        if wind_turbine_type3_iec is not None:
            self.wind_turbine_type3_iec = wind_turbine_type3_iec
