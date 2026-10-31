"""CIM class FieldSafetySupervisor (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.crew_member import CrewMember

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.safety_document import SafetyDocument


class FieldSafetySupervisor(CrewMember):
    """Crew member on work site responsible for all local safety measures for the work crew
    doing maintenance, construction and repair in a substation or on a power line/cable."""

    __slots__ = ("_issued_safety_documents", "_released_safety_documents")

    issued_safety_documents: Many[SafetyDocument] = Many(
        EndMeta(
            name="issued_safety_documents",
            cim_role="IssuedSafetyDocuments",
            target="cim_python_sdk.model.iec61968.operations.safety_document:SafetyDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="issued_to_supervisor",
            aggregation="none",
        )
    )
    released_safety_documents: Many[SafetyDocument] = Many(
        EndMeta(
            name="released_safety_documents",
            cim_role="ReleasedSafetyDocuments",
            target="cim_python_sdk.model.iec61968.operations.safety_document:SafetyDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="released_by_supervisor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FieldSafetySupervisor",
        package="TC57CIM/IEC61968/Operations",
        guid="{A4E26C63-7079-4b95-9862-97326FEA4EFA}",
        ends=(
            issued_safety_documents.meta,
            released_safety_documents.meta,
        ),
    )

    def __init__(
        self,
        *,
        issued_safety_documents: Iterable[SafetyDocument] | None = None,
        released_safety_documents: Iterable[SafetyDocument] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if issued_safety_documents is not None:
            FieldSafetySupervisor.issued_safety_documents.extend(self, issued_safety_documents)
        if released_safety_documents is not None:
            FieldSafetySupervisor.released_safety_documents.extend(self, released_safety_documents)

    def add_issued_safety_document(self, issued_safety_document: SafetyDocument) -> Self:
        return FieldSafetySupervisor.issued_safety_documents.add(self, issued_safety_document)

    def remove_issued_safety_document(self, issued_safety_document: SafetyDocument) -> Self:
        return FieldSafetySupervisor.issued_safety_documents.remove(self, issued_safety_document)

    def clear_issued_safety_documents(self) -> Self:
        return FieldSafetySupervisor.issued_safety_documents.clear(self)

    def num_issued_safety_document(self) -> int:
        return FieldSafetySupervisor.issued_safety_documents.count(self)

    def get_issued_safety_document_by_mrid(self, mrid: str) -> SafetyDocument | None:
        return FieldSafetySupervisor.issued_safety_documents.get_by_mrid(self, mrid)

    def add_released_safety_document(self, released_safety_document: SafetyDocument) -> Self:
        return FieldSafetySupervisor.released_safety_documents.add(self, released_safety_document)

    def remove_released_safety_document(self, released_safety_document: SafetyDocument) -> Self:
        return FieldSafetySupervisor.released_safety_documents.remove(
            self, released_safety_document
        )

    def clear_released_safety_documents(self) -> Self:
        return FieldSafetySupervisor.released_safety_documents.clear(self)

    def num_released_safety_document(self) -> int:
        return FieldSafetySupervisor.released_safety_documents.count(self)

    def get_released_safety_document_by_mrid(self, mrid: str) -> SafetyDocument | None:
        return FieldSafetySupervisor.released_safety_documents.get_by_mrid(self, mrid)
