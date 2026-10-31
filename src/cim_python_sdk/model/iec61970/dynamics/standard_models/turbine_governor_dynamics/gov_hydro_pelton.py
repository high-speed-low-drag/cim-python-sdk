"""CIM class GovHydroPelton (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovHydroPelton(TurbineGovernorDynamics):
    """Detailed hydro unit - Pelton model. This model can be used to represent the dynamic
    related to water tunnel and surge chamber.

    The DetailedHydroModelHydraulicSystem diagram, located under the GovHydroFrancis class,
    provides a schematic of the hydraulic system of detailed hydro unit models, such as
    Francis and Pelton."""

    __slots__ = (
        "av0",
        "av1",
        "bp",
        "db1",
        "db2",
        "h1",
        "h2",
        "hn",
        "kc",
        "kg",
        "qc0",
        "qn",
        "simplified_pelton",
        "static_compensating",
        "ta",
        "ts",
        "tv",
        "twnc",
        "twng",
        "tx",
        "va",
        "valvmax",
        "valvmin",
        "vav",
        "vc",
        "vcv",
        "water_tunnel_surge_chamber_simulation",
        "zsfc",
    )

    av0: float | None  # Area
    av1: float | None  # Area
    bp: float | None  # PU
    db1: float | None  # Frequency
    db2: float | None  # Frequency
    h1: float | None  # Length
    h2: float | None  # Length
    hn: float | None  # Length
    kc: float | None  # PU
    kg: float | None  # PU
    qc0: float | None  # PU
    qn: float | None  # VolumeFlowRate
    simplified_pelton: bool | None
    static_compensating: bool | None
    ta: float | None  # Seconds
    ts: float | None  # Seconds
    tv: float | None  # Seconds
    twnc: float | None  # Seconds
    twng: float | None  # Seconds
    tx: float | None  # Seconds
    va: float | None
    valvmax: float | None  # PU
    valvmin: float | None  # PU
    vav: float | None  # PU
    vc: float | None
    vcv: float | None  # PU
    water_tunnel_surge_chamber_simulation: bool | None
    zsfc: float | None  # Length

    _cim_meta = ClassMeta(
        cim_name="GovHydroPelton",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{93F7CE4F-A7AD-4c0a-A714-1F6BB59E4CF2}",
        attributes=(
            AttrMeta("av0", "av0", "Area", 0, 1, "cimdatatype"),
            AttrMeta("av1", "av1", "Area", 0, 1, "cimdatatype"),
            AttrMeta("bp", "bp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("db1", "db1", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("db2", "db2", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("h1", "h1", "Length", 0, 1, "cimdatatype"),
            AttrMeta("h2", "h2", "Length", 0, 1, "cimdatatype"),
            AttrMeta("hn", "hn", "Length", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qc0", "qc0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qn", "qn", "VolumeFlowRate", 0, 1, "cimdatatype"),
            AttrMeta("simplified_pelton", "simplifiedPelton", "bool", 0, 1, "primitive"),
            AttrMeta("static_compensating", "staticCompensating", "bool", 0, 1, "primitive"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts", "ts", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tv", "tv", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twnc", "twnc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twng", "twng", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tx", "tx", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("va", "va", "float", 0, 1, "primitive"),
            AttrMeta("valvmax", "valvmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("valvmin", "valvmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vav", "vav", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vc", "vc", "float", 0, 1, "primitive"),
            AttrMeta("vcv", "vcv", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "water_tunnel_surge_chamber_simulation",
                "waterTunnelSurgeChamberSimulation",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta("zsfc", "zsfc", "Length", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        av0: float | None = None,
        av1: float | None = None,
        bp: float | None = None,
        db1: float | None = None,
        db2: float | None = None,
        h1: float | None = None,
        h2: float | None = None,
        hn: float | None = None,
        kc: float | None = None,
        kg: float | None = None,
        qc0: float | None = None,
        qn: float | None = None,
        simplified_pelton: bool | None = None,
        static_compensating: bool | None = None,
        ta: float | None = None,
        ts: float | None = None,
        tv: float | None = None,
        twnc: float | None = None,
        twng: float | None = None,
        tx: float | None = None,
        va: float | None = None,
        valvmax: float | None = None,
        valvmin: float | None = None,
        vav: float | None = None,
        vc: float | None = None,
        vcv: float | None = None,
        water_tunnel_surge_chamber_simulation: bool | None = None,
        zsfc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.av0 = av0
        self.av1 = av1
        self.bp = bp
        self.db1 = db1
        self.db2 = db2
        self.h1 = h1
        self.h2 = h2
        self.hn = hn
        self.kc = kc
        self.kg = kg
        self.qc0 = qc0
        self.qn = qn
        self.simplified_pelton = simplified_pelton
        self.static_compensating = static_compensating
        self.ta = ta
        self.ts = ts
        self.tv = tv
        self.twnc = twnc
        self.twng = twng
        self.tx = tx
        self.va = va
        self.valvmax = valvmax
        self.valvmin = valvmin
        self.vav = vav
        self.vc = vc
        self.vcv = vcv
        self.water_tunnel_surge_chamber_simulation = water_tunnel_surge_chamber_simulation
        self.zsfc = zsfc
