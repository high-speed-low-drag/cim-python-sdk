"""CIM enumeration BreakerConfiguration (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BreakerConfiguration(CimEnum):
    """Switching arrangement for bay."""

    singleBreaker = "singleBreaker"
    breakerAndAHalf = "breakerAndAHalf"
    doubleBreaker = "doubleBreaker"
    noBreaker = "noBreaker"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BreakerConfiguration",
            package="TC57CIM/IEC61970/Base/Core",
            guid="{39D7FD4A-0CE4-41e0-B792-B4F546674C1C}",
            kind="enumeration",
        )
    )
