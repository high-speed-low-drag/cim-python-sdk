"""CIM enumeration FlowDirectionType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FlowDirectionType(CimEnum):
    """Specifies the direction of energy flow in the flowgate."""

    Forward = "Forward"
    Reverse = "Reverse"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FlowDirectionType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{19F19F68-B788-471e-8349-A3EDF95BEE79}",
            kind="enumeration",
        )
    )
