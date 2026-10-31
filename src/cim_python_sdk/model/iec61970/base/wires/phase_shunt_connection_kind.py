"""CIM enumeration PhaseShuntConnectionKind (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PhaseShuntConnectionKind(CimEnum):
    """The configuration of phase connections for a single terminal device such as a load or
    capacitor."""

    D = "D"
    Y = "Y"
    Yn = "Yn"
    I = "I"
    G = "G"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PhaseShuntConnectionKind",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{5DE5A24B-B6E5-4f26-890B-6906EB2213C8}",
            kind="enumeration",
        )
    )
