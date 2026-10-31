"""CIM class ExcIEEEDC3A (TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
    ExcitationSystemDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExcIEEEDC3A(ExcitationSystemDynamics):
    """IEEE 421.5-2005 type DC3A model. This model represents older systems, in particular
    those DC commutator exciters with non-continuously acting regulators that were commonly
    used before the development of the continuously acting varieties. These systems respond
    at basically two different rates, depending upon the magnitude of voltage error. For
    small errors, adjustment is made periodically with a signal to a motor-operated
    rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong
    forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat
    occurs for these larger error signals, even though it is bypassed by contactor action.

    Reference: IEEE 421.5-2005, 5.3."""

    __slots__ = (
        "efd1",
        "efd2",
        "exclim",
        "ke",
        "kv",
        "seefd1",
        "seefd2",
        "te",
        "trh",
        "vrmax",
        "vrmin",
    )

    trh: float | None  # Seconds
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

    _cim_meta = ClassMeta(
        cim_name="ExcIEEEDC3A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/ExcitationSystemDynamics",
        guid="{BD327C73-BB24-4204-81F0-1D7C0CBE4B73}",
        attributes=(
            AttrMeta("trh", "trh", "Seconds", 0, 1, "cimdatatype"),
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
        ),
    )

    def __init__(
        self,
        *,
        trh: float | None = None,
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
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.trh = trh
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
