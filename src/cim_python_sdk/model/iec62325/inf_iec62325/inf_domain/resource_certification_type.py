"""CIM enumeration ResourceCertificationType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ResourceCertificationType(CimEnum):
    """CIM enumeration ResourceCertificationType."""

    GT = "GT"
    RG = "RG"
    SR = "SR"
    NR = "NR"
    IR = "IR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ResourceCertificationType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{BB1C814A-CBFB-4aa8-BF54-BBDFA7EB1C18}",
            kind="enumeration",
        )
    )
