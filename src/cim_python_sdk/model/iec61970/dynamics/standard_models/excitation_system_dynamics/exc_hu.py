"""CIM class ExcHU (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcHU(ExcitationSystemDynamics):
    """Hungarian excitation system, with built-in voltage transducer."""

    __slots__ = ("ae", "ai", "atr", "emax", "emin", "imax", "imin", "ke", "ki", "te", "ti", "tr")

    tr: float | None  # Seconds
    te: float | None  # Seconds
    imin: float | None  # PU
    imax: float | None  # PU
    ae: float | None  # PU
    emin: float | None  # PU
    emax: float | None  # PU
    ki: float | None
    ai: float | None  # PU
    ti: float | None  # Seconds
    atr: float | None  # PU
    ke: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcHU",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{CA42FF68-2CA7-467e-AF70-883F91E7B54F}",
        attributes=(
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("imin", "imin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("imax", "imax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ae", "ae", "PU", 0, 1, "cimdatatype"),
            AttrMeta("emin", "emin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("emax", "emax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ki", "ki", "float", 0, 1, "primitive"),
            AttrMeta("ai", "ai", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ti", "ti", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("atr", "atr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ke", "ke", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        tr: float | None = None,
        te: float | None = None,
        imin: float | None = None,
        imax: float | None = None,
        ae: float | None = None,
        emin: float | None = None,
        emax: float | None = None,
        ki: float | None = None,
        ai: float | None = None,
        ti: float | None = None,
        atr: float | None = None,
        ke: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tr = tr
        self.te = te
        self.imin = imin
        self.imax = imax
        self.ae = ae
        self.emin = emin
        self.emax = emax
        self.ki = ki
        self.ai = ai
        self.ti = ti
        self.atr = atr
        self.ke = ke
