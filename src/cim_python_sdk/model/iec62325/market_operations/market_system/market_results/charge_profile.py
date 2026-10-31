"""CIM class ChargeProfile (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.profile import (
    Profile,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant import (
        BillDeterminant,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile_data import (
        ChargeProfileData,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pass_through_bill import (
        PassThroughBill,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid


class ChargeProfile(Profile):
    """A type of profile for financial charges."""

    __slots__ = (
        "_bid",
        "_bill_determinant",
        "_charge_profile_data",
        "_pass_trough_bill",
        "frequency",
        "number_interval",
        "type",
        "unit_of_measure",
    )

    type: str | None
    frequency: str | None
    number_interval: int | None
    unit_of_measure: str | None

    bill_determinant: One[BillDeterminant] = One(
        EndMeta(
            name="bill_determinant",
            cim_role="BillDeterminant",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant:BillDeterminant",
            many=False,
            lower=0,
            upper=1,
            inverse="charge_profile",
            aggregation="none",
        )
    )
    pass_trough_bill: One[PassThroughBill] = One(
        EndMeta(
            name="pass_trough_bill",
            cim_role="PassTroughBill",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pass_through_bill:PassThroughBill",
            many=False,
            lower=0,
            upper=1,
            inverse="charge_profiles",
            aggregation="none",
        )
    )
    bid: One[Bid] = One(
        EndMeta(
            name="bid",
            cim_role="Bid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid:Bid",
            many=False,
            lower=0,
            upper=1,
            inverse="charge_profiles",
            aggregation="none",
        )
    )
    charge_profile_data: Many[ChargeProfileData] = Many(
        EndMeta(
            name="charge_profile_data",
            cim_role="ChargeProfileData",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.charge_profile_data:ChargeProfileData",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_profile",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ChargeProfile",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{FE65A9AC-50B4-4e6e-A021-A8F3EE1A7109}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("frequency", "frequency", "str", 0, 1, "primitive"),
            AttrMeta("number_interval", "numberInterval", "int", 0, 1, "primitive"),
            AttrMeta("unit_of_measure", "unitOfMeasure", "str", 0, 1, "primitive"),
        ),
        ends=(
            bill_determinant.meta,
            pass_trough_bill.meta,
            bid.meta,
            charge_profile_data.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        frequency: str | None = None,
        number_interval: int | None = None,
        unit_of_measure: str | None = None,
        bill_determinant: BillDeterminant | None = None,
        pass_trough_bill: PassThroughBill | None = None,
        bid: Bid | None = None,
        charge_profile_data: Iterable[ChargeProfileData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.frequency = frequency
        self.number_interval = number_interval
        self.unit_of_measure = unit_of_measure
        if bill_determinant is not None:
            self.bill_determinant = bill_determinant
        if pass_trough_bill is not None:
            self.pass_trough_bill = pass_trough_bill
        if bid is not None:
            self.bid = bid
        if charge_profile_data is not None:
            ChargeProfile.charge_profile_data.extend(self, charge_profile_data)

    def add_charge_profile_data(self, charge_profile_data: ChargeProfileData) -> Self:
        return ChargeProfile.charge_profile_data.add(self, charge_profile_data)

    def remove_charge_profile_data(self, charge_profile_data: ChargeProfileData) -> Self:
        return ChargeProfile.charge_profile_data.remove(self, charge_profile_data)

    def clear_charge_profile_data(self) -> Self:
        return ChargeProfile.charge_profile_data.clear(self)

    def num_charge_profile_data(self) -> int:
        return ChargeProfile.charge_profile_data.count(self)
