"""CIM class PFVArType1IEEEPFController (TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType1Dynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.pfv_ar_controller_type1_dynamics.pfv_ar_controller_type1_dynamics import (
    PFVArControllerType1Dynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
    """IEEE PF controller type 1 which operates by moving the voltage reference directly.

    Reference: IEEE 421.5-2005, 11.2."""

    __slots__ = ("ovex", "tpfc", "vitmin", "vpf", "vpfcbw", "vpfref", "vvtmax", "vvtmin")

    ovex: bool | None
    tpfc: float | None  # Seconds
    vitmin: float | None  # PU
    vpf: float | None  # PU
    vpfcbw: float | None
    vpfref: float | None  # PU
    vvtmax: float | None  # PU
    vvtmin: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PFVArType1IEEEPFController",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PFVArControllerType1Dynamics",
        guid="{536A2525-1C48-4d52-A97C-4234E27B5BD9}",
        attributes=(
            AttrMeta("ovex", "ovex", "bool", 0, 1, "primitive"),
            AttrMeta("tpfc", "tpfc", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vitmin", "vitmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vpf", "vpf", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vpfcbw", "vpfcbw", "float", 0, 1, "primitive"),
            AttrMeta("vpfref", "vpfref", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vvtmax", "vvtmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vvtmin", "vvtmin", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ovex: bool | None = None,
        tpfc: float | None = None,
        vitmin: float | None = None,
        vpf: float | None = None,
        vpfcbw: float | None = None,
        vpfref: float | None = None,
        vvtmax: float | None = None,
        vvtmin: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ovex = ovex
        self.tpfc = tpfc
        self.vitmin = vitmin
        self.vpf = vpf
        self.vpfcbw = vpfcbw
        self.vpfref = vpfref
        self.vvtmax = vvtmax
        self.vvtmin = vvtmin
