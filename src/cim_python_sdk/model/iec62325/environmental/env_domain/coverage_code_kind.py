"""CIM enumeration CoverageCodeKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CoverageCodeKind(CimEnum):
    """Kinds of weather condition coverage."""

    brief = "brief"
    frequent = "frequent"
    intermittant = "intermittant"
    isolated = "isolated"
    numerous = "numerous"
    occasional = "occasional"
    partly = "partly"
    patchy = "patchy"
    periodsOf = "periodsOf"
    scattered = "scattered"
    widespread = "widespread"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CoverageCodeKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{20BCE8A9-2982-4817-B8C5-01F2991E1617}",
            kind="enumeration",
        )
    )
