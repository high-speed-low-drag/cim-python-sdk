"""CIM enumeration ResourceLimitIndicator (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResourceLimitIndicator(CimEnum):
    """Locational AS Flags indicating whether the Upper or Lower Bound limit of the AS regional
    procurement is binding."""

    UPPER = "UPPER"
    LOWER = "LOWER"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResourceLimitIndicator",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{DA416C3B-7202-4b9c-BFF9-3DDA372D5A73}",
            kind="enumeration",
        )
    )
