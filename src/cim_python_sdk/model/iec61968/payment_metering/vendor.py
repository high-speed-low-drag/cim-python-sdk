"""CIM class Vendor (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.vendor_shift import VendorShift


class Vendor(IdentifiedObject):
    """The entity that owns the point of sale and contracts with the cashier to receipt
    payments and vend tokens using the payment system. The vendor has a private contract
    with and is managed by the merchant which is a type of organisation. The vendor is
    accountable to the merchant for revenue collected, and the merchant is in turn
    accountable to the supplier."""

    __slots__ = ("_vendor_shifts",)

    vendor_shifts: Many[VendorShift] = Many(
        EndMeta(
            name="vendor_shifts",
            cim_role="VendorShifts",
            target="cim_python_sdk.model.iec61968.payment_metering.vendor_shift:VendorShift",
            many=True,
            lower=0,
            upper=None,
            inverse="vendor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Vendor",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{F66E6B41-82E4-4a55-AABC-14660887E4A6}",
        ends=(vendor_shifts.meta,),
    )

    def __init__(
        self,
        *,
        vendor_shifts: Iterable[VendorShift] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if vendor_shifts is not None:
            Vendor.vendor_shifts.extend(self, vendor_shifts)

    def add_vendor_shift(self, vendor_shift: VendorShift) -> Self:
        return Vendor.vendor_shifts.add(self, vendor_shift)

    def remove_vendor_shift(self, vendor_shift: VendorShift) -> Self:
        return Vendor.vendor_shifts.remove(self, vendor_shift)

    def clear_vendor_shifts(self) -> Self:
        return Vendor.vendor_shifts.clear(self)

    def num_vendor_shift(self) -> int:
        return Vendor.vendor_shifts.count(self)

    def get_vendor_shift_by_mrid(self, mrid: str) -> VendorShift | None:
        return Vendor.vendor_shifts.get_by_mrid(self, mrid)
