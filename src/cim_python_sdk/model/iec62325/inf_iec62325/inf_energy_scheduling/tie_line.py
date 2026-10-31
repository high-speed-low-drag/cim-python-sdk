"""CIM class TieLine (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.control_area_operator import (
        ControlAreaOperator,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.customer_consumer import (
        CustomerConsumer,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction import (
        EnergyTransaction,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class TieLine(IdentifiedObject):
    """CIM class TieLine."""

    __slots__ = (
        "_energy_transaction",
        "_parent_of_a",
        "_parent_of_b",
        "_side_a_sub_control_area",
        "_side_b_sub_control_area",
    )

    parent_of_a: Many[ControlAreaOperator] = Many(
        EndMeta(
            name="parent_of_a",
            cim_role="ParentOfA",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.control_area_operator:ControlAreaOperator",
            many=True,
            lower=0,
            upper=None,
            inverse="ca_child_of",
            aggregation="none",
        )
    )
    side_b_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="side_b_sub_control_area",
            cim_role="SideB_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="side_b_tie_lines",
            aggregation="none",
        )
    )
    side_a_sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="side_a_sub_control_area",
            cim_role="SideA_SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="side_a_tie_lines",
            aggregation="none",
        )
    )
    parent_of_b: One[CustomerConsumer] = One(
        EndMeta(
            name="parent_of_b",
            cim_role="ParentOfB",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.customer_consumer:CustomerConsumer",
            many=False,
            lower=0,
            upper=1,
            inverse="cust_child_of",
            aggregation="none",
        )
    )
    energy_transaction: One[EnergyTransaction] = One(
        EndMeta(
            name="energy_transaction",
            cim_role="EnergyTransaction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=False,
            lower=0,
            upper=1,
            inverse="tie_lines",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TieLine",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{5E38218F-5C3C-4eea-B97B-CA3E8932B344}",
        ends=(
            parent_of_a.meta,
            side_b_sub_control_area.meta,
            side_a_sub_control_area.meta,
            parent_of_b.meta,
            energy_transaction.meta,
        ),
    )

    def __init__(
        self,
        *,
        parent_of_a: Iterable[ControlAreaOperator] | None = None,
        side_b_sub_control_area: SubControlArea | None = None,
        side_a_sub_control_area: SubControlArea | None = None,
        parent_of_b: CustomerConsumer | None = None,
        energy_transaction: EnergyTransaction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if parent_of_a is not None:
            TieLine.parent_of_a.extend(self, parent_of_a)
        if side_b_sub_control_area is not None:
            self.side_b_sub_control_area = side_b_sub_control_area
        if side_a_sub_control_area is not None:
            self.side_a_sub_control_area = side_a_sub_control_area
        if parent_of_b is not None:
            self.parent_of_b = parent_of_b
        if energy_transaction is not None:
            self.energy_transaction = energy_transaction

    def add_parent_of_a(self, parent_of_a: ControlAreaOperator) -> Self:
        return TieLine.parent_of_a.add(self, parent_of_a)

    def remove_parent_of_a(self, parent_of_a: ControlAreaOperator) -> Self:
        return TieLine.parent_of_a.remove(self, parent_of_a)

    def clear_parent_of_a(self) -> Self:
        return TieLine.parent_of_a.clear(self)

    def num_parent_of_a(self) -> int:
        return TieLine.parent_of_a.count(self)

    def get_parent_of_a_by_mrid(self, mrid: str) -> ControlAreaOperator | None:
        return TieLine.parent_of_a.get_by_mrid(self, mrid)
