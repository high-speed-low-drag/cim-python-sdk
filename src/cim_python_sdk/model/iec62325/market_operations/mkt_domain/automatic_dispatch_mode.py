"""CIM enumeration AutomaticDispatchMode (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AutomaticDispatchMode(CimEnum):
    """Automatic Dispatch mode."""

    INTERVAL = "INTERVAL"
    CONTINGENCY = "CONTINGENCY"
    MANUAL = "MANUAL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AutomaticDispatchMode",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{C910FC36-D192-46e2-8291-BB9D98E27DF0}",
            kind="enumeration",
        )
    )
