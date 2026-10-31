"""CIM enumeration ISOStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ISOStandardEditionKind(CimEnum):
    """List of editions for ISO standards."""

    v1973 = "1973"
    v1974 = "1974"
    v1976 = "1976"
    v1983 = "1983"
    v1985 = "1985"
    v1988 = "1988"
    v1992 = "1992"
    v1993 = "1993"
    v1994 = "1994"
    v1994_Cor1_1997 = "1994/Cor1:1997"
    v1998 = "1998"
    v2000 = "2000"
    v2002 = "2002"
    v2005 = "2005"
    v2008 = "2008"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ISOStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{C1E47926-3880-4b91-83B6-3E6027D88AC2}",
            kind="enumeration",
        )
    )
