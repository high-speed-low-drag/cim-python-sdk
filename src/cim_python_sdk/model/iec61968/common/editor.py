"""CIM class Editor (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document_person_role import DocumentPersonRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.document import Document


class Editor(DocumentPersonRole):
    """Person who modified the document."""

    __slots__ = ("_documents",)

    documents: Many[Document] = Many(
        EndMeta(
            name="documents",
            cim_role="Documents",
            target="cim_python_sdk.model.iec61968.common.document:Document",
            many=True,
            lower=0,
            upper=None,
            inverse="editor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Editor",
        package="TC57CIM/IEC61968/Common",
        guid="{8D12ED95-AB71-4d76-BA0D-2C318F5CD164}",
        ends=(documents.meta,),
    )

    def __init__(
        self,
        *,
        documents: Iterable[Document] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if documents is not None:
            Editor.documents.extend(self, documents)

    def add_document(self, document: Document) -> Self:
        return Editor.documents.add(self, document)

    def remove_document(self, document: Document) -> Self:
        return Editor.documents.remove(self, document)

    def clear_documents(self) -> Self:
        return Editor.documents.clear(self)

    def num_document(self) -> int:
        return Editor.documents.count(self)

    def get_document_by_mrid(self, mrid: str) -> Document | None:
        return Editor.documents.get_by_mrid(self, mrid)
