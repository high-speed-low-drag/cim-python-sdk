"""CIM class EstimatedRestorationTime (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.ert_confidence_kind import ERTConfidenceKind
    from cim_python_sdk.model.iec61968.operations.outage import Outage


class EstimatedRestorationTime(CimObject):
    """The Estimated Restoration Time (ERT) for a single outage"""

    __slots__ = ("_outage", "confidence_kind", "ert", "ert_source")

    confidence_kind: ERTConfidenceKind | None
    ert: _dt.datetime | None
    ert_source: str | None

    outage: Many[Outage] = Many(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=True,
            lower=0,
            upper=None,
            inverse="estimated_restoration_time",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EstimatedRestorationTime",
        package="TC57CIM/IEC61968/Operations",
        guid="{FC049904-001D-4ca5-B4B0-1082AA699C7B}",
        attributes=(
            AttrMeta("confidence_kind", "confidenceKind", "ERTConfidenceKind", 0, 1, "enumeration"),
            AttrMeta("ert", "ert", "datetime", 0, 1, "primitive"),
            AttrMeta("ert_source", "ertSource", "str", 0, 1, "primitive"),
        ),
        ends=(outage.meta,),
    )

    def __init__(
        self,
        *,
        confidence_kind: ERTConfidenceKind | None = None,
        ert: _dt.datetime | None = None,
        ert_source: str | None = None,
        outage: Iterable[Outage] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.confidence_kind = confidence_kind
        self.ert = ert
        self.ert_source = ert_source
        if outage is not None:
            EstimatedRestorationTime.outage.extend(self, outage)

    def add_outage(self, outage: Outage) -> Self:
        return EstimatedRestorationTime.outage.add(self, outage)

    def remove_outage(self, outage: Outage) -> Self:
        return EstimatedRestorationTime.outage.remove(self, outage)

    def clear_outage(self) -> Self:
        return EstimatedRestorationTime.outage.clear(self)

    def num_outage(self) -> int:
        return EstimatedRestorationTime.outage.count(self)

    def get_outage_by_mrid(self, mrid: str) -> Outage | None:
        return EstimatedRestorationTime.outage.get_by_mrid(self, mrid)
