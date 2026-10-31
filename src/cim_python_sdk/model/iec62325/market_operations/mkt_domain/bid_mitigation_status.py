"""CIM enumeration BidMitigationStatus (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BidMitigationStatus(CimEnum):
    """For example:

    'S' - Mitigated by SMPM because of "misconduct"

    'L; - Mitigated by LMPM because of "misconduct"

    'R' - Modified by LMPM because of RMR rules

    'M' - Mitigated because of "misconduct" both by SMPM and LMPM

    'B' - Mitigated because of "misconduct" both by SMPM and modified by LMLM because of RMR
    rules

    'O' - original"""

    S = "S"
    L = "L"
    R = "R"
    M = "M"
    B = "B"
    O = "O"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BidMitigationStatus",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{4FDAC396-55D9-4e8d-9A3C-795331B27DD0}",
            kind="enumeration",
        )
    )
