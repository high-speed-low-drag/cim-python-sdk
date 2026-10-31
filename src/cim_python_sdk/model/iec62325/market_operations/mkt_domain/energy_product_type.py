"""CIM enumeration EnergyProductType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EnergyProductType(CimEnum):
    """Energy product type."""

    FIRM = "FIRM"
    NFRM = "NFRM"
    DYN = "DYN"
    WHL = "WHL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EnergyProductType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{B4EB7F1F-E534-4ed9-B1B2-5474E9B13D45}",
            kind="enumeration",
        )
    )
