"""CIM class LimitScalingLimit (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency import (
    LimitDependency,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import (
        OperationalLimit,
    )


class LimitScalingLimit(LimitDependency):
    """Specifies an operational limit is calculated by scaling another operational limit."""

    __slots__ = ("_source_operational_limit", "limit_scaling_percent")

    limit_scaling_percent: float | None  # PerCent

    source_operational_limit: One[OperationalLimit] = One(
        EndMeta(
            name="source_operational_limit",
            cim_role="SourceOperationalLimit",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit:OperationalLimit",
            many=False,
            lower=1,
            upper=1,
            inverse="limit_scaling_limit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LimitScalingLimit",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{8E9F6A36-A81C-4cc7-BD92-738BE123B1F5}",
        attributes=(
            AttrMeta(
                "limit_scaling_percent", "limitScalingPercent", "PerCent", 0, 1, "cimdatatype"
            ),
        ),
        ends=(source_operational_limit.meta,),
    )

    def __init__(
        self,
        *,
        limit_scaling_percent: float | None = None,
        source_operational_limit: OperationalLimit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.limit_scaling_percent = limit_scaling_percent
        if source_operational_limit is not None:
            self.source_operational_limit = source_operational_limit
