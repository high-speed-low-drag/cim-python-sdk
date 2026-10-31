"""CIM enumeration DispatchTransactionType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DispatchTransactionType(CimEnum):
    """CIM enumeration DispatchTransactionType."""

    Purchase = "Purchase"
    Sale = "Sale"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DispatchTransactionType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{91B09035-05A0-4374-AD01-9B8DE8B5B204}",
            kind="enumeration",
        )
    )
