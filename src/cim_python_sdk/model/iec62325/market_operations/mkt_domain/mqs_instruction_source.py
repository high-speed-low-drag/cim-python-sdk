"""CIM enumeration MQSInstructionSource (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MQSInstructionSource(CimEnum):
    """Valid values, for example:

    INS - Instruction from RTM

    ACT - Actual instruction after the fact"""

    INS = "INS"
    ACT = "ACT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MQSInstructionSource",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{4E798929-48FC-4231-8A87-E70ABF184684}",
            kind="enumeration",
        )
    )
