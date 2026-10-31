"""CIM class ChargeType (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute import (
        MktUserAttribute,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_component import (
        ChargeComponent,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_group import (
        ChargeGroup,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.major_charge_group import (
        MajorChargeGroup,
    )


class ChargeType(Document):
    """Charge Type is the basic level configuration for settlement to process specific charges
    for invoicing purpose. Examples such as: Day Ahead Spinning Reserve Default Invoice
    Interest Charge, etc."""

    __slots__ = (
        "_charge_components",
        "_charge_group",
        "_major_charge_group",
        "_mkt_user_attribute",
        "charge_order",
        "charge_version",
        "effective_date",
        "factor",
        "frequency_type",
        "termination_date",
        "total_interval",
    )

    effective_date: _dt.datetime | None
    termination_date: _dt.datetime | None
    factor: str | None
    charge_order: str | None
    frequency_type: str | None
    charge_version: str | None
    total_interval: str | None

    charge_group: Many[ChargeGroup] = Many(
        EndMeta(
            name="charge_group",
            cim_role="ChargeGroup",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_group:ChargeGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_type",
            aggregation="none",
        )
    )
    major_charge_group: Many[MajorChargeGroup] = Many(
        EndMeta(
            name="major_charge_group",
            cim_role="MajorChargeGroup",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.major_charge_group:MajorChargeGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_type",
            aggregation="none",
        )
    )
    charge_components: Many[ChargeComponent] = Many(
        EndMeta(
            name="charge_components",
            cim_role="ChargeComponents",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_component:ChargeComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_types",
            aggregation="none",
        )
    )
    mkt_user_attribute: Many[MktUserAttribute] = Many(
        EndMeta(
            name="mkt_user_attribute",
            cim_role="MktUserAttribute",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute:MktUserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ChargeType",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{F63E4B25-4A11-4ee0-9B6B-D95CE0EA7304}",
        attributes=(
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("termination_date", "terminationDate", "datetime", 0, 1, "primitive"),
            AttrMeta("factor", "factor", "str", 0, 1, "primitive"),
            AttrMeta("charge_order", "chargeOrder", "str", 0, 1, "primitive"),
            AttrMeta("frequency_type", "frequencyType", "str", 0, 1, "primitive"),
            AttrMeta("charge_version", "chargeVersion", "str", 0, 1, "primitive"),
            AttrMeta("total_interval", "totalInterval", "str", 0, 1, "primitive"),
        ),
        ends=(
            charge_group.meta,
            major_charge_group.meta,
            charge_components.meta,
            mkt_user_attribute.meta,
        ),
    )

    def __init__(
        self,
        *,
        effective_date: _dt.datetime | None = None,
        termination_date: _dt.datetime | None = None,
        factor: str | None = None,
        charge_order: str | None = None,
        frequency_type: str | None = None,
        charge_version: str | None = None,
        total_interval: str | None = None,
        charge_group: Iterable[ChargeGroup] | None = None,
        major_charge_group: Iterable[MajorChargeGroup] | None = None,
        charge_components: Iterable[ChargeComponent] | None = None,
        mkt_user_attribute: Iterable[MktUserAttribute] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.effective_date = effective_date
        self.termination_date = termination_date
        self.factor = factor
        self.charge_order = charge_order
        self.frequency_type = frequency_type
        self.charge_version = charge_version
        self.total_interval = total_interval
        if charge_group is not None:
            ChargeType.charge_group.extend(self, charge_group)
        if major_charge_group is not None:
            ChargeType.major_charge_group.extend(self, major_charge_group)
        if charge_components is not None:
            ChargeType.charge_components.extend(self, charge_components)
        if mkt_user_attribute is not None:
            ChargeType.mkt_user_attribute.extend(self, mkt_user_attribute)

    def add_charge_group(self, charge_group: ChargeGroup) -> Self:
        return ChargeType.charge_group.add(self, charge_group)

    def remove_charge_group(self, charge_group: ChargeGroup) -> Self:
        return ChargeType.charge_group.remove(self, charge_group)

    def clear_charge_group(self) -> Self:
        return ChargeType.charge_group.clear(self)

    def num_charge_group(self) -> int:
        return ChargeType.charge_group.count(self)

    def get_charge_group_by_mrid(self, mrid: str) -> ChargeGroup | None:
        return ChargeType.charge_group.get_by_mrid(self, mrid)

    def add_major_charge_group(self, major_charge_group: MajorChargeGroup) -> Self:
        return ChargeType.major_charge_group.add(self, major_charge_group)

    def remove_major_charge_group(self, major_charge_group: MajorChargeGroup) -> Self:
        return ChargeType.major_charge_group.remove(self, major_charge_group)

    def clear_major_charge_group(self) -> Self:
        return ChargeType.major_charge_group.clear(self)

    def num_major_charge_group(self) -> int:
        return ChargeType.major_charge_group.count(self)

    def get_major_charge_group_by_mrid(self, mrid: str) -> MajorChargeGroup | None:
        return ChargeType.major_charge_group.get_by_mrid(self, mrid)

    def add_charge_component(self, charge_component: ChargeComponent) -> Self:
        return ChargeType.charge_components.add(self, charge_component)

    def remove_charge_component(self, charge_component: ChargeComponent) -> Self:
        return ChargeType.charge_components.remove(self, charge_component)

    def clear_charge_components(self) -> Self:
        return ChargeType.charge_components.clear(self)

    def num_charge_component(self) -> int:
        return ChargeType.charge_components.count(self)

    def get_charge_component_by_mrid(self, mrid: str) -> ChargeComponent | None:
        return ChargeType.charge_components.get_by_mrid(self, mrid)

    def add_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return ChargeType.mkt_user_attribute.add(self, mkt_user_attribute)

    def remove_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return ChargeType.mkt_user_attribute.remove(self, mkt_user_attribute)

    def clear_mkt_user_attribute(self) -> Self:
        return ChargeType.mkt_user_attribute.clear(self)

    def num_mkt_user_attribute(self) -> int:
        return ChargeType.mkt_user_attribute.count(self)
