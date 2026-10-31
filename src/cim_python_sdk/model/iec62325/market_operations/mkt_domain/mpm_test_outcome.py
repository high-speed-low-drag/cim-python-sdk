"""CIM enumeration MPMTestOutcome (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MPMTestOutcome(CimEnum):
    """For example:

    Passed

    Failed

    Disabled

    Skipped"""

    P = "P"
    F = "F"
    D = "D"
    S = "S"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MPMTestOutcome",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{39FD64E4-1D0A-4656-9F31-CEFA9E3D343E}",
            kind="enumeration",
        )
    )
