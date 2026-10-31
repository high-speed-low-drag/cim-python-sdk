"""CIM enumeration UncertaintyKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UncertaintyKind(CimEnum):
    """The type of uncertainty for a reading."""

    standard = "standard"
    interpolated = "interpolated"
    estimated = "estimated"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UncertaintyKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{1CFCF12A-F6AE-4d4e-82F5-3B2358D2340D}",
            kind="enumeration",
        )
    )
