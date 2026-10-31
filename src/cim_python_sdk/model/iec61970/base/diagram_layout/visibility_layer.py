"""CIM class VisibilityLayer (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object import DiagramObject


class VisibilityLayer(IdentifiedObject):
    """Layers are typically used for grouping diagram objects according to themes and scales.
    Themes are used to display or hide certain information (e.g., lakes, borders), while
    scales are used for hiding or displaying information depending on the current zoom level
    (hide text when it is too small to be read, or when it exceeds the screen size). This is
    also called de-cluttering.

    CIM based graphics exchange supports an m:n relationship between diagram objects and
    layers. The importing system shall convert an m:n case into an appropriate 1:n
    representation if the importing system does not support m:n."""

    __slots__ = ("_visible_objects", "drawing_order")

    drawing_order: int | None

    visible_objects: Many[DiagramObject] = Many(
        EndMeta(
            name="visible_objects",
            cim_role="VisibleObjects",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object:DiagramObject",
            many=True,
            lower=0,
            upper=None,
            inverse="visibility_layers",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VisibilityLayer",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{8EE633AA-3247-439f-BD39-59D924061A0B}",
        attributes=(AttrMeta("drawing_order", "drawingOrder", "int", 0, 1, "primitive"),),
        ends=(visible_objects.meta,),
    )

    def __init__(
        self,
        *,
        drawing_order: int | None = None,
        visible_objects: Iterable[DiagramObject] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.drawing_order = drawing_order
        if visible_objects is not None:
            VisibilityLayer.visible_objects.extend(self, visible_objects)

    def add_visible_object(self, visible_object: DiagramObject) -> Self:
        return VisibilityLayer.visible_objects.add(self, visible_object)

    def remove_visible_object(self, visible_object: DiagramObject) -> Self:
        return VisibilityLayer.visible_objects.remove(self, visible_object)

    def clear_visible_objects(self) -> Self:
        return VisibilityLayer.visible_objects.clear(self)

    def num_visible_object(self) -> int:
        return VisibilityLayer.visible_objects.count(self)

    def get_visible_object_by_mrid(self, mrid: str) -> DiagramObject | None:
        return VisibilityLayer.visible_objects.get_by_mrid(self, mrid)
