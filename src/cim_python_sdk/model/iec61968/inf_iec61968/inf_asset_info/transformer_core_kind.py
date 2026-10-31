"""CIM enumeration TransformerCoreKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransformerCoreKind(CimEnum):
    """Kind of transformer construction."""

    core = "core"
    shell = "shell"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransformerCoreKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{6D41676A-0497-413b-BC16-FCDBC360EFEA}",
            kind="enumeration",
        )
    )
