"""CIM enumeration ResourceCertificationKind (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResourceCertificationKind(CimEnum):
    """Types used for resource certification."""

    RegulationUp = "RegulationUp"
    RegulationDown = "RegulationDown"
    SpinningReserve = "SpinningReserve"
    NonSpinningReserve = "NonSpinningReserve"
    ReliabilityMustRun = "ReliabilityMustRun"
    BLACKSTART = "BLACKSTART"
    DemandSideResponse = "DemandSideResponse"
    SynchronousCondenser = "SynchronousCondenser"
    IntermittentResource = "IntermittentResource"
    ReliabilityUnitCommitment = "ReliabilityUnitCommitment"
    Energy = "Energy"
    Capacity = "Capacity"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResourceCertificationKind",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{1A8E9455-69B0-4569-AB6A-139B5AF62D66}",
            kind="enumeration",
        )
    )
