"""CIM enumeration UOMType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UOMType(CimEnum):
    """CIM enumeration UOMType."""

    MW = "MW"
    MWh = "MWh"
    US_dollar = "US$"
    percent = "%"
    INTEGER = "INTEGER"
    FLAG = "FLAG"
    dollar_mmBTU = "$/mmBTU"
    dollar_lb = "$/lb"
    US_dollar_MW = "US$/MW"
    US_dollar_MWh = "US$/MWh"
    FACTOR = "FACTOR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UOMType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{097BE75E-CE72-4123-A21B-4E5235E281EB}",
            kind="enumeration",
        )
    )
