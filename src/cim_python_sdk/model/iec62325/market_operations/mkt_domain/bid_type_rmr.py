"""CIM enumeration BidTypeRMR (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BidTypeRMR(CimEnum):
    """Bid self schedule type has two types as the required output of requirements and
    qualified pre-dispatch."""

    REQUIREMENTS = "REQUIREMENTS"
    QUALIFIED_PREDISPATCH = "QUALIFIED_PREDISPATCH"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BidTypeRMR",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{E57AD2E0-4F36-4c55-ADCD-FEB338707237}",
            kind="enumeration",
        )
    )
