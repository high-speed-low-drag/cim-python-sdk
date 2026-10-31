"""CIM enumeration SelfSchedReferenceType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SelfSchedReferenceType(CimEnum):
    """Indication of which type of self schedule is being referenced."""

    ETC = "ETC"
    TOR = "TOR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SelfSchedReferenceType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{CE41E713-4E36-4980-A41D-DB7426A83045}",
            kind="enumeration",
        )
    )
