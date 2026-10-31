"""CIM enumeration SinglePhaseKind (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SinglePhaseKind(CimEnum):
    """Enumeration of single phase identifiers. Allows designation of single phases for both
    transmission and distribution equipment, circuits and loads."""

    A = "A"
    B = "B"
    C = "C"
    N = "N"
    s1 = "s1"
    s2 = "s2"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SinglePhaseKind",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{0AD52D65-4270-45c1-9AF4-29C53A398AE3}",
            kind="enumeration",
        )
    )
