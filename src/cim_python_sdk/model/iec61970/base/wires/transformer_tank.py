"""CIM class TransformerTank (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation import (
        TransformerObservation,
    )
    from cim_python_sdk.model.iec61970.base.wires.power_transformer import PowerTransformer
    from cim_python_sdk.model.iec61970.base.wires.transformer_tank_end import TransformerTankEnd


class TransformerTank(Equipment):
    """An assembly of two or more coupled windings that transform electrical power between
    voltage levels. These windings are bound on a common core and placed in the same tank.
    Transformer tank can be used to model both single-phase and 3-phase transformers."""

    __slots__ = ("_power_transformer", "_transformer_observations", "_transformer_tank_ends")

    transformer_observations: Many[TransformerObservation] = Many(
        EndMeta(
            name="transformer_observations",
            cim_role="TransformerObservations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation:TransformerObservation",
            many=True,
            lower=0,
            upper=None,
            inverse="transformer",
            aggregation="none",
        )
    )
    power_transformer: One[PowerTransformer] = One(
        EndMeta(
            name="power_transformer",
            cim_role="PowerTransformer",
            target="cim_python_sdk.model.iec61970.base.wires.power_transformer:PowerTransformer",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_tanks",
            aggregation="none",
        )
    )
    transformer_tank_ends: Many[TransformerTankEnd] = Many(
        EndMeta(
            name="transformer_tank_ends",
            cim_role="TransformerTankEnds",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_tank_end:TransformerTankEnd",
            many=True,
            lower=1,
            upper=None,
            inverse="transformer_tank",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerTank",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{0CAA4373-C2DA-47f6-A18B-9EDC59465FCE}",
        ends=(
            transformer_observations.meta,
            power_transformer.meta,
            transformer_tank_ends.meta,
        ),
    )

    def __init__(
        self,
        *,
        transformer_observations: Iterable[TransformerObservation] | None = None,
        power_transformer: PowerTransformer | None = None,
        transformer_tank_ends: Iterable[TransformerTankEnd] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if transformer_observations is not None:
            TransformerTank.transformer_observations.extend(self, transformer_observations)
        if power_transformer is not None:
            self.power_transformer = power_transformer
        if transformer_tank_ends is not None:
            TransformerTank.transformer_tank_ends.extend(self, transformer_tank_ends)

    def add_transformer_observation(self, transformer_observation: TransformerObservation) -> Self:
        return TransformerTank.transformer_observations.add(self, transformer_observation)

    def remove_transformer_observation(
        self, transformer_observation: TransformerObservation
    ) -> Self:
        return TransformerTank.transformer_observations.remove(self, transformer_observation)

    def clear_transformer_observations(self) -> Self:
        return TransformerTank.transformer_observations.clear(self)

    def num_transformer_observation(self) -> int:
        return TransformerTank.transformer_observations.count(self)

    def get_transformer_observation_by_mrid(self, mrid: str) -> TransformerObservation | None:
        return TransformerTank.transformer_observations.get_by_mrid(self, mrid)

    def add_transformer_tank_end(self, transformer_tank_end: TransformerTankEnd) -> Self:
        return TransformerTank.transformer_tank_ends.add(self, transformer_tank_end)

    def remove_transformer_tank_end(self, transformer_tank_end: TransformerTankEnd) -> Self:
        return TransformerTank.transformer_tank_ends.remove(self, transformer_tank_end)

    def clear_transformer_tank_ends(self) -> Self:
        return TransformerTank.transformer_tank_ends.clear(self)

    def num_transformer_tank_end(self) -> int:
        return TransformerTank.transformer_tank_ends.count(self)

    def get_transformer_tank_end_by_mrid(self, mrid: str) -> TransformerTankEnd | None:
        return TransformerTank.transformer_tank_ends.get_by_mrid(self, mrid)
