"""CIM enumeration ComDirectionKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ComDirectionKind(CimEnum):
    """Kind of communication direction."""

    fromDevice = "fromDevice"
    toDevice = "toDevice"
    biDirectional = "biDirectional"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ComDirectionKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{93720672-7143-45d5-8911-0228006C90DB}",
            kind="enumeration",
        )
    )
