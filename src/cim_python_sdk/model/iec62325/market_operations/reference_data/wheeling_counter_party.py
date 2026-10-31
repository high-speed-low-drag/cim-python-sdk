"""CIM class WheelingCounterParty (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie import (
        RegisteredInterTie,
    )


class WheelingCounterParty(IdentifiedObject):
    """Counter party in a wheeling transaction."""

    __slots__ = ("_registered_inter_tie",)

    registered_inter_tie: Many[RegisteredInterTie] = Many(
        EndMeta(
            name="registered_inter_tie",
            cim_role="RegisteredInterTie",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_inter_tie:RegisteredInterTie",
            many=True,
            lower=0,
            upper=None,
            inverse="wheeling_counter_party",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WheelingCounterParty",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{6901C2B7-81B7-4efd-984D-F43E4F6AB1C3}",
        ends=(registered_inter_tie.meta,),
    )

    def __init__(
        self,
        *,
        registered_inter_tie: Iterable[RegisteredInterTie] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if registered_inter_tie is not None:
            WheelingCounterParty.registered_inter_tie.extend(self, registered_inter_tie)

    def add_registered_inter_tie(self, registered_inter_tie: RegisteredInterTie) -> Self:
        return WheelingCounterParty.registered_inter_tie.add(self, registered_inter_tie)

    def remove_registered_inter_tie(self, registered_inter_tie: RegisteredInterTie) -> Self:
        return WheelingCounterParty.registered_inter_tie.remove(self, registered_inter_tie)

    def clear_registered_inter_tie(self) -> Self:
        return WheelingCounterParty.registered_inter_tie.clear(self)

    def num_registered_inter_tie(self) -> int:
        return WheelingCounterParty.registered_inter_tie.count(self)

    def get_registered_inter_tie_by_mrid(self, mrid: str) -> RegisteredInterTie | None:
        return WheelingCounterParty.registered_inter_tie.get_by_mrid(self, mrid)
