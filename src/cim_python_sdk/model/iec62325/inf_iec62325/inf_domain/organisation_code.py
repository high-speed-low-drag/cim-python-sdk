"""CIM enumeration OrganisationCode (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OrganisationCode(CimEnum):
    """organization code"""

    BILL_TO = "BILL_TO"
    PAY_TO = "PAY_TO"
    SOLD_TO = "SOLD_TO"
    PROVIDED_BY = "PROVIDED_BY"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OrganisationCode",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{56C04FBA-90C5-4e50-9897-DFB5473A7EFC}",
            kind="enumeration",
        )
    )
