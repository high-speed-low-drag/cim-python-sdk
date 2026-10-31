"""CIM enumeration RampCurveType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RampCurveType(CimEnum):
    """For example:

    0 - Fixed ramp rate independent of rate function unit MW output

    1 - Static ramp rates as a function of unit MW output only

    2 - Dynamic ramp rates as a function of unit MW output and ramping time"""

    v0 = "0"
    v1 = "1"
    v2 = "2"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RampCurveType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{53370A5E-4445-4ab9-BB26-5FAF551BA6E6}",
            kind="enumeration",
        )
    )
