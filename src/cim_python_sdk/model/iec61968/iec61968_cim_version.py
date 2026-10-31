"""CIM class IEC61968CIMVersion (TC57CIM/IEC61968). Generated code: do not edit."""

from __future__ import annotations

import datetime as _dt

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import ClassVar


class IEC61968CIMVersion(CimObject):
    """IEC 61968 version number assigned to this UML model."""

    __slots__ = ()

    date: ClassVar[_dt.date] = _dt.date(2022, 7, 4)
    version: ClassVar[str] = "IEC61968CIM13v13b"

    _cim_meta = ClassMeta(
        cim_name="IEC61968CIMVersion",
        package="TC57CIM/IEC61968",
        guid="{E7F88519-1D37-4cd2-86C2-3C0CE06246CE}",
        attributes=(
            AttrMeta("date", "date", "date", 0, 1, "primitive", _dt.date(2022, 7, 4), static=True),
            AttrMeta(
                "version", "version", "str", 0, 1, "primitive", "IEC61968CIM13v13b", static=True
            ),
        ),
    )
