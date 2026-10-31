"""CIM class RevisionHistory (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.revision_kind import RevisionKind
    from cim_python_sdk.model.iec61968.operations.switching_step import SwitchingStep


class RevisionHistory(CimObject):
    """History of changes made to a switching plan step after the switching plan has been
    approved."""

    __slots__ = (
        "_switching_step",
        "kind",
        "revision_author",
        "revision_date_time",
        "revision_reason",
    )

    kind: RevisionKind | None
    revision_date_time: _dt.datetime | None
    revision_reason: str | None
    revision_author: str | None

    switching_step: One[SwitchingStep] = One(
        EndMeta(
            name="switching_step",
            cim_role="SwitchingStep",
            target="cim_python_sdk.model.iec61968.operations.switching_step:SwitchingStep",
            many=False,
            lower=0,
            upper=1,
            inverse="revision_history",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RevisionHistory",
        package="TC57CIM/IEC61968/Operations",
        guid="{93D02920-BAD0-4638-8E60-1866E0C3B226}",
        attributes=(
            AttrMeta("kind", "kind", "RevisionKind", 1, 1, "enumeration"),
            AttrMeta("revision_date_time", "revisionDateTime", "datetime", 1, 1, "primitive"),
            AttrMeta("revision_reason", "revisionReason", "str", 1, 1, "primitive"),
            AttrMeta("revision_author", "revisionAuthor", "str", 1, 1, "primitive"),
        ),
        ends=(switching_step.meta,),
    )

    def __init__(
        self,
        *,
        kind: RevisionKind | None = None,
        revision_date_time: _dt.datetime | None = None,
        revision_reason: str | None = None,
        revision_author: str | None = None,
        switching_step: SwitchingStep | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.revision_date_time = revision_date_time
        self.revision_reason = revision_reason
        self.revision_author = revision_author
        if switching_step is not None:
            self.switching_step = switching_step
