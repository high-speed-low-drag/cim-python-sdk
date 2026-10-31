"""CIM class ReactiveCapabilityCurve (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.equivalents.equivalent_injection import (
        EquivalentInjection,
    )
    from cim_python_sdk.model.iec61970.base.wires.synchronous_machine import SynchronousMachine


class ReactiveCapabilityCurve(Curve):
    """Reactive power rating envelope versus the synchronous machine's active power, in both
    the generating and motoring modes. For each active power value there is a corresponding
    high and low reactive power limit value. Typically there will be a separate curve for
    each coolant condition, such as hydrogen pressure. The Y1 axis values represent reactive
    minimum and the Y2 axis values represent reactive maximum."""

    __slots__ = (
        "_equivalent_injection",
        "_initially_used_by_synchronous_machines",
        "_synchronous_machines",
        "coolant_temperature",
        "hydrogen_pressure",
    )

    coolant_temperature: float | None  # Temperature
    hydrogen_pressure: float | None  # Pressure

    synchronous_machines: Many[SynchronousMachine] = Many(
        EndMeta(
            name="synchronous_machines",
            cim_role="SynchronousMachines",
            target="cim_python_sdk.model.iec61970.base.wires.synchronous_machine:SynchronousMachine",
            many=True,
            lower=1,
            upper=None,
            inverse="reactive_capability_curves",
            aggregation="none",
        )
    )
    initially_used_by_synchronous_machines: Many[SynchronousMachine] = Many(
        EndMeta(
            name="initially_used_by_synchronous_machines",
            cim_role="InitiallyUsedBySynchronousMachines",
            target="cim_python_sdk.model.iec61970.base.wires.synchronous_machine:SynchronousMachine",
            many=True,
            lower=1,
            upper=None,
            inverse="initial_reactive_capability_curve",
            aggregation="none",
        )
    )
    equivalent_injection: Many[EquivalentInjection] = Many(
        EndMeta(
            name="equivalent_injection",
            cim_role="EquivalentInjection",
            target="cim_python_sdk.model.iec61970.base.equivalents.equivalent_injection:EquivalentInjection",
            many=True,
            lower=0,
            upper=None,
            inverse="reactive_capability_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReactiveCapabilityCurve",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{AB5F986C-93A1-4f1f-A62B-CFB733BEF874}",
        attributes=(
            AttrMeta(
                "coolant_temperature", "coolantTemperature", "Temperature", 0, 1, "cimdatatype"
            ),
            AttrMeta("hydrogen_pressure", "hydrogenPressure", "Pressure", 0, 1, "cimdatatype"),
        ),
        ends=(
            synchronous_machines.meta,
            initially_used_by_synchronous_machines.meta,
            equivalent_injection.meta,
        ),
    )

    def __init__(
        self,
        *,
        coolant_temperature: float | None = None,
        hydrogen_pressure: float | None = None,
        synchronous_machines: Iterable[SynchronousMachine] | None = None,
        initially_used_by_synchronous_machines: Iterable[SynchronousMachine] | None = None,
        equivalent_injection: Iterable[EquivalentInjection] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.coolant_temperature = coolant_temperature
        self.hydrogen_pressure = hydrogen_pressure
        if synchronous_machines is not None:
            ReactiveCapabilityCurve.synchronous_machines.extend(self, synchronous_machines)
        if initially_used_by_synchronous_machines is not None:
            ReactiveCapabilityCurve.initially_used_by_synchronous_machines.extend(
                self, initially_used_by_synchronous_machines
            )
        if equivalent_injection is not None:
            ReactiveCapabilityCurve.equivalent_injection.extend(self, equivalent_injection)

    def add_synchronous_machine(self, synchronous_machine: SynchronousMachine) -> Self:
        return ReactiveCapabilityCurve.synchronous_machines.add(self, synchronous_machine)

    def remove_synchronous_machine(self, synchronous_machine: SynchronousMachine) -> Self:
        return ReactiveCapabilityCurve.synchronous_machines.remove(self, synchronous_machine)

    def clear_synchronous_machines(self) -> Self:
        return ReactiveCapabilityCurve.synchronous_machines.clear(self)

    def num_synchronous_machine(self) -> int:
        return ReactiveCapabilityCurve.synchronous_machines.count(self)

    def get_synchronous_machine_by_mrid(self, mrid: str) -> SynchronousMachine | None:
        return ReactiveCapabilityCurve.synchronous_machines.get_by_mrid(self, mrid)

    def add_initially_used_by_synchronous_machine(
        self, initially_used_by_synchronous_machine: SynchronousMachine
    ) -> Self:
        return ReactiveCapabilityCurve.initially_used_by_synchronous_machines.add(
            self, initially_used_by_synchronous_machine
        )

    def remove_initially_used_by_synchronous_machine(
        self, initially_used_by_synchronous_machine: SynchronousMachine
    ) -> Self:
        return ReactiveCapabilityCurve.initially_used_by_synchronous_machines.remove(
            self, initially_used_by_synchronous_machine
        )

    def clear_initially_used_by_synchronous_machines(self) -> Self:
        return ReactiveCapabilityCurve.initially_used_by_synchronous_machines.clear(self)

    def num_initially_used_by_synchronous_machine(self) -> int:
        return ReactiveCapabilityCurve.initially_used_by_synchronous_machines.count(self)

    def get_initially_used_by_synchronous_machine_by_mrid(
        self, mrid: str
    ) -> SynchronousMachine | None:
        return ReactiveCapabilityCurve.initially_used_by_synchronous_machines.get_by_mrid(
            self, mrid
        )

    def add_equivalent_injection(self, equivalent_injection: EquivalentInjection) -> Self:
        return ReactiveCapabilityCurve.equivalent_injection.add(self, equivalent_injection)

    def remove_equivalent_injection(self, equivalent_injection: EquivalentInjection) -> Self:
        return ReactiveCapabilityCurve.equivalent_injection.remove(self, equivalent_injection)

    def clear_equivalent_injection(self) -> Self:
        return ReactiveCapabilityCurve.equivalent_injection.clear(self)

    def num_equivalent_injection(self) -> int:
        return ReactiveCapabilityCurve.equivalent_injection.count(self)

    def get_equivalent_injection_by_mrid(self, mrid: str) -> EquivalentInjection | None:
        return ReactiveCapabilityCurve.equivalent_injection.get_by_mrid(self, mrid)
