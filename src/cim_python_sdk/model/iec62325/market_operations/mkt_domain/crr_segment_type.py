"""CIM enumeration CRRSegmentType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CRRSegmentType(CimEnum):
    """Type of the CRR, from the possible type definitions in the CRR System (e.g. 'LSE',
    'ETC')."""

    AUC = "AUC"
    CAP = "CAP"
    CF = "CF"
    CVR = "CVR"
    ETC = "ETC"
    LSE = "LSE"
    MT = "MT"
    TOR = "TOR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CRRSegmentType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{B5915675-DD90-4e4c-BEF1-5C121B762665}",
            kind="enumeration",
        )
    )
