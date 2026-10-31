"""CIM class ExcSCRX (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcSCRX(ExcitationSystemDynamics):
    """Simple excitation system with generic characteristics typical of many excitation
    systems; intended for use where negative field current could be a problem."""

    __slots__ = ("cswitch", "emax", "emin", "k", "rcrfd", "tatb", "tb", "te")

    tatb: float | None
    tb: float | None  # Seconds
    k: float | None  # PU
    te: float | None  # Seconds
    emin: float | None  # PU
    emax: float | None  # PU
    cswitch: bool | None
    rcrfd: float | None

    _cim_meta = ClassMeta(
        cim_name="ExcSCRX",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{A153B28E-4577-4ff7-9EFA-EF47377694D7}",
        attributes=(
            AttrMeta("tatb", "tatb", "float", 0, 1, "primitive"),
            AttrMeta("tb", "tb", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("k", "k", "PU", 0, 1, "cimdatatype"),
            AttrMeta("te", "te", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("emin", "emin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("emax", "emax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cswitch", "cswitch", "bool", 0, 1, "primitive"),
            AttrMeta("rcrfd", "rcrfd", "float", 0, 1, "primitive"),
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
        cswitch: bool | None = None,
        rcrfd: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tatb = tatb
        self.tb = tb
        self.k = k
        self.te = te
        self.emin = emin
        self.emax = emax
        self.cswitch = cswitch
        self.rcrfd = rcrfd
