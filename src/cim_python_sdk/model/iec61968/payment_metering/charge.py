"""CIM class Charge (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.payment_metering.accounting_unit import AccountingUnit
    from cim_python_sdk.model.iec61968.payment_metering.auxiliary_account import AuxiliaryAccount
    from cim_python_sdk.model.iec61968.payment_metering.charge_kind import ChargeKind
    from cim_python_sdk.model.iec61968.payment_metering.consumption_tariff_interval import (
        ConsumptionTariffInterval,
    )
    from cim_python_sdk.model.iec61968.payment_metering.time_tariff_interval import (
        TimeTariffInterval,
    )


class Charge(IdentifiedObject):
    """A charge element associated with other entities such as tariff structures, auxiliary
    agreements or other charge elements. The total charge amount applicable to this instance
    of charge is the sum of fixed and variable portion."""

    __slots__ = (
        "_auxiliary_accounts",
        "_child_charges",
        "_consumption_tariff_intervals",
        "_parent_charge",
        "_time_tariff_intervals",
        "fixed_portion",
        "kind",
        "variable_portion",
    )

    kind: ChargeKind | None
    fixed_portion: AccountingUnit | None
    variable_portion: float | None  # PerCent

    child_charges: Many[Charge] = Many(
        EndMeta(
            name="child_charges",
            cim_role="ChildCharges",
            target="cim_python_sdk.model.iec61968.payment_metering.charge:Charge",
            many=True,
            lower=0,
            upper=None,
            inverse="parent_charge",
            aggregation="none",
        )
    )
    parent_charge: One[Charge] = One(
        EndMeta(
            name="parent_charge",
            cim_role="ParentCharge",
            target="cim_python_sdk.model.iec61968.payment_metering.charge:Charge",
            many=False,
            lower=0,
            upper=1,
            inverse="child_charges",
            aggregation="none",
        )
    )
    time_tariff_intervals: Many[TimeTariffInterval] = Many(
        EndMeta(
            name="time_tariff_intervals",
            cim_role="TimeTariffIntervals",
            target="cim_python_sdk.model.iec61968.payment_metering.time_tariff_interval:TimeTariffInterval",
            many=True,
            lower=0,
            upper=None,
            inverse="charges",
            aggregation="none",
        )
    )
    consumption_tariff_intervals: Many[ConsumptionTariffInterval] = Many(
        EndMeta(
            name="consumption_tariff_intervals",
            cim_role="ConsumptionTariffIntervals",
            target="cim_python_sdk.model.iec61968.payment_metering.consumption_tariff_interval:ConsumptionTariffInterval",
            many=True,
            lower=0,
            upper=None,
            inverse="charges",
            aggregation="none",
        )
    )
    auxiliary_accounts: Many[AuxiliaryAccount] = Many(
        EndMeta(
            name="auxiliary_accounts",
            cim_role="AuxiliaryAccounts",
            target="cim_python_sdk.model.iec61968.payment_metering.auxiliary_account:AuxiliaryAccount",
            many=True,
            lower=0,
            upper=None,
            inverse="charges",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Charge",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{036046C7-95D4-403e-9997-B628005B934B}",
        attributes=(
            AttrMeta("kind", "kind", "ChargeKind", 0, 1, "enumeration"),
            AttrMeta("fixed_portion", "fixedPortion", "AccountingUnit", 0, 1, "compound"),
            AttrMeta("variable_portion", "variablePortion", "PerCent", 0, 1, "cimdatatype"),
        ),
        ends=(
            child_charges.meta,
            parent_charge.meta,
            time_tariff_intervals.meta,
            consumption_tariff_intervals.meta,
            auxiliary_accounts.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: ChargeKind | None = None,
        fixed_portion: AccountingUnit | None = None,
        variable_portion: float | None = None,
        child_charges: Iterable[Charge] | None = None,
        parent_charge: Charge | None = None,
        time_tariff_intervals: Iterable[TimeTariffInterval] | None = None,
        consumption_tariff_intervals: Iterable[ConsumptionTariffInterval] | None = None,
        auxiliary_accounts: Iterable[AuxiliaryAccount] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.fixed_portion = fixed_portion
        self.variable_portion = variable_portion
        if child_charges is not None:
            Charge.child_charges.extend(self, child_charges)
        if parent_charge is not None:
            self.parent_charge = parent_charge
        if time_tariff_intervals is not None:
            Charge.time_tariff_intervals.extend(self, time_tariff_intervals)
        if consumption_tariff_intervals is not None:
            Charge.consumption_tariff_intervals.extend(self, consumption_tariff_intervals)
        if auxiliary_accounts is not None:
            Charge.auxiliary_accounts.extend(self, auxiliary_accounts)

    def add_child_charge(self, child_charge: Charge) -> Self:
        return Charge.child_charges.add(self, child_charge)

    def remove_child_charge(self, child_charge: Charge) -> Self:
        return Charge.child_charges.remove(self, child_charge)

    def clear_child_charges(self) -> Self:
        return Charge.child_charges.clear(self)

    def num_child_charge(self) -> int:
        return Charge.child_charges.count(self)

    def get_child_charge_by_mrid(self, mrid: str) -> Charge | None:
        return Charge.child_charges.get_by_mrid(self, mrid)

    def add_time_tariff_interval(self, time_tariff_interval: TimeTariffInterval) -> Self:
        return Charge.time_tariff_intervals.add(self, time_tariff_interval)

    def remove_time_tariff_interval(self, time_tariff_interval: TimeTariffInterval) -> Self:
        return Charge.time_tariff_intervals.remove(self, time_tariff_interval)

    def clear_time_tariff_intervals(self) -> Self:
        return Charge.time_tariff_intervals.clear(self)

    def num_time_tariff_interval(self) -> int:
        return Charge.time_tariff_intervals.count(self)

    def add_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return Charge.consumption_tariff_intervals.add(self, consumption_tariff_interval)

    def remove_consumption_tariff_interval(
        self, consumption_tariff_interval: ConsumptionTariffInterval
    ) -> Self:
        return Charge.consumption_tariff_intervals.remove(self, consumption_tariff_interval)

    def clear_consumption_tariff_intervals(self) -> Self:
        return Charge.consumption_tariff_intervals.clear(self)

    def num_consumption_tariff_interval(self) -> int:
        return Charge.consumption_tariff_intervals.count(self)

    def add_auxiliary_account(self, auxiliary_account: AuxiliaryAccount) -> Self:
        return Charge.auxiliary_accounts.add(self, auxiliary_account)

    def remove_auxiliary_account(self, auxiliary_account: AuxiliaryAccount) -> Self:
        return Charge.auxiliary_accounts.remove(self, auxiliary_account)

    def clear_auxiliary_accounts(self) -> Self:
        return Charge.auxiliary_accounts.clear(self)

    def num_auxiliary_account(self) -> int:
        return Charge.auxiliary_accounts.count(self)

    def get_auxiliary_account_by_mrid(self, mrid: str) -> AuxiliaryAccount | None:
        return Charge.auxiliary_accounts.get_by_mrid(self, mrid)
