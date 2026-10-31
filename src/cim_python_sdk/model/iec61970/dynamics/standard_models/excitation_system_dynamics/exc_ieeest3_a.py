"""CIM class ExcIEEEST3A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEST3A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type ST3A model. Some static systems utilize a field voltage control
    loop to linearize the exciter control characteristic. This also makes the output
    independent of supply source variations until supply limitations are reached. These
    systems utilize a variety of controlled-rectifier designs: full thyristor complements or
    hybrid bridges in either series or shunt configurations. The power source can consist of
    only a potential source, either fed from the machine terminals or from internal
    windings. Some designs can have compound power sources utilizing both machine potential
    and current. These power sources are represented as phasor combinations of machine
    terminal current and voltage and are accommodated by suitable parameters in model type
    ST3A which is represented by ExcIEEEST3A.

    Reference: IEEE 421.5-2005, 7.3."""

    __slots__ = (
        "ka",
        "kc",
        "kg",
        "ki",
        "km",
        "kp",
        "ta",
        "tb",
        "tc",
        "thetap",
        "tm",
        "vbmax",
        "vgmax",
        "vimax",
        "vimin",
        "vmmax",
        "vmmin",
        "vrmax",
        "vrmin",
        "xl",
    )

    vimax: float | None  # PU
    vimin: float | None  # PU
    ka: float | None  # PU
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    km: float | None  # PU
    tm: float | None  # Seconds
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

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEST3A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{BE50DBC0-E168-4afe-A988-66841022814A}",
        attributes=(
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("km", "km", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tm", "tm", "Seconds", 0, 1, "cimdatatype"),
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
        ),
    )

    def __init__(
        self,
        *,
        vimax: float | None = None,
        vimin: float | None = None,
        ka: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        km: float | None = None,
        tm: float | None = None,
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
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vimax = vimax
        self.vimin = vimin
        self.ka = ka
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.km = km
        self.tm = tm
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
