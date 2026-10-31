"""CIM class WindMechIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_iec import (
        WindTurbineType1or2IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec import (
        WindTurbineType3IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4b_iec import (
        WindTurbineType4bIEC,
    )


class WindMechIEC(IdentifiedObject):
    """Two mass model.

    Reference: IEC 61400-27-1:2015, 5.6.2.1."""

    __slots__ = (
        "_wind_turbine_type1or2_iec",
        "_wind_turbine_type3_iec",
        "_wind_turbine_type4b_iec",
        "cdrt",
        "hgen",
        "hwtr",
        "kdrt",
    )

    cdrt: float | None  # PU
    hgen: float | None  # Seconds
    hwtr: float | None  # Seconds
    kdrt: float | None  # PU

    wind_turbine_type1or2_iec: One[WindTurbineType1or2IEC] = One(
        EndMeta(
            name="wind_turbine_type1or2_iec",
            cim_role="WindTurbineType1or2IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_iec:WindTurbineType1or2IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_mech_iec",
            aggregation="none",
        )
    )
    wind_turbine_type3_iec: One[WindTurbineType3IEC] = One(
        EndMeta(
            name="wind_turbine_type3_iec",
            cim_role="WindTurbineType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec:WindTurbineType3IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_mech_iec",
            aggregation="none",
        )
    )
    wind_turbine_type4b_iec: One[WindTurbineType4bIEC] = One(
        EndMeta(
            name="wind_turbine_type4b_iec",
            cim_role="WindTurbineType4bIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4b_iec:WindTurbineType4bIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_mech_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindMechIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{9E677047-A1CF-4e4f-81D6-778E126A0B0C}",
        attributes=(
            AttrMeta("cdrt", "cdrt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hgen", "hgen", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("hwtr", "hwtr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kdrt", "kdrt", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_turbine_type1or2_iec.meta,
            wind_turbine_type3_iec.meta,
            wind_turbine_type4b_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        cdrt: float | None = None,
        hgen: float | None = None,
        hwtr: float | None = None,
        kdrt: float | None = None,
        wind_turbine_type1or2_iec: WindTurbineType1or2IEC | None = None,
        wind_turbine_type3_iec: WindTurbineType3IEC | None = None,
        wind_turbine_type4b_iec: WindTurbineType4bIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cdrt = cdrt
        self.hgen = hgen
        self.hwtr = hwtr
        self.kdrt = kdrt
        if wind_turbine_type1or2_iec is not None:
            self.wind_turbine_type1or2_iec = wind_turbine_type1or2_iec
        if wind_turbine_type3_iec is not None:
            self.wind_turbine_type3_iec = wind_turbine_type3_iec
        if wind_turbine_type4b_iec is not None:
            self.wind_turbine_type4b_iec = wind_turbine_type4b_iec
