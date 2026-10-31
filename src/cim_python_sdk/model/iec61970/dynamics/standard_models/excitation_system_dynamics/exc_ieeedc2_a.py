"""CIM class ExcIEEEDC2A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEDC2A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type DC2A model. This model represents field-controlled DC commutator
    exciters with continuously acting voltage regulators having supplies obtained from the
    generator or auxiliary bus. It differs from the type DC1A model only in the voltage
    regulator output limits, which are now proportional to terminal voltage VT.

    It is representative of solid-state replacements for various forms of older mechanical
    and rotating amplifier regulating equipment connected to DC commutator exciters.

    Reference: IEEE 421.5-2005, 5.2."""

    __slots__ = (
        "efd1",
        "efd2",
        "exclim",
        "ka",
        "ke",
        "kf",
        "seefd1",
        "seefd2",
        "ta",
        "tb",
        "tc",
        "te",
        "tf",
        "uelin",
        "vrmax",
        "vrmin",
    )

    efd1: float | None  # PU
    efd2: float | None  # PU
    exclim: float | None  # PU
    ka: float | None  # PU
    ke: float | None  # PU
    kf: float | None  # PU
    seefd1: float | None
    seefd2: float | None
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    te: float | None  # Seconds
    tf: float | None  # Seconds
    uelin: bool | None
    vrmax: float | None  # PU
    vrmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEDC2A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{3D715368-2991-450d-B9BB-F687CD39CD43}",
        attributes=(
            AttrMeta("efd1", "efd1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efd2", "efd2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("exclim", "exclim", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seefd1", "seefd1", "float", 0, 1, "primitive"),
            AttrMeta("seefd2", "seefd2", "float", 0, 1, "primitive"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uelin", "uelin", "bool", 0, 1, "primitive"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        efd1: float | None = None,
        efd2: float | None = None,
        exclim: float | None = None,
        ka: float | None = None,
        ke: float | None = None,
        kf: float | None = None,
        seefd1: float | None = None,
        seefd2: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        te: float | None = None,
        tf: float | None = None,
        uelin: bool | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.efd1 = efd1
        self.efd2 = efd2
        self.exclim = exclim
        self.ka = ka
        self.ke = ke
        self.kf = kf
        self.seefd1 = seefd1
        self.seefd2 = seefd2
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.te = te
        self.tf = tf
        self.uelin = uelin
        self.vrmax = vrmax
        self.vrmin = vrmin
