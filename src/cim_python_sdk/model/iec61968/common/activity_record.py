"""CIM class ActivityRecord (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.common.author import Author
    from cim_python_sdk.model.iec61968.common.document import Document
    from cim_python_sdk.model.iec61968.common.status import Status


class ActivityRecord(IdentifiedObject):
    """Records activity for an entity at a point in time; activity may be for an event that has
    already occurred or for a planned activity."""

    __slots__ = (
        "_assets",
        "_author",
        "_document",
        "created_date_time",
        "reason",
        "severity",
        "status",
        "type",
    )

    created_date_time: _dt.datetime | None
    type: str | None
    severity: str | None
    reason: str | None
    status: Status | None

    document: One[Document] = One(
        EndMeta(
            name="document",
            cim_role="Document",
            target="cim_python_sdk.model.iec61968.common.document:Document",
            many=False,
            lower=0,
            upper=1,
            inverse="activity_record",
            aggregation="none",
        )
    )
    author: One[Author] = One(
        EndMeta(
            name="author",
            cim_role="Author",
            target="cim_python_sdk.model.iec61968.common.author:Author",
            many=False,
            lower=0,
            upper=1,
            inverse="activity_records",
            aggregation="none",
        )
    )
    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="activity_records",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ActivityRecord",
        package="TC57CIM/IEC61968/Common",
        guid="{53D429E3-8E92-4098-8545-54DEEFC803C9}",
        attributes=(
            AttrMeta("created_date_time", "createdDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("severity", "severity", "str", 0, 1, "primitive"),
            AttrMeta("reason", "reason", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            document.meta,
            author.meta,
            assets.meta,
        ),
    )

    def __init__(
        self,
        *,
        created_date_time: _dt.datetime | None = None,
        type: str | None = None,
        severity: str | None = None,
        reason: str | None = None,
        status: Status | None = None,
        document: Document | None = None,
        author: Author | None = None,
        assets: Iterable[Asset] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.created_date_time = created_date_time
        self.type = type
        self.severity = severity
        self.reason = reason
        self.status = status
        if document is not None:
            self.document = document
        if author is not None:
            self.author = author
        if assets is not None:
            ActivityRecord.assets.extend(self, assets)

    def add_asset(self, asset: Asset) -> Self:
        return ActivityRecord.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return ActivityRecord.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return ActivityRecord.assets.clear(self)

    def num_asset(self) -> int:
        return ActivityRecord.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return ActivityRecord.assets.get_by_mrid(self, mrid)
