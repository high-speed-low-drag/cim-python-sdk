"""CIM class OperatingMechanism (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.interrupter_unit import InterrupterUnit


class OperatingMechanism(Asset):
    """Breaker mechanism."""

    __slots__ = ("_interrupter_unit",)

    interrupter_unit: Many[InterrupterUnit] = Many(
        EndMeta(
            name="interrupter_unit",
            cim_role="InterrupterUnit",
            target="cim_python_sdk.model.iec61968.assets.interrupter_unit:InterrupterUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="operating_mechanism",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperatingMechanism",
        package="TC57CIM/IEC61968/Assets",
        guid="{7467E313-35CE-4845-9B1E-F4D19D77CE46}",
        ends=(interrupter_unit.meta,),
    )

    def __init__(
        self,
        *,
        interrupter_unit: Iterable[InterrupterUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if interrupter_unit is not None:
            OperatingMechanism.interrupter_unit.extend(self, interrupter_unit)

    def add_interrupter_unit(self, interrupter_unit: InterrupterUnit) -> Self:
        return OperatingMechanism.interrupter_unit.add(self, interrupter_unit)

    def remove_interrupter_unit(self, interrupter_unit: InterrupterUnit) -> Self:
        return OperatingMechanism.interrupter_unit.remove(self, interrupter_unit)

    def clear_interrupter_unit(self) -> Self:
        return OperatingMechanism.interrupter_unit.clear(self)

    def num_interrupter_unit(self) -> int:
        return OperatingMechanism.interrupter_unit.count(self)

    def get_interrupter_unit_by_mrid(self, mrid: str) -> InterrupterUnit | None:
        return OperatingMechanism.interrupter_unit.get_by_mrid(self, mrid)
