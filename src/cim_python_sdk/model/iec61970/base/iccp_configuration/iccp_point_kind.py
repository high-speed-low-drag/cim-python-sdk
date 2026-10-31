"""CIM enumeration ICCPPointKind (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ICCPPointKind(CimEnum):
    """The kind of ICCP point that is to be conveyed."""

    discrete = "discrete"
    real = "real"
    state = "state"
    stateSupplemental = "stateSupplemental"
    singleProtectionEvent = "singleProtectionEvent"
    packedProtectionEvent = "packedProtectionEvent"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ICCPPointKind",
            package="TC57CIM/IEC61970/Base/ICCPConfiguration",
            guid="{00C531A3-C3C1-4c30-97C3-1419D06F0B15}",
            kind="enumeration",
        )
    )
