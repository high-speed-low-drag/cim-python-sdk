"""CIM class ServiceMultiplier (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.service_multiplier_kind import ServiceMultiplierKind
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint


class ServiceMultiplier(IdentifiedObject):
    """Multiplier applied at the usage point."""

    __slots__ = ("_usage_point", "kind", "value")

    kind: ServiceMultiplierKind | None
    value: float | None

    usage_point: One[UsagePoint] = One(
        EndMeta(
            name="usage_point",
            cim_role="UsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="service_multipliers",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ServiceMultiplier",
        package="TC57CIM/IEC61968/Metering",
        guid="{64F18056-C8A2-4d2c-9A6B-ABA98536ED37}",
        attributes=(
            AttrMeta("kind", "kind", "ServiceMultiplierKind", 0, 1, "enumeration"),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
        ends=(usage_point.meta,),
    )

    def __init__(
        self,
        *,
        kind: ServiceMultiplierKind | None = None,
        value: float | None = None,
        usage_point: UsagePoint | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.value = value
        if usage_point is not None:
            self.usage_point = usage_point
