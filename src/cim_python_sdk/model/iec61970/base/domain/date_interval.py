"""CIM compound DateInterval (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class DateInterval(CimCompound):
    """Interval between two dates."""

    __slots__ = ("end", "start")

    start: _dt.date | None
    end: _dt.date | None

    _cim_meta = ClassMeta(
        cim_name="DateInterval",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{28B6A229-F6A8-4d93-BD50-F337824B5C8F}",
        kind="compound",
        attributes=(
            AttrMeta("start", "start", "date", 0, 1, "primitive"),
            AttrMeta("end", "end", "date", 0, 1, "primitive"),
        ),
    )
