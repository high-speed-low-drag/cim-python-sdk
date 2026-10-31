"""CIM enumeration DAMMarketType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DAMMarketType(CimEnum):
    """CIM enumeration DAMMarketType."""

    DAM = "DAM"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DAMMarketType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{6C25932E-59FB-4c48-88A5-021742E5127D}",
            kind="enumeration",
        )
    )
