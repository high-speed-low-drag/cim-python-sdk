"""CIM enumeration AssetStringKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetStringKind(CimEnum):
    """Definition of type of string useful in asset domain."""

    visualExamRemarks = "visualExamRemarks"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetStringKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{5859D755-5C64-48b5-9CB0-6A4483BE14C3}",
            kind="enumeration",
        )
    )
