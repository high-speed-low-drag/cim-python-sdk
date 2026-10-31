"""CIM class DiagramObject (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram import Diagram
    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_point import (
        DiagramObjectPoint,
    )
    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_style import (
        DiagramObjectStyle,
    )
    from cim_python_sdk.model.iec61970.base.diagram_layout.visibility_layer import VisibilityLayer


class DiagramObject(IdentifiedObject):
    """An object that defines one or more points in a given space. This object can be
    associated with anything that specializes IdentifiedObject. For single line diagrams
    such objects typically include such items as analog values, breakers, disconnectors,
    power transformers, and transmission lines."""

    __slots__ = (
        "_diagram",
        "_diagram_object_points",
        "_diagram_object_style",
        "_identified_object",
        "_visibility_layers",
        "drawing_order",
        "is_polygon",
        "offset_x",
        "offset_y",
        "rotation",
    )

    drawing_order: int | None
    is_polygon: bool | None
    offset_x: float | None
    offset_y: float | None
    rotation: float | None  # AngleDegrees

    identified_object: One[IdentifiedObject] = One(
        EndMeta(
            name="identified_object",
            cim_role="IdentifiedObject",
            target="cim_python_sdk.model.iec61970.base.core.identified_object:IdentifiedObject",
            many=False,
            lower=0,
            upper=1,
            inverse="diagram_objects",
            aggregation="none",
        )
    )
    diagram_object_style: One[DiagramObjectStyle] = One(
        EndMeta(
            name="diagram_object_style",
            cim_role="DiagramObjectStyle",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_style:DiagramObjectStyle",
            many=False,
            lower=0,
            upper=1,
            inverse="styled_objects",
            aggregation="none",
        )
    )
    diagram_object_points: Many[DiagramObjectPoint] = Many(
        EndMeta(
            name="diagram_object_points",
            cim_role="DiagramObjectPoints",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_point:DiagramObjectPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="diagram_object",
            aggregation="none",
        )
    )
    diagram: One[Diagram] = One(
        EndMeta(
            name="diagram",
            cim_role="Diagram",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram:Diagram",
            many=False,
            lower=0,
            upper=1,
            inverse="diagram_elements",
            aggregation="none",
        )
    )
    visibility_layers: Many[VisibilityLayer] = Many(
        EndMeta(
            name="visibility_layers",
            cim_role="VisibilityLayers",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.visibility_layer:VisibilityLayer",
            many=True,
            lower=0,
            upper=None,
            inverse="visible_objects",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DiagramObject",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{E5A0EE1A-EA81-4542-8974-B5D3C2F3F465}",
        attributes=(
            AttrMeta("drawing_order", "drawingOrder", "int", 0, 1, "primitive"),
            AttrMeta("is_polygon", "isPolygon", "bool", 0, 1, "primitive"),
            AttrMeta("offset_x", "offsetX", "float", 0, 1, "primitive"),
            AttrMeta("offset_y", "offsetY", "float", 0, 1, "primitive"),
            AttrMeta("rotation", "rotation", "AngleDegrees", 0, 1, "cimdatatype"),
        ),
        ends=(
            identified_object.meta,
            diagram_object_style.meta,
            diagram_object_points.meta,
            diagram.meta,
            visibility_layers.meta,
        ),
    )

    def __init__(
        self,
        *,
        drawing_order: int | None = None,
        is_polygon: bool | None = None,
        offset_x: float | None = None,
        offset_y: float | None = None,
        rotation: float | None = None,
        identified_object: IdentifiedObject | None = None,
        diagram_object_style: DiagramObjectStyle | None = None,
        diagram_object_points: Iterable[DiagramObjectPoint] | None = None,
        diagram: Diagram | None = None,
        visibility_layers: Iterable[VisibilityLayer] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.drawing_order = drawing_order
        self.is_polygon = is_polygon
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.rotation = rotation
        if identified_object is not None:
            self.identified_object = identified_object
        if diagram_object_style is not None:
            self.diagram_object_style = diagram_object_style
        if diagram_object_points is not None:
            DiagramObject.diagram_object_points.extend(self, diagram_object_points)
        if diagram is not None:
            self.diagram = diagram
        if visibility_layers is not None:
            DiagramObject.visibility_layers.extend(self, visibility_layers)

    def add_diagram_object_point(self, diagram_object_point: DiagramObjectPoint) -> Self:
        return DiagramObject.diagram_object_points.add(self, diagram_object_point)

    def remove_diagram_object_point(self, diagram_object_point: DiagramObjectPoint) -> Self:
        return DiagramObject.diagram_object_points.remove(self, diagram_object_point)

    def clear_diagram_object_points(self) -> Self:
        return DiagramObject.diagram_object_points.clear(self)

    def num_diagram_object_point(self) -> int:
        return DiagramObject.diagram_object_points.count(self)

    def add_visibility_layer(self, visibility_layer: VisibilityLayer) -> Self:
        return DiagramObject.visibility_layers.add(self, visibility_layer)

    def remove_visibility_layer(self, visibility_layer: VisibilityLayer) -> Self:
        return DiagramObject.visibility_layers.remove(self, visibility_layer)

    def clear_visibility_layers(self) -> Self:
        return DiagramObject.visibility_layers.clear(self)

    def num_visibility_layer(self) -> int:
        return DiagramObject.visibility_layers.count(self)

    def get_visibility_layer_by_mrid(self, mrid: str) -> VisibilityLayer | None:
        return DiagramObject.visibility_layers.get_by_mrid(self, mrid)
