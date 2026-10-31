"""CIM enumeration LocationKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LocationKind(CimEnum):
    """The nature of the location being defined for an environmental entity. Possible values
    are center, perimeter, primary, secondary."""

    center = "center"
    extent = "extent"
    primary = "primary"
    secondary = "secondary"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LocationKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{D661E2A1-1ABC-4c6c-9422-08455FFE3715}",
            kind="enumeration",
        )
    )
