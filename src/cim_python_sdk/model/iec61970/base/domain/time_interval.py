"""CIM compound TimeInterval (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class TimeInterval(CimCompound):
    """Interval between two times."""

    __slots__ = ("end", "start")

    start: _dt.time | None
    end: _dt.time | None

    _cim_meta = ClassMeta(
        cim_name="TimeInterval",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{1A62B1E2-8C2D-4459-A10B-118C16A22A03}",
        kind="compound",
        attributes=(
            AttrMeta("start", "start", "time", 0, 1, "primitive"),
            AttrMeta("end", "end", "time", 0, 1, "primitive"),
        ),
    )
