"""CIM enumeration MPMTestMethodType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MPMTestMethodType(CimEnum):
    """Market power mitigation test method type.

    Tests with the normal (default) thresholds or tests with the alternate thresholds."""

    NORMAL = "NORMAL"
    ALTERNATE = "ALTERNATE"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MPMTestMethodType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{E789C4C4-C240-4a01-88F8-DDE49392EE31}",
            kind="enumeration",
        )
    )
