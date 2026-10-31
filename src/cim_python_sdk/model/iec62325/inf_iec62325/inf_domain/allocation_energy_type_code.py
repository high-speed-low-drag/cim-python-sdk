"""CIM enumeration AllocationEnergyTypeCode (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AllocationEnergyTypeCode(CimEnum):
    """CIM enumeration AllocationEnergyTypeCode."""

    DASE = "DASE"
    OE = "OE"
    HASE = "HASE"
    SRE = "SRE"
    RED = "RED"
    MSSLFE = "MSSLFE"
    RE = "RE"
    MLE = "MLE"
    SE = "SE"
    RTSSE = "RTSSE"
    PE = "PE"
    DAPE = "DAPE"
    ESRT = "ESRT"
    ESYS = "ESYS"
    RMRD = "RMRD"
    RMRR = "RMRR"
    RMRS = "RMRS"
    RMRT = "RMRT"
    STRT = "STRT"
    SDWN = "SDWN"
    TEST = "TEST"
    OVGN = "OVGN"
    VS = "VS"
    ETC = "ETC"
    TOR = "TOR"
    RSYS = "RSYS"
    RCNG = "RCNG"
    ACNG = "ACNG"
    TCNG = "TCNG"
    LMPM = "LMPM"
    BS = "BS"
    MINL = "MINL"
    SUMR = "SUMR"
    RMRH = "RMRH"
    SLIC = "SLIC"
    OTHER = "OTHER"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AllocationEnergyTypeCode",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{E5C1B2E5-D611-46d6-BB83-6B5848E0A360}",
            kind="enumeration",
        )
    )
