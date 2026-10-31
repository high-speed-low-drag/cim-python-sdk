"""CIM class OperationalLimitSet (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.acdc_terminal import ACDCTerminal
    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.base.operational_limits.operational_limit import (
        OperationalLimit,
    )


class OperationalLimitSet(IdentifiedObject):
    """A set of limits associated with equipment. Sets of limits might apply to a specific
    temperature, or season for example. A set of limits may contain different severities of
    limit levels that would apply to the same equipment. The set may contain limits of
    different types such as apparent power and current limits or high and low voltage limits
    that are logically applied together as a set."""

    __slots__ = ("_equipment", "_operational_limit_value", "_terminal")

    operational_limit_value: Many[OperationalLimit] = Many(
        EndMeta(
            name="operational_limit_value",
            cim_role="OperationalLimitValue",
            target="cim_python_sdk.model.iec61970.base.operational_limits.operational_limit:OperationalLimit",
            many=True,
            lower=0,
            upper=None,
            inverse="operational_limit_set",
            aggregation="shared",
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
            inverse="operational_limit_set",
            aggregation="none",
        )
    )
    terminal: One[ACDCTerminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.acdc_terminal:ACDCTerminal",
            many=False,
            lower=0,
            upper=1,
            inverse="operational_limit_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperationalLimitSet",
        package="TC57CIM/IEC61970/Base/OperationalLimits",
        guid="{B0D1133E-CFA4-467d-81D1-75719BF02976}",
        ends=(
            operational_limit_value.meta,
            equipment.meta,
            terminal.meta,
        ),
    )

    def __init__(
        self,
        *,
        operational_limit_value: Iterable[OperationalLimit] | None = None,
        equipment: Equipment | None = None,
        terminal: ACDCTerminal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if operational_limit_value is not None:
            OperationalLimitSet.operational_limit_value.extend(self, operational_limit_value)
        if equipment is not None:
            self.equipment = equipment
        if terminal is not None:
            self.terminal = terminal

    def add_operational_limit_value(self, operational_limit_value: OperationalLimit) -> Self:
        return OperationalLimitSet.operational_limit_value.add(self, operational_limit_value)

    def remove_operational_limit_value(self, operational_limit_value: OperationalLimit) -> Self:
        return OperationalLimitSet.operational_limit_value.remove(self, operational_limit_value)

    def clear_operational_limit_value(self) -> Self:
        return OperationalLimitSet.operational_limit_value.clear(self)

    def num_operational_limit_value(self) -> int:
        return OperationalLimitSet.operational_limit_value.count(self)

    def get_operational_limit_value_by_mrid(self, mrid: str) -> OperationalLimit | None:
        return OperationalLimitSet.operational_limit_value.get_by_mrid(self, mrid)
