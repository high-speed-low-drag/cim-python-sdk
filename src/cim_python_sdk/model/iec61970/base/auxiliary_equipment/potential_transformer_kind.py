"""CIM enumeration PotentialTransformerKind (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PotentialTransformerKind(CimEnum):
    """The construction kind of the potential transformer."""

    inductive = "inductive"
    capacitiveCoupling = "capacitiveCoupling"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PotentialTransformerKind",
            package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
            guid="{0EC6DEF8-4139-47b7-82C7-7E8E18A3D4A1}",
            kind="enumeration",
        )
    )
