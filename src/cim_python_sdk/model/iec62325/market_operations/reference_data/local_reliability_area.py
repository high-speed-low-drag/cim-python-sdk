"""CIM class LocalReliabilityArea (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class LocalReliabilityArea(IdentifiedObject):
    """Allows definition of reliability areas (e.g.. load pockets) within the ISO/RTO."""

    __slots__ = ("_registered_generator", "_rto")

    registered_generator: Many[RegisteredGenerator] = Many(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=True,
            lower=0,
            upper=None,
            inverse="local_reliability_area",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="local_reliability_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LocalReliabilityArea",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{2577783B-B2ED-4938-B2BB-071686AA5A25}",
        ends=(
            registered_generator.meta,
            rto.meta,
        ),
    )

    def __init__(
        self,
        *,
        registered_generator: Iterable[RegisteredGenerator] | None = None,
        rto: RTO | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if registered_generator is not None:
            LocalReliabilityArea.registered_generator.extend(self, registered_generator)
        if rto is not None:
            self.rto = rto

    def add_registered_generator(self, registered_generator: RegisteredGenerator) -> Self:
        return LocalReliabilityArea.registered_generator.add(self, registered_generator)

    def remove_registered_generator(self, registered_generator: RegisteredGenerator) -> Self:
        return LocalReliabilityArea.registered_generator.remove(self, registered_generator)

    def clear_registered_generator(self) -> Self:
        return LocalReliabilityArea.registered_generator.clear(self)

    def num_registered_generator(self) -> int:
        return LocalReliabilityArea.registered_generator.count(self)

    def get_registered_generator_by_mrid(self, mrid: str) -> RegisteredGenerator | None:
        return LocalReliabilityArea.registered_generator.get_by_mrid(self, mrid)
