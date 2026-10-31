"""CIM compound MonthDayInterval (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class MonthDayInterval(CimCompound):
    """Interval between two times specified as month and day."""

    __slots__ = ("end", "start")

    end: str | None
    start: str | None

    _cim_meta = ClassMeta(
        cim_name="MonthDayInterval",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{4EA61E08-03B6-4eec-9C3B-0978F4898AB3}",
        kind="compound",
        attributes=(
            AttrMeta("end", "end", "str", 0, 1, "primitive"),
            AttrMeta("start", "start", "str", 0, 1, "primitive"),
        ),
    )
