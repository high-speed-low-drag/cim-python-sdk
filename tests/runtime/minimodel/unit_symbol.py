"""CIM enumeration UnitSymbol (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UnitSymbol(CimEnum):
    """The units defined for usage in the CIM."""

    A = "A"
    V = "V"
    W = "W"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UnitSymbol",
            package="TC57CIM/IEC61970/Base/Domain",
            guid="{00000000-0000-0000-0000-00000000A002}",
            kind="enumeration",
        )
    )
