"""CIM enumeration ISOStandardKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ISOStandardKind(CimEnum):
    """List of ISO standards."""

    v2592 = "2592"
    v2719 = "2719"
    v3016 = "3016"
    v3104 = "3104"
    v3675 = "3675"
    v1924 = "1924"
    v1924_1 = "1924-1"
    v1924_2 = "1924-2"
    v1924_3 = "1924-3"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ISOStandardKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{1EF67A3A-FC5E-4e52-A356-8D98C8C10EFB}",
            kind="enumeration",
        )
    )
