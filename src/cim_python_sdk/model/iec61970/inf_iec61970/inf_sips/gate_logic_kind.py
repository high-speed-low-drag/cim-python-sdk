"""CIM enumeration GateLogicKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class GateLogicKind(CimEnum):
    """Define the different logical operations."""

    and_ = "and"
    or_ = "or"
    nor = "nor"
    nand = "nand"
    not_ = "not"
    xnor = "xnor"
    xor = "xor"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="GateLogicKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{512FB5B2-9206-4fc1-B233-F8EF2A054F44}",
            kind="enumeration",
        )
    )
