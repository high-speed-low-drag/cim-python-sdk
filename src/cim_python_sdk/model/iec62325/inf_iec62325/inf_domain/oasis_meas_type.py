"""CIM enumeration OASISMeasType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OASISMeasType(CimEnum):
    """CIM enumeration OASISMeasType."""

    MW = "MW"
    MWh = "MWh"
    US_dollar = "US$"
    percent = "%"
    INTEGER = "INTEGER"
    FLAG = "FLAG"
    US_dollar_MW = "US$/MW"
    US_dollar_MWh = "US$/MWh"
    FACTOR = "FACTOR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OASISMeasType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{12DE137A-06F7-41af-8572-A2F8DFFA65B7}",
            kind="enumeration",
        )
    )
