"""CIM enumeration MeasurementTypeEMS (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MeasurementTypeEMS(CimEnum):
    """Path Flow - PF

    Path Inflow Limit - PIL

    Path Inflow Available Limit - PIAL

    Path Inflow Armed Limit - PIML

    Path Outflow Limit - POL

    Path Outflow Available Limit - POAL

    Path Outflow Armed Limit - OARL

    Generation Output - GO

    Generation Max Operating Limit - GMOL

    Generation Min Operating Limit - GNOL

    Generation Regulation - GR

    Generation Status - GS

    Pump Production - PP

    System Load - SL

    System ACE - ACE

    System INADV - INADV"""

    PF = "PF"
    PIL = "PIL"
    PIAL = "PIAL"
    PIML = "PIML"
    POL = "POL"
    POAL = "POAL"
    OARL = "OARL"
    GO = "GO"
    GMOL = "GMOL"
    GNOL = "GNOL"
    GR = "GR"
    GS = "GS"
    PP = "PP"
    SL = "SL"
    ACE = "ACE"
    INADV = "INADV"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MeasurementTypeEMS",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{CDBBE8AA-2696-4cfa-9520-FB470C37ECCA}",
            kind="enumeration",
        )
    )
