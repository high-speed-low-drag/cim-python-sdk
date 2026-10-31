"""CIM enumeration StructureMaterialKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class StructureMaterialKind(CimEnum):
    """Kind of material used for structures."""

    wood = "wood"
    steel = "steel"
    concrete = "concrete"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="StructureMaterialKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{F4916917-6D37-4b5b-A967-F4D9B2644D92}",
            kind="enumeration",
        )
    )
