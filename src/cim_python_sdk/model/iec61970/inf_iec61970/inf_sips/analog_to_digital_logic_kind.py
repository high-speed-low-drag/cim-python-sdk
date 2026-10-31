"""CIM enumeration AnalogToDigitalLogicKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AnalogToDigitalLogicKind(CimEnum):
    """Categories of analog to digital (or logical result) comparison."""

    ne = "ne"
    eq = "eq"
    le = "le"
    lt = "lt"
    ge = "ge"
    gt = "gt"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AnalogToDigitalLogicKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{4A652597-C1C1-4ef1-ABB7-A33022ABE056}",
            kind="enumeration",
        )
    )
