"""CIM class OutageArea (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.area_kind import AreaKind
    from cim_python_sdk.model.iec61968.operations.outage import Outage


class OutageArea(CimObject):
    """This defines the area covered by the Outage."""

    __slots__ = ("_outage", "earliest_reported_time", "meters_served", "outage_area_kind")

    earliest_reported_time: _dt.datetime | None
    meters_served: int | None
    outage_area_kind: AreaKind | None

    outage: Many[Outage] = Many(
        EndMeta(
            name="outage",
            cim_role="Outage",
            target="cim_python_sdk.model.iec61968.operations.outage:Outage",
            many=True,
            lower=0,
            upper=None,
            inverse="outage_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OutageArea",
        package="TC57CIM/IEC61968/Operations",
        guid="{4CCB893D-9C2D-4985-AAA1-756A8708B31D}",
        attributes=(
            AttrMeta(
                "earliest_reported_time", "earliestReportedTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("meters_served", "metersServed", "int", 0, 1, "primitive"),
            AttrMeta("outage_area_kind", "outageAreaKind", "AreaKind", 0, 1, "enumeration"),
        ),
        ends=(outage.meta,),
    )

    def __init__(
        self,
        *,
        earliest_reported_time: _dt.datetime | None = None,
        meters_served: int | None = None,
        outage_area_kind: AreaKind | None = None,
        outage: Iterable[Outage] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.earliest_reported_time = earliest_reported_time
        self.meters_served = meters_served
        self.outage_area_kind = outage_area_kind
        if outage is not None:
            OutageArea.outage.extend(self, outage)

    def add_outage(self, outage: Outage) -> Self:
        return OutageArea.outage.add(self, outage)

    def remove_outage(self, outage: Outage) -> Self:
        return OutageArea.outage.remove(self, outage)

    def clear_outage(self) -> Self:
        return OutageArea.outage.clear(self)

    def num_outage(self) -> int:
        return OutageArea.outage.count(self)

    def get_outage_by_mrid(self, mrid: str) -> Outage | None:
        return OutageArea.outage.get_by_mrid(self, mrid)
