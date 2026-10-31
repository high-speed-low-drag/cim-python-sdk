"""CIM enumeration ConstraintLimitType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ConstraintLimitType(CimEnum):
    """Binding constraint results limit type, For example:

    MAXIMUM

    MINIMUM"""

    MAXIMUM = "MAXIMUM"
    MINIMUM = "MINIMUM"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ConstraintLimitType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{0ACB76B5-D584-430c-A28B-6DF5FDC471A6}",
            kind="enumeration",
        )
    )
