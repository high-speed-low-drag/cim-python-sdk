"""CIM class WorkLocation (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.location import Location

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location import DesignLocation
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.one_call_request import OneCallRequest
    from cim_python_sdk.model.iec61968.work.base_work import BaseWork


class WorkLocation(Location):
    """Information about a particular location for various forms of work."""

    __slots__ = ("_base_works", "_design_locations", "_one_call_request")

    base_works: Many[BaseWork] = Many(
        EndMeta(
            name="base_works",
            cim_role="BaseWorks",
            target="cim_python_sdk.model.iec61968.work.base_work:BaseWork",
            many=True,
            lower=0,
            upper=None,
            inverse="work_location",
            aggregation="none",
        )
    )
    design_locations: Many[DesignLocation] = Many(
        EndMeta(
            name="design_locations",
            cim_role="DesignLocations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location:DesignLocation",
            many=True,
            lower=0,
            upper=None,
            inverse="work_locations",
            aggregation="none",
        )
    )
    one_call_request: One[OneCallRequest] = One(
        EndMeta(
            name="one_call_request",
            cim_role="OneCallRequest",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.one_call_request:OneCallRequest",
            many=False,
            lower=0,
            upper=1,
            inverse="work_locations",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkLocation",
        package="TC57CIM/IEC61968/Work",
        guid="{CFEB5DD5-B1F3-4dc1-8312-174824017CC9}",
        ends=(
            base_works.meta,
            design_locations.meta,
            one_call_request.meta,
        ),
    )

    def __init__(
        self,
        *,
        base_works: Iterable[BaseWork] | None = None,
        design_locations: Iterable[DesignLocation] | None = None,
        one_call_request: OneCallRequest | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if base_works is not None:
            WorkLocation.base_works.extend(self, base_works)
        if design_locations is not None:
            WorkLocation.design_locations.extend(self, design_locations)
        if one_call_request is not None:
            self.one_call_request = one_call_request

    def add_base_work(self, base_work: BaseWork) -> Self:
        return WorkLocation.base_works.add(self, base_work)

    def remove_base_work(self, base_work: BaseWork) -> Self:
        return WorkLocation.base_works.remove(self, base_work)

    def clear_base_works(self) -> Self:
        return WorkLocation.base_works.clear(self)

    def num_base_work(self) -> int:
        return WorkLocation.base_works.count(self)

    def get_base_work_by_mrid(self, mrid: str) -> BaseWork | None:
        return WorkLocation.base_works.get_by_mrid(self, mrid)

    def add_design_location(self, design_location: DesignLocation) -> Self:
        return WorkLocation.design_locations.add(self, design_location)

    def remove_design_location(self, design_location: DesignLocation) -> Self:
        return WorkLocation.design_locations.remove(self, design_location)

    def clear_design_locations(self) -> Self:
        return WorkLocation.design_locations.clear(self)

    def num_design_location(self) -> int:
        return WorkLocation.design_locations.count(self)

    def get_design_location_by_mrid(self, mrid: str) -> DesignLocation | None:
        return WorkLocation.design_locations.get_by_mrid(self, mrid)
