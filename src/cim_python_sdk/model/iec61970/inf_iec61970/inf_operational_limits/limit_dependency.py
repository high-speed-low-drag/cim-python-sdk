"""CIM class LimitDependency (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import (
        OperationalLimit,
    )


class LimitDependency(IdentifiedObject):
    """A limit calculation model used to compute an operational limit based on external input
    such as temperature. These are intended to be shared among operational limits with the
    same calculation form that apply to a piece of equipment.."""

    __slots__ = ("_equipment", "_operational_limit")

    operational_limit: Many[OperationalLimit] = Many(
        EndMeta(
            name="operational_limit",
            cim_role="OperationalLimit",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit:OperationalLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="limit_dependency_model",
            aggregation="none",
        )
    )
    equipment: One[Equipment] = One(
        EndMeta(
            name="equipment",
            cim_role="Equipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=False,
            lower=0,
            upper=1,
            inverse="limit_dependency_model",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LimitDependency",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{B2593470-2C8B-4b8e-B88E-5C9B177172DB}",
        ends=(
            operational_limit.meta,
            equipment.meta,
        ),
    )

    def __init__(
        self,
        *,
        operational_limit: Iterable[OperationalLimit] | None = None,
        equipment: Equipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if operational_limit is not None:
            LimitDependency.operational_limit.extend(self, operational_limit)
        if equipment is not None:
            self.equipment = equipment

    def add_operational_limit(self, operational_limit: OperationalLimit) -> Self:
        return LimitDependency.operational_limit.add(self, operational_limit)

    def remove_operational_limit(self, operational_limit: OperationalLimit) -> Self:
        return LimitDependency.operational_limit.remove(self, operational_limit)

    def clear_operational_limit(self) -> Self:
        return LimitDependency.operational_limit.clear(self)

    def num_operational_limit(self) -> int:
        return LimitDependency.operational_limit.count(self)

    def get_operational_limit_by_mrid(self, mrid: str) -> OperationalLimit | None:
        return LimitDependency.operational_limit.get_by_mrid(self, mrid)
