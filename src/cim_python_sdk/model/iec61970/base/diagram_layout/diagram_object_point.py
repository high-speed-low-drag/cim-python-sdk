"""CIM class DiagramObjectPoint (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object import DiagramObject
    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_glue_point import (
        DiagramObjectGluePoint,
    )


class DiagramObjectPoint(CimObject):
    """A point in a given space defined by 3 coordinates and associated to a diagram object.
    The coordinates may be positive or negative as the origin does not have to be in the
    corner of a diagram."""

    __slots__ = (
        "_diagram_object",
        "_diagram_object_glue_point",
        "sequence_number",
        "x_position",
        "y_position",
        "z_position",
    )

    sequence_number: int | None
    x_position: float | None
    y_position: float | None
    z_position: float | None

    diagram_object_glue_point: One[DiagramObjectGluePoint] = One(
        EndMeta(
            name="diagram_object_glue_point",
            cim_role="DiagramObjectGluePoint",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object_glue_point:DiagramObjectGluePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="diagram_object_points",
            aggregation="none",
        )
    )
    diagram_object: One[DiagramObject] = One(
        EndMeta(
            name="diagram_object",
            cim_role="DiagramObject",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object:DiagramObject",
            many=False,
            lower=1,
            upper=1,
            inverse="diagram_object_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DiagramObjectPoint",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{4E77FE4E-1547-4538-A26A-26B06F42FA7C}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("x_position", "xPosition", "float", 0, 1, "primitive"),
            AttrMeta("y_position", "yPosition", "float", 0, 1, "primitive"),
            AttrMeta("z_position", "zPosition", "float", 0, 1, "primitive"),
        ),
        ends=(
            diagram_object_glue_point.meta,
            diagram_object.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        x_position: float | None = None,
        y_position: float | None = None,
        z_position: float | None = None,
        diagram_object_glue_point: DiagramObjectGluePoint | None = None,
        diagram_object: DiagramObject | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.x_position = x_position
        self.y_position = y_position
        self.z_position = z_position
        if diagram_object_glue_point is not None:
            self.diagram_object_glue_point = diagram_object_glue_point
        if diagram_object is not None:
            self.diagram_object = diagram_object
