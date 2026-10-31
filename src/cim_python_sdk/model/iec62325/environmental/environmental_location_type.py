"""CIM class EnvironmentalLocationType (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec62325.environmental.env_domain.location_kind import LocationKind
    from cim_python_sdk.model.iec62325.environmental.environmental_alert import EnvironmentalAlert
    from cim_python_sdk.model.iec62325.environmental.environmental_phenomenon import (
        EnvironmentalPhenomenon,
    )


class EnvironmentalLocationType(CimObject):
    """Type of environmental location. Used when an environmental alert or phenomenon has
    multiple locations associated with it."""

    __slots__ = ("_environmental_alert", "_environmental_phenomenon", "_location", "kind")

    kind: LocationKind | None

    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_location_kind",
            aggregation="none",
        )
    )
    environmental_phenomenon: Many[EnvironmentalPhenomenon] = Many(
        EndMeta(
            name="environmental_phenomenon",
            cim_role="EnvironmentalPhenomenon",
            target="cim_python_sdk.model.iec62325.environmental.environmental_phenomenon:EnvironmentalPhenomenon",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_location_kind",
            aggregation="none",
        )
    )
    environmental_alert: Many[EnvironmentalAlert] = Many(
        EndMeta(
            name="environmental_alert",
            cim_role="EnvironmentalAlert",
            target="cim_python_sdk.model.iec62325.environmental.environmental_alert:EnvironmentalAlert",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_location_kind",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalLocationType",
        package="TC57CIM/IEC62325/Environmental",
        guid="{4F05C799-C6C3-46da-8408-7B9C074FC888}",
        attributes=(AttrMeta("kind", "kind", "LocationKind", 0, 1, "enumeration"),),
        ends=(
            location.meta,
            environmental_phenomenon.meta,
            environmental_alert.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: LocationKind | None = None,
        location: Location | None = None,
        environmental_phenomenon: Iterable[EnvironmentalPhenomenon] | None = None,
        environmental_alert: Iterable[EnvironmentalAlert] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if location is not None:
            self.location = location
        if environmental_phenomenon is not None:
            EnvironmentalLocationType.environmental_phenomenon.extend(
                self, environmental_phenomenon
            )
        if environmental_alert is not None:
            EnvironmentalLocationType.environmental_alert.extend(self, environmental_alert)

    def add_environmental_phenomenon(
        self, environmental_phenomenon: EnvironmentalPhenomenon
    ) -> Self:
        return EnvironmentalLocationType.environmental_phenomenon.add(
            self, environmental_phenomenon
        )

    def remove_environmental_phenomenon(
        self, environmental_phenomenon: EnvironmentalPhenomenon
    ) -> Self:
        return EnvironmentalLocationType.environmental_phenomenon.remove(
            self, environmental_phenomenon
        )

    def clear_environmental_phenomenon(self) -> Self:
        return EnvironmentalLocationType.environmental_phenomenon.clear(self)

    def num_environmental_phenomenon(self) -> int:
        return EnvironmentalLocationType.environmental_phenomenon.count(self)

    def add_environmental_alert(self, environmental_alert: EnvironmentalAlert) -> Self:
        return EnvironmentalLocationType.environmental_alert.add(self, environmental_alert)

    def remove_environmental_alert(self, environmental_alert: EnvironmentalAlert) -> Self:
        return EnvironmentalLocationType.environmental_alert.remove(self, environmental_alert)

    def clear_environmental_alert(self) -> Self:
        return EnvironmentalLocationType.environmental_alert.clear(self)

    def num_environmental_alert(self) -> int:
        return EnvironmentalLocationType.environmental_alert.count(self)

    def get_environmental_alert_by_mrid(self, mrid: str) -> EnvironmentalAlert | None:
        return EnvironmentalLocationType.environmental_alert.get_by_mrid(self, mrid)
