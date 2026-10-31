"""CIM class ExcSEXS (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcSEXS(ExcitationSystemDynamics):
    """Simplified excitation system."""

    __slots__ = ("efdmax", "efdmin", "emax", "emin", "k", "kc", "tatb", "tb", "tc", "te")

    tatb: float | None
    tb: float | None  # Seconds
    k: float | None  # PU
    te: float | None  # Seconds
    emin: float | None  # PU
    emax: float | None  # PU
    kc: float | None  # PU
    tc: float | None  # Seconds
    efdmin: float | None  # PU
    efdmax: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="ExcSEXS",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{58E2432F-4610-47c7-A972-A243939E860B}",
        attributes=(
            AttrMeta("tatb", "tatb", "float", 0, 1, "primitive"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("emin", "emin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("emax", "emax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kc", "kc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("efdmin", "efdmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        tatb: float | None = None,
        tb: float | None = None,
        k: float | None = None,
        te: float | None = None,
        emin: float | None = None,
        emax: float | None = None,
        kc: float | None = None,
        tc: float | None = None,
        efdmin: float | None = None,
        efdmax: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tatb = tatb
        self.tb = tb
        self.k = k
        self.te = te
        self.emin = emin
        self.emax = emax
        self.kc = kc
        self.tc = tc
        self.efdmin = efdmin
        self.efdmax = efdmax
