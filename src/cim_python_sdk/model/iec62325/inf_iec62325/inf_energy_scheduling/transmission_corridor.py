"""CIM class TransmissionCorridor (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_right_of_way import (
        TransmissionRightOfWay,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path import (
        TransmissionPath,
    )


class TransmissionCorridor(PowerSystemResource):
    """A corridor containing one or more rights of way"""

    __slots__ = ("_contained_in", "_transmission_right_of_ways")

    transmission_right_of_ways: Many[TransmissionRightOfWay] = Many(
        EndMeta(
            name="transmission_right_of_ways",
            cim_role="TransmissionRightOfWays",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_right_of_way:TransmissionRightOfWay",
            many=True,
            lower=1,
            upper=None,
            inverse="transmission_corridor",
            aggregation="shared",
        )
    )
    contained_in: Many[TransmissionPath] = Many(
        EndMeta(
            name="contained_in",
            cim_role="ContainedIn",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path:TransmissionPath",
            many=True,
            lower=0,
            upper=None,
            inverse="for_",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionCorridor",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{E5523AA5-47CB-4537-ACC5-E09A4AA0B9D9}",
        ends=(
            transmission_right_of_ways.meta,
            contained_in.meta,
        ),
    )

    def __init__(
        self,
        *,
        transmission_right_of_ways: Iterable[TransmissionRightOfWay] | None = None,
        contained_in: Iterable[TransmissionPath] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if transmission_right_of_ways is not None:
            TransmissionCorridor.transmission_right_of_ways.extend(self, transmission_right_of_ways)
        if contained_in is not None:
            TransmissionCorridor.contained_in.extend(self, contained_in)

    def add_transmission_right_of_way(
        self, transmission_right_of_way: TransmissionRightOfWay
    ) -> Self:
        return TransmissionCorridor.transmission_right_of_ways.add(self, transmission_right_of_way)

    def remove_transmission_right_of_way(
        self, transmission_right_of_way: TransmissionRightOfWay
    ) -> Self:
        return TransmissionCorridor.transmission_right_of_ways.remove(
            self, transmission_right_of_way
        )

    def clear_transmission_right_of_ways(self) -> Self:
        return TransmissionCorridor.transmission_right_of_ways.clear(self)

    def num_transmission_right_of_way(self) -> int:
        return TransmissionCorridor.transmission_right_of_ways.count(self)

    def get_transmission_right_of_way_by_mrid(self, mrid: str) -> TransmissionRightOfWay | None:
        return TransmissionCorridor.transmission_right_of_ways.get_by_mrid(self, mrid)

    def add_contained_in(self, contained_in: TransmissionPath) -> Self:
        return TransmissionCorridor.contained_in.add(self, contained_in)

    def remove_contained_in(self, contained_in: TransmissionPath) -> Self:
        return TransmissionCorridor.contained_in.remove(self, contained_in)

    def clear_contained_in(self) -> Self:
        return TransmissionCorridor.contained_in.clear(self)

    def num_contained_in(self) -> int:
        return TransmissionCorridor.contained_in.count(self)

    def get_contained_in_by_mrid(self, mrid: str) -> TransmissionPath | None:
        return TransmissionCorridor.contained_in.get_by_mrid(self, mrid)
