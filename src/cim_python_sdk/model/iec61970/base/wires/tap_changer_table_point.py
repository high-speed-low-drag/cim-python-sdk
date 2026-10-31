"""CIM class TapChangerTablePoint (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TapChangerTablePoint(CimObject):
    """Describes each tap step in the tabular curve."""

    __slots__ = ("b", "g", "r", "ratio", "step", "x")

    b: float | None  # PerCent
    g: float | None  # PerCent
    r: float | None  # PerCent
    ratio: float | None
    step: int | None
    x: float | None  # PerCent

    _cim_meta = ClassMeta(
        cim_name="TapChangerTablePoint",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{199B695F-644C-4cbf-AB67-76AB51EE5078}",
        attributes=(
            AttrMeta("b", "b", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("g", "g", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("ratio", "ratio", "float", 0, 1, "primitive"),
            AttrMeta("step", "step", "int", 0, 1, "primitive"),
            AttrMeta("x", "x", "PerCent", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        b: float | None = None,
        g: float | None = None,
        r: float | None = None,
        ratio: float | None = None,
        step: int | None = None,
        x: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b = b
        self.g = g
        self.r = r
        self.ratio = ratio
        self.step = step
        self.x = x
