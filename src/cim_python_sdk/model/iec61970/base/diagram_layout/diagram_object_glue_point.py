"""CIM class DiagramObjectGluePoint (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_point import (
        DiagramObjectPoint,
    )


class DiagramObjectGluePoint(CimObject):
    """This is used for grouping diagram object points from different diagram objects that are
    considered to be glued together in a diagram even if they are not at the exact same
    coordinates."""

    __slots__ = ("_diagram_object_points",)

    diagram_object_points: Many[DiagramObjectPoint] = Many(
        EndMeta(
            name="diagram_object_points",
            cim_role="DiagramObjectPoints",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_point:DiagramObjectPoint",
            many=True,
            lower=2,
            upper=None,
            inverse="diagram_object_glue_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DiagramObjectGluePoint",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{9C1F1E7A-8711-422b-9415-9BCC8A04C0CD}",
        ends=(diagram_object_points.meta,),
    )

    def __init__(
        self,
        *,
        diagram_object_points: Iterable[DiagramObjectPoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if diagram_object_points is not None:
            DiagramObjectGluePoint.diagram_object_points.extend(self, diagram_object_points)

    def add_diagram_object_point(self, diagram_object_point: DiagramObjectPoint) -> Self:
        return DiagramObjectGluePoint.diagram_object_points.add(self, diagram_object_point)

    def remove_diagram_object_point(self, diagram_object_point: DiagramObjectPoint) -> Self:
        return DiagramObjectGluePoint.diagram_object_points.remove(self, diagram_object_point)

    def clear_diagram_object_points(self) -> Self:
        return DiagramObjectGluePoint.diagram_object_points.clear(self)

    def num_diagram_object_point(self) -> int:
        return DiagramObjectGluePoint.diagram_object_points.count(self)
