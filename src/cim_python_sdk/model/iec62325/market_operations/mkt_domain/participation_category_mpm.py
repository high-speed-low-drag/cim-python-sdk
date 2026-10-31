"""CIM enumeration ParticipationCategoryMPM (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ParticipationCategoryMPM(CimEnum):
    """For example:

    'Y' - Participates in both LMPM and SMPM

    'N' - Not included in LMP price measures

    'S' - Participates in SMPM price measures

    'L' - Participates in LMPM price measures"""

    Y = "Y"
    N = "N"
    S = "S"
    L = "L"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ParticipationCategoryMPM",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{6AC4A6FC-64C2-4776-AB71-537ADF0EF100}",
            kind="enumeration",
        )
    )
