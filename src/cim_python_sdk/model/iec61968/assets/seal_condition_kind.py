"""CIM enumeration SealConditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SealConditionKind(CimEnum):
    """Kind of seal condition."""

    locked = "locked"
    open = "open"
    broken = "broken"
    missing = "missing"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SealConditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{44679AEE-F169-4f0a-B42B-4306FC058FB2}",
            kind="enumeration",
        )
    )
