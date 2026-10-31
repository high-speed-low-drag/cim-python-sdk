"""CIM class ControlAreaGeneratingUnit (TC57CIM/IEC61970/Base/ControlArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.control_area.alt_generating_unit_meas import (
        AltGeneratingUnitMeas,
    )
    from cim_python_sdk.model.iec61970.base.control_area.control_area import ControlArea
    from cim_python_sdk.model.iec61970.base.generation.production.generating_unit import (
        GeneratingUnit,
    )


class ControlAreaGeneratingUnit(IdentifiedObject):
    """A control area generating unit. This class is needed so that alternate control area
    definitions may include the same generating unit. It should be noted that only one
    instance within a control area should reference a specific generating unit."""

    __slots__ = ("_alt_generating_unit_meas", "_control_area", "_generating_unit")

    alt_generating_unit_meas: Many[AltGeneratingUnitMeas] = Many(
        EndMeta(
            name="alt_generating_unit_meas",
            cim_role="AltGeneratingUnitMeas",
            target="cim_python_sdk.model.iec61970.base.control_area.alt_generating_unit_meas:AltGeneratingUnitMeas",
            many=True,
            lower=0,
            upper=None,
            inverse="control_area_generating_unit",
            aggregation="shared",
        )
    )
    generating_unit: One[GeneratingUnit] = One(
        EndMeta(
            name="generating_unit",
            cim_role="GeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.generating_unit:GeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="control_area_generating_unit",
            aggregation="none",
        )
    )
    control_area: One[ControlArea] = One(
        EndMeta(
            name="control_area",
            cim_role="ControlArea",
            target="cim_python_sdk.model.iec61970.base.control_area.control_area:ControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="control_area_generating_unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ControlAreaGeneratingUnit",
        package="TC57CIM/IEC61970/Base/ControlArea",
        guid="{F60BBA5C-76E4-4429-8437-2846CBBD9480}",
        ends=(
            alt_generating_unit_meas.meta,
            generating_unit.meta,
            control_area.meta,
        ),
    )

    def __init__(
        self,
        *,
        alt_generating_unit_meas: Iterable[AltGeneratingUnitMeas] | None = None,
        generating_unit: GeneratingUnit | None = None,
        control_area: ControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if alt_generating_unit_meas is not None:
            ControlAreaGeneratingUnit.alt_generating_unit_meas.extend(
                self, alt_generating_unit_meas
            )
        if generating_unit is not None:
            self.generating_unit = generating_unit
        if control_area is not None:
            self.control_area = control_area

    def add_alt_generating_unit_mea(self, alt_generating_unit_mea: AltGeneratingUnitMeas) -> Self:
        return ControlAreaGeneratingUnit.alt_generating_unit_meas.add(self, alt_generating_unit_mea)

    def remove_alt_generating_unit_mea(
        self, alt_generating_unit_mea: AltGeneratingUnitMeas
    ) -> Self:
        return ControlAreaGeneratingUnit.alt_generating_unit_meas.remove(
            self, alt_generating_unit_mea
        )

    def clear_alt_generating_unit_meas(self) -> Self:
        return ControlAreaGeneratingUnit.alt_generating_unit_meas.clear(self)

    def num_alt_generating_unit_mea(self) -> int:
        return ControlAreaGeneratingUnit.alt_generating_unit_meas.count(self)

    def get_alt_generating_unit_mea_by_mrid(self, mrid: str) -> AltGeneratingUnitMeas | None:
        return ControlAreaGeneratingUnit.alt_generating_unit_meas.get_by_mrid(self, mrid)
