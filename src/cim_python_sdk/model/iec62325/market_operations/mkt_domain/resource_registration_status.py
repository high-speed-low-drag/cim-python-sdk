"""CIM enumeration ResourceRegistrationStatus (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResourceRegistrationStatus(CimEnum):
    """Types of resource registration status, for example:

    Active

    Mothballed

    Planned

    Decommissioned"""

    Active = "Active"
    Planned = "Planned"
    Mothballed = "Mothballed"
    Decommissioned = "Decommissioned"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResourceRegistrationStatus",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{C19F80AC-7457-4a2e-8AFE-481193821C55}",
            kind="enumeration",
        )
    )
