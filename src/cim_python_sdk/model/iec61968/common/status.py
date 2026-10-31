"""CIM compound Status (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class Status(CimCompound):
    """Current status information relevant to an entity."""

    __slots__ = ("date_time", "reason", "remark", "value")

    value: str | None
    date_time: _dt.datetime | None
    remark: str | None
    reason: str | None

    _cim_meta = ClassMeta(
        cim_name="Status",
        package="TC57CIM/IEC61968/Common",
        guid="{9EF7B157-4B24-45ee-A340-2CFB8F049D68}",
        kind="compound",
        attributes=(
            AttrMeta("value", "value", "str", 0, 1, "primitive"),
            AttrMeta("date_time", "dateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("remark", "remark", "str", 0, 1, "primitive"),
            AttrMeta("reason", "reason", "str", 0, 1, "primitive"),
        ),
    )
