"""CIM class IEC61970CIMVersion (TC57CIM/IEC61970). Generated code: do not edit."""

from __future__ import annotations

import datetime as _dt

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import ClassVar


class IEC61970CIMVersion(CimObject):
    """This is the IEC 61970 CIM version number assigned to this UML model."""

    __slots__ = ()

    date: ClassVar[_dt.date] = _dt.date(2020, 8, 24)
    version: ClassVar[str] = "IEC61970CIM17v40"

    _cim_meta = ClassMeta(
        cim_name="IEC61970CIMVersion",
        package="TC57CIM/IEC61970",
        guid="{990AB50C-5CF8-46d2-B5FF-887BBBD3346F}",
        attributes=(
            AttrMeta("date", "date", "date", 0, 1, "primitive", _dt.date(2020, 8, 24), static=True),
            AttrMeta(
                "version", "version", "str", 0, 1, "primitive", "IEC61970CIM17v40", static=True
            ),
        ),
    )
