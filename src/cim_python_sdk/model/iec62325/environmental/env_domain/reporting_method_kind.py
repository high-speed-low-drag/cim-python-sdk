"""CIM enumeration ReportingMethodKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ReportingMethodKind(CimEnum):
    """Method by which information is gathered from station."""

    automated = "automated"
    queried = "queried"
    manual = "manual"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ReportingMethodKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{4CF94AE5-3B0A-4089-99C5-5AAB31F71603}",
            kind="enumeration",
        )
    )
