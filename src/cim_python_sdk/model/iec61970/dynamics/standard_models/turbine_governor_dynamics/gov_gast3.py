"""CIM class GovGAST3 (TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.turbine_governor_dynamics.turbine_governor_dynamics import (
    TurbineGovernorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GovGAST3(TurbineGovernorDynamics):
    """Generic turbogas with acceleration and temperature controller."""

    __slots__ = (
        "bca",
        "bp",
        "dtc",
        "ka",
        "kac",
        "kca",
        "ksi",
        "ky",
        "mnef",
        "mxef",
        "rcmn",
        "rcmx",
        "tac",
        "tc",
        "td",
        "tfen",
        "tg",
        "tsi",
        "tt",
        "ttc",
        "ty",
    )

    bp: float | None  # PU
    tg: float | None  # Seconds
    rcmx: float | None  # PU
    rcmn: float | None  # PU
    ky: float | None
    ty: float | None  # Seconds
    tac: float | None  # Seconds
    kac: float | None
    tc: float | None  # Seconds
    bca: float | None
    kca: float | None
    dtc: float | None  # Temperature
    ka: float | None  # PU
    tsi: float | None  # Seconds
    ksi: float | None
    ttc: float | None  # Seconds
    tfen: float | None  # Temperature
    td: float | None  # Seconds
    tt: float | None  # Temperature
    mxef: float | None  # PU
    mnef: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="GovGAST3",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/TurbineGovernorDynamics",
        guid="{153BECCA-9710-4d48-8BEC-30215D859B61}",
        attributes=(
            AttrMeta("bp", "bp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("rcmx", "rcmx", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rcmn", "rcmn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ky", "ky", "float", 0, 1, "primitive"),
            AttrMeta("ty", "ty", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tac", "tac", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kac", "kac", "float", 0, 1, "primitive"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("bca", "bca", "float", 0, 1, "primitive"),
            AttrMeta("kca", "kca", "float", 0, 1, "primitive"),
            AttrMeta("dtc", "dtc", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tsi", "tsi", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ksi", "ksi", "float", 0, 1, "primitive"),
            AttrMeta("ttc", "ttc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tfen", "tfen", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tt", "tt", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("mxef", "mxef", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mnef", "mnef", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        bp: float | None = None,
        tg: float | None = None,
        rcmx: float | None = None,
        rcmn: float | None = None,
        ky: float | None = None,
        ty: float | None = None,
        tac: float | None = None,
        kac: float | None = None,
        tc: float | None = None,
        bca: float | None = None,
        kca: float | None = None,
        dtc: float | None = None,
        ka: float | None = None,
        tsi: float | None = None,
        ksi: float | None = None,
        ttc: float | None = None,
        tfen: float | None = None,
        td: float | None = None,
        tt: float | None = None,
        mxef: float | None = None,
        mnef: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bp = bp
        self.tg = tg
        self.rcmx = rcmx
        self.rcmn = rcmn
        self.ky = ky
        self.ty = ty
        self.tac = tac
        self.kac = kac
        self.tc = tc
        self.bca = bca
        self.kca = kca
        self.dtc = dtc
        self.ka = ka
        self.tsi = tsi
        self.ksi = ksi
        self.ttc = ttc
        self.tfen = tfen
        self.td = td
        self.tt = tt
        self.mxef = mxef
        self.mnef = mnef
