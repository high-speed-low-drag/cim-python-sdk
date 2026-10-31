"""CIM class Diagram (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object import DiagramObject
    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_style import DiagramStyle
    from cim_python_sdk.model.iec61970.base.diagram_layout.orientation_kind import OrientationKind


class Diagram(IdentifiedObject):
    """The diagram being exchanged. The coordinate system is a standard Cartesian coordinate
    system and the orientation attribute defines the orientation. The initial view related
    attributes can be used to specify an initial view with the x,y coordinates of the
    diagonal points."""

    __slots__ = (
        "_diagram_elements",
        "_diagram_style",
        "orientation",
        "x1_initial_view",
        "x2_initial_view",
        "y1_initial_view",
        "y2_initial_view",
    )

    orientation: OrientationKind | None
    x1_initial_view: float | None
    x2_initial_view: float | None
    y1_initial_view: float | None
    y2_initial_view: float | None

    diagram_style: One[DiagramStyle] = One(
        EndMeta(
            name="diagram_style",
            cim_role="DiagramStyle",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_style:DiagramStyle",
            many=False,
            lower=0,
            upper=1,
            inverse="diagram",
            aggregation="none",
        )
    )
    diagram_elements: Many[DiagramObject] = Many(
        EndMeta(
            name="diagram_elements",
            cim_role="DiagramElements",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object:DiagramObject",
            many=True,
            lower=0,
            upper=None,
            inverse="diagram",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Diagram",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{E982A207-6642-4fb9-A092-40DFA2B37027}",
        attributes=(
            AttrMeta("orientation", "orientation", "OrientationKind", 0, 1, "enumeration"),
            AttrMeta("x1_initial_view", "x1InitialView", "float", 0, 1, "primitive"),
            AttrMeta("x2_initial_view", "x2InitialView", "float", 0, 1, "primitive"),
            AttrMeta("y1_initial_view", "y1InitialView", "float", 0, 1, "primitive"),
            AttrMeta("y2_initial_view", "y2InitialView", "float", 0, 1, "primitive"),
        ),
        ends=(
            diagram_style.meta,
            diagram_elements.meta,
        ),
    )

    def __init__(
        self,
        *,
        orientation: OrientationKind | None = None,
        x1_initial_view: float | None = None,
        x2_initial_view: float | None = None,
        y1_initial_view: float | None = None,
        y2_initial_view: float | None = None,
        diagram_style: DiagramStyle | None = None,
        diagram_elements: Iterable[DiagramObject] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.orientation = orientation
        self.x1_initial_view = x1_initial_view
        self.x2_initial_view = x2_initial_view
        self.y1_initial_view = y1_initial_view
        self.y2_initial_view = y2_initial_view
        if diagram_style is not None:
            self.diagram_style = diagram_style
        if diagram_elements is not None:
            Diagram.diagram_elements.extend(self, diagram_elements)

    def add_diagram_element(self, diagram_element: DiagramObject) -> Self:
        return Diagram.diagram_elements.add(self, diagram_element)

    def remove_diagram_element(self, diagram_element: DiagramObject) -> Self:
        return Diagram.diagram_elements.remove(self, diagram_element)

    def clear_diagram_elements(self) -> Self:
        return Diagram.diagram_elements.clear(self)

    def num_diagram_element(self) -> int:
        return Diagram.diagram_elements.count(self)

    def get_diagram_element_by_mrid(self, mrid: str) -> DiagramObject | None:
        return Diagram.diagram_elements.get_by_mrid(self, mrid)
