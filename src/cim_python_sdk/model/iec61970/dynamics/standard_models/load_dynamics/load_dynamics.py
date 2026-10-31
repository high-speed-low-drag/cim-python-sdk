"""CIM class LoadDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer


class LoadDynamics(IdentifiedObject):
    """Load whose behaviour is described by reference to a standard model or by definition of a
    user-defined model.

    A standard feature of dynamic load behaviour modelling is the ability to associate the
    same behaviour to multiple energy consumers by means of a single load definition. The
    load model is always applied to individual bus loads (energy consumers)."""

    __slots__ = ("_energy_consumer",)

    energy_consumer: Many[EnergyConsumer] = Many(
        EndMeta(
            name="energy_consumer",
            cim_role="EnergyConsumer",
            target="cim_python_sdk.model.iec61970.base.wires.energy_consumer:EnergyConsumer",
            many=True,
            lower=0,
            upper=None,
            inverse="load_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
        guid="{0589465F-40A5-4de5-B0FE-A21D8275117B}",
        ends=(energy_consumer.meta,),
    )

    def __init__(
        self,
        *,
        energy_consumer: Iterable[EnergyConsumer] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_consumer is not None:
            LoadDynamics.energy_consumer.extend(self, energy_consumer)

    def add_energy_consumer(self, energy_consumer: EnergyConsumer) -> Self:
        return LoadDynamics.energy_consumer.add(self, energy_consumer)

    def remove_energy_consumer(self, energy_consumer: EnergyConsumer) -> Self:
        return LoadDynamics.energy_consumer.remove(self, energy_consumer)

    def clear_energy_consumer(self) -> Self:
        return LoadDynamics.energy_consumer.clear(self)

    def num_energy_consumer(self) -> int:
        return LoadDynamics.energy_consumer.count(self)

    def get_energy_consumer_by_mrid(self, mrid: str) -> EnergyConsumer | None:
        return LoadDynamics.energy_consumer.get_by_mrid(self, mrid)
