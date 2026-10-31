"""CIM class ExcST4B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcST4B(ExcitationSystemDynamics):
    """Modified IEEE ST4B static excitation system with maximum inner loop feedback gain Vgmax."""

    __slots__ = (
        "kc",
        "kg",
        "ki",
        "kim",
        "kir",
        "kp",
        "kpm",
        "kpr",
        "lvgate",
        "ta",
        "thetap",
        "uel",
        "vbmax",
        "vgmax",
        "vmmax",
        "vmmin",
        "vrmax",
        "vrmin",
        "xl",
    )

    kpr: float | None  # PU
    kir: float | None  # PU
    ta: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    kpm: float | None  # PU
    kim: float | None  # PU
    vmmax: float | None  # PU
    vmmin: float | None  # PU
    kg: float | None  # PU
    kp: float | None  # PU
    thetap: float | None  # AngleDegrees
    ki: float | None  # PU
    kc: float | None  # PU
    xl: float | None  # PU
    vbmax: float | None  # PU
    vgmax: float | None  # PU
    uel: bool | None
    lvgate: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcST4B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{85D10103-7F88-4241-8E66-58D467B5AAB4}",
        attributes=(
            AttrMeta("kpr", "kpr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kir", "kir", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpm", "kpm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kim", "kim", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmmax", "vmmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vmmin", "vmmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kg", "kg", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kp", "kp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("thetap", "thetap", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xl", "xl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vbmax", "vbmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vgmax", "vgmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("uel", "uel", "bool", 0, 1, "primitive"),
            AttrMeta("lvgate", "lvgate", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        kpr: float | None = None,
        kir: float | None = None,
        ta: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        kpm: float | None = None,
        kim: float | None = None,
        vmmax: float | None = None,
        vmmin: float | None = None,
        kg: float | None = None,
        kp: float | None = None,
        thetap: float | None = None,
        ki: float | None = None,
        kc: float | None = None,
        xl: float | None = None,
        vbmax: float | None = None,
        vgmax: float | None = None,
        uel: bool | None = None,
        lvgate: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kpr = kpr
        self.kir = kir
        self.ta = ta
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.kpm = kpm
        self.kim = kim
        self.vmmax = vmmax
        self.vmmin = vmmin
        self.kg = kg
        self.kp = kp
        self.thetap = thetap
        self.ki = ki
        self.kc = kc
        self.xl = xl
        self.vbmax = vbmax
        self.vgmax = vgmax
        self.uel = uel
        self.lvgate = lvgate
