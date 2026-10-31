"""CIM enumeration SelfScheduleType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SelfScheduleType(CimEnum):
    """self schedule types

    PT

    ETC

    TOR

    RMR

    RMT

    RGMR

    ORFC

    SP"""

    PT = "PT"
    ETC = "ETC"
    TOR = "TOR"
    RMR = "RMR"
    RMT = "RMT"
    RGMR = "RGMR"
    ORFC = "ORFC"
    SP = "SP"
    IFM = "IFM"
    RUC = "RUC"
    RA = "RA"
    PUMP_ETC = "PUMP_ETC"
    PUMP_TOR = "PUMP_TOR"
    BAS = "BAS"
    LOF = "LOF"
    WHL = "WHL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SelfScheduleType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{AD3CD604-1975-4c32-9EB7-FACDD1E9CA6A}",
            kind="enumeration",
        )
    )
