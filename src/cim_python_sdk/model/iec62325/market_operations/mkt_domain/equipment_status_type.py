"""CIM enumeration EquipmentStatusType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EquipmentStatusType(CimEnum):
    """Status of equipment."""

    In = "In"
    Out = "Out"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EquipmentStatusType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{B731F8DA-5DDA-4018-9BA8-7DA634AB5125}",
            kind="enumeration",
        )
    )
