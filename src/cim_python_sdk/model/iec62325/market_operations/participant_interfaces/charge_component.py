"""CIM class ChargeComponent (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant import (
        BillDeterminant,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_type import (
        ChargeType,
    )


class ChargeComponent(IdentifiedObject):
    """A Charge Component is a list of configurable charge quality items to feed into
    settlement calculation and/or bill determinants."""

    __slots__ = (
        "_bill_determinants",
        "_charge_types",
        "delete_status",
        "effective_date",
        "equation",
        "message",
        "round_off",
        "sum",
        "termination_date",
        "type",
    )

    delete_status: str | None
    effective_date: _dt.datetime | None
    termination_date: _dt.datetime | None
    message: str | None
    type: str | None
    sum: str | None
    round_off: str | None
    equation: str | None

    bill_determinants: Many[BillDeterminant] = Many(
        EndMeta(
            name="bill_determinants",
            cim_role="BillDeterminants",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.bill_determinant:BillDeterminant",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_components",
            aggregation="none",
        )
    )
    charge_types: Many[ChargeType] = Many(
        EndMeta(
            name="charge_types",
            cim_role="ChargeTypes",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_type:ChargeType",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_components",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ChargeComponent",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{4A37C8E3-7E6A-4893-A1DC-9D2427D16EDF}",
        attributes=(
            AttrMeta("delete_status", "deleteStatus", "str", 0, 1, "primitive"),
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("termination_date", "terminationDate", "datetime", 0, 1, "primitive"),
            AttrMeta("message", "message", "str", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("sum", "sum", "str", 0, 1, "primitive"),
            AttrMeta("round_off", "roundOff", "str", 0, 1, "primitive"),
            AttrMeta("equation", "equation", "str", 0, 1, "primitive"),
        ),
        ends=(
            bill_determinants.meta,
            charge_types.meta,
        ),
    )

    def __init__(
        self,
        *,
        delete_status: str | None = None,
        effective_date: _dt.datetime | None = None,
        termination_date: _dt.datetime | None = None,
        message: str | None = None,
        type: str | None = None,
        sum: str | None = None,
        round_off: str | None = None,
        equation: str | None = None,
        bill_determinants: Iterable[BillDeterminant] | None = None,
        charge_types: Iterable[ChargeType] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.delete_status = delete_status
        self.effective_date = effective_date
        self.termination_date = termination_date
        self.message = message
        self.type = type
        self.sum = sum
        self.round_off = round_off
        self.equation = equation
        if bill_determinants is not None:
            ChargeComponent.bill_determinants.extend(self, bill_determinants)
        if charge_types is not None:
            ChargeComponent.charge_types.extend(self, charge_types)

    def add_bill_determinant(self, bill_determinant: BillDeterminant) -> Self:
        return ChargeComponent.bill_determinants.add(self, bill_determinant)

    def remove_bill_determinant(self, bill_determinant: BillDeterminant) -> Self:
        return ChargeComponent.bill_determinants.remove(self, bill_determinant)

    def clear_bill_determinants(self) -> Self:
        return ChargeComponent.bill_determinants.clear(self)

    def num_bill_determinant(self) -> int:
        return ChargeComponent.bill_determinants.count(self)

    def get_bill_determinant_by_mrid(self, mrid: str) -> BillDeterminant | None:
        return ChargeComponent.bill_determinants.get_by_mrid(self, mrid)

    def add_charge_type(self, charge_type: ChargeType) -> Self:
        return ChargeComponent.charge_types.add(self, charge_type)

    def remove_charge_type(self, charge_type: ChargeType) -> Self:
        return ChargeComponent.charge_types.remove(self, charge_type)

    def clear_charge_types(self) -> Self:
        return ChargeComponent.charge_types.clear(self)

    def num_charge_type(self) -> int:
        return ChargeComponent.charge_types.count(self)

    def get_charge_type_by_mrid(self, mrid: str) -> ChargeType | None:
        return ChargeComponent.charge_types.get_by_mrid(self, mrid)
