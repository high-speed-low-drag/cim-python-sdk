"""CIM enumeration CustomerBillingKind (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CustomerBillingKind(CimEnum):
    """Kind of customer billing."""

    consolidatedEss = "consolidatedEss"
    consolidatedUdc = "consolidatedUdc"
    separateEssUdc = "separateEssUdc"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CustomerBillingKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
            guid="{65173887-4B95-4890-A0B9-32C0303EEB2C}",
            kind="enumeration",
        )
    )
