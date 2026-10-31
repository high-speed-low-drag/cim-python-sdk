"""CIM class CurveData (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.curve import Curve


class CurveData(CimObject):
    """Multi-purpose data points for defining a curve. The use of this generic class is
    discouraged if a more specific class can be used to specify the X and Y axis values
    along with their specific data types."""

    __slots__ = ("_curve", "xvalue", "y1value", "y2value", "y3value")

    xvalue: float | None
    y1value: float | None
    y2value: float | None
    y3value: float | None

    curve: One[Curve] = One(
        EndMeta(
            name="curve",
            cim_role="Curve",
            target="cim_python_sdk.model.iec61970.base.core.curve:Curve",
            many=False,
            lower=1,
            upper=1,
            inverse="curve_datas",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CurveData",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{49452B3C-BB66-4c7a-A86B-6BE155BB7193}",
        attributes=(
            AttrMeta("xvalue", "xvalue", "float", 0, 1, "primitive"),
            AttrMeta("y1value", "y1value", "float", 0, 1, "primitive"),
            AttrMeta("y2value", "y2value", "float", 0, 1, "primitive"),
            AttrMeta("y3value", "y3value", "float", 0, 1, "primitive"),
        ),
        ends=(curve.meta,),
    )

    def __init__(
        self,
        *,
        xvalue: float | None = None,
        y1value: float | None = None,
        y2value: float | None = None,
        y3value: float | None = None,
        curve: Curve | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.xvalue = xvalue
        self.y1value = y1value
        self.y2value = y2value
        self.y3value = y3value
        if curve is not None:
            self.curve = curve
