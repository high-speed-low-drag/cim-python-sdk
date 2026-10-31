"""CIM enumeration RevisionKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RevisionKind(CimEnum):
    """List of the kinds of revisions that can be made to a SwitchingStep."""

    void = "void"
    added = "added"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RevisionKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{62EACC8A-E0B2-43c8-9592-4873B5ED6590}",
            kind="enumeration",
        )
    )
