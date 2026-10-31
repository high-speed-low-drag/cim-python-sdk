"""CIM class EnvironmentalDataProvider (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.environmental.environmental_alert import EnvironmentalAlert
    from cim_python_sdk.model.iec62325.environmental.environmental_information import (
        EnvironmentalInformation,
    )


class EnvironmentalDataProvider(OrganisationRole):
    """Entity providing environmental data. Could be an observed weather data provider, an
    entity providing forecasts, an authority providing alerts, etc."""

    __slots__ = ("_environmental_alert", "_environmental_information")

    environmental_alert: Many[EnvironmentalAlert] = Many(
        EndMeta(
            name="environmental_alert",
            cim_role="EnvironmentalAlert",
            target="cim_python_sdk.model.iec62325.environmental.environmental_alert:EnvironmentalAlert",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_data_provider",
            aggregation="none",
        )
    )
    environmental_information: Many[EnvironmentalInformation] = Many(
        EndMeta(
            name="environmental_information",
            cim_role="EnvironmentalInformation",
            target="cim_python_sdk.model.iec62325.environmental.environmental_information:EnvironmentalInformation",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_data_provider",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalDataProvider",
        package="TC57CIM/IEC62325/Environmental",
        guid="{5C4D4CE8-7157-4493-91A6-EB085F29B2A9}",
        ends=(
            environmental_alert.meta,
            environmental_information.meta,
        ),
    )

    def __init__(
        self,
        *,
        environmental_alert: Iterable[EnvironmentalAlert] | None = None,
        environmental_information: Iterable[EnvironmentalInformation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if environmental_alert is not None:
            EnvironmentalDataProvider.environmental_alert.extend(self, environmental_alert)
        if environmental_information is not None:
            EnvironmentalDataProvider.environmental_information.extend(
                self, environmental_information
            )

    def add_environmental_alert(self, environmental_alert: EnvironmentalAlert) -> Self:
        return EnvironmentalDataProvider.environmental_alert.add(self, environmental_alert)

    def remove_environmental_alert(self, environmental_alert: EnvironmentalAlert) -> Self:
        return EnvironmentalDataProvider.environmental_alert.remove(self, environmental_alert)

    def clear_environmental_alert(self) -> Self:
        return EnvironmentalDataProvider.environmental_alert.clear(self)

    def num_environmental_alert(self) -> int:
        return EnvironmentalDataProvider.environmental_alert.count(self)

    def get_environmental_alert_by_mrid(self, mrid: str) -> EnvironmentalAlert | None:
        return EnvironmentalDataProvider.environmental_alert.get_by_mrid(self, mrid)

    def add_environmental_information(
        self, environmental_information: EnvironmentalInformation
    ) -> Self:
        return EnvironmentalDataProvider.environmental_information.add(
            self, environmental_information
        )

    def remove_environmental_information(
        self, environmental_information: EnvironmentalInformation
    ) -> Self:
        return EnvironmentalDataProvider.environmental_information.remove(
            self, environmental_information
        )

    def clear_environmental_information(self) -> Self:
        return EnvironmentalDataProvider.environmental_information.clear(self)

    def num_environmental_information(self) -> int:
        return EnvironmentalDataProvider.environmental_information.count(self)

    def get_environmental_information_by_mrid(self, mrid: str) -> EnvironmentalInformation | None:
        return EnvironmentalDataProvider.environmental_information.get_by_mrid(self, mrid)
