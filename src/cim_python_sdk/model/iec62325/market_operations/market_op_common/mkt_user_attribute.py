"""CIM class MktUserAttribute (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.user_attribute import UserAttribute

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant import (
        BillDeterminant,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item import (
        MarketStatementLineItem,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pass_through_bill import (
        PassThroughBill,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.attribute_property import (
        AttributeProperty,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_group import (
        ChargeGroup,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_type import (
        ChargeType,
    )


class MktUserAttribute(UserAttribute):
    """Subclass of IEC61968:Domain2:UserAttribute."""

    __slots__ = (
        "_attribute_property",
        "_bill_determinant",
        "_charge_group",
        "_charge_type",
        "_market_statement_line_item",
        "_pass_through_bill",
    )

    bill_determinant: Many[BillDeterminant] = Many(
        EndMeta(
            name="bill_determinant",
            cim_role="BillDeterminant",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant:BillDeterminant",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_user_attribute",
            aggregation="none",
        )
    )
    attribute_property: Many[AttributeProperty] = Many(
        EndMeta(
            name="attribute_property",
            cim_role="AttributeProperty",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.attribute_property:AttributeProperty",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_user_attribute",
            aggregation="none",
        )
    )
    charge_group: Many[ChargeGroup] = Many(
        EndMeta(
            name="charge_group",
            cim_role="ChargeGroup",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_group:ChargeGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_user_attribute",
            aggregation="none",
        )
    )
    pass_through_bill: Many[PassThroughBill] = Many(
        EndMeta(
            name="pass_through_bill",
            cim_role="PassThroughBill",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.pass_through_bill:PassThroughBill",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_user_attribute",
            aggregation="none",
        )
    )
    market_statement_line_item: Many[MarketStatementLineItem] = Many(
        EndMeta(
            name="market_statement_line_item",
            cim_role="MarketStatementLineItem",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.market_statement_line_item:MarketStatementLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_user_attribute",
            aggregation="none",
        )
    )
    charge_type: Many[ChargeType] = Many(
        EndMeta(
            name="charge_type",
            cim_role="ChargeType",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_type:ChargeType",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_user_attribute",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktUserAttribute",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{480FBBF0-926A-4125-ADAA-6CA279DCEF6E}",
        ends=(
            bill_determinant.meta,
            attribute_property.meta,
            charge_group.meta,
            pass_through_bill.meta,
            market_statement_line_item.meta,
            charge_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        bill_determinant: Iterable[BillDeterminant] | None = None,
        attribute_property: Iterable[AttributeProperty] | None = None,
        charge_group: Iterable[ChargeGroup] | None = None,
        pass_through_bill: Iterable[PassThroughBill] | None = None,
        market_statement_line_item: Iterable[MarketStatementLineItem] | None = None,
        charge_type: Iterable[ChargeType] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if bill_determinant is not None:
            MktUserAttribute.bill_determinant.extend(self, bill_determinant)
        if attribute_property is not None:
            MktUserAttribute.attribute_property.extend(self, attribute_property)
        if charge_group is not None:
            MktUserAttribute.charge_group.extend(self, charge_group)
        if pass_through_bill is not None:
            MktUserAttribute.pass_through_bill.extend(self, pass_through_bill)
        if market_statement_line_item is not None:
            MktUserAttribute.market_statement_line_item.extend(self, market_statement_line_item)
        if charge_type is not None:
            MktUserAttribute.charge_type.extend(self, charge_type)

    def add_bill_determinant(self, bill_determinant: BillDeterminant) -> Self:
        return MktUserAttribute.bill_determinant.add(self, bill_determinant)

    def remove_bill_determinant(self, bill_determinant: BillDeterminant) -> Self:
        return MktUserAttribute.bill_determinant.remove(self, bill_determinant)

    def clear_bill_determinant(self) -> Self:
        return MktUserAttribute.bill_determinant.clear(self)

    def num_bill_determinant(self) -> int:
        return MktUserAttribute.bill_determinant.count(self)

    def get_bill_determinant_by_mrid(self, mrid: str) -> BillDeterminant | None:
        return MktUserAttribute.bill_determinant.get_by_mrid(self, mrid)

    def add_attribute_property(self, attribute_property: AttributeProperty) -> Self:
        return MktUserAttribute.attribute_property.add(self, attribute_property)

    def remove_attribute_property(self, attribute_property: AttributeProperty) -> Self:
        return MktUserAttribute.attribute_property.remove(self, attribute_property)

    def clear_attribute_property(self) -> Self:
        return MktUserAttribute.attribute_property.clear(self)

    def num_attribute_property(self) -> int:
        return MktUserAttribute.attribute_property.count(self)

    def add_charge_group(self, charge_group: ChargeGroup) -> Self:
        return MktUserAttribute.charge_group.add(self, charge_group)

    def remove_charge_group(self, charge_group: ChargeGroup) -> Self:
        return MktUserAttribute.charge_group.remove(self, charge_group)

    def clear_charge_group(self) -> Self:
        return MktUserAttribute.charge_group.clear(self)

    def num_charge_group(self) -> int:
        return MktUserAttribute.charge_group.count(self)

    def get_charge_group_by_mrid(self, mrid: str) -> ChargeGroup | None:
        return MktUserAttribute.charge_group.get_by_mrid(self, mrid)

    def add_pass_through_bill(self, pass_through_bill: PassThroughBill) -> Self:
        return MktUserAttribute.pass_through_bill.add(self, pass_through_bill)

    def remove_pass_through_bill(self, pass_through_bill: PassThroughBill) -> Self:
        return MktUserAttribute.pass_through_bill.remove(self, pass_through_bill)

    def clear_pass_through_bill(self) -> Self:
        return MktUserAttribute.pass_through_bill.clear(self)

    def num_pass_through_bill(self) -> int:
        return MktUserAttribute.pass_through_bill.count(self)

    def get_pass_through_bill_by_mrid(self, mrid: str) -> PassThroughBill | None:
        return MktUserAttribute.pass_through_bill.get_by_mrid(self, mrid)

    def add_market_statement_line_item(
        self, market_statement_line_item: MarketStatementLineItem
    ) -> Self:
        return MktUserAttribute.market_statement_line_item.add(self, market_statement_line_item)

    def remove_market_statement_line_item(
        self, market_statement_line_item: MarketStatementLineItem
    ) -> Self:
        return MktUserAttribute.market_statement_line_item.remove(self, market_statement_line_item)

    def clear_market_statement_line_item(self) -> Self:
        return MktUserAttribute.market_statement_line_item.clear(self)

    def num_market_statement_line_item(self) -> int:
        return MktUserAttribute.market_statement_line_item.count(self)

    def get_market_statement_line_item_by_mrid(self, mrid: str) -> MarketStatementLineItem | None:
        return MktUserAttribute.market_statement_line_item.get_by_mrid(self, mrid)

    def add_charge_type(self, charge_type: ChargeType) -> Self:
        return MktUserAttribute.charge_type.add(self, charge_type)

    def remove_charge_type(self, charge_type: ChargeType) -> Self:
        return MktUserAttribute.charge_type.remove(self, charge_type)

    def clear_charge_type(self) -> Self:
        return MktUserAttribute.charge_type.clear(self)

    def num_charge_type(self) -> int:
        return MktUserAttribute.charge_type.count(self)

    def get_charge_type_by_mrid(self, mrid: str) -> ChargeType | None:
        return MktUserAttribute.charge_type.get_by_mrid(self, mrid)
