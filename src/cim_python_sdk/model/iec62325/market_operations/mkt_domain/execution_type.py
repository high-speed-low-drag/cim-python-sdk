"""CIM enumeration ExecutionType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ExecutionType(CimEnum):
    """Execution types of Market Runs."""

    DA = "DA"
    HASP = "HASP"
    RTPD = "RTPD"
    RTD = "RTD"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ExecutionType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{B5E8F179-7284-425b-B1EA-41102D76AD66}",
            kind="enumeration",
        )
    )
