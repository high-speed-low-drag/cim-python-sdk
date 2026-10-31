"""CIM class ExcELIN2 (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcELIN2(ExcitationSystemDynamics):
    """Detailed excitation system ELIN (VATECH). This model represents an all-static excitation
    system. A PI voltage controller establishes a desired field current set point for a
    proportional current controller. The integrator of the PI controller has a follow-up
    input to match its signal to the present field current. Power system stabilizer models
    used in conjunction with this excitation system model: PssELIN2, PssIEEE2B, Pss2B."""

    __slots__ = (
        "efdbas",
        "iefmax",
        "iefmax2",
        "iefmin",
        "k1",
        "k1ec",
        "k2",
        "k3",
        "k4",
        "kd1",
        "ke2",
        "ketb",
        "pid1max",
        "seve1",
        "seve2",
        "tb1",
        "te",
        "te2",
        "ti1",
        "ti3",
        "ti4",
        "tr4",
        "upmax",
        "upmin",
        "ve1",
        "ve2",
        "xp",
    )

    k1: float | None  # PU
    k1ec: float | None  # PU
    kd1: float | None  # PU
    tb1: float | None  # Seconds
    pid1max: float | None  # PU
    ti1: float | None  # PU
    iefmax2: float | None  # PU
    k2: float | None  # PU
    ketb: float | None  # PU
    upmax: float | None  # PU
    upmin: float | None  # PU
    te: float | None  # Seconds
    xp: float | None  # PU
    te2: float | None  # Seconds
    ke2: float | None  # PU
    ve1: float | None  # PU
    seve1: float | None  # PU
    ve2: float | None  # PU
    seve2: float | None  # PU
    tr4: float | None  # Seconds
    k3: float | None  # PU
    ti3: float | None  # Seconds
    k4: float | None  # PU
    ti4: float | None  # Seconds
    iefmax: float | None  # PU
    iefmin: float | None  # PU
    efdbas: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcELIN2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{A70C011D-657F-48d6-9773-355DE124B959}",
        attributes=(
            AttrMeta("k1", "k1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k1ec", "k1ec", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kd1", "kd1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tb1", "tb1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("pid1max", "pid1max", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ti1", "ti1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("iefmax2", "iefmax2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k2", "k2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ketb", "ketb", "PU", 0, 1, "cimdatatype"),
            AttrMeta("upmax", "upmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("upmin", "upmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("xp", "xp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te2", "te2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ke2", "ke2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve1", "ve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve1", "seve1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ve2", "ve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seve2", "seve2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tr4", "tr4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k3", "k3", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ti3", "ti3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k4", "k4", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ti4", "ti4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("iefmax", "iefmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("iefmin", "iefmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdbas", "efdbas", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        k1: float | None = None,
        k1ec: float | None = None,
        kd1: float | None = None,
        tb1: float | None = None,
        pid1max: float | None = None,
        ti1: float | None = None,
        iefmax2: float | None = None,
        k2: float | None = None,
        ketb: float | None = None,
        upmax: float | None = None,
        upmin: float | None = None,
        te: float | None = None,
        xp: float | None = None,
        te2: float | None = None,
        ke2: float | None = None,
        ve1: float | None = None,
        seve1: float | None = None,
        ve2: float | None = None,
        seve2: float | None = None,
        tr4: float | None = None,
        k3: float | None = None,
        ti3: float | None = None,
        k4: float | None = None,
        ti4: float | None = None,
        iefmax: float | None = None,
        iefmin: float | None = None,
        efdbas: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.k1 = k1
        self.k1ec = k1ec
        self.kd1 = kd1
        self.tb1 = tb1
        self.pid1max = pid1max
        self.ti1 = ti1
        self.iefmax2 = iefmax2
        self.k2 = k2
        self.ketb = ketb
        self.upmax = upmax
        self.upmin = upmin
        self.te = te
        self.xp = xp
        self.te2 = te2
        self.ke2 = ke2
        self.ve1 = ve1
        self.seve1 = seve1
        self.ve2 = ve2
        self.seve2 = seve2
        self.tr4 = tr4
        self.k3 = k3
        self.ti3 = ti3
        self.k4 = k4
        self.ti4 = ti4
        self.iefmax = iefmax
        self.iefmin = iefmin
        self.efdbas = efdbas
