"""CIM compound InUseDate (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class InUseDate(CimCompound):
    """Dates associated with asset 'in use' status. May have multiple in use dates for this
    device and a compound type allows a query to return multiple dates."""

    __slots__ = ("in_use_date", "not_ready_for_use_date", "ready_for_use_date")

    in_use_date: _dt.date | None
    ready_for_use_date: _dt.date | None
    not_ready_for_use_date: _dt.date | None

    _cim_meta = ClassMeta(
        cim_name="InUseDate",
        package="TC57CIM/IEC61968/Assets",
        guid="{48B1F3CD-2256-40e3-BC42-EB2331E89D28}",
        kind="compound",
        attributes=(
            AttrMeta("in_use_date", "inUseDate", "date", 0, 1, "primitive"),
            AttrMeta("ready_for_use_date", "readyForUseDate", "date", 0, 1, "primitive"),
            AttrMeta("not_ready_for_use_date", "notReadyForUseDate", "date", 0, 1, "primitive"),
        ),
    )
