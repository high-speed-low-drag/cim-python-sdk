"""CIM enumeration AreaControlMode (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AreaControlMode(CimEnum):
    """Area's present control mode."""

    CF = "CF"
    CTL = "CTL"
    TLB = "TLB"
    OFF = "OFF"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AreaControlMode",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{3B815580-37E3-4f7e-A282-D2762848B2C8}",
            kind="enumeration",
        )
    )
