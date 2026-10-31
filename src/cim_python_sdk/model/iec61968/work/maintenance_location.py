"""CIM class MaintenanceLocation (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.work.work_location import WorkLocation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class MaintenanceLocation(WorkLocation):
    """Location where to perform maintenance work."""

    __slots__ = ("block", "lot", "nearest_intersection", "subdivision")

    nearest_intersection: str | None
    subdivision: str | None
    lot: str | None
    block: str | None

    _cim_meta = ClassMeta(
        cim_name="MaintenanceLocation",
        package="TC57CIM/IEC61968/Work",
        guid="{71079308-2B69-4067-8A52-46B62BBD1F48}",
        attributes=(
            AttrMeta("nearest_intersection", "nearestIntersection", "str", 0, 1, "primitive"),
            AttrMeta("subdivision", "subdivision", "str", 0, 1, "primitive"),
            AttrMeta("lot", "lot", "str", 0, 1, "primitive"),
            AttrMeta("block", "block", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        nearest_intersection: str | None = None,
        subdivision: str | None = None,
        lot: str | None = None,
        block: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.nearest_intersection = nearest_intersection
        self.subdivision = subdivision
        self.lot = lot
        self.block = block
