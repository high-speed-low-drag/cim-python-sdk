"""CIM enumeration OASISMarketType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OASISMarketType(CimEnum):
    """CIM enumeration OASISMarketType."""

    IFM = "IFM"
    RUC = "RUC"
    HASP = "HASP"
    RTM = "RTM"
    N_A = "N/A"
    All = "All"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OASISMarketType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{0C172CD1-7F9C-4623-940D-A382E4A7ADAF}",
            kind="enumeration",
        )
    )
