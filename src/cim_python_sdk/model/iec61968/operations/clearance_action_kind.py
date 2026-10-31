"""CIM enumeration ClearanceActionKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ClearanceActionKind(CimEnum):
    """Type of clearance action."""

    issue = "issue"
    update = "update"
    release = "release"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ClearanceActionKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{45A80A5F-B5F8-4b80-9B6A-A17BB65ED1AD}",
            kind="enumeration",
        )
    )
