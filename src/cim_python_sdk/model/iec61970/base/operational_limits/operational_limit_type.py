"""CIM class OperationalLimitType (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.european.ext_iec61970.ext_eu_base.ext_eu_operational_limits.limit_kind import (
        LimitKind,
    )
    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import (
        OperationalLimit,
    )
    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit_direction_kind import (
        OperationalLimitDirectionKind,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.operatonal_limit_type_scaling import (
        OperatonalLimitTypeScaling,
    )


class OperationalLimitType(IdentifiedObject):
    """The operational meaning of a category of limits."""

    __slots__ = (
        "_operational_limit",
        "_source_operational_limit_type_scaling",
        "_target_operational_limitm_type_scaling",
        "acceptable_duration",
        "direction",
        "is_infinite_duration",
        "kind",
    )

    acceptable_duration: float | None  # Seconds
    direction: OperationalLimitDirectionKind | None
    is_infinite_duration: bool | None
    kind: LimitKind | None

    target_operational_limitm_type_scaling: One[OperatonalLimitTypeScaling] = One(
        EndMeta(
            name="target_operational_limitm_type_scaling",
            cim_role="TargetOperationalLimitmTypeScaling",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.operatonal_limit_type_scaling:OperatonalLimitTypeScaling",
            many=False,
            lower=0,
            upper=1,
            inverse="target_operational_limit",
            aggregation="none",
        )
    )
    source_operational_limit_type_scaling: Many[OperatonalLimitTypeScaling] = Many(
        EndMeta(
            name="source_operational_limit_type_scaling",
            cim_role="SourceOperationalLimitTypeScaling",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.operatonal_limit_type_scaling:OperatonalLimitTypeScaling",
            many=True,
            lower=0,
            upper=None,
            inverse="source_operational_limit_type",
            aggregation="none",
        )
    )
    operational_limit: Many[OperationalLimit] = Many(
        EndMeta(
            name="operational_limit",
            cim_role="OperationalLimit",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit:OperationalLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="operational_limit_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperationalLimitType",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{B5E14C75-6C8D-4e7e-9FAF-D49F3BE177B9}",
        attributes=(
            AttrMeta("acceptable_duration", "acceptableDuration", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta(
                "direction", "direction", "OperationalLimitDirectionKind", 0, 1, "enumeration"
            ),
            AttrMeta("is_infinite_duration", "isInfiniteDuration", "bool", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "LimitKind", 0, 1, "enumeration", namespace="eu"),
        ),
        ends=(
            target_operational_limitm_type_scaling.meta,
            source_operational_limit_type_scaling.meta,
            operational_limit.meta,
        ),
    )

    def __init__(
        self,
        *,
        acceptable_duration: float | None = None,
        direction: OperationalLimitDirectionKind | None = None,
        is_infinite_duration: bool | None = None,
        kind: LimitKind | None = None,
        target_operational_limitm_type_scaling: OperatonalLimitTypeScaling | None = None,
        source_operational_limit_type_scaling: Iterable[OperatonalLimitTypeScaling] | None = None,
        operational_limit: Iterable[OperationalLimit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.acceptable_duration = acceptable_duration
        self.direction = direction
        self.is_infinite_duration = is_infinite_duration
        self.kind = kind
        if target_operational_limitm_type_scaling is not None:
            self.target_operational_limitm_type_scaling = target_operational_limitm_type_scaling
        if source_operational_limit_type_scaling is not None:
            OperationalLimitType.source_operational_limit_type_scaling.extend(
                self, source_operational_limit_type_scaling
            )
        if operational_limit is not None:
            OperationalLimitType.operational_limit.extend(self, operational_limit)

    def add_source_operational_limit_type_scaling(
        self, source_operational_limit_type_scaling: OperatonalLimitTypeScaling
    ) -> Self:
        return OperationalLimitType.source_operational_limit_type_scaling.add(
            self, source_operational_limit_type_scaling
        )

    def remove_source_operational_limit_type_scaling(
        self, source_operational_limit_type_scaling: OperatonalLimitTypeScaling
    ) -> Self:
        return OperationalLimitType.source_operational_limit_type_scaling.remove(
            self, source_operational_limit_type_scaling
        )

    def clear_source_operational_limit_type_scaling(self) -> Self:
        return OperationalLimitType.source_operational_limit_type_scaling.clear(self)

    def num_source_operational_limit_type_scaling(self) -> int:
        return OperationalLimitType.source_operational_limit_type_scaling.count(self)

    def add_operational_limit(self, operational_limit: OperationalLimit) -> Self:
        return OperationalLimitType.operational_limit.add(self, operational_limit)

    def remove_operational_limit(self, operational_limit: OperationalLimit) -> Self:
        return OperationalLimitType.operational_limit.remove(self, operational_limit)

    def clear_operational_limit(self) -> Self:
        return OperationalLimitType.operational_limit.clear(self)

    def num_operational_limit(self) -> int:
        return OperationalLimitType.operational_limit.count(self)

    def get_operational_limit_by_mrid(self, mrid: str) -> OperationalLimit | None:
        return OperationalLimitType.operational_limit.get_by_mrid(self, mrid)
