"""CIM class PositionPoint (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.location import Location


class PositionPoint(CimObject):
    """Set of spatial coordinates that determine a point, defined in the coordinate system
    specified in 'Location.CoordinateSystem'. Use a single position point instance to
    describe a point-oriented location. Use a sequence of position points to describe a
    line-oriented object (physical location of non-point oriented objects like cables or
    lines), or area of an object (like a substation or a geographical zone - in this case,
    have first and last position point with the same values)."""

    __slots__ = (
        "_location",
        "group_number",
        "sequence_number",
        "x_position",
        "y_position",
        "z_position",
    )

    sequence_number: int | None
    x_position: str | None
    y_position: str | None
    z_position: str | None
    group_number: int | None

    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=False,
            lower=1,
            upper=1,
            inverse="position_points",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PositionPoint",
        package="TC57CIM/IEC61968/Common",
        guid="{17847D7C-A86C-43c9-B8AA-522B70002D29}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("x_position", "xPosition", "str", 0, 1, "primitive"),
            AttrMeta("y_position", "yPosition", "str", 0, 1, "primitive"),
            AttrMeta("z_position", "zPosition", "str", 0, 1, "primitive"),
            AttrMeta("group_number", "groupNumber", "int", 0, 1, "primitive"),
        ),
        ends=(location.meta,),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        x_position: str | None = None,
        y_position: str | None = None,
        z_position: str | None = None,
        group_number: int | None = None,
        location: Location | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.x_position = x_position
        self.y_position = y_position
        self.z_position = z_position
        self.group_number = group_number
        if location is not None:
            self.location = location
