"""CIM enumeration EnergyTypeCode (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EnergyTypeCode(CimEnum):
    """Valid Enumerations:

    1) DASE Day Ahead Scheduled Energy;

    2) DSSE Day Ahead Incremental Self Schedule Energy;

    3) DABE Day Ahead Incremental Energy Bid Awarded Energy;

    4) OE Optimal Energy;

    5) HASE Hour ahead pre-dispatched schedule energy;

    6) SRE Standard Ramping Energy;

    7) RED Ramping Energy Deviation;

    8) EDE Exceptional Dispatch energy;

    9) RMRE RMR Energy;

    10) MSSLFE MSSLF Energy;

    11) RE Residual Energy;

    12) MLE Minimum Load Energy;

    13) SE SLIC Energy;

    14) RTSSE Real time self scheduled energy;

    15) DMLE Day ahead minimum load energy;

    16) PE Pumping Energy;

    17) TEE Total Expected Energy;

    18) DAPE - Day-Ahead Pumping Energy;"""

    DASE = "DASE"
    DSSE = "DSSE"
    DABE = "DABE"
    OE = "OE"
    HASE = "HASE"
    SRE = "SRE"
    RED = "RED"
    EDE = "EDE"
    RMRE = "RMRE"
    MSSLFE = "MSSLFE"
    RE = "RE"
    MLE = "MLE"
    SE = "SE"
    RTSSE = "RTSSE"
    DMLE = "DMLE"
    PE = "PE"
    TEE = "TEE"
    DAPE = "DAPE"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EnergyTypeCode",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{98177A18-B8A3-4699-81EE-65B36F1E4F97}",
            kind="enumeration",
        )
    )
