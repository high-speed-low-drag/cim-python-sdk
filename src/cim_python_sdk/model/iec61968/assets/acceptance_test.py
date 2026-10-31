"""CIM compound AcceptanceTest (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class AcceptanceTest(CimCompound):
    """Acceptance test for assets."""

    __slots__ = ("date_time", "success", "type")

    type: str | None
    success: bool | None
    date_time: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="AcceptanceTest",
        package="TC57CIM/IEC61968/Assets",
        guid="{CEA89CFD-93CD-4599-9940-BCB3369ECF93}",
        kind="compound",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("success", "success", "bool", 0, 1, "primitive"),
            AttrMeta("date_time", "dateTime", "datetime", 0, 1, "primitive"),
        ),
    )
