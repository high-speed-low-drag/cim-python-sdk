"""CIM enumeration AnalogLimitType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AnalogLimitType(CimEnum):
    """Limit type specified for AnalogLimits."""

    BranchMediumTerm = "BranchMediumTerm"
    BranchLongTerm = "BranchLongTerm"
    BranchShortTerm = "BranchShortTerm"
    VoltageHigh = "VoltageHigh"
    VoltageLow = "VoltageLow"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AnalogLimitType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{5C3BE105-70E4-4789-84FE-B6A1D3FFB5CF}",
            kind="enumeration",
        )
    )
