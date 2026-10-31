"""CIM enumeration SealKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SealKind(CimEnum):
    """Kind of seal."""

    steel = "steel"
    lead = "lead"
    lock = "lock"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SealKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{16AB0BBD-B6D6-4206-A8FB-1840132542A9}",
            kind="enumeration",
        )
    )
