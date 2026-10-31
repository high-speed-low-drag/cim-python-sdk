"""CIM enumeration ContractType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ContractType(CimEnum):
    """Transmission Contract Type, For example:

    O - Other

    TE - Transmission Export

    TI - Transmission Import

    ETC - Existing Transmission Contract

    RMT - RMT Contract

    TOR - Transmission Ownership Right

    RMR - Reliability Must Run Contract

    CVR - Converted contract"""

    ETC = "ETC"
    TOR = "TOR"
    RMR = "RMR"
    RMT = "RMT"
    O = "O"
    TE = "TE"
    TI = "TI"
    CVR = "CVR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ContractType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{A3F13F7E-E69B-4442-963A-B84BF28E8677}",
            kind="enumeration",
        )
    )
