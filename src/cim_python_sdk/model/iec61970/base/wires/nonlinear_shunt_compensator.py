"""CIM class NonlinearShuntCompensator (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.shunt_compensator import ShuntCompensator

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator_point import (
        NonlinearShuntCompensatorPoint,
    )


class NonlinearShuntCompensator(ShuntCompensator):
    """A non linear shunt compensator has bank or section admittance values that differ. The
    attributes g, b, g0 and b0 of the associated NonlinearShuntCompensatorPoint describe the
    total conductance and admittance of a NonlinearShuntCompensatorPoint at a section number
    specified by NonlinearShuntCompensatorPoint.sectionNumber."""

    __slots__ = ("_nonlinear_shunt_compensator_points",)

    nonlinear_shunt_compensator_points: Many[NonlinearShuntCompensatorPoint] = Many(
        EndMeta(
            name="nonlinear_shunt_compensator_points",
            cim_role="NonlinearShuntCompensatorPoints",
            target="cim_python_sdk.model.iec61970.base.wires.nonlinear_shunt_compensator_point:NonlinearShuntCompensatorPoint",
            many=True,
            lower=1,
            upper=None,
            inverse="nonlinear_shunt_compensator",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NonlinearShuntCompensator",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{111DB4FF-7967-4eb5-AABE-CDA0EA065CF8}",
        ends=(nonlinear_shunt_compensator_points.meta,),
    )

    def __init__(
        self,
        *,
        nonlinear_shunt_compensator_points: Iterable[NonlinearShuntCompensatorPoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if nonlinear_shunt_compensator_points is not None:
            NonlinearShuntCompensator.nonlinear_shunt_compensator_points.extend(
                self, nonlinear_shunt_compensator_points
            )

    def add_nonlinear_shunt_compensator_point(
        self, nonlinear_shunt_compensator_point: NonlinearShuntCompensatorPoint
    ) -> Self:
        return NonlinearShuntCompensator.nonlinear_shunt_compensator_points.add(
            self, nonlinear_shunt_compensator_point
        )

    def remove_nonlinear_shunt_compensator_point(
        self, nonlinear_shunt_compensator_point: NonlinearShuntCompensatorPoint
    ) -> Self:
        return NonlinearShuntCompensator.nonlinear_shunt_compensator_points.remove(
            self, nonlinear_shunt_compensator_point
        )

    def clear_nonlinear_shunt_compensator_points(self) -> Self:
        return NonlinearShuntCompensator.nonlinear_shunt_compensator_points.clear(self)

    def num_nonlinear_shunt_compensator_point(self) -> int:
        return NonlinearShuntCompensator.nonlinear_shunt_compensator_points.count(self)
