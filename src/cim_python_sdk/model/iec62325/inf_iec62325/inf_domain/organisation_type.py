"""CIM enumeration OrganisationType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OrganisationType(CimEnum):
    """organization type"""

    CUSTOMER = "CUSTOMER"
    RTO = "RTO"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OrganisationType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{1CB85EEA-8552-4683-96A2-CE5D796C6ECE}",
            kind="enumeration",
        )
    )
