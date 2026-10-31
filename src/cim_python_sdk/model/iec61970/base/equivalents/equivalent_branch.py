"""CIM class EquivalentBranch (TC57CIM/IEC61970/Base/Equivalents). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.equivalents.equivalent_equipment import EquivalentEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class EquivalentBranch(EquivalentEquipment):
    """The class represents equivalent branches. In cases where a transformer phase shift is
    modelled and the EquivalentBranch is spanning the same nodes, the impedance quantities
    for the EquivalentBranch shall consider the needed phase shift."""

    __slots__ = (
        "negative_r12",
        "negative_r21",
        "negative_x12",
        "negative_x21",
        "positive_r12",
        "positive_r21",
        "positive_x12",
        "positive_x21",
        "r",
        "r21",
        "x",
        "x21",
        "zero_r12",
        "zero_r21",
        "zero_x12",
        "zero_x21",
    )

    negative_r12: float | None  # Resistance
    negative_r21: float | None  # Resistance
    negative_x12: float | None  # Reactance
    negative_x21: float | None  # Reactance
    positive_r12: float | None  # Resistance
    positive_r21: float | None  # Resistance
    positive_x12: float | None  # Reactance
    positive_x21: float | None  # Reactance
    r: float | None  # Resistance
    r21: float | None  # Resistance
    x: float | None  # Reactance
    x21: float | None  # Reactance
    zero_r12: float | None  # Resistance
    zero_r21: float | None  # Resistance
    zero_x12: float | None  # Reactance
    zero_x21: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="EquivalentBranch",
        package="TC57CIM/IEC61970/Base/Equivalents",
        guid="{FC8BE368-2F3E-4ff8-BDC1-4229823DC5AE}",
        attributes=(
            AttrMeta("negative_r12", "negativeR12", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("negative_r21", "negativeR21", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("negative_x12", "negativeX12", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("negative_x21", "negativeX21", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("positive_r12", "positiveR12", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("positive_r21", "positiveR21", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("positive_x12", "positiveX12", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("positive_x21", "positiveX21", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r21", "r21", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x21", "x21", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("zero_r12", "zeroR12", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("zero_r21", "zeroR21", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("zero_x12", "zeroX12", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("zero_x21", "zeroX21", "Reactance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        negative_r12: float | None = None,
        negative_r21: float | None = None,
        negative_x12: float | None = None,
        negative_x21: float | None = None,
        positive_r12: float | None = None,
        positive_r21: float | None = None,
        positive_x12: float | None = None,
        positive_x21: float | None = None,
        r: float | None = None,
        r21: float | None = None,
        x: float | None = None,
        x21: float | None = None,
        zero_r12: float | None = None,
        zero_r21: float | None = None,
        zero_x12: float | None = None,
        zero_x21: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.negative_r12 = negative_r12
        self.negative_r21 = negative_r21
        self.negative_x12 = negative_x12
        self.negative_x21 = negative_x21
        self.positive_r12 = positive_r12
        self.positive_r21 = positive_r21
        self.positive_x12 = positive_x12
        self.positive_x21 = positive_x21
        self.r = r
        self.r21 = r21
        self.x = x
        self.x21 = x21
        self.zero_r12 = zero_r12
        self.zero_r21 = zero_r21
        self.zero_x12 = zero_x12
        self.zero_x21 = zero_x21
