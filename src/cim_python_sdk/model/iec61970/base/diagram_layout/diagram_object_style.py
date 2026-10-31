"""CIM class DiagramObjectStyle (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object import DiagramObject


class DiagramObjectStyle(IdentifiedObject):
    """A reference to a style used by the originating system for a diagram object. A diagram
    object style describes information such as line thickness, shape such as circle or
    rectangle etc, and colour."""

    __slots__ = ("_styled_objects",)

    styled_objects: Many[DiagramObject] = Many(
        EndMeta(
            name="styled_objects",
            cim_role="StyledObjects",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object:DiagramObject",
            many=True,
            lower=0,
            upper=None,
            inverse="diagram_object_style",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DiagramObjectStyle",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{2145CBC1-D95B-40b2-BCF9-A9ED41CE9941}",
        ends=(styled_objects.meta,),
    )

    def __init__(
        self,
        *,
        styled_objects: Iterable[DiagramObject] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if styled_objects is not None:
            DiagramObjectStyle.styled_objects.extend(self, styled_objects)

    def add_styled_object(self, styled_object: DiagramObject) -> Self:
        return DiagramObjectStyle.styled_objects.add(self, styled_object)

    def remove_styled_object(self, styled_object: DiagramObject) -> Self:
        return DiagramObjectStyle.styled_objects.remove(self, styled_object)

    def clear_styled_objects(self) -> Self:
        return DiagramObjectStyle.styled_objects.clear(self)

    def num_styled_object(self) -> int:
        return DiagramObjectStyle.styled_objects.count(self)

    def get_styled_object_by_mrid(self, mrid: str) -> DiagramObject | None:
        return DiagramObjectStyle.styled_objects.get_by_mrid(self, mrid)
