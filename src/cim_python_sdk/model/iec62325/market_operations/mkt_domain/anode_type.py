"""CIM enumeration AnodeType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AnodeType(CimEnum):
    """Aggregated Nodes Types for example:

    - SYS - System Zone/Region;

    - RUC - RUC Zone;

    - LFZ - Load Forecast Zone;

    - REG - Market Energy/Ancillary Service Region;

    - AGR - Aggregate Generation Resource;

    - POD - Point of Delivery;

    - ALR - Aggregate Load Resource;

    - LTAC - Load TransmissionAccessCharge (TAC) Group;

    - ACA - Adjacent Control Area

    - ASR - Aggregated System Resource

    - ECA - Embedded Control Area"""

    SYS = "SYS"
    RUC = "RUC"
    LFZ = "LFZ"
    REG = "REG"
    AGR = "AGR"
    POD = "POD"
    ALR = "ALR"
    LTAC = "LTAC"
    ACA = "ACA"
    ASR = "ASR"
    ECA = "ECA"
    DER = "DER"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AnodeType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{24EF2FC5-1D75-417f-881B-C45C0E8DC00C}",
            kind="enumeration",
        )
    )
