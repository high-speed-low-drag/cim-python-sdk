"""CIM enumeration UnitType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UnitType(CimEnum):
    """Combined Cycle

    Gas Turbine

    Hydro Turbine

    Other

    Photovoltaic

    Hydro Pump-Turbine

    Reciprocating Engine

    Steam Turbine

    Synchronous Condenser

    Wind Turbine"""

    CCYC = "CCYC"
    GTUR = "GTUR"
    HYDR = "HYDR"
    OTHR = "OTHR"
    PHOT = "PHOT"
    PTUR = "PTUR"
    RECP = "RECP"
    STUR = "STUR"
    SYNC = "SYNC"
    WIND = "WIND"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UnitType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{047F37B4-5A6D-43a9-A632-0262342CD67F}",
            kind="enumeration",
        )
    )
