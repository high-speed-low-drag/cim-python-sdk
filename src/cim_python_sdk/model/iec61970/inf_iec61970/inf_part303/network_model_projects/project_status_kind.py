"""CIM enumeration ProjectStatusKind (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ProjectStatusKind(CimEnum):
    """CIM enumeration ProjectStatusKind."""

    draft = "draft"
    cancelled = "cancelled"
    frozen = "frozen"
    closed = "closed"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ProjectStatusKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
            guid="{1EAAE124-6945-4d0e-977D-1D4C5A1A3E6B}",
            kind="enumeration",
        )
    )
