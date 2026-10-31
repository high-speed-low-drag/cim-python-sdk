"""CIM enumeration ApnodeType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ApnodeType(CimEnum):
    """Aggregate Node Types for example:

    AG - Aggregated Generation

    CPZ - Custom Price Zone

    DPZ - Default Price Zone

    LAP - Load Aggregation Point

    TH - Trading Hub

    SYS - System Zone

    CA - Control Area

    GA - generic aggregation

    EHV - 500 kV

    GH - generic hub

    ZN - zone

    INT - Interface

    BUS - Bus"""

    AG = "AG"
    CPZ = "CPZ"
    DPZ = "DPZ"
    TH = "TH"
    SYS = "SYS"
    CA = "CA"
    DCA = "DCA"
    GA = "GA"
    GH = "GH"
    EHV = "EHV"
    ZN = "ZN"
    INT = "INT"
    BUS = "BUS"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ApnodeType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{7634CAB9-E602-483a-91AC-EF3B8D693A66}",
            kind="enumeration",
        )
    )
