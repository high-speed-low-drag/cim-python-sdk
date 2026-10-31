"""CIM enumeration ApplicationSecurityKind (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ApplicationSecurityKind(CimEnum):
    """Specifies the expected security mechanism, per IEC 62351-4, to be utilized."""

    nonSecure = "nonSecure"
    secure = "secure"
    endToEndSecure = "endToEndSecure"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ApplicationSecurityKind",
            package="TC57CIM/IEC61970/Base/ICCPConfiguration",
            guid="{74D73777-3CA4-4c75-9275-F97BD3AD3097}",
            kind="enumeration",
        )
    )
