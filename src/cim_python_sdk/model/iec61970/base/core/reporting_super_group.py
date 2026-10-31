"""CIM class ReportingSuperGroup (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.reporting_group import ReportingGroup


class ReportingSuperGroup(IdentifiedObject):
    """A reporting super group, groups reporting groups for a higher level report."""

    __slots__ = ("_reporting_group",)

    reporting_group: Many[ReportingGroup] = Many(
        EndMeta(
            name="reporting_group",
            cim_role="ReportingGroup",
            target="cim_python_sdk.model.iec61970.base.core.reporting_group:ReportingGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="reporting_super_group",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReportingSuperGroup",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{68A3A6AE-719A-4172-9EE1-5858D6327ED4}",
        ends=(reporting_group.meta,),
    )

    def __init__(
        self,
        *,
        reporting_group: Iterable[ReportingGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if reporting_group is not None:
            ReportingSuperGroup.reporting_group.extend(self, reporting_group)

    def add_reporting_group(self, reporting_group: ReportingGroup) -> Self:
        return ReportingSuperGroup.reporting_group.add(self, reporting_group)

    def remove_reporting_group(self, reporting_group: ReportingGroup) -> Self:
        return ReportingSuperGroup.reporting_group.remove(self, reporting_group)

    def clear_reporting_group(self) -> Self:
        return ReportingSuperGroup.reporting_group.clear(self)

    def num_reporting_group(self) -> int:
        return ReportingSuperGroup.reporting_group.count(self)

    def get_reporting_group_by_mrid(self, mrid: str) -> ReportingGroup | None:
        return ReportingSuperGroup.reporting_group.get_by_mrid(self, mrid)
