"""CIM class ExcRQB (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcRQB(ExcitationSystemDynamics):
    """Excitation system type RQB (four-loop regulator, r?gulateur quatre boucles, developed in
    France) primarily used in nuclear or thermal generating units. This excitation system
    shall be always used together with power system stabilizer type PssRQB."""

    __slots__ = (
        "ki0",
        "ki1",
        "klir",
        "klus",
        "lsat",
        "lus",
        "mesu",
        "t4m",
        "tc",
        "te",
        "tf",
        "ucmax",
        "ucmin",
    )

    ki0: float | None
    ki1: float | None
    te: float | None  # Seconds
    tc: float | None  # Seconds
    klir: float | None
    ucmin: float | None  # PU
    ucmax: float | None  # PU
    lus: float | None  # PU
    klus: float | None
    mesu: float | None  # Seconds
    t4m: float | None  # Seconds
    lsat: float | None  # PU
    tf: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="ExcRQB",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{1EF393B6-BC78-42f1-B8C7-30791D76FC50}",
        attributes=(
            AttrMeta("ki0", "ki0", "float", 0, 1, "primitive"),
            AttrMeta("ki1", "ki1", "float", 0, 1, "primitive"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("klir", "klir", "float", 0, 1, "primitive"),
            AttrMeta("ucmin", "ucmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ucmax", "ucmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("lus", "lus", "PU", 0, 1, "cimdatatype"),
            AttrMeta("klus", "klus", "float", 0, 1, "primitive"),
            AttrMeta("mesu", "mesu", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("t4m", "t4m", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("lsat", "lsat", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ki0: float | None = None,
        ki1: float | None = None,
        te: float | None = None,
        tc: float | None = None,
        klir: float | None = None,
        ucmin: float | None = None,
        ucmax: float | None = None,
        lus: float | None = None,
        klus: float | None = None,
        mesu: float | None = None,
        t4m: float | None = None,
        lsat: float | None = None,
        tf: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ki0 = ki0
        self.ki1 = ki1
        self.te = te
        self.tc = tc
        self.klir = klir
        self.ucmin = ucmin
        self.ucmax = ucmax
        self.lus = lus
        self.klus = klus
        self.mesu = mesu
        self.t4m = t4m
        self.lsat = lsat
        self.tf = tf
