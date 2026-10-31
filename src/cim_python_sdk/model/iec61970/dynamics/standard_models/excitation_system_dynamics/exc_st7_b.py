"""CIM class ExcST7B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.exc_st7_boe_lselector_kind import (
        ExcST7BOELselectorKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.exc_st7_bue_lselector_kind import (
        ExcST7BUELselectorKind,
    )


class ExcST7B(ExcitationSystemDynamics):
    """Modified IEEE ST7B static excitation system without stator current limiter (SCL) and
    current compensator (DROOP) inputs."""

    __slots__ = (
        "kh",
        "kia",
        "kl",
        "kpa",
        "oelin",
        "tb",
        "tc",
        "tf",
        "tg",
        "tia",
        "ts",
        "uelin",
        "vmax",
        "vmin",
        "vrmax",
        "vrmin",
    )

    kh: float | None  # PU
    kia: float | None  # PU
    kl: float | None  # PU
    kpa: float | None  # PU
    oelin: ExcST7BOELselectorKind | None
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    tf: float | None  # Seconds
    tg: float | None  # Seconds
    tia: float | None  # Seconds
    ts: float | None  # Seconds
    uelin: ExcST7BUELselectorKind | None
    vmax: float | None  # PU
    vmin: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcST7B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{57B557A4-6D9F-4ce9-975F-88A6D06C98A9}",
        attributes=(
            AttrMeta("kh", "kh", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kia", "kia", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kl", "kl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpa", "kpa", "PU", 0, 1, "cimdatatype"),
            AttrMeta("oelin", "oelin", "ExcST7BOELselectorKind", 0, 1, "enumeration"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tia", "tia", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts", "ts", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uelin", "uelin", "ExcST7BUELselectorKind", 0, 1, "enumeration"),
            AttrMeta("vmax", "vmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmin", "vmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        kh: float | None = None,
        kia: float | None = None,
        kl: float | None = None,
        kpa: float | None = None,
        oelin: ExcST7BOELselectorKind | None = None,
        tb: float | None = None,
        tc: float | None = None,
        tf: float | None = None,
        tg: float | None = None,
        tia: float | None = None,
        ts: float | None = None,
        uelin: ExcST7BUELselectorKind | None = None,
        vmax: float | None = None,
        vmin: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kh = kh
        self.kia = kia
        self.kl = kl
        self.kpa = kpa
        self.oelin = oelin
        self.tb = tb
        self.tc = tc
        self.tf = tf
        self.tg = tg
        self.tia = tia
        self.ts = ts
        self.uelin = uelin
        self.vmax = vmax
        self.vmin = vmin
        self.vrmax = vrmax
        self.vrmin = vrmin
