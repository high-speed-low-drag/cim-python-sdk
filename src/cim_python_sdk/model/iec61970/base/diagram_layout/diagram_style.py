"""CIM class DiagramStyle (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram import Diagram


class DiagramStyle(IdentifiedObject):
    """The diagram style refers to a style used by the originating system for a diagram. A
    diagram style describes information such as schematic, geographic, etc."""

    __slots__ = ("_diagram",)

    diagram: Many[Diagram] = Many(
        EndMeta(
            name="diagram",
            cim_role="Diagram",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram:Diagram",
            many=True,
            lower=0,
            upper=None,
            inverse="diagram_style",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DiagramStyle",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{30A35FB7-F62D-46cf-BB1E-B6F33BD62651}",
        ends=(diagram.meta,),
    )

    def __init__(
        self,
        *,
        diagram: Iterable[Diagram] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if diagram is not None:
            DiagramStyle.diagram.extend(self, diagram)

    def add_diagram(self, diagram: Diagram) -> Self:
        return DiagramStyle.diagram.add(self, diagram)

    def remove_diagram(self, diagram: Diagram) -> Self:
        return DiagramStyle.diagram.remove(self, diagram)

    def clear_diagram(self) -> Self:
        return DiagramStyle.diagram.clear(self)

    def num_diagram(self) -> int:
        return DiagramStyle.diagram.count(self)

    def get_diagram_by_mrid(self, mrid: str) -> Diagram | None:
        return DiagramStyle.diagram.get_by_mrid(self, mrid)
