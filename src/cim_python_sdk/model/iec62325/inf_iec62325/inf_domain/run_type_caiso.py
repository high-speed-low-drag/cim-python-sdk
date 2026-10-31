"""CIM enumeration runTypeCAISO (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class runTypeCAISO(CimEnum):
    """S - Scheduling

    P - Pricing"""

    S = "S"
    P = "P"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="runTypeCAISO",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{C308C5FD-C74E-449c-848B-CDF8778016B6}",
            kind="enumeration",
        )
    )
