"""CIM class TurbLCFB1 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineLoadControllerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_load_controller_dynamics.turbine_load_controller_dynamics import (
    TurbineLoadControllerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TurbLCFB1(TurbineLoadControllerDynamics):
    """Turbine load controller model developed by WECC. This model represents a supervisory
    turbine load controller that acts to maintain turbine power at a set value by continuous
    adjustment of the turbine governor speed-load reference. This model is intended to
    represent slow reset 'outer loop' controllers managing the action of the turbine
    governor."""

    __slots__ = (
        "db",
        "emax",
        "fb",
        "fbf",
        "irmax",
        "ki",
        "kp",
        "mwbase",
        "pbf",
        "pmwset",
        "speed_reference_governor",
        "tpelec",
    )

    mwbase: float | None  # ActivePower
    speed_reference_governor: bool | None
    db: float | None  # PU
    emax: float | None  # PU
    fb: float | None  # PU
    kp: float | None  # PU
    ki: float | None  # PU
    fbf: bool | None
    pbf: bool | None
    tpelec: float | None  # Seconds
    irmax: float | None  # PU
    pmwset: float | None  # ActivePower

    _cim_meta = ClassMeta(
        cim_name="TurbLCFB1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineLoadControllerDynamics",
        guid="{B04FCA7C-DB3E-4dcc-B991-F9B87BBC1330}",
        attributes=(
            AttrMeta("mwbase", "mwbase", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "speed_reference_governor", "speedReferenceGovernor", "bool", 0, 1, "primitive"
            ),
            AttrMeta("db", "db", "PU", 0, 1, "cimdatatype"),
            AttrMeta("emax", "emax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fb", "fb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fbf", "fbf", "bool", 0, 1, "primitive"),
            AttrMeta("pbf", "pbf", "bool", 0, 1, "primitive"),
            AttrMeta("tpelec", "tpelec", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("irmax", "irmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmwset", "pmwset", "ActivePower", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        mwbase: float | None = None,
        speed_reference_governor: bool | None = None,
        db: float | None = None,
        emax: float | None = None,
        fb: float | None = None,
        kp: float | None = None,
        ki: float | None = None,
        fbf: bool | None = None,
        pbf: bool | None = None,
        tpelec: float | None = None,
        irmax: float | None = None,
        pmwset: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwbase = mwbase
        self.speed_reference_governor = speed_reference_governor
        self.db = db
        self.emax = emax
        self.fb = fb
        self.kp = kp
        self.ki = ki
        self.fbf = fbf
        self.pbf = pbf
        self.tpelec = tpelec
        self.irmax = irmax
        self.pmwset = pmwset
