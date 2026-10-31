"""CIM class CULaborItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_code import CULaborCode
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement import (
        QualificationRequirement,
    )


class CULaborItem(WorkIdentifiedObject):
    """Compatible unit labor item."""

    __slots__ = (
        "_compatible_units",
        "_cu_labor_code",
        "_qualification_requirements",
        "activity_code",
        "labor_duration",
        "labor_rate",
        "status",
    )

    activity_code: str | None
    labor_duration: float | None  # Hours
    labor_rate: float | None  # CostRate
    status: Status | None

    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_labor_items",
            aggregation="none",
        )
    )
    qualification_requirements: Many[QualificationRequirement] = Many(
        EndMeta(
            name="qualification_requirements",
            cim_role="QualificationRequirements",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement:QualificationRequirement",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_labor_items",
            aggregation="none",
        )
    )
    cu_labor_code: One[CULaborCode] = One(
        EndMeta(
            name="cu_labor_code",
            cim_role="CULaborCode",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_labor_code:CULaborCode",
            many=False,
            lower=0,
            upper=1,
            inverse="cu_labor_items",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CULaborItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{5E6C18AB-5DAC-46d3-B5E3-9786534DBBAA}",
        attributes=(
            AttrMeta("activity_code", "activityCode", "str", 0, 1, "primitive"),
            AttrMeta("labor_duration", "laborDuration", "Hours", 0, 1, "cimdatatype"),
            AttrMeta("labor_rate", "laborRate", "CostRate", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            compatible_units.meta,
            qualification_requirements.meta,
            cu_labor_code.meta,
        ),
    )

    def __init__(
        self,
        *,
        activity_code: str | None = None,
        labor_duration: float | None = None,
        labor_rate: float | None = None,
        status: Status | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        qualification_requirements: Iterable[QualificationRequirement] | None = None,
        cu_labor_code: CULaborCode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.activity_code = activity_code
        self.labor_duration = labor_duration
        self.labor_rate = labor_rate
        self.status = status
        if compatible_units is not None:
            CULaborItem.compatible_units.extend(self, compatible_units)
        if qualification_requirements is not None:
            CULaborItem.qualification_requirements.extend(self, qualification_requirements)
        if cu_labor_code is not None:
            self.cu_labor_code = cu_labor_code

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CULaborItem.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CULaborItem.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CULaborItem.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CULaborItem.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CULaborItem.compatible_units.get_by_mrid(self, mrid)

    def add_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return CULaborItem.qualification_requirements.add(self, qualification_requirement)

    def remove_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return CULaborItem.qualification_requirements.remove(self, qualification_requirement)

    def clear_qualification_requirements(self) -> Self:
        return CULaborItem.qualification_requirements.clear(self)

    def num_qualification_requirement(self) -> int:
        return CULaborItem.qualification_requirements.count(self)

    def get_qualification_requirement_by_mrid(self, mrid: str) -> QualificationRequirement | None:
        return CULaborItem.qualification_requirements.get_by_mrid(self, mrid)
