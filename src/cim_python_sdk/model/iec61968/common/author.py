"""CIM class Author (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document_person_role import DocumentPersonRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord
    from cim_python_sdk.model.iec61968.common.document import Document


class Author(DocumentPersonRole):
    """Person who created document or activity record."""

    __slots__ = ("_activity_records", "_documents")

    documents: Many[Document] = Many(
        EndMeta(
            name="documents",
            cim_role="Documents",
            target="cim_python_sdk.model.iec61968.common.document:Document",
            many=True,
            lower=0,
            upper=None,
            inverse="author",
            aggregation="none",
        )
    )
    activity_records: Many[ActivityRecord] = Many(
        EndMeta(
            name="activity_records",
            cim_role="ActivityRecords",
            target="cim_python_sdk.model.iec61968.common.activity_record:ActivityRecord",
            many=True,
            lower=0,
            upper=None,
            inverse="author",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Author",
        package="TC57CIM/IEC61968/Common",
        guid="{ECE4B2D2-00C0-4f64-A658-76BD9A6E2773}",
        ends=(
            documents.meta,
            activity_records.meta,
        ),
    )

    def __init__(
        self,
        *,
        documents: Iterable[Document] | None = None,
        activity_records: Iterable[ActivityRecord] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if documents is not None:
            Author.documents.extend(self, documents)
        if activity_records is not None:
            Author.activity_records.extend(self, activity_records)

    def add_document(self, document: Document) -> Self:
        return Author.documents.add(self, document)

    def remove_document(self, document: Document) -> Self:
        return Author.documents.remove(self, document)

    def clear_documents(self) -> Self:
        return Author.documents.clear(self)

    def num_document(self) -> int:
        return Author.documents.count(self)

    def get_document_by_mrid(self, mrid: str) -> Document | None:
        return Author.documents.get_by_mrid(self, mrid)

    def add_activity_record(self, activity_record: ActivityRecord) -> Self:
        return Author.activity_records.add(self, activity_record)

    def remove_activity_record(self, activity_record: ActivityRecord) -> Self:
        return Author.activity_records.remove(self, activity_record)

    def clear_activity_records(self) -> Self:
        return Author.activity_records.clear(self)

    def num_activity_record(self) -> int:
        return Author.activity_records.count(self)

    def get_activity_record_by_mrid(self, mrid: str) -> ActivityRecord | None:
        return Author.activity_records.get_by_mrid(self, mrid)
