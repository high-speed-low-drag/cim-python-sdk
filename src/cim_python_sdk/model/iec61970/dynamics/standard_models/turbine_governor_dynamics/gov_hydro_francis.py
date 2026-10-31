"""CIM class GovHydroFrancis (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.francis_governor_control_kind import (
        FrancisGovernorControlKind,
    )


class GovHydroFrancis(TurbineGovernorDynamics):
    """Detailed hydro unit - Francis model. This model can be used to represent three types of
    governors.

    A schematic of the hydraulic system of detailed hydro unit models, such as Francis and
    Pelton, is provided in the DetailedHydroModelHydraulicSystem diagram."""

    __slots__ = (
        "am",
        "av0",
        "av1",
        "bp",
        "db1",
        "etamax",
        "governor_control",
        "h1",
        "h2",
        "hn",
        "kc",
        "kg",
        "kt",
        "qc0",
        "qn",
        "ta",
        "td",
        "ts",
        "twnc",
        "twng",
        "tx",
        "va",
        "valvmax",
        "valvmin",
        "vc",
        "water_tunnel_surge_chamber_simulation",
        "zsfc",
    )

    am: float | None  # PU
    av0: float | None  # Area
    av1: float | None  # Area
    bp: float | None  # PU
    db1: float | None  # Frequency
    etamax: float | None  # PU
    governor_control: FrancisGovernorControlKind | None
    h1: float | None  # Length
    h2: float | None  # Length
    hn: float | None  # Length
    kc: float | None  # PU
    kg: float | None  # PU
    kt: float | None  # PU
    qc0: float | None  # PU
    qn: float | None  # VolumeFlowRate
    ta: float | None  # Seconds
    td: float | None  # Seconds
    ts: float | None  # Seconds
    twnc: float | None  # Seconds
    twng: float | None  # Seconds
    tx: float | None  # Seconds
    va: float | None
    valvmax: float | None  # PU
    valvmin: float | None  # PU
    vc: float | None
    water_tunnel_surge_chamber_simulation: bool | None
    zsfc: float | None  # Length

    _cim_meta = ClassMeta(
        cim_name="GovHydroFrancis",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{340132B0-5FB9-4bc4-B48C-ED58E4386135}",
        attributes=(
            AttrMeta("am", "am", "PU", 0, 1, "cimdatatype"),
            AttrMeta("av0", "av0", "Area", 0, 1, "cimdatatype"),
            AttrMeta("av1", "av1", "Area", 0, 1, "cimdatatype"),
            AttrMeta("bp", "bp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("db1", "db1", "Frequency", 0, 1, "cimdatatype"),
            AttrMeta("etamax", "etamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "governor_control",
                "governorControl",
                "FrancisGovernorControlKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("h1", "h1", "Length", 0, 1, "cimdatatype"),
            AttrMeta("h2", "h2", "Length", 0, 1, "cimdatatype"),
            AttrMeta("hn", "hn", "Length", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kt", "kt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qc0", "qc0", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qn", "qn", "VolumeFlowRate", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts", "ts", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twnc", "twnc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twng", "twng", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tx", "tx", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("va", "va", "float", 0, 1, "primitive"),
            AttrMeta("valvmax", "valvmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("valvmin", "valvmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vc", "vc", "float", 0, 1, "primitive"),
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
        am: float | None = None,
        av0: float | None = None,
        av1: float | None = None,
        bp: float | None = None,
        db1: float | None = None,
        etamax: float | None = None,
        governor_control: FrancisGovernorControlKind | None = None,
        h1: float | None = None,
        h2: float | None = None,
        hn: float | None = None,
        kc: float | None = None,
        kg: float | None = None,
        kt: float | None = None,
        qc0: float | None = None,
        qn: float | None = None,
        ta: float | None = None,
        td: float | None = None,
        ts: float | None = None,
        twnc: float | None = None,
        twng: float | None = None,
        tx: float | None = None,
        va: float | None = None,
        valvmax: float | None = None,
        valvmin: float | None = None,
        vc: float | None = None,
        water_tunnel_surge_chamber_simulation: bool | None = None,
        zsfc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.am = am
        self.av0 = av0
        self.av1 = av1
        self.bp = bp
        self.db1 = db1
        self.etamax = etamax
        self.governor_control = governor_control
        self.h1 = h1
        self.h2 = h2
        self.hn = hn
        self.kc = kc
        self.kg = kg
        self.kt = kt
        self.qc0 = qc0
        self.qn = qn
        self.ta = ta
        self.td = td
        self.ts = ts
        self.twnc = twnc
        self.twng = twng
        self.tx = tx
        self.va = va
        self.valvmax = valvmax
        self.valvmin = valvmin
        self.vc = vc
        self.water_tunnel_surge_chamber_simulation = water_tunnel_surge_chamber_simulation
        self.zsfc = zsfc
