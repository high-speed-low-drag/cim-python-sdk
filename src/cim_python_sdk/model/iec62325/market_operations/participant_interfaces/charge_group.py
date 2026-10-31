"""CIM class ChargeGroup (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute import (
        MktUserAttribute,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_type import (
        ChargeType,
    )


class ChargeGroup(IdentifiedObject):
    """Charge Group is the grouping of Charge Types for settlement invoicing purpose. Examples
    such as Ancillary Services, Interests, etc."""

    __slots__ = (
        "_charge_group_child",
        "_charge_group_parent",
        "_charge_type",
        "_mkt_user_attribute",
        "effective_date",
        "market_code",
        "termination_date",
    )

    market_code: str | None
    effective_date: _dt.datetime | None
    termination_date: _dt.datetime | None

    charge_group_parent: One[ChargeGroup] = One(
        EndMeta(
            name="charge_group_parent",
            cim_role="ChargeGroupParent",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_group:ChargeGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="charge_group_child",
            aggregation="none",
        )
    )
    charge_group_child: Many[ChargeGroup] = Many(
        EndMeta(
            name="charge_group_child",
            cim_role="ChargeGroupChild",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.charge_group:ChargeGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="charge_group_parent",
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
            inverse="charge_group",
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
            inverse="charge_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ChargeGroup",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{E649DF9F-A47D-4f5a-8BAD-6DBD3D2397F1}",
        attributes=(
            AttrMeta("market_code", "marketCode", "str", 0, 1, "primitive"),
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("termination_date", "terminationDate", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            charge_group_parent.meta,
            charge_group_child.meta,
            charge_type.meta,
            mkt_user_attribute.meta,
        ),
    )

    def __init__(
        self,
        *,
        market_code: str | None = None,
        effective_date: _dt.datetime | None = None,
        termination_date: _dt.datetime | None = None,
        charge_group_parent: ChargeGroup | None = None,
        charge_group_child: Iterable[ChargeGroup] | None = None,
        charge_type: Iterable[ChargeType] | None = None,
        mkt_user_attribute: Iterable[MktUserAttribute] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.market_code = market_code
        self.effective_date = effective_date
        self.termination_date = termination_date
        if charge_group_parent is not None:
            self.charge_group_parent = charge_group_parent
        if charge_group_child is not None:
            ChargeGroup.charge_group_child.extend(self, charge_group_child)
        if charge_type is not None:
            ChargeGroup.charge_type.extend(self, charge_type)
        if mkt_user_attribute is not None:
            ChargeGroup.mkt_user_attribute.extend(self, mkt_user_attribute)

    def add_charge_group_child(self, charge_group_child: ChargeGroup) -> Self:
        return ChargeGroup.charge_group_child.add(self, charge_group_child)

    def remove_charge_group_child(self, charge_group_child: ChargeGroup) -> Self:
        return ChargeGroup.charge_group_child.remove(self, charge_group_child)

    def clear_charge_group_child(self) -> Self:
        return ChargeGroup.charge_group_child.clear(self)

    def num_charge_group_child(self) -> int:
        return ChargeGroup.charge_group_child.count(self)

    def get_charge_group_child_by_mrid(self, mrid: str) -> ChargeGroup | None:
        return ChargeGroup.charge_group_child.get_by_mrid(self, mrid)

    def add_charge_type(self, charge_type: ChargeType) -> Self:
        return ChargeGroup.charge_type.add(self, charge_type)

    def remove_charge_type(self, charge_type: ChargeType) -> Self:
        return ChargeGroup.charge_type.remove(self, charge_type)

    def clear_charge_type(self) -> Self:
        return ChargeGroup.charge_type.clear(self)

    def num_charge_type(self) -> int:
        return ChargeGroup.charge_type.count(self)

    def get_charge_type_by_mrid(self, mrid: str) -> ChargeType | None:
        return ChargeGroup.charge_type.get_by_mrid(self, mrid)

    def add_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return ChargeGroup.mkt_user_attribute.add(self, mkt_user_attribute)

    def remove_mkt_user_attribute(self, mkt_user_attribute: MktUserAttribute) -> Self:
        return ChargeGroup.mkt_user_attribute.remove(self, mkt_user_attribute)

    def clear_mkt_user_attribute(self) -> Self:
        return ChargeGroup.mkt_user_attribute.clear(self)

    def num_mkt_user_attribute(self) -> int:
        return ChargeGroup.mkt_user_attribute.count(self)
