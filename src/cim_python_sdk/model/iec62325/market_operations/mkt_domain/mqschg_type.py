"""CIM enumeration MQSCHGType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MQSCHGType(CimEnum):
    """For example:

    ADD - add

    CHG - change"""

    ADD = "ADD"
    CHG = "CHG"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MQSCHGType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{DBF7DFA5-206A-4db1-AE0C-5EC07F52D6F9}",
            kind="enumeration",
        )
    )
