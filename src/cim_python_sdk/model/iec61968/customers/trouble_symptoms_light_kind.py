"""CIM enumeration TroubleSymptomsLightKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleSymptomsLightKind(CimEnum):
    """The list of values that define the light problem."""

    ok = "ok"
    allOut = "allOut"
    partOut = "partOut"
    flickering = "flickering"
    dim = "dim"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleSymptomsLightKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{FC32DC68-B564-43e0-8CBB-221DC8793611}",
            kind="enumeration",
        )
    )
