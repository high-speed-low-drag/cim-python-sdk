"""CIM enumeration AssetLifecycleStateKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetLifecycleStateKind(CimEnum):
    """Lifecycle states an asset can be in.

    While the possible lifecycle states are standardized, the allowed transitions are not -
    they are intended to be defined by the business process requirements of local
    implementations."""

    manufactured = "manufactured"
    purchased = "purchased"
    received = "received"
    retired = "retired"
    disposedOf = "disposedOf"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetLifecycleStateKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{C07287F4-DEF3-481f-8BEE-705D116B6CA3}",
            kind="enumeration",
        )
    )
