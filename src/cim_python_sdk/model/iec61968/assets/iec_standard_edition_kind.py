"""CIM enumeration IECStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class IECStandardEditionKind(CimEnum):
    """List of editions for IEC standards."""

    v1963 = "1963"
    v1967 = "1967"
    v1973 = "1973"
    v1974 = "1974"
    v1977 = "1977"
    v1978 = "1978"
    v1979 = "1979"
    v1985 = "1985"
    v1989 = "1989"
    v1992 = "1992"
    v1992_AMD1_2004 = "1992/AMD1:2004"
    v1992_COR1_1992 = "1992/COR1:1992"
    v1993 = "1993"
    v1995 = "1995"
    v1997 = "1997"
    v1998 = "1998"
    v2004 = "2004"
    v2004_AMD1_2007 = "2004/AMD1:2007"
    v2004_AMD1_2007CSV = "2004/AMD1:2007CSV"
    v2005 = "2005"
    v2007 = "2007"
    v2008 = "2008"
    v2010 = "2010"
    v2011 = "2011"
    v2012 = "2012"
    v2013 = "2013"
    v2013_COR_2013 = "2013/COR:2013"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="IECStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{0F8569A9-9436-45bf-9138-CEEA87517630}",
            kind="enumeration",
        )
    )
