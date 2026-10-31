"""CIM enumeration FlagTypeRMR (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FlagTypeRMR(CimEnum):
    """Indicates whether the unit is RMR and it's condition type, for example:

    N' - not an RMR unit

    '1' - RMR Condition 1 unit

    '2' - RMR Condition 2 unit"""

    N = "N"
    v1 = "1"
    v2 = "2"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FlagTypeRMR",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{CF74BB1B-3F7F-43ac-B99E-4C1132A094AC}",
            kind="enumeration",
        )
    )
