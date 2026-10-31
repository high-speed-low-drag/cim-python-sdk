"""CIM class TenMinAuxiliaryData (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

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


class TenMinAuxiliaryData(CimObject):
    """Models 10-Minutes Auxiliary Data."""

    __slots__ = ("_auxillary_data", "interval_start_time", "update_time_stamp", "update_user")

    interval_start_time: _dt.datetime | None
    update_user: str | None
    update_time_stamp: _dt.datetime | None

    auxillary_data: Many[AuxiliaryValues] = Many(
        EndMeta(
            name="auxillary_data",
            cim_role="AuxillaryData",
            target="cim_python_sdk.model.iec62325.market_operations.market_quality_system.auxiliary_values:AuxiliaryValues",
            many=True,
            lower=1,
            upper=None,
            inverse="ten_min_auxillary_data",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TenMinAuxiliaryData",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{DA559358-89B5-4579-A3C6-1B01513FCC22}",
        attributes=(
            AttrMeta("interval_start_time", "intervalStartTime", "datetime", 0, 1, "primitive"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
        ),
        ends=(auxillary_data.meta,),
    )

    def __init__(
        self,
        *,
        interval_start_time: _dt.datetime | None = None,
        update_user: str | None = None,
        update_time_stamp: _dt.datetime | None = None,
        auxillary_data: Iterable[AuxiliaryValues] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interval_start_time = interval_start_time
        self.update_user = update_user
        self.update_time_stamp = update_time_stamp
        if auxillary_data is not None:
            TenMinAuxiliaryData.auxillary_data.extend(self, auxillary_data)

    def add_auxillary_data(self, auxillary_data: AuxiliaryValues) -> Self:
        return TenMinAuxiliaryData.auxillary_data.add(self, auxillary_data)

    def remove_auxillary_data(self, auxillary_data: AuxiliaryValues) -> Self:
        return TenMinAuxiliaryData.auxillary_data.remove(self, auxillary_data)

    def clear_auxillary_data(self) -> Self:
        return TenMinAuxiliaryData.auxillary_data.clear(self)

    def num_auxillary_data(self) -> int:
        return TenMinAuxiliaryData.auxillary_data.count(self)
