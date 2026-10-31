"""CIM class MktShuntCompensator (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.shunt_compensator import ShuntCompensator

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.shunt_compensator_dynamic_data import (
        ShuntCompensatorDynamicData,
    )


class MktShuntCompensator(ShuntCompensator):
    """Subclass of IEC 61970:Wires:ShuntCompensator."""

    __slots__ = ("_shunt_compensator_dynamic_data",)

    shunt_compensator_dynamic_data: Many[ShuntCompensatorDynamicData] = Many(
        EndMeta(
            name="shunt_compensator_dynamic_data",
            cim_role="ShuntCompensatorDynamicData",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.shunt_compensator_dynamic_data:ShuntCompensatorDynamicData",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_shunt_compensator",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktShuntCompensator",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{63B45A42-9F8C-4462-9CF9-194D2CA60E17}",
        ends=(shunt_compensator_dynamic_data.meta,),
    )

    def __init__(
        self,
        *,
        shunt_compensator_dynamic_data: Iterable[ShuntCompensatorDynamicData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if shunt_compensator_dynamic_data is not None:
            MktShuntCompensator.shunt_compensator_dynamic_data.extend(
                self, shunt_compensator_dynamic_data
            )

    def add_shunt_compensator_dynamic_data(
        self, shunt_compensator_dynamic_data: ShuntCompensatorDynamicData
    ) -> Self:
        return MktShuntCompensator.shunt_compensator_dynamic_data.add(
            self, shunt_compensator_dynamic_data
        )

    def remove_shunt_compensator_dynamic_data(
        self, shunt_compensator_dynamic_data: ShuntCompensatorDynamicData
    ) -> Self:
        return MktShuntCompensator.shunt_compensator_dynamic_data.remove(
            self, shunt_compensator_dynamic_data
        )

    def clear_shunt_compensator_dynamic_data(self) -> Self:
        return MktShuntCompensator.shunt_compensator_dynamic_data.clear(self)

    def num_shunt_compensator_dynamic_data(self) -> int:
        return MktShuntCompensator.shunt_compensator_dynamic_data.count(self)
