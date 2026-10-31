"""CIM enumeration AssetKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetKind(CimEnum):
    """Kind of asset."""

    breaker = "breaker"
    other = "other"
    v3phase_transformer = "3phaseTransformer"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{00000000-0000-0000-0000-00000000A001}",
            kind="enumeration",
        )
    )
