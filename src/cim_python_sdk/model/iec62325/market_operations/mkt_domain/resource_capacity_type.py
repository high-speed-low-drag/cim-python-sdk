"""CIM enumeration ResourceCapacityType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResourceCapacityType(CimEnum):
    """Resource capacity type."""

    RU = "RU"
    RD = "RD"
    SR = "SR"
    NR = "NR"
    MO = "MO"
    FO = "FO"
    RA = "RA"
    RMR = "RMR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResourceCapacityType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{B1F01A3B-E3FC-4f5f-B836-1AF45A135A8B}",
            kind="enumeration",
        )
    )
