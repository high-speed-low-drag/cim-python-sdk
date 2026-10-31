"""CIM enumeration SwitchStatusType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SwitchStatusType(CimEnum):
    """Circuit Breaker Status (closed or open) of the circuit breaker."""

    Closed = "Closed"
    Open = "Open"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SwitchStatusType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{7D3C1DA0-2B00-486c-A8BC-6A284EF41DAC}",
            kind="enumeration",
        )
    )
