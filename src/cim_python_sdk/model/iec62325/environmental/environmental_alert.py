"""CIM class EnvironmentalAlert (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec62325.environmental.alert_type_list import AlertTypeList
    from cim_python_sdk.model.iec62325.environmental.environmental_data_provider import (
        EnvironmentalDataProvider,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_location_type import (
        EnvironmentalLocationType,
    )


class EnvironmentalAlert(ActivityRecord):
    """An environmental alert issued by a provider or system."""

    __slots__ = (
        "_alert_type_list",
        "_environmental_data_provider",
        "_environmental_location_kind",
        "alert_type",
        "cancelled_date_time",
        "headline",
        "in_effect",
    )

    alert_type: str | None
    cancelled_date_time: _dt.datetime | None
    headline: str | None
    in_effect: DateTimeInterval | None

    environmental_location_kind: Many[EnvironmentalLocationType] = Many(
        EndMeta(
            name="environmental_location_kind",
            cim_role="EnvironmentalLocationKind",
            target="cim_python_sdk.model.iec62325.environmental.environmental_location_type:EnvironmentalLocationType",
            many=True,
            lower=1,
            upper=None,
            inverse="environmental_alert",
            aggregation="none",
        )
    )
    alert_type_list: One[AlertTypeList] = One(
        EndMeta(
            name="alert_type_list",
            cim_role="AlertTypeList",
            target="cim_python_sdk.model.iec62325.environmental.alert_type_list:AlertTypeList",
            many=False,
            lower=1,
            upper=1,
            inverse="environmental_alert",
            aggregation="none",
        )
    )
    environmental_data_provider: One[EnvironmentalDataProvider] = One(
        EndMeta(
            name="environmental_data_provider",
            cim_role="EnvironmentalDataProvider",
            target="cim_python_sdk.model.iec62325.environmental.environmental_data_provider:EnvironmentalDataProvider",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_alert",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalAlert",
        package="TC57CIM/IEC62325/Environmental",
        guid="{0602A6D7-03E3-4067-94A9-A79A9EA3CAB3}",
        attributes=(
            AttrMeta("alert_type", "alertType", "str", 0, 1, "primitive"),
            AttrMeta("cancelled_date_time", "cancelledDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("headline", "headline", "str", 0, 1, "primitive"),
            AttrMeta("in_effect", "inEffect", "DateTimeInterval", 0, 1, "compound"),
        ),
        ends=(
            environmental_location_kind.meta,
            alert_type_list.meta,
            environmental_data_provider.meta,
        ),
    )

    def __init__(
        self,
        *,
        alert_type: str | None = None,
        cancelled_date_time: _dt.datetime | None = None,
        headline: str | None = None,
        in_effect: DateTimeInterval | None = None,
        environmental_location_kind: Iterable[EnvironmentalLocationType] | None = None,
        alert_type_list: AlertTypeList | None = None,
        environmental_data_provider: EnvironmentalDataProvider | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.alert_type = alert_type
        self.cancelled_date_time = cancelled_date_time
        self.headline = headline
        self.in_effect = in_effect
        if environmental_location_kind is not None:
            EnvironmentalAlert.environmental_location_kind.extend(self, environmental_location_kind)
        if alert_type_list is not None:
            self.alert_type_list = alert_type_list
        if environmental_data_provider is not None:
            self.environmental_data_provider = environmental_data_provider

    def add_environmental_location_kind(
        self, environmental_location_kind: EnvironmentalLocationType
    ) -> Self:
        return EnvironmentalAlert.environmental_location_kind.add(self, environmental_location_kind)

    def remove_environmental_location_kind(
        self, environmental_location_kind: EnvironmentalLocationType
    ) -> Self:
        return EnvironmentalAlert.environmental_location_kind.remove(
            self, environmental_location_kind
        )

    def clear_environmental_location_kind(self) -> Self:
        return EnvironmentalAlert.environmental_location_kind.clear(self)

    def num_environmental_location_kind(self) -> int:
        return EnvironmentalAlert.environmental_location_kind.count(self)
