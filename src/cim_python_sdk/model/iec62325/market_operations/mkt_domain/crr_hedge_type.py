"""CIM enumeration CRRHedgeType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CRRHedgeType(CimEnum):
    """Congestion Revenue Right hedge type."""

    OBLIGATION = "OBLIGATION"
    OPTION = "OPTION"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CRRHedgeType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{5E61277D-3A24-45dd-BD94-A44A0AE79CCC}",
            kind="enumeration",
        )
    )
