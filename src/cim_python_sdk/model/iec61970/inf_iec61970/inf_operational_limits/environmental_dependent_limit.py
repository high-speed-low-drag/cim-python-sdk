"""CIM class EnvironmentalDependentLimit (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency import (
    LimitDependency,
)


class EnvironmentalDependentLimit(LimitDependency):
    """This is a environmental based limit dependency model for calculating operational limits."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalDependentLimit",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{E2741DD1-E9F5-4abd-B45E-8EA808647E09}",
    )
