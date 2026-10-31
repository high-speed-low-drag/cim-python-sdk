"""CIM class Cashier (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.electronic_address import ElectronicAddress
    from cim_python_sdk.model.iec61968.payment_metering.cashier_shift import CashierShift


class Cashier(IdentifiedObject):
    """The operator of the point of sale for the duration of CashierShift. Cashier is under the
    exclusive management control of Vendor."""

    __slots__ = ("_cashier_shifts", "electronic_address")

    electronic_address: ElectronicAddress | None

    cashier_shifts: Many[CashierShift] = Many(
        EndMeta(
            name="cashier_shifts",
            cim_role="CashierShifts",
            target="cim_python_sdk.model.iec61968.payment_metering.cashier_shift:CashierShift",
            many=True,
            lower=0,
            upper=None,
            inverse="cashier",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Cashier",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{A27103EB-96BA-4f2e-9CE3-3B9FE8EE9776}",
        attributes=(
            AttrMeta(
                "electronic_address", "electronicAddress", "ElectronicAddress", 0, 1, "compound"
            ),
        ),
        ends=(cashier_shifts.meta,),
    )

    def __init__(
        self,
        *,
        electronic_address: ElectronicAddress | None = None,
        cashier_shifts: Iterable[CashierShift] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.electronic_address = electronic_address
        if cashier_shifts is not None:
            Cashier.cashier_shifts.extend(self, cashier_shifts)

    def add_cashier_shift(self, cashier_shift: CashierShift) -> Self:
        return Cashier.cashier_shifts.add(self, cashier_shift)

    def remove_cashier_shift(self, cashier_shift: CashierShift) -> Self:
        return Cashier.cashier_shifts.remove(self, cashier_shift)

    def clear_cashier_shifts(self) -> Self:
        return Cashier.cashier_shifts.clear(self)

    def num_cashier_shift(self) -> int:
        return Cashier.cashier_shifts.count(self)

    def get_cashier_shift_by_mrid(self, mrid: str) -> CashierShift | None:
        return Cashier.cashier_shifts.get_by_mrid(self, mrid)
