"""CIM class IEC62325CIMVersion (TC57CIM/IEC62325). Generated code: do not edit."""

from __future__ import annotations

import datetime as _dt

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import ClassVar


class IEC62325CIMVersion(CimObject):
    """IEC 62325 version number assigned to this UML model."""

    __slots__ = ()

    date: ClassVar[_dt.date] = _dt.date(2022, 3, 29)
    version: ClassVar[str] = "IEC62325CIM03v17b"

    _cim_meta = ClassMeta(
        cim_name="IEC62325CIMVersion",
        package="TC57CIM/IEC62325",
        guid="{6240F09E-51C4-49b5-8222-A4C4FB63CE67}",
        attributes=(
            AttrMeta("date", "date", "date", 0, 1, "primitive", _dt.date(2022, 3, 29), static=True),
            AttrMeta(
                "version", "version", "str", 0, 1, "primitive", "IEC62325CIM03v17b", static=True
            ),
        ),
    )
