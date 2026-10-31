"""CIM class ExcIEEEDC1A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEDC1A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type DC1A model. This model represents field-controlled DC commutator
    exciters with continuously acting voltage regulators (especially the direct-acting
    rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has
    been widely implemented by the industry, it is sometimes used to represent other types
    of systems when detailed data for them are not available or when a simplified model is
    required.

    Reference: IEEE 421.5-2005, 5.1."""

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

    ka: float | None  # PU
    ta: float | None  # Seconds
    tb: float | None  # Seconds
    tc: float | None  # Seconds
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    ke: float | None  # PU
    te: float | None  # Seconds
    kf: float | None  # PU
    tf: float | None  # Seconds
    efd1: float | None  # PU
    seefd1: float | None
    efd2: float | None  # PU
    seefd2: float | None
    uelin: bool | None
    exclim: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEDC1A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{8045C2BD-5BDB-401f-BB79-0FA9E8E30E27}",
        attributes=(
            AttrMeta("ka", "ka", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ta", "ta", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("kf", "kf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tf", "tf", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efd1", "efd1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seefd1", "seefd1", "float", 0, 1, "primitive"),
            AttrMeta("efd2", "efd2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seefd2", "seefd2", "float", 0, 1, "primitive"),
            AttrMeta("uelin", "uelin", "bool", 0, 1, "primitive"),
            AttrMeta("exclim", "exclim", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        ta: float | None = None,
        tb: float | None = None,
        tc: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        ke: float | None = None,
        te: float | None = None,
        kf: float | None = None,
        tf: float | None = None,
        efd1: float | None = None,
        seefd1: float | None = None,
        efd2: float | None = None,
        seefd2: float | None = None,
        uelin: bool | None = None,
        exclim: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.ta = ta
        self.tb = tb
        self.tc = tc
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.ke = ke
        self.te = te
        self.kf = kf
        self.tf = tf
        self.efd1 = efd1
        self.seefd1 = seefd1
        self.efd2 = efd2
        self.seefd2 = seefd2
        self.uelin = uelin
        self.exclim = exclim
