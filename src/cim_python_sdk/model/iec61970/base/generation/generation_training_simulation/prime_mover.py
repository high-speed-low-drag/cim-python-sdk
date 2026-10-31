"""CIM class PrimeMover (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.synchronous_machine import SynchronousMachine


class PrimeMover(PowerSystemResource):
    """The machine used to develop mechanical energy used to drive a generator."""

    __slots__ = ("_synchronous_machines", "prime_mover_rating")

    prime_mover_rating: float | None

    synchronous_machines: Many[SynchronousMachine] = Many(
        EndMeta(
            name="synchronous_machines",
            cim_role="SynchronousMachines",
            target="cim_python_sdk.model.iec61970.base.wires.synchronous_machine:SynchronousMachine",
            many=True,
            lower=0,
            upper=None,
            inverse="prime_movers",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PrimeMover",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{D20ACBF5-8A0B-472e-8155-B4B70315ADA3}",
        attributes=(
            AttrMeta("prime_mover_rating", "primeMoverRating", "float", 0, 1, "primitive"),
        ),
        ends=(synchronous_machines.meta,),
    )

    def __init__(
        self,
        *,
        prime_mover_rating: float | None = None,
        synchronous_machines: Iterable[SynchronousMachine] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.prime_mover_rating = prime_mover_rating
        if synchronous_machines is not None:
            PrimeMover.synchronous_machines.extend(self, synchronous_machines)

    def add_synchronous_machine(self, synchronous_machine: SynchronousMachine) -> Self:
        return PrimeMover.synchronous_machines.add(self, synchronous_machine)

    def remove_synchronous_machine(self, synchronous_machine: SynchronousMachine) -> Self:
        return PrimeMover.synchronous_machines.remove(self, synchronous_machine)

    def clear_synchronous_machines(self) -> Self:
        return PrimeMover.synchronous_machines.clear(self)

    def num_synchronous_machine(self) -> int:
        return PrimeMover.synchronous_machines.count(self)

    def get_synchronous_machine_by_mrid(self, mrid: str) -> SynchronousMachine | None:
        return PrimeMover.synchronous_machines.get_by_mrid(self, mrid)
