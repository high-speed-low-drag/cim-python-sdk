"""CIM enumeration CalculationKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CalculationKind(CimEnum):
    """Categorisation of calculation operation that can be done to Measurement."""

    sum = "sum"
    mul = "mul"
    div = "div"
    sqrt = "sqrt"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CalculationKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{722FB9D1-7114-4a3c-87A0-2E26AEFC1A5B}",
            kind="enumeration",
        )
    )
