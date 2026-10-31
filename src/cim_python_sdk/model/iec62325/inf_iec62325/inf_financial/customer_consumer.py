"""CIM class CustomerConsumer (TC57CIM/IEC62325/InfIEC62325/InfFinancial). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation import Organisation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line import TieLine


class CustomerConsumer(Organisation):
    """The energy buyer in the energy marketplace."""

    __slots__ = ("_cust_child_of",)

    cust_child_of: Many[TieLine] = Many(
        EndMeta(
            name="cust_child_of",
            cim_role="CustChildOf",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line:TieLine",
            many=True,
            lower=0,
            upper=None,
            inverse="parent_of_b",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CustomerConsumer",
        package="TC57CIM/IEC62325/InfIEC62325/InfFinancial",
        guid="{EED6DB7B-9331-4741-8911-8EE740B767AA}",
        ends=(cust_child_of.meta,),
    )

    def __init__(
        self,
        *,
        cust_child_of: Iterable[TieLine] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if cust_child_of is not None:
            CustomerConsumer.cust_child_of.extend(self, cust_child_of)

    def add_cust_child_of(self, cust_child_of: TieLine) -> Self:
        return CustomerConsumer.cust_child_of.add(self, cust_child_of)

    def remove_cust_child_of(self, cust_child_of: TieLine) -> Self:
        return CustomerConsumer.cust_child_of.remove(self, cust_child_of)

    def clear_cust_child_of(self) -> Self:
        return CustomerConsumer.cust_child_of.clear(self)

    def num_cust_child_of(self) -> int:
        return CustomerConsumer.cust_child_of.count(self)

    def get_cust_child_of_by_mrid(self, mrid: str) -> TieLine | None:
        return CustomerConsumer.cust_child_of.get_by_mrid(self, mrid)
