"""CIM class ExcIEEEST4B (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEST4B(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type ST4B model. This model is a variation of the type ST3A model, with
    a proportional plus integral (PI) regulator block replacing the lag-lead regulator
    characteristic that is in the ST3A model. Both potential and compound source rectifier
    excitation systems are modelled. The PI regulator blocks have non-windup limits that are
    represented. The voltage regulator of this model is typically implemented digitally.

    Reference: IEEE 421.5-2005, 7.4."""

    __slots__ = (
        "kc",
        "kg",
        "ki",
        "kim",
        "kir",
        "kp",
        "kpm",
        "kpr",
        "ta",
        "thetap",
        "vbmax",
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

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEST4B",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{9245EED1-30E1-4f2f-9988-4F1BB548767B}",
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
