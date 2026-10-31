"""CIM compound DateTimeInterval (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class DateTimeInterval(CimCompound):
    """Interval between two date and time points, where the interval includes the start time
    but excludes end time."""

    __slots__ = ("end", "start")

    start: _dt.datetime | None
    end: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="DateTimeInterval",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{DDF0ECB1-36BC-4660-912F-9B7EF4A672D2}",
        kind="compound",
        attributes=(
            AttrMeta("start", "start", "datetime", 0, 1, "primitive"),
            AttrMeta("end", "end", "datetime", 0, 1, "primitive"),
        ),
    )
