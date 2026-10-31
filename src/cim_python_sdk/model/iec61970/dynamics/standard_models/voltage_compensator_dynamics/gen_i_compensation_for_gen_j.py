"""CIM class GenICompensationForGenJ (TC57CIM/IEC61970/Dynamics/StandardModels/VoltageCompensatorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
        SynchronousMachineDynamics,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.v_comp_ieee_type2 import (
        VCompIEEEType2,
    )


class GenICompensationForGenJ(IdentifiedObject):
    """Resistive and reactive components of compensation for generator associated with IEEE
    type 2 voltage compensator for current flow out of another generator in the
    interconnection."""

    __slots__ = ("_synchronous_machine_dynamics", "_vcomp_ieee_type2", "rcij", "xcij")

    rcij: float | None  # PU
    xcij: float | None  # PU

    vcomp_ieee_type2: One[VCompIEEEType2] = One(
        EndMeta(
            name="vcomp_ieee_type2",
            cim_role="VcompIEEEType2",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.v_comp_ieee_type2:VCompIEEEType2",
            many=False,
            lower=1,
            upper=1,
            inverse="gen_i_compensation_for_gen_j",
            aggregation="none",
        )
    )
    synchronous_machine_dynamics: One[SynchronousMachineDynamics] = One(
        EndMeta(
            name="synchronous_machine_dynamics",
            cim_role="SynchronousMachineDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics:SynchronousMachineDynamics",
            many=False,
            lower=1,
            upper=1,
            inverse="gen_i_compensation_for_gen_j",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GenICompensationForGenJ",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/VoltageCompensatorDynamics",
        guid="{FEED90B2-2208-4aca-AFD0-1ABDF5B94DE8}",
        attributes=(
            AttrMeta("rcij", "rcij", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xcij", "xcij", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            vcomp_ieee_type2.meta,
            synchronous_machine_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        rcij: float | None = None,
        xcij: float | None = None,
        vcomp_ieee_type2: VCompIEEEType2 | None = None,
        synchronous_machine_dynamics: SynchronousMachineDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rcij = rcij
        self.xcij = xcij
        if vcomp_ieee_type2 is not None:
            self.vcomp_ieee_type2 = vcomp_ieee_type2
        if synchronous_machine_dynamics is not None:
            self.synchronous_machine_dynamics = synchronous_machine_dynamics
