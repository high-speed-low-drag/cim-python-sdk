"""CIM enumeration EnergyTypeKind (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EnergyTypeKind(CimEnum):
    """CIM enumeration EnergyTypeKind."""

    PVpark = "PVpark"
    WindPark = "WindPark"
    ConsumerLoad = "ConsumerLoad"
    IndustrialLoad = "IndustrialLoad"
    Other = "Other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EnergyTypeKind",
            package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
            guid="{1D7EE73C-8476-40c6-B2B9-10BA57199D7A}",
            kind="enumeration",
        )
    )
