"""CIM enumeration DependencyKind (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DependencyKind(CimEnum):
    """CIM enumeration DependencyKind."""

    mutuallyExclusive = "mutuallyExclusive"
    required = "required"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DependencyKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
            guid="{52E660F3-5A5F-4947-8252-DF6466A00B0B}",
            kind="enumeration",
        )
    )
