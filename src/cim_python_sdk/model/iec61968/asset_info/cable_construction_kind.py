"""CIM enumeration CableConstructionKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CableConstructionKind(CimEnum):
    """Kind of cable construction."""

    compacted = "compacted"
    compressed = "compressed"
    sector = "sector"
    segmental = "segmental"
    solid = "solid"
    stranded = "stranded"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CableConstructionKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{13DF7BB8-6268-45bb-9169-8F1A08072878}",
            kind="enumeration",
        )
    )
