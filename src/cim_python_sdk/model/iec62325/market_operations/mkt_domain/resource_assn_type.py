"""CIM enumeration ResourceAssnType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResourceAssnType(CimEnum):
    """For example:

    Asset Owner Sink designator for use by CRR

    Asset Owner Source designator for use by CRR

    Reliability Must Run

    Scheduling Coordinator

    Load Serving Entity"""

    CSNK = "CSNK"
    CSRC = "CSRC"
    RMR = "RMR"
    SC = "SC"
    LSE = "LSE"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResourceAssnType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{0A9B91BC-AD35-4990-A8BA-CC4401EA8032}",
            kind="enumeration",
        )
    )
