"""CIM class Curve (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.curve_data import CurveData
    from cim_python_sdk.model.iec61970.base.core.curve_style import CurveStyle
    from cim_python_sdk.model.iec61970.base.domain.unit_multiplier import UnitMultiplier
    from cim_python_sdk.model.iec61970.base.domain.unit_symbol import UnitSymbol


class Curve(IdentifiedObject):
    """A multi-purpose curve or functional relationship between an independent variable
    (X-axis) and dependent (Y-axis) variables."""

    __slots__ = (
        "_curve_datas",
        "curve_style",
        "x_multiplier",
        "x_unit",
        "y1_multiplier",
        "y1_unit",
        "y2_multiplier",
        "y2_unit",
        "y3_multiplier",
        "y3_unit",
    )

    curve_style: CurveStyle | None
    x_multiplier: UnitMultiplier | None
    x_unit: UnitSymbol | None
    y1_multiplier: UnitMultiplier | None
    y1_unit: UnitSymbol | None
    y2_multiplier: UnitMultiplier | None
    y2_unit: UnitSymbol | None
    y3_multiplier: UnitMultiplier | None
    y3_unit: UnitSymbol | None

    curve_datas: Many[CurveData] = Many(
        EndMeta(
            name="curve_datas",
            cim_role="CurveDatas",
            target="cim_python_sdk.model.iec61970.base.core.curve_data:CurveData",
            many=True,
            lower=0,
            upper=None,
            inverse="curve",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Curve",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{73A500A6-E7FF-4abe-8FDA-E68B4E60FF9F}",
        attributes=(
            AttrMeta("curve_style", "curveStyle", "CurveStyle", 0, 1, "enumeration"),
            AttrMeta("x_multiplier", "xMultiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("x_unit", "xUnit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("y1_multiplier", "y1Multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("y1_unit", "y1Unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("y2_multiplier", "y2Multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("y2_unit", "y2Unit", "UnitSymbol", 0, 1, "enumeration"),
            AttrMeta("y3_multiplier", "y3Multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("y3_unit", "y3Unit", "UnitSymbol", 0, 1, "enumeration"),
        ),
        ends=(curve_datas.meta,),
    )

    def __init__(
        self,
        *,
        curve_style: CurveStyle | None = None,
        x_multiplier: UnitMultiplier | None = None,
        x_unit: UnitSymbol | None = None,
        y1_multiplier: UnitMultiplier | None = None,
        y1_unit: UnitSymbol | None = None,
        y2_multiplier: UnitMultiplier | None = None,
        y2_unit: UnitSymbol | None = None,
        y3_multiplier: UnitMultiplier | None = None,
        y3_unit: UnitSymbol | None = None,
        curve_datas: Iterable[CurveData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.curve_style = curve_style
        self.x_multiplier = x_multiplier
        self.x_unit = x_unit
        self.y1_multiplier = y1_multiplier
        self.y1_unit = y1_unit
        self.y2_multiplier = y2_multiplier
        self.y2_unit = y2_unit
        self.y3_multiplier = y3_multiplier
        self.y3_unit = y3_unit
        if curve_datas is not None:
            Curve.curve_datas.extend(self, curve_datas)

    def add_curve_data(self, curve_data: CurveData) -> Self:
        return Curve.curve_datas.add(self, curve_data)

    def remove_curve_data(self, curve_data: CurveData) -> Self:
        return Curve.curve_datas.remove(self, curve_data)

    def clear_curve_datas(self) -> Self:
        return Curve.curve_datas.clear(self)

    def num_curve_data(self) -> int:
        return Curve.curve_datas.count(self)
