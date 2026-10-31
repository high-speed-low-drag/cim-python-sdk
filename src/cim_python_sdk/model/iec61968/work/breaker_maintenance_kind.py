"""CIM enumeration BreakerMaintenanceKind (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BreakerMaintenanceKind(CimEnum):
    """Possible types of breaker maintenance work."""

    externalOutOfService = "externalOutOfService"
    internalOutOfService = "internalOutOfService"
    interrupterOverhaul = "interrupterOverhaul"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BreakerMaintenanceKind",
            package="TC57CIM/IEC61968/Work",
            guid="{0CFB19E4-A310-4416-A6E2-F8E722D12350}",
            kind="enumeration",
        )
    )
