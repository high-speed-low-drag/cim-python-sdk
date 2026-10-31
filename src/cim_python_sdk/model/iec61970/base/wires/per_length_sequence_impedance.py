"""CIM class PerLengthSequenceImpedance (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.per_length_impedance import PerLengthImpedance

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PerLengthSequenceImpedance(PerLengthImpedance):
    """Sequence impedance and admittance parameters per unit length, for transposed lines of 1,
    2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm
    and x0=xs+xm."""

    __slots__ = ("b0ch", "bch", "g0ch", "gch", "r", "r0", "x", "x0")

    b0ch: float | None  # SusceptancePerLength
    bch: float | None  # SusceptancePerLength
    g0ch: float | None  # ConductancePerLength
    gch: float | None  # ConductancePerLength
    r: float | None  # ResistancePerLength
    r0: float | None  # ResistancePerLength
    x: float | None  # ReactancePerLength
    x0: float | None  # ReactancePerLength

    _cim_meta = ClassMeta(
        cim_name="PerLengthSequenceImpedance",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{03E92000-9F13-4deb-B5E1-B3262BEBDE92}",
        attributes=(
            AttrMeta("b0ch", "b0ch", "SusceptancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("bch", "bch", "SusceptancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("g0ch", "g0ch", "ConductancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("gch", "gch", "ConductancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "ResistancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "ResistancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "ReactancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "ReactancePerLength", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        b0ch: float | None = None,
        bch: float | None = None,
        g0ch: float | None = None,
        gch: float | None = None,
        r: float | None = None,
        r0: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b0ch = b0ch
        self.bch = bch
        self.g0ch = g0ch
        self.gch = gch
        self.r = r
        self.r0 = r0
        self.x = x
        self.x0 = x0
