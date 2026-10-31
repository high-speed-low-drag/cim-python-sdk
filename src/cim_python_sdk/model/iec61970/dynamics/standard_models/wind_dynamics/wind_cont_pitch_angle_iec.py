"""CIM class WindContPitchAngleIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec import (
        WindTurbineType3IEC,
    )


class WindContPitchAngleIEC(IdentifiedObject):
    """Pitch angle control model.

    Reference: IEC 61400-27-1:2015, 5.6.5.2."""

    __slots__ = (
        "_wind_turbine_type3_iec",
        "dthetamax",
        "dthetamin",
        "kic",
        "kiomega",
        "kpc",
        "kpomega",
        "kpx",
        "thetamax",
        "thetamin",
        "ttheta",
    )

    dthetamax: float | None
    dthetamin: float | None
    kic: float | None  # PU
    kiomega: float | None  # PU
    kpc: float | None  # PU
    kpomega: float | None  # PU
    kpx: float | None  # PU
    thetamax: float | None  # AngleDegrees
    thetamin: float | None  # AngleDegrees
    ttheta: float | None  # Seconds

    wind_turbine_type3_iec: One[WindTurbineType3IEC] = One(
        EndMeta(
            name="wind_turbine_type3_iec",
            cim_role="WindTurbineType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec:WindTurbineType3IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_cont_pitch_angle_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContPitchAngleIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{371F797D-6704-46b0-88C0-ED38AE045309}",
        attributes=(
            AttrMeta("dthetamax", "dthetamax", "float", 0, 1, "primitive"),
            AttrMeta("dthetamin", "dthetamin", "float", 0, 1, "primitive"),
            AttrMeta("kic", "kic", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiomega", "kiomega", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpc", "kpc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpomega", "kpomega", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpx", "kpx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("thetamax", "thetamax", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("thetamin", "thetamin", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("ttheta", "ttheta", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type3_iec.meta,),
    )

    def __init__(
        self,
        *,
        dthetamax: float | None = None,
        dthetamin: float | None = None,
        kic: float | None = None,
        kiomega: float | None = None,
        kpc: float | None = None,
        kpomega: float | None = None,
        kpx: float | None = None,
        thetamax: float | None = None,
        thetamin: float | None = None,
        ttheta: float | None = None,
        wind_turbine_type3_iec: WindTurbineType3IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dthetamax = dthetamax
        self.dthetamin = dthetamin
        self.kic = kic
        self.kiomega = kiomega
        self.kpc = kpc
        self.kpomega = kpomega
        self.kpx = kpx
        self.thetamax = thetamax
        self.thetamin = thetamin
        self.ttheta = ttheta
        if wind_turbine_type3_iec is not None:
            self.wind_turbine_type3_iec = wind_turbine_type3_iec
