"""CIM class Document (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord
    from cim_python_sdk.model.iec61968.common.approver import Approver
    from cim_python_sdk.model.iec61968.common.author import Author
    from cim_python_sdk.model.iec61968.common.configuration_event import ConfigurationEvent
    from cim_python_sdk.model.iec61968.common.editor import Editor
    from cim_python_sdk.model.iec61968.common.electronic_address import ElectronicAddress
    from cim_python_sdk.model.iec61968.common.issuer import Issuer
    from cim_python_sdk.model.iec61968.common.status import Status


class Document(IdentifiedObject):
    """Parent class for different groupings of information collected and managed as a part of a
    business process. It will frequently contain references to other objects, such as
    assets, people and power system resources."""

    __slots__ = (
        "_activity_record",
        "_approver",
        "_author",
        "_configuration_events",
        "_editor",
        "_issuer",
        "author_name",
        "comment",
        "created_date_time",
        "doc_status",
        "electronic_address",
        "last_modified_date_time",
        "revision_number",
        "status",
        "subject",
        "title",
        "type",
    )

    type: str | None
    author_name: str | None
    created_date_time: _dt.datetime | None
    last_modified_date_time: _dt.datetime | None
    revision_number: str | None
    electronic_address: ElectronicAddress | None
    subject: str | None
    title: str | None
    doc_status: Status | None
    status: Status | None
    comment: str | None

    author: One[Author] = One(
        EndMeta(
            name="author",
            cim_role="Author",
            target="cim_python_sdk.model.iec61968.common.author:Author",
            many=False,
            lower=0,
            upper=1,
            inverse="documents",
            aggregation="none",
        )
    )
    editor: One[Editor] = One(
        EndMeta(
            name="editor",
            cim_role="Editor",
            target="cim_python_sdk.model.iec61968.common.editor:Editor",
            many=False,
            lower=0,
            upper=1,
            inverse="documents",
            aggregation="none",
        )
    )
    activity_record: Many[ActivityRecord] = Many(
        EndMeta(
            name="activity_record",
            cim_role="ActivityRecord",
            target="cim_python_sdk.model.iec61968.common.activity_record:ActivityRecord",
            many=True,
            lower=0,
            upper=None,
            inverse="document",
            aggregation="none",
        )
    )
    issuer: One[Issuer] = One(
        EndMeta(
            name="issuer",
            cim_role="Issuer",
            target="cim_python_sdk.model.iec61968.common.issuer:Issuer",
            many=False,
            lower=0,
            upper=1,
            inverse="documents",
            aggregation="none",
        )
    )
    configuration_events: Many[ConfigurationEvent] = Many(
        EndMeta(
            name="configuration_events",
            cim_role="ConfigurationEvents",
            target="cim_python_sdk.model.iec61968.common.configuration_event:ConfigurationEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="changed_document",
            aggregation="none",
        )
    )
    approver: One[Approver] = One(
        EndMeta(
            name="approver",
            cim_role="Approver",
            target="cim_python_sdk.model.iec61968.common.approver:Approver",
            many=False,
            lower=0,
            upper=1,
            inverse="documents",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Document",
        package="TC57CIM/IEC61968/Common",
        guid="{EF39687B-42C9-4204-972C-0F1A9520DC31}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("author_name", "authorName", "str", 0, 1, "primitive"),
            AttrMeta("created_date_time", "createdDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "last_modified_date_time", "lastModifiedDateTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("revision_number", "revisionNumber", "str", 0, 1, "primitive"),
            AttrMeta(
                "electronic_address", "electronicAddress", "ElectronicAddress", 0, 1, "compound"
            ),
            AttrMeta("subject", "subject", "str", 0, 1, "primitive"),
            AttrMeta("title", "title", "str", 0, 1, "primitive"),
            AttrMeta("doc_status", "docStatus", "Status", 0, 1, "compound"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
            AttrMeta("comment", "comment", "str", 0, 1, "primitive"),
        ),
        ends=(
            author.meta,
            editor.meta,
            activity_record.meta,
            issuer.meta,
            configuration_events.meta,
            approver.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        author_name: str | None = None,
        created_date_time: _dt.datetime | None = None,
        last_modified_date_time: _dt.datetime | None = None,
        revision_number: str | None = None,
        electronic_address: ElectronicAddress | None = None,
        subject: str | None = None,
        title: str | None = None,
        doc_status: Status | None = None,
        status: Status | None = None,
        comment: str | None = None,
        author: Author | None = None,
        editor: Editor | None = None,
        activity_record: Iterable[ActivityRecord] | None = None,
        issuer: Issuer | None = None,
        configuration_events: Iterable[ConfigurationEvent] | None = None,
        approver: Approver | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.author_name = author_name
        self.created_date_time = created_date_time
        self.last_modified_date_time = last_modified_date_time
        self.revision_number = revision_number
        self.electronic_address = electronic_address
        self.subject = subject
        self.title = title
        self.doc_status = doc_status
        self.status = status
        self.comment = comment
        if author is not None:
            self.author = author
        if editor is not None:
            self.editor = editor
        if activity_record is not None:
            Document.activity_record.extend(self, activity_record)
        if issuer is not None:
            self.issuer = issuer
        if configuration_events is not None:
            Document.configuration_events.extend(self, configuration_events)
        if approver is not None:
            self.approver = approver

    def add_activity_record(self, activity_record: ActivityRecord) -> Self:
        return Document.activity_record.add(self, activity_record)

    def remove_activity_record(self, activity_record: ActivityRecord) -> Self:
        return Document.activity_record.remove(self, activity_record)

    def clear_activity_record(self) -> Self:
        return Document.activity_record.clear(self)

    def num_activity_record(self) -> int:
        return Document.activity_record.count(self)

    def get_activity_record_by_mrid(self, mrid: str) -> ActivityRecord | None:
        return Document.activity_record.get_by_mrid(self, mrid)

    def add_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return Document.configuration_events.add(self, configuration_event)

    def remove_configuration_event(self, configuration_event: ConfigurationEvent) -> Self:
        return Document.configuration_events.remove(self, configuration_event)

    def clear_configuration_events(self) -> Self:
        return Document.configuration_events.clear(self)

    def num_configuration_event(self) -> int:
        return Document.configuration_events.count(self)

    def get_configuration_event_by_mrid(self, mrid: str) -> ConfigurationEvent | None:
        return Document.configuration_events.get_by_mrid(self, mrid)
