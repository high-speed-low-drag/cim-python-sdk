"""CIM enumeration SelfSchedTypeRawBid (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SelfSchedTypeRawBid(CimEnum):
    """CIM enumeration SelfSchedTypeRawBid."""

    PT = "PT"
    ETC = "ETC"
    TOR = "TOR"
    RMT = "RMT"
    SP = "SP"
    RA = "RA"
    BAS = "BAS"
    LOF = "LOF"
    WHL = "WHL"
    LPT = "LPT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SelfSchedTypeRawBid",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{77EE204F-678E-418c-8983-7CED48150194}",
            kind="enumeration",
        )
    )
