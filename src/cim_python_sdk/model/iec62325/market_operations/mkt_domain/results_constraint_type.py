"""CIM enumeration ResultsConstraintType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResultsConstraintType(CimEnum):
    """Market results binding constraint types."""

    FG_act = "FG_act"
    Contingency = "Contingency"
    Interface = "Interface"
    Actual = "Actual"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResultsConstraintType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{3A3A99EF-3315-42ac-80E3-0E64307353EA}",
            kind="enumeration",
        )
    )
