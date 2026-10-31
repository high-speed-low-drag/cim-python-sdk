"""CIM enumeration ResourceCertificationCategory (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResourceCertificationCategory(CimEnum):
    """CIM enumeration ResourceCertificationCategory."""

    DAM = "DAM"
    RTM = "RTM"
    RC = "RC"
    GT = "GT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResourceCertificationCategory",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{08242269-903E-4785-A027-5FB69930C2D8}",
            kind="enumeration",
        )
    )
