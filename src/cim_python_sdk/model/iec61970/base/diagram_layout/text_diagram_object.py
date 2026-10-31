"""CIM class TextDiagramObject (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object import DiagramObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TextDiagramObject(DiagramObject):
    """A diagram object for placing free-text or text derived from an associated domain object."""

    __slots__ = ("text",)

    text: str | None

    _cim_meta = ClassMeta(
        cim_name="TextDiagramObject",
        package="TC57CIM/IEC61970/Base/DiagramLayout",
        guid="{ECCF586E-4F69-4f21-B234-DDE8C6974F0F}",
        attributes=(AttrMeta("text", "text", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        text: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.text = text
