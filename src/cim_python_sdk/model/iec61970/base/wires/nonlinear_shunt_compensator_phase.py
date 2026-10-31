"""CIM class NonlinearShuntCompensatorPhase (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.shunt_compensator_phase import ShuntCompensatorPhase

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator_phase_point import (
        NonlinearShuntCompensatorPhasePoint,
    )


class NonlinearShuntCompensatorPhase(ShuntCompensatorPhase):
    """A per phase non linear shunt compensator has bank or section admittance values that
    differ. The attributes g and b of the associated NonlinearShuntCompensatorPhasePoint
    describe the total conductance and admittance of a NonlinearShuntCompensatorPhasePoint
    at a section number specified by NonlinearShuntCompensatorPhasePoint.sectionNumber."""

    __slots__ = ("_nonlinear_shunt_compensator_phase_points",)

    nonlinear_shunt_compensator_phase_points: Many[NonlinearShuntCompensatorPhasePoint] = Many(
        EndMeta(
            name="nonlinear_shunt_compensator_phase_points",
            cim_role="NonlinearShuntCompensatorPhasePoints",
            target="cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator_phase_point:NonlinearShuntCompensatorPhasePoint",
            many=True,
            lower=1,
            upper=None,
            inverse="nonlinear_shunt_compensator_phase",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NonlinearShuntCompensatorPhase",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{178D630D-8883-41d1-BFE0-81BFD2B70087}",
        ends=(nonlinear_shunt_compensator_phase_points.meta,),
    )

    def __init__(
        self,
        *,
        nonlinear_shunt_compensator_phase_points: Iterable[NonlinearShuntCompensatorPhasePoint]
        | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if nonlinear_shunt_compensator_phase_points is not None:
            NonlinearShuntCompensatorPhase.nonlinear_shunt_compensator_phase_points.extend(
                self, nonlinear_shunt_compensator_phase_points
            )

    def add_nonlinear_shunt_compensator_phase_point(
        self, nonlinear_shunt_compensator_phase_point: NonlinearShuntCompensatorPhasePoint
    ) -> Self:
        return NonlinearShuntCompensatorPhase.nonlinear_shunt_compensator_phase_points.add(
            self, nonlinear_shunt_compensator_phase_point
        )

    def remove_nonlinear_shunt_compensator_phase_point(
        self, nonlinear_shunt_compensator_phase_point: NonlinearShuntCompensatorPhasePoint
    ) -> Self:
        return NonlinearShuntCompensatorPhase.nonlinear_shunt_compensator_phase_points.remove(
            self, nonlinear_shunt_compensator_phase_point
        )

    def clear_nonlinear_shunt_compensator_phase_points(self) -> Self:
        return NonlinearShuntCompensatorPhase.nonlinear_shunt_compensator_phase_points.clear(self)

    def num_nonlinear_shunt_compensator_phase_point(self) -> int:
        return NonlinearShuntCompensatorPhase.nonlinear_shunt_compensator_phase_points.count(self)
