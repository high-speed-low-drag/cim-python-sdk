"""CIM class ExcST6B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.exc_st6_boe_lselector_kind import (
        ExcST6BOELselectorKind,
    )


class ExcST6B(ExcitationSystemDynamics):
    """Modified IEEE ST6B static excitation system with PID controller and optional inner
    feedback loop."""

    __slots__ = (
        "ilr",
        "k1",
        "kcl",
        "kff",
        "kg",
        "kia",
        "klr",
        "km",
        "kpa",
        "kvd",
        "oelin",
        "tg",
        "ts",
        "tvd",
        "vamax",
        "vamin",
        "vilim",
        "vimax",
        "vimin",
        "vmult",
        "vrmax",
        "vrmin",
        "xc",
    )

    ilr: float | None  # PU
    k1: bool | None
    kcl: float | None  # PU
    kff: float | None  # PU
    kg: float | None  # PU
    kia: float | None  # PU
    klr: float | None  # PU
    km: float | None  # PU
    kpa: float | None  # PU
    kvd: float | None  # PU
    oelin: ExcST6BOELselectorKind | None
    tg: float | None  # Seconds
    ts: float | None  # Seconds
    tvd: float | None  # Seconds
    vamax: float | None  # PU
    vamin: float | None  # PU
    vilim: bool | None
    vimax: float | None  # PU
    vimin: float | None  # PU
    vmult: bool | None
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    xc: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcST6B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{BDCDDFDC-9773-41d0-A4FA-5A2004FAD693}",
        attributes=(
            AttrMeta("ilr", "ilr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("k1", "k1", "bool", 0, 1, "primitive"),
            AttrMeta("kcl", "kcl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kff", "kff", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kia", "kia", "PU", 0, 1, "cimdatatype"),
            AttrMeta("klr", "klr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("km", "km", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpa", "kpa", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kvd", "kvd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("oelin", "oelin", "ExcST6BOELselectorKind", 0, 1, "enumeration"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts", "ts", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tvd", "tvd", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vilim", "vilim", "bool", 0, 1, "primitive"),
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmult", "vmult", "bool", 0, 1, "primitive"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xc", "xc", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ilr: float | None = None,
        k1: bool | None = None,
        kcl: float | None = None,
        kff: float | None = None,
        kg: float | None = None,
        kia: float | None = None,
        klr: float | None = None,
        km: float | None = None,
        kpa: float | None = None,
        kvd: float | None = None,
        oelin: ExcST6BOELselectorKind | None = None,
        tg: float | None = None,
        ts: float | None = None,
        tvd: float | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        vilim: bool | None = None,
        vimax: float | None = None,
        vimin: float | None = None,
        vmult: bool | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        xc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ilr = ilr
        self.k1 = k1
        self.kcl = kcl
        self.kff = kff
        self.kg = kg
        self.kia = kia
        self.klr = klr
        self.km = km
        self.kpa = kpa
        self.kvd = kvd
        self.oelin = oelin
        self.tg = tg
        self.ts = ts
        self.tvd = tvd
        self.vamax = vamax
        self.vamin = vamin
        self.vilim = vilim
        self.vimax = vimax
        self.vimin = vimin
        self.vmult = vmult
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.xc = xc
