"""CIM class AuxiliaryCost (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_values import (
        AuxiliaryValues,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.market_type import MarketType


class AuxiliaryCost(CimObject):
    """Models Market clearing results for Auxiliary costs."""

    __slots__ = (
        "_auxillary_values",
        "interval_start_time",
        "market_type",
        "update_time_stamp",
        "update_user",
    )

    interval_start_time: _dt.datetime | None
    market_type: MarketType | None
    update_time_stamp: _dt.datetime | None
    update_user: str | None

    auxillary_values: Many[AuxiliaryValues] = Many(
        EndMeta(
            name="auxillary_values",
            cim_role="AuxillaryValues",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_values:AuxiliaryValues",
            many=True,
            lower=1,
            upper=None,
            inverse="auxillary_cost",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AuxiliaryCost",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{B672FFF0-809C-4141-9128-CFBB46BB9E9E}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "MarketType", 0, 1, "enumeration"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
        ),
        ends=(auxillary_values.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        market_type: MarketType | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_user: str | None = None,
        auxillary_values: Iterable[AuxiliaryValues] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.market_type = market_type
        self.update_time_stamp = update_time_stamp
        self.update_user = update_user
        if auxillary_values is not None:
            AuxiliaryCost.auxillary_values.extend(self, auxillary_values)

    def add_auxillary_value(self, auxillary_value: AuxiliaryValues) -> Self:
        return AuxiliaryCost.auxillary_values.add(self, auxillary_value)

    def remove_auxillary_value(self, auxillary_value: AuxiliaryValues) -> Self:
        return AuxiliaryCost.auxillary_values.remove(self, auxillary_value)

    def clear_auxillary_values(self) -> Self:
        return AuxiliaryCost.auxillary_values.clear(self)

    def num_auxillary_value(self) -> int:
        return AuxiliaryCost.auxillary_values.count(self)
