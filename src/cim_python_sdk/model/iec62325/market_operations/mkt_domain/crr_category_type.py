"""CIM enumeration CRRCategoryType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CRRCategoryType(CimEnum):
    """Congestion Revenue Rights category types."""

    NSR = "NSR"
    PTP = "PTP"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CRRCategoryType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{0890C55A-143E-48c3-BAEB-854733B12466}",
            kind="enumeration",
        )
    )
