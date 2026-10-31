"""CIM class InternalLocation (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.work.work_location import WorkLocation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class InternalLocation(WorkLocation):
    """Description of location internal to a building."""

    __slots__ = ("building_name", "building_number", "floor", "room_number")

    building_name: str | None
    building_number: str | None
    floor: int | None
    room_number: str | None

    _cim_meta = ClassMeta(
        cim_name="InternalLocation",
        package="TC57CIM/IEC61968/Work",
        guid="{BDBC338B-362B-44d7-B28A-8EA84B84D512}",
        attributes=(
            AttrMeta("building_name", "buildingName", "str", 0, 1, "primitive"),
            AttrMeta("building_number", "buildingNumber", "str", 0, 1, "primitive"),
            AttrMeta("floor", "floor", "int", 0, 1, "primitive"),
            AttrMeta("room_number", "roomNumber", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        building_name: str | None = None,
        building_number: str | None = None,
        floor: int | None = None,
        room_number: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.building_name = building_name
        self.building_number = building_number
        self.floor = floor
        self.room_number = room_number
