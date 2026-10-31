"""CIM class DiscExcContIEEEDEC1A (TC57CIM/IEC61970/Dynamics/StandardModels/DiscontinuousExcitationControlDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.discontinuous_excitation_control_dynamics.discontinuous_excitation_control_dynamics import (
    DiscontinuousExcitationControlDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    """IEEE type DEC1A discontinuous excitation control model that boosts generator excitation
    to a level higher than that demanded by the voltage regulator and stabilizer immediately
    following a system fault.

    Reference: IEEE 421.5-2005, 12.2."""

    __slots__ = (
        "esc",
        "kan",
        "ketl",
        "tan",
        "td",
        "tl1",
        "tl2",
        "tw5",
        "val",
        "vanmax",
        "vomax",
        "vomin",
        "vsmax",
        "vsmin",
        "vtc",
        "vtlmt",
        "vtm",
        "vtn",
    )

    vtlmt: float | None  # PU
    vomax: float | None  # PU
    vomin: float | None  # PU
    ketl: float | None  # PU
    vtc: float | None  # PU
    val: float | None  # PU
    esc: float | None  # PU
    kan: float | None  # PU
    tan: float | None  # Seconds
    tw5: float | None  # Seconds
    vsmax: float | None  # PU
    vsmin: float | None  # PU
    td: float | None  # Seconds
    tl1: float | None  # Seconds
    tl2: float | None  # Seconds
    vtm: float | None  # PU
    vtn: float | None  # PU
    vanmax: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="DiscExcContIEEEDEC1A",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/DiscontinuousExcitationControlDynamics",
        guid="{A1EB988B-922A-43f8-A266-0B77B8F608A1}",
        attributes=(
            AttrMeta("vtlmt", "vtlmt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vomax", "vomax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vomin", "vomin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ketl", "ketl", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vtc", "vtc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("val", "val", "PU", 0, 1, "cimdatatype"),
            AttrMeta("esc", "esc", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kan", "kan", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tan", "tan", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tw5", "tw5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vsmax", "vsmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vsmin", "vsmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("td", "td", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl1", "tl1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tl2", "tl2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("vtm", "vtm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vtn", "vtn", "PU", 0, 1, "cimdatatype"),
            AttrMeta("vanmax", "vanmax", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        vtlmt: float | None = None,
        vomax: float | None = None,
        vomin: float | None = None,
        ketl: float | None = None,
        vtc: float | None = None,
        val: float | None = None,
        esc: float | None = None,
        kan: float | None = None,
        tan: float | None = None,
        tw5: float | None = None,
        vsmax: float | None = None,
        vsmin: float | None = None,
        td: float | None = None,
        tl1: float | None = None,
        tl2: float | None = None,
        vtm: float | None = None,
        vtn: float | None = None,
        vanmax: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.vtlmt = vtlmt
        self.vomax = vomax
        self.vomin = vomin
        self.ketl = ketl
        self.vtc = vtc
        self.val = val
        self.esc = esc
        self.kan = kan
        self.tan = tan
        self.tw5 = tw5
        self.vsmax = vsmax
        self.vsmin = vsmin
        self.td = td
        self.tl1 = tl1
        self.tl2 = tl2
        self.vtm = vtm
        self.vtn = vtn
        self.vanmax = vanmax
