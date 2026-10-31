"""CIM class CUAllowableAction (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit


class CUAllowableAction(WorkIdentifiedObject):
    """Allowed actions: Install, Remove, Transfer, Abandon, etc."""

    __slots__ = ("_compatible_units", "status")

    status: Status | None

    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_allowable_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CUAllowableAction",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{E4E9DA68-B1C9-4003-AB25-8F49404DCBD0}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(compatible_units.meta,),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if compatible_units is not None:
            CUAllowableAction.compatible_units.extend(self, compatible_units)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUAllowableAction.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUAllowableAction.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CUAllowableAction.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CUAllowableAction.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CUAllowableAction.compatible_units.get_by_mrid(self, mrid)
