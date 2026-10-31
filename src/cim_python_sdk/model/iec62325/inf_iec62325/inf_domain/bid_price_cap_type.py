"""CIM enumeration BidPriceCapType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BidPriceCapType(CimEnum):
    """CIM enumeration BidPriceCapType."""

    ENERGY = "ENERGY"
    AS = "AS"
    RUC = "RUC"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BidPriceCapType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{C9A65772-C08E-42ec-93A1-86FDBA50AD29}",
            kind="enumeration",
        )
    )
