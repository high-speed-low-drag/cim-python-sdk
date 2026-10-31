"""CIM class PointOfSale (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.cashier_shift import CashierShift


class PointOfSale(IdentifiedObject):
    """Logical point where transactions take place with operational interaction between cashier
    and the payment system; in certain cases the point of sale interacts directly with the
    end customer, in which case the cashier might not be a real person: for example a
    self-service kiosk or over the internet."""

    __slots__ = ("_cashier_shifts", "location")

    location: str | None

    cashier_shifts: Many[CashierShift] = Many(
        EndMeta(
            name="cashier_shifts",
            cim_role="CashierShifts",
            target="cim_python_sdk.model.iec61968.payment_metering.cashier_shift:CashierShift",
            many=True,
            lower=0,
            upper=None,
            inverse="point_of_sale",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PointOfSale",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{5F4F45D1-B356-4efb-8D4C-C2C2F635D65A}",
        attributes=(AttrMeta("location", "location", "str", 0, 1, "primitive"),),
        ends=(cashier_shifts.meta,),
    )

    def __init__(
        self,
        *,
        location: str | None = None,
        cashier_shifts: Iterable[CashierShift] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.location = location
        if cashier_shifts is not None:
            PointOfSale.cashier_shifts.extend(self, cashier_shifts)

    def add_cashier_shift(self, cashier_shift: CashierShift) -> Self:
        return PointOfSale.cashier_shifts.add(self, cashier_shift)

    def remove_cashier_shift(self, cashier_shift: CashierShift) -> Self:
        return PointOfSale.cashier_shifts.remove(self, cashier_shift)

    def clear_cashier_shifts(self) -> Self:
        return PointOfSale.cashier_shifts.clear(self)

    def num_cashier_shift(self) -> int:
        return PointOfSale.cashier_shifts.count(self)

    def get_cashier_shift_by_mrid(self, mrid: str) -> CashierShift | None:
        return PointOfSale.cashier_shifts.get_by_mrid(self, mrid)
