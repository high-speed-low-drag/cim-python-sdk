"""CIM enumeration SelfSchedTypeCleanBid (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SelfSchedTypeCleanBid(CimEnum):
    """CIM enumeration SelfSchedTypeCleanBid."""

    PT = "PT"
    ETC = "ETC"
    TOR = "TOR"
    RMT = "RMT"
    SP = "SP"
    RA = "RA"
    IFM = "IFM"
    BAS = "BAS"
    LOF = "LOF"
    WHL = "WHL"
    LPT = "LPT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SelfSchedTypeCleanBid",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{F93913DC-9FD9-4954-85C4-2BCA478D06F7}",
            kind="enumeration",
        )
    )
