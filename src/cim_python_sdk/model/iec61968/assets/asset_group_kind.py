"""CIM enumeration AssetGroupKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetGroupKind(CimEnum):
    """Possible kinds of asset groups."""

    analysisGroup = "analysisGroup"
    inventoryGroup = "inventoryGroup"
    complianceGroup = "complianceGroup"
    functionalGroup = "functionalGroup"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetGroupKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{61FE121F-F762-4873-96B9-EC5B01DBA4C6}",
            kind="enumeration",
        )
    )
