"""CIM class VCompIEEEType2 (TC57CIM/IEC61970/Dynamics/StandardModels/VoltageCompensatorDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.voltage_compensator_dynamics import (
    VoltageCompensatorDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.gen_i_compensation_for_gen_j import (
        GenICompensationForGenJ,
    )


class VCompIEEEType2(VoltageCompensatorDynamics):
    """Terminal voltage transducer and load compensator as defined in IEEE 421.5-2005, 4. This
    model is designed to cover the following types of compensation:

    - reactive droop;

    - transformer-drop or line-drop compensation;

    - reactive differential compensation known also as cross-current compensation.

    Reference: IEEE 421.5-2005, 4."""

    __slots__ = ("_gen_i_compensation_for_gen_j", "tr")

    tr: float | None  # Seconds

    gen_i_compensation_for_gen_j: Many[GenICompensationForGenJ] = Many(
        EndMeta(
            name="gen_i_compensation_for_gen_j",
            cim_role="GenICompensationForGenJ",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.voltage_compensator_dynamics.gen_i_compensation_for_gen_j:GenICompensationForGenJ",
            many=True,
            lower=2,
            upper=None,
            inverse="vcomp_ieee_type2",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VCompIEEEType2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/VoltageCompensatorDynamics",
        guid="{4B0B8BCB-A18C-4ad3-BCA6-8669B3E51D26}",
        attributes=(AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),),
        ends=(gen_i_compensation_for_gen_j.meta,),
    )

    def __init__(
        self,
        *,
        tr: float | None = None,
        gen_i_compensation_for_gen_j: Iterable[GenICompensationForGenJ] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tr = tr
        if gen_i_compensation_for_gen_j is not None:
            VCompIEEEType2.gen_i_compensation_for_gen_j.extend(self, gen_i_compensation_for_gen_j)

    def add_gen_i_compensation_for_gen_j(
        self, gen_i_compensation_for_gen_j: GenICompensationForGenJ
    ) -> Self:
        return VCompIEEEType2.gen_i_compensation_for_gen_j.add(self, gen_i_compensation_for_gen_j)

    def remove_gen_i_compensation_for_gen_j(
        self, gen_i_compensation_for_gen_j: GenICompensationForGenJ
    ) -> Self:
        return VCompIEEEType2.gen_i_compensation_for_gen_j.remove(
            self, gen_i_compensation_for_gen_j
        )

    def clear_gen_i_compensation_for_gen_j(self) -> Self:
        return VCompIEEEType2.gen_i_compensation_for_gen_j.clear(self)

    def num_gen_i_compensation_for_gen_j(self) -> int:
        return VCompIEEEType2.gen_i_compensation_for_gen_j.count(self)

    def get_gen_i_compensation_for_gen_j_by_mrid(self, mrid: str) -> GenICompensationForGenJ | None:
        return VCompIEEEType2.gen_i_compensation_for_gen_j.get_by_mrid(self, mrid)
