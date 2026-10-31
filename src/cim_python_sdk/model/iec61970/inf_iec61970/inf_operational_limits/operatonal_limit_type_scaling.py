"""CIM class OperatonalLimitTypeScaling (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_type import (
        OperationalLimitType,
    )


class OperatonalLimitTypeScaling(CimObject):
    """One operational limit type scales values of another operational limit type when under
    the same operational limit set. This applies to any operational limit assigned to the
    target operational limit type and without other limit dependency models."""

    __slots__ = ("_source_operational_limit_type", "_target_operational_limit", "scaling_percent")

    scaling_percent: float | None  # PerCent

    target_operational_limit: One[OperationalLimitType] = One(
        EndMeta(
            name="target_operational_limit",
            cim_role="TargetOperationalLimit",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_type:OperationalLimitType",
            many=False,
            lower=1,
            upper=1,
            inverse="target_operational_limitm_type_scaling",
            aggregation="none",
        )
    )
    source_operational_limit_type: One[OperationalLimitType] = One(
        EndMeta(
            name="source_operational_limit_type",
            cim_role="SourceOperationalLimitType",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_type:OperationalLimitType",
            many=False,
            lower=0,
            upper=1,
            inverse="source_operational_limit_type_scaling",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperatonalLimitTypeScaling",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{E75CE86C-80F7-43b3-A52B-45D4D28093FC}",
        attributes=(AttrMeta("scaling_percent", "scalingPercent", "PerCent", 0, 1, "cimdatatype"),),
        ends=(
            target_operational_limit.meta,
            source_operational_limit_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        scaling_percent: float | None = None,
        target_operational_limit: OperationalLimitType | None = None,
        source_operational_limit_type: OperationalLimitType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.scaling_percent = scaling_percent
        if target_operational_limit is not None:
            self.target_operational_limit = target_operational_limit
        if source_operational_limit_type is not None:
            self.source_operational_limit_type = source_operational_limit_type
