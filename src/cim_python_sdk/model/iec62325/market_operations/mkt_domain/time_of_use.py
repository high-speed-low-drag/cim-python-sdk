"""CIM enumeration TimeOfUse (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TimeOfUse(CimEnum):
    """Time of Use used by a CRR definition for specifying the time the CRR spans. ON - CRR
    spans the on peak hours of the day, OFF - CRR spans the off peak hours of the day, 24HR
    - CRR spans the entire day."""

    ON = "ON"
    OFF = "OFF"
    v24HR = "24HR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TimeOfUse",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{95168B2D-6BDF-4442-99C0-C7C729EA8BC0}",
            kind="enumeration",
        )
    )
