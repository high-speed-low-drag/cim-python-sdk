"""CIM class Reconditioning (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.cooling_power_rating import (
        CoolingPowerRating,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation import (
        TransformerObservation,
    )


class Reconditioning(IdentifiedObject):
    """Reconditioning information for an asset."""

    __slots__ = ("_asset", "_power_ratings", "_transformer_observations", "date_time")

    date_time: _dt.datetime | None

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="reconditionings",
            aggregation="none",
        )
    )
    power_ratings: Many[CoolingPowerRating] = Many(
        EndMeta(
            name="power_ratings",
            cim_role="PowerRatings",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.cooling_power_rating:CoolingPowerRating",
            many=True,
            lower=0,
            upper=None,
            inverse="reconditionings",
            aggregation="none",
        )
    )
    transformer_observations: Many[TransformerObservation] = Many(
        EndMeta(
            name="transformer_observations",
            cim_role="TransformerObservations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation:TransformerObservation",
            many=True,
            lower=0,
            upper=None,
            inverse="reconditioning",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Reconditioning",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{23446D7A-AE7B-42a2-A40F-37999AF3A101}",
        attributes=(AttrMeta("date_time", "dateTime", "datetime", 0, 1, "primitive"),),
        ends=(
            asset.meta,
            power_ratings.meta,
            transformer_observations.meta,
        ),
    )

    def __init__(
        self,
        *,
        date_time: _dt.datetime | None = None,
        asset: Asset | None = None,
        power_ratings: Iterable[CoolingPowerRating] | None = None,
        transformer_observations: Iterable[TransformerObservation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.date_time = date_time
        if asset is not None:
            self.asset = asset
        if power_ratings is not None:
            Reconditioning.power_ratings.extend(self, power_ratings)
        if transformer_observations is not None:
            Reconditioning.transformer_observations.extend(self, transformer_observations)

    def add_power_rating(self, power_rating: CoolingPowerRating) -> Self:
        return Reconditioning.power_ratings.add(self, power_rating)

    def remove_power_rating(self, power_rating: CoolingPowerRating) -> Self:
        return Reconditioning.power_ratings.remove(self, power_rating)

    def clear_power_ratings(self) -> Self:
        return Reconditioning.power_ratings.clear(self)

    def num_power_rating(self) -> int:
        return Reconditioning.power_ratings.count(self)

    def get_power_rating_by_mrid(self, mrid: str) -> CoolingPowerRating | None:
        return Reconditioning.power_ratings.get_by_mrid(self, mrid)

    def add_transformer_observation(self, transformer_observation: TransformerObservation) -> Self:
        return Reconditioning.transformer_observations.add(self, transformer_observation)

    def remove_transformer_observation(
        self, transformer_observation: TransformerObservation
    ) -> Self:
        return Reconditioning.transformer_observations.remove(self, transformer_observation)

    def clear_transformer_observations(self) -> Self:
        return Reconditioning.transformer_observations.clear(self)

    def num_transformer_observation(self) -> int:
        return Reconditioning.transformer_observations.count(self)

    def get_transformer_observation_by_mrid(self, mrid: str) -> TransformerObservation | None:
        return Reconditioning.transformer_observations.get_by_mrid(self, mrid)
