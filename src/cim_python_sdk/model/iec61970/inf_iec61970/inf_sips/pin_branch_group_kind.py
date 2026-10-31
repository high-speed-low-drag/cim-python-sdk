"""CIM enumeration PinBranchGroupKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PinBranchGroupKind(CimEnum):
    """Categorisation of type of compare done on a branch group."""

    activePower = "activePower"
    reactivePower = "reactivePower"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PinBranchGroupKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{EB08D837-948F-439c-A26F-97F411BB2EE4}",
            kind="enumeration",
        )
    )
