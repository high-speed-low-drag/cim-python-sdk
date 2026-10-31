"""CIM enumeration MQSDELType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MQSDELType(CimEnum):
    """ADD - add

    DEL - delete

    CHG - change"""

    ADD = "ADD"
    DEL = "DEL"
    CHG = "CHG"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MQSDELType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{9E965561-6FC8-47d0-882E-F353338B2405}",
            kind="enumeration",
        )
    )
