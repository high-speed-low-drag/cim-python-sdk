"""CIM class MajorChargeGroup (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice import (
        MarketInvoice,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement import (
        Settlement,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_type import (
        ChargeType,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.market_scheduled_event import (
        MarketScheduledEvent,
    )


class MajorChargeGroup(IdentifiedObject):
    """A Major Charge Group is the same as Invoice Type which provides the highest level of
    grouping for charge types configuration. Examples: Market, FERC, RMR."""

    __slots__ = (
        "_charge_type",
        "_market_invoice",
        "_mkt_scheduled_event",
        "_settlement",
        "effective_date",
        "frequency_type",
        "invoice_type",
        "require_autorun",
        "revision_number",
        "run_type",
        "run_version",
        "termination_date",
    )

    run_type: str | None
    run_version: str | None
    frequency_type: str | None
    invoice_type: str | None
    effective_date: _dt.datetime | None
    termination_date: _dt.datetime | None
    require_autorun: str | None
    revision_number: str | None

    settlement: Many[Settlement] = Many(
        EndMeta(
            name="settlement",
            cim_role="Settlement",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.settlement:Settlement",
            many=True,
            lower=0,
            upper=None,
            inverse="major_charge_group",
            aggregation="none",
        )
    )
    mkt_scheduled_event: Many[MarketScheduledEvent] = Many(
        EndMeta(
            name="mkt_scheduled_event",
            cim_role="MktScheduledEvent",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.market_scheduled_event:MarketScheduledEvent",
            many=True,
            lower=0,
            upper=None,
            inverse="major_charge_group",
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
            inverse="major_charge_group",
            aggregation="none",
        )
    )
    market_invoice: Many[MarketInvoice] = Many(
        EndMeta(
            name="market_invoice",
            cim_role="MarketInvoice",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.market_invoice:MarketInvoice",
            many=True,
            lower=0,
            upper=None,
            inverse="major_charge_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MajorChargeGroup",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{C6DA5003-F272-4d50-8183-33E7FA08E3B9}",
        attributes=(
            AttrMeta("run_type", "runType", "str", 0, 1, "primitive"),
            AttrMeta("run_version", "runVersion", "str", 0, 1, "primitive"),
            AttrMeta("frequency_type", "frequencyType", "str", 0, 1, "primitive"),
            AttrMeta("invoice_type", "invoiceType", "str", 0, 1, "primitive"),
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("termination_date", "terminationDate", "datetime", 0, 1, "primitive"),
            AttrMeta("require_autorun", "requireAutorun", "str", 0, 1, "primitive"),
            AttrMeta("revision_number", "revisionNumber", "str", 0, 1, "primitive"),
        ),
        ends=(
            settlement.meta,
            mkt_scheduled_event.meta,
            charge_type.meta,
            market_invoice.meta,
        ),
    )

    def __init__(
        self,
        *,
        run_type: str | None = None,
        run_version: str | None = None,
        frequency_type: str | None = None,
        invoice_type: str | None = None,
        effective_date: _dt.datetime | None = None,
        termination_date: _dt.datetime | None = None,
        require_autorun: str | None = None,
        revision_number: str | None = None,
        settlement: Iterable[Settlement] | None = None,
        mkt_scheduled_event: Iterable[MarketScheduledEvent] | None = None,
        charge_type: Iterable[ChargeType] | None = None,
        market_invoice: Iterable[MarketInvoice] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.run_type = run_type
        self.run_version = run_version
        self.frequency_type = frequency_type
        self.invoice_type = invoice_type
        self.effective_date = effective_date
        self.termination_date = termination_date
        self.require_autorun = require_autorun
        self.revision_number = revision_number
        if settlement is not None:
            MajorChargeGroup.settlement.extend(self, settlement)
        if mkt_scheduled_event is not None:
            MajorChargeGroup.mkt_scheduled_event.extend(self, mkt_scheduled_event)
        if charge_type is not None:
            MajorChargeGroup.charge_type.extend(self, charge_type)
        if market_invoice is not None:
            MajorChargeGroup.market_invoice.extend(self, market_invoice)

    def add_settlement(self, settlement: Settlement) -> Self:
        return MajorChargeGroup.settlement.add(self, settlement)

    def remove_settlement(self, settlement: Settlement) -> Self:
        return MajorChargeGroup.settlement.remove(self, settlement)

    def clear_settlement(self) -> Self:
        return MajorChargeGroup.settlement.clear(self)

    def num_settlement(self) -> int:
        return MajorChargeGroup.settlement.count(self)

    def get_settlement_by_mrid(self, mrid: str) -> Settlement | None:
        return MajorChargeGroup.settlement.get_by_mrid(self, mrid)

    def add_mkt_scheduled_event(self, mkt_scheduled_event: MarketScheduledEvent) -> Self:
        return MajorChargeGroup.mkt_scheduled_event.add(self, mkt_scheduled_event)

    def remove_mkt_scheduled_event(self, mkt_scheduled_event: MarketScheduledEvent) -> Self:
        return MajorChargeGroup.mkt_scheduled_event.remove(self, mkt_scheduled_event)

    def clear_mkt_scheduled_event(self) -> Self:
        return MajorChargeGroup.mkt_scheduled_event.clear(self)

    def num_mkt_scheduled_event(self) -> int:
        return MajorChargeGroup.mkt_scheduled_event.count(self)

    def get_mkt_scheduled_event_by_mrid(self, mrid: str) -> MarketScheduledEvent | None:
        return MajorChargeGroup.mkt_scheduled_event.get_by_mrid(self, mrid)

    def add_charge_type(self, charge_type: ChargeType) -> Self:
        return MajorChargeGroup.charge_type.add(self, charge_type)

    def remove_charge_type(self, charge_type: ChargeType) -> Self:
        return MajorChargeGroup.charge_type.remove(self, charge_type)

    def clear_charge_type(self) -> Self:
        return MajorChargeGroup.charge_type.clear(self)

    def num_charge_type(self) -> int:
        return MajorChargeGroup.charge_type.count(self)

    def get_charge_type_by_mrid(self, mrid: str) -> ChargeType | None:
        return MajorChargeGroup.charge_type.get_by_mrid(self, mrid)

    def add_market_invoice(self, market_invoice: MarketInvoice) -> Self:
        return MajorChargeGroup.market_invoice.add(self, market_invoice)

    def remove_market_invoice(self, market_invoice: MarketInvoice) -> Self:
        return MajorChargeGroup.market_invoice.remove(self, market_invoice)

    def clear_market_invoice(self) -> Self:
        return MajorChargeGroup.market_invoice.clear(self)

    def num_market_invoice(self) -> int:
        return MajorChargeGroup.market_invoice.count(self)
