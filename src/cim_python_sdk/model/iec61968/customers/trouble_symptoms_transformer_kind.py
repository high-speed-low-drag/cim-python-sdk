"""CIM enumeration TroubleSymptomsTransformerKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleSymptomsTransformerKind(CimEnum):
    """The list of items that define the transformer problem."""

    ok = "ok"
    burning = "burning"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleSymptomsTransformerKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{5A50DDA6-1A2F-4412-B3CC-112454433DFE}",
            kind="enumeration",
        )
    )
