"""CIM class PowerSystemStabilizerDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.dynamics_function_block import (
    DynamicsFunctionBlock,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal import (
        RemoteInputSignal,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics import (
        ExcitationSystemDynamics,
    )


class PowerSystemStabilizerDynamics(DynamicsFunctionBlock):
    """Power system stabilizer function block whose behaviour is described by reference to a
    standard model or by definition of a user-defined model."""

    __slots__ = ("_excitation_system_dynamics", "_remote_input_signal")

    remote_input_signal: Many[RemoteInputSignal] = Many(
        EndMeta(
            name="remote_input_signal",
            cim_role="RemoteInputSignal",
            target="cim_python_sdk.model.iec61970.dynamics.standard_interconnections.remote_input_signal:RemoteInputSignal",
            many=True,
            lower=0,
            upper=None,
            inverse="power_system_stabilizer_dynamics",
            aggregation="none",
        )
    )
    excitation_system_dynamics: One[ExcitationSystemDynamics] = One(
        EndMeta(
            name="excitation_system_dynamics",
            cim_role="ExcitationSystemDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.excitation_system_dynamics.excitation_system_dynamics:ExcitationSystemDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="power_system_stabilizer_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerSystemStabilizerDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{3F0A3D95-88A1-428a-8F47-7B6F73E52AB6}",
        ends=(
            remote_input_signal.meta,
            excitation_system_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        remote_input_signal: Iterable[RemoteInputSignal] | None = None,
        excitation_system_dynamics: ExcitationSystemDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if remote_input_signal is not None:
            PowerSystemStabilizerDynamics.remote_input_signal.extend(self, remote_input_signal)
        if excitation_system_dynamics is not None:
            self.excitation_system_dynamics = excitation_system_dynamics

    def add_remote_input_signal(self, remote_input_signal: RemoteInputSignal) -> Self:
        return PowerSystemStabilizerDynamics.remote_input_signal.add(self, remote_input_signal)

    def remove_remote_input_signal(self, remote_input_signal: RemoteInputSignal) -> Self:
        return PowerSystemStabilizerDynamics.remote_input_signal.remove(self, remote_input_signal)

    def clear_remote_input_signal(self) -> Self:
        return PowerSystemStabilizerDynamics.remote_input_signal.clear(self)

    def num_remote_input_signal(self) -> int:
        return PowerSystemStabilizerDynamics.remote_input_signal.count(self)

    def get_remote_input_signal_by_mrid(self, mrid: str) -> RemoteInputSignal | None:
        return PowerSystemStabilizerDynamics.remote_input_signal.get_by_mrid(self, mrid)
