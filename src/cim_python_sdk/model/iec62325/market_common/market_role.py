"""CIM class MarketRole (TC57CIM/IEC62325/MarketCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant


class MarketRole(OrganisationRole):
    """The external intended behavior played by a party within the electricity market."""

    __slots__ = ("_market_participant", "type")

    type: str | None

    market_participant: Many[MarketParticipant] = Many(
        EndMeta(
            name="market_participant",
            cim_role="MarketParticipant",
            target="cim_python_sdk.model.iec62325.market_common.market_participant:MarketParticipant",
            many=True,
            lower=0,
            upper=None,
            inverse="market_role",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketRole",
        package="TC57CIM/IEC62325/MarketCommon",
        guid="{67F6267D-A999-4c0d-8D42-18D30418307C}",
        attributes=(AttrMeta("type", "type", "str", 0, 1, "primitive"),),
        ends=(market_participant.meta,),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        market_participant: Iterable[MarketParticipant] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        if market_participant is not None:
            MarketRole.market_participant.extend(self, market_participant)

    def add_market_participant(self, market_participant: MarketParticipant) -> Self:
        return MarketRole.market_participant.add(self, market_participant)

    def remove_market_participant(self, market_participant: MarketParticipant) -> Self:
        return MarketRole.market_participant.remove(self, market_participant)

    def clear_market_participant(self) -> Self:
        return MarketRole.market_participant.clear(self)

    def num_market_participant(self) -> int:
        return MarketRole.market_participant.count(self)

    def get_market_participant_by_mrid(self, mrid: str) -> MarketParticipant | None:
        return MarketRole.market_participant.get_by_mrid(self, mrid)
