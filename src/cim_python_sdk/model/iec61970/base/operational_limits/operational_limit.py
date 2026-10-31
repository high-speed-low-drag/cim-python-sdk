"""CIM class OperationalLimit (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_set import (
        OperationalLimitSet,
    )
    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_type import (
        OperationalLimitType,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency import (
        LimitDependency,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_scaling_limit import (
        LimitScalingLimit,
    )


class OperationalLimit(IdentifiedObject):
    """A value and normal value associated with a specific kind of limit.

    The sub class value and normalValue attributes vary inversely to the associated
    OperationalLimitType.acceptableDuration (acceptableDuration for short).

    If a particular piece of equipment has multiple operational limits of the same kind
    (apparent power, current, etc.), the limit with the greatest acceptableDuration shall
    have the smallest limit value and the limit with the smallest acceptableDuration shall
    have the largest limit value. Note: A large current can only be allowed to flow through
    a piece of equipment for a short duration without causing damage, but a lesser current
    can be allowed to flow for a longer duration."""

    __slots__ = (
        "_limit_dependency_model",
        "_limit_scaling_limit",
        "_operational_limit_set",
        "_operational_limit_type",
    )

    limit_scaling_limit: Many[LimitScalingLimit] = Many(
        EndMeta(
            name="limit_scaling_limit",
            cim_role="LimitScalingLimit",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_scaling_limit:LimitScalingLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="source_operational_limit",
            aggregation="none",
        )
    )
    operational_limit_set: One[OperationalLimitSet] = One(
        EndMeta(
            name="operational_limit_set",
            cim_role="OperationalLimitSet",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_set:OperationalLimitSet",
            many=False,
            lower=1,
            upper=1,
            inverse="operational_limit_value",
            aggregation="none",
        )
    )
    limit_dependency_model: Many[LimitDependency] = Many(
        EndMeta(
            name="limit_dependency_model",
            cim_role="LimitDependencyModel",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.limit_dependency:LimitDependency",
            many=True,
            lower=0,
            upper=None,
            inverse="operational_limit",
            aggregation="none",
        )
    )
    operational_limit_type: One[OperationalLimitType] = One(
        EndMeta(
            name="operational_limit_type",
            cim_role="OperationalLimitType",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_type:OperationalLimitType",
            many=False,
            lower=0,
            upper=1,
            inverse="operational_limit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperationalLimit",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{2E614D04-0107-4d78-B959-28ECD475219C}",
        ends=(
            limit_scaling_limit.meta,
            operational_limit_set.meta,
            limit_dependency_model.meta,
            operational_limit_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        limit_scaling_limit: Iterable[LimitScalingLimit] | None = None,
        operational_limit_set: OperationalLimitSet | None = None,
        limit_dependency_model: Iterable[LimitDependency] | None = None,
        operational_limit_type: OperationalLimitType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if limit_scaling_limit is not None:
            OperationalLimit.limit_scaling_limit.extend(self, limit_scaling_limit)
        if operational_limit_set is not None:
            self.operational_limit_set = operational_limit_set
        if limit_dependency_model is not None:
            OperationalLimit.limit_dependency_model.extend(self, limit_dependency_model)
        if operational_limit_type is not None:
            self.operational_limit_type = operational_limit_type

    def add_limit_scaling_limit(self, limit_scaling_limit: LimitScalingLimit) -> Self:
        return OperationalLimit.limit_scaling_limit.add(self, limit_scaling_limit)

    def remove_limit_scaling_limit(self, limit_scaling_limit: LimitScalingLimit) -> Self:
        return OperationalLimit.limit_scaling_limit.remove(self, limit_scaling_limit)

    def clear_limit_scaling_limit(self) -> Self:
        return OperationalLimit.limit_scaling_limit.clear(self)

    def num_limit_scaling_limit(self) -> int:
        return OperationalLimit.limit_scaling_limit.count(self)

    def get_limit_scaling_limit_by_mrid(self, mrid: str) -> LimitScalingLimit | None:
        return OperationalLimit.limit_scaling_limit.get_by_mrid(self, mrid)

    def add_limit_dependency_model(self, limit_dependency_model: LimitDependency) -> Self:
        return OperationalLimit.limit_dependency_model.add(self, limit_dependency_model)

    def remove_limit_dependency_model(self, limit_dependency_model: LimitDependency) -> Self:
        return OperationalLimit.limit_dependency_model.remove(self, limit_dependency_model)

    def clear_limit_dependency_model(self) -> Self:
        return OperationalLimit.limit_dependency_model.clear(self)

    def num_limit_dependency_model(self) -> int:
        return OperationalLimit.limit_dependency_model.count(self)

    def get_limit_dependency_model_by_mrid(self, mrid: str) -> LimitDependency | None:
        return OperationalLimit.limit_dependency_model.get_by_mrid(self, mrid)
