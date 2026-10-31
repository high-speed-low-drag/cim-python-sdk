"""CIM enumeration CurrentStatusSC (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CurrentStatusSC(CimEnum):
    """ACTIVE

    INACTIVE"""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CurrentStatusSC",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{C4ED7836-B4AF-45a0-B462-99137A351CA9}",
            kind="enumeration",
        )
    )
