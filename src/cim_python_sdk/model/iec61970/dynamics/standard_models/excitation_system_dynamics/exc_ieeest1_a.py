"""CIM class ExcIEEEST1A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.exc_ieeest1_aue_lselector_kind import (
        ExcIEEEST1AUELselectorKind,
    )


class ExcIEEEST1A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type ST1A model. This model represents systems in which excitation power
    is supplied through a transformer from the generator terminals (or the unit’s auxiliary
    bus) and is regulated by a controlled rectifier. The maximum exciter voltage available
    from such systems is directly related to the generator terminal voltage.

    Reference: IEEE 421.5-2005, 7.1."""

    __slots__ = (
        "ilr",
        "ka",
        "kc",
        "kf",
        "klr",
        "pssin",
        "ta",
        "tb",
        "tb1",
        "tc",
        "tc1",
        "tf",
        "uelin",
        "vamax",
        "vamin",
        "vimax",
        "vimin",
        "vrmax",
        "vrmin",
    )

    ilr: float | None  # PU
    ka: float | None  # PU
    kc: float | None  # PU
    kf: float | None  # PU
    klr: float | None  # PU
    pssin: bool | None
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    tb1: float | None  # Seconds
    tc: float | None  # Seconds
    tc1: float | None  # Seconds
    tf: float | None  # Seconds
    uelin: ExcIEEEST1AUELselectorKind | None
    vamax: float | None  # PU
    vamin: float | None  # PU
    vimax: float | None  # PU
    vimin: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEST1A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{538E9666-4A7D-4819-9C99-E8601AFE86B3}",
        attributes=(
            AttrMeta("ilr", "ilr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("klr", "klr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pssin", "pssin", "bool", 0, 1, "primitive"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb1", "tb1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc1", "tc1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uelin", "uelin", "ExcIEEEST1AUELselectorKind", 0, 1, "enumeration"),
            AttrMeta("vamax", "vamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vamin", "vamin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimax", "vimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vimin", "vimin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ilr: float | None = None,
        ka: float | None = None,
        kc: float | None = None,
        kf: float | None = None,
        klr: float | None = None,
        pssin: bool | None = None,
        ta: float | None = None,
        tb: float | None = None,
        tb1: float | None = None,
        tc: float | None = None,
        tc1: float | None = None,
        tf: float | None = None,
        uelin: ExcIEEEST1AUELselectorKind | None = None,
        vamax: float | None = None,
        vamin: float | None = None,
        vimax: float | None = None,
        vimin: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ilr = ilr
        self.ka = ka
        self.kc = kc
        self.kf = kf
        self.klr = klr
        self.pssin = pssin
        self.ta = ta
        self.tb = tb
        self.tb1 = tb1
        self.tc = tc
        self.tc1 = tc1
        self.tf = tf
        self.uelin = uelin
        self.vamax = vamax
        self.vamin = vamin
        self.vimax = vimax
        self.vimin = vimin
        self.vrmax = vrmax
        self.vrmin = vrmin
