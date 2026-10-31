"""CIM class Approver (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document_person_role import DocumentPersonRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.document import Document


class Approver(DocumentPersonRole):
    """Person who accepted/signed or rejected the document."""

    __slots__ = ("_documents",)

    documents: Many[Document] = Many(
        EndMeta(
            name="documents",
            cim_role="Documents",
            target="cim_python_sdk.model.iec61968.common.document:Document",
            many=True,
            lower=0,
            upper=None,
            inverse="approver",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Approver",
        package="TC57CIM/IEC61968/Common",
        guid="{DC3D9F04-D322-4d2d-9033-42C238CAD8B6}",
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
            Approver.documents.extend(self, documents)

    def add_document(self, document: Document) -> Self:
        return Approver.documents.add(self, document)

    def remove_document(self, document: Document) -> Self:
        return Approver.documents.remove(self, document)

    def clear_documents(self) -> Self:
        return Approver.documents.clear(self)

    def num_document(self) -> int:
        return Approver.documents.count(self)

    def get_document_by_mrid(self, mrid: str) -> Document | None:
        return Approver.documents.get_by_mrid(self, mrid)
