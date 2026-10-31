"""CIM class WindContQIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_qcontrol_mode_kind import (
        WindQcontrolModeKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec import (
        WindTurbineType3or4IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_uvrt_qcontrol_mode_kind import (
        WindUVRTQcontrolModeKind,
    )


class WindContQIEC(IdentifiedObject):
    """Q control model.

    Reference: IEC 61400-27-1:2015, 5.6.5.7."""

    __slots__ = (
        "_wind_turbine_type3or4_iec",
        "iqh1",
        "iqmax",
        "iqmin",
        "iqpost",
        "kiq",
        "kiu",
        "kpq",
        "kpu",
        "kqv",
        "rdroop",
        "tpfiltq",
        "tpost",
        "tqord",
        "tufiltq",
        "udb1",
        "udb2",
        "umax",
        "umin",
        "uqdip",
        "uref0",
        "wind_qcontrol_modes_type",
        "wind_uvrt_qcontrol_modes_type",
        "xdroop",
    )

    iqh1: float | None  # PU
    iqmax: float | None  # PU
    iqmin: float | None  # PU
    iqpost: float | None  # PU
    kiq: float | None  # PU
    kiu: float | None  # PU
    kpq: float | None  # PU
    kpu: float | None  # PU
    kqv: float | None  # PU
    rdroop: float | None  # PU
    tpfiltq: float | None  # Seconds
    tpost: float | None  # Seconds
    tqord: float | None  # Seconds
    tufiltq: float | None  # Seconds
    udb1: float | None  # PU
    udb2: float | None  # PU
    umax: float | None  # PU
    umin: float | None  # PU
    uqdip: float | None  # PU
    uref0: float | None  # PU
    wind_qcontrol_modes_type: WindQcontrolModeKind | None
    wind_uvrt_qcontrol_modes_type: WindUVRTQcontrolModeKind | None
    xdroop: float | None  # PU

    wind_turbine_type3or4_iec: One[WindTurbineType3or4IEC] = One(
        EndMeta(
            name="wind_turbine_type3or4_iec",
            cim_role="WindTurbineType3or4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec:WindTurbineType3or4IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="w_ind_cont_qiec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContQIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{D845C466-FD3D-4777-A5D9-0A4F09CFC513}",
        attributes=(
            AttrMeta("iqh1", "iqh1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("iqmax", "iqmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("iqmin", "iqmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("iqpost", "iqpost", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiq", "kiq", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiu", "kiu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpq", "kpq", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpu", "kpu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kqv", "kqv", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rdroop", "rdroop", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpfiltq", "tpfiltq", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpost", "tpost", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tqord", "tqord", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tufiltq", "tufiltq", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("udb1", "udb1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("udb2", "udb2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("umax", "umax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("umin", "umin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("uqdip", "uqdip", "PU", 0, 1, "cimdatatype"),
            AttrMeta("uref0", "uref0", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "wind_qcontrol_modes_type",
                "windQcontrolModesType",
                "WindQcontrolModeKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "wind_uvrt_qcontrol_modes_type",
                "windUVRTQcontrolModesType",
                "WindUVRTQcontrolModeKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("xdroop", "xdroop", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type3or4_iec.meta,),
    )

    def __init__(
        self,
        *,
        iqh1: float | None = None,
        iqmax: float | None = None,
        iqmin: float | None = None,
        iqpost: float | None = None,
        kiq: float | None = None,
        kiu: float | None = None,
        kpq: float | None = None,
        kpu: float | None = None,
        kqv: float | None = None,
        rdroop: float | None = None,
        tpfiltq: float | None = None,
        tpost: float | None = None,
        tqord: float | None = None,
        tufiltq: float | None = None,
        udb1: float | None = None,
        udb2: float | None = None,
        umax: float | None = None,
        umin: float | None = None,
        uqdip: float | None = None,
        uref0: float | None = None,
        wind_qcontrol_modes_type: WindQcontrolModeKind | None = None,
        wind_uvrt_qcontrol_modes_type: WindUVRTQcontrolModeKind | None = None,
        xdroop: float | None = None,
        wind_turbine_type3or4_iec: WindTurbineType3or4IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.iqh1 = iqh1
        self.iqmax = iqmax
        self.iqmin = iqmin
        self.iqpost = iqpost
        self.kiq = kiq
        self.kiu = kiu
        self.kpq = kpq
        self.kpu = kpu
        self.kqv = kqv
        self.rdroop = rdroop
        self.tpfiltq = tpfiltq
        self.tpost = tpost
        self.tqord = tqord
        self.tufiltq = tufiltq
        self.udb1 = udb1
        self.udb2 = udb2
        self.umax = umax
        self.umin = umin
        self.uqdip = uqdip
        self.uref0 = uref0
        self.wind_qcontrol_modes_type = wind_qcontrol_modes_type
        self.wind_uvrt_qcontrol_modes_type = wind_uvrt_qcontrol_modes_type
        self.xdroop = xdroop
        if wind_turbine_type3or4_iec is not None:
            self.wind_turbine_type3or4_iec = wind_turbine_type3or4_iec
