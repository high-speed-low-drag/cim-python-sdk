"""CIM class DERGroupForecast (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup


class DERGroupForecast(IdentifiedObject):
    """Specifies the forecasted values of the DERMonitorableParameters for a DER Group over a
    specific time interval."""

    __slots__ = ("_end_device_group", "prediction_creation_date")

    prediction_creation_date: _dt.datetime | None

    end_device_group: Many[EndDeviceGroup] = Many(
        EndMeta(
            name="end_device_group",
            cim_role="EndDeviceGroup",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=True,
            lower=1,
            upper=None,
            inverse="der_group_forecast",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DERGroupForecast",
        package="TC57CIM/IEC61968/DER",
        guid="{F9CB8CC5-A128-4b25-8EF9-8C0280844DD2}",
        attributes=(
            AttrMeta(
                "prediction_creation_date", "predictionCreationDate", "datetime", 0, 1, "primitive"
            ),
        ),
        ends=(end_device_group.meta,),
    )

    def __init__(
        self,
        *,
        prediction_creation_date: _dt.datetime | None = None,
        end_device_group: Iterable[EndDeviceGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.prediction_creation_date = prediction_creation_date
        if end_device_group is not None:
            DERGroupForecast.end_device_group.extend(self, end_device_group)

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERGroupForecast.end_device_group.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERGroupForecast.end_device_group.remove(self, end_device_group)

    def clear_end_device_group(self) -> Self:
        return DERGroupForecast.end_device_group.clear(self)

    def num_end_device_group(self) -> int:
        return DERGroupForecast.end_device_group.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return DERGroupForecast.end_device_group.get_by_mrid(self, mrid)
