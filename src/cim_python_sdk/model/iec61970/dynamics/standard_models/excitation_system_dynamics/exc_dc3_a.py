"""CIM class ExcDC3A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcDC3A(ExcitationSystemDynamics):
    """Modified IEEE DC3A direct current commutator exciter with speed input, and deadband. DC
    old type 4."""

    __slots__ = (
        "efd1",
        "efd2",
        "efdlim",
        "efdmax",
        "efdmin",
        "exclim",
        "ke",
        "kr",
        "ks",
        "kv",
        "seefd1",
        "seefd2",
        "te",
        "trh",
        "vrmax",
        "vrmin",
    )

    trh: float | None  # Seconds
    ks: float | None  # PU
    kr: float | None  # PU
    kv: float | None  # PU
    vrmax: float | None  # PU
    vrmin: float | None  # PU
    te: float | None  # Seconds
    ke: float | None  # PU
    efd1: float | None  # PU
    seefd1: float | None
    efd2: float | None  # PU
    seefd2: float | None
    exclim: bool | None
    efdmax: float | None  # PU
    efdmin: float | None  # PU
    efdlim: bool | None

    _cim_meta = ClassMeta(
        cim_name="ExcDC3A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{D4FAEA40-9F0D-4494-A94F-C976B7B21BB8}",
        attributes=(
            AttrMeta("trh", "trh", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ks", "ks", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kr", "kr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kv", "kv", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmax", "vrmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vrmin", "vrmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efd1", "efd1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seefd1", "seefd1", "float", 0, 1, "primitive"),
            AttrMeta("efd2", "efd2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("seefd2", "seefd2", "float", 0, 1, "primitive"),
            AttrMeta("exclim", "exclim", "bool", 0, 1, "primitive"),
            AttrMeta("efdmax", "efdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdmin", "efdmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("efdlim", "efdlim", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        trh: float | None = None,
        ks: float | None = None,
        kr: float | None = None,
        kv: float | None = None,
        vrmax: float | None = None,
        vrmin: float | None = None,
        te: float | None = None,
        ke: float | None = None,
        efd1: float | None = None,
        seefd1: float | None = None,
        efd2: float | None = None,
        seefd2: float | None = None,
        exclim: bool | None = None,
        efdmax: float | None = None,
        efdmin: float | None = None,
        efdlim: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trh = trh
        self.ks = ks
        self.kr = kr
        self.kv = kv
        self.vrmax = vrmax
        self.vrmin = vrmin
        self.te = te
        self.ke = ke
        self.efd1 = efd1
        self.seefd1 = seefd1
        self.efd2 = efd2
        self.seefd2 = seefd2
        self.exclim = exclim
        self.efdmax = efdmax
        self.efdmin = efdmin
        self.efdlim = efdlim
