"""CIM class ClearanceDocument (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.operations.safety_document import SafetyDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.operations.clearance_action import ClearanceAction
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class ClearanceDocument(SafetyDocument):
    """Safety document used to authorise work on conducting equipment in the field. Tagged
    equipment is not allowed to be operated."""

    __slots__ = ("_clearance_action", "_tagged_psrs", "must_be_deenergised", "must_be_grounded")

    must_be_deenergised: bool | None
    must_be_grounded: bool | None

    tagged_psrs: Many[PowerSystemResource] = Many(
        EndMeta(
            name="tagged_psrs",
            cim_role="TaggedPSRs",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=True,
            lower=0,
            upper=None,
            inverse="clearances",
            aggregation="none",
        )
    )
    clearance_action: One[ClearanceAction] = One(
        EndMeta(
            name="clearance_action",
            cim_role="ClearanceAction",
            target="cim_python_sdk.model.iec61968.operations.clearance_action:ClearanceAction",
            many=False,
            lower=0,
            upper=1,
            inverse="clearance",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ClearanceDocument",
        package="TC57CIM/IEC61968/Operations",
        guid="{99D01537-9D57-421f-B795-AD2E5C40B628}",
        attributes=(
            AttrMeta("must_be_deenergised", "mustBeDeenergised", "bool", 0, 1, "primitive"),
            AttrMeta("must_be_grounded", "mustBeGrounded", "bool", 0, 1, "primitive"),
        ),
        ends=(
            tagged_psrs.meta,
            clearance_action.meta,
        ),
    )

    def __init__(
        self,
        *,
        must_be_deenergised: bool | None = None,
        must_be_grounded: bool | None = None,
        tagged_psrs: Iterable[PowerSystemResource] | None = None,
        clearance_action: ClearanceAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.must_be_deenergised = must_be_deenergised
        self.must_be_grounded = must_be_grounded
        if tagged_psrs is not None:
            ClearanceDocument.tagged_psrs.extend(self, tagged_psrs)
        if clearance_action is not None:
            self.clearance_action = clearance_action

    def add_tagged_psr(self, tagged_psr: PowerSystemResource) -> Self:
        return ClearanceDocument.tagged_psrs.add(self, tagged_psr)

    def remove_tagged_psr(self, tagged_psr: PowerSystemResource) -> Self:
        return ClearanceDocument.tagged_psrs.remove(self, tagged_psr)

    def clear_tagged_psrs(self) -> Self:
        return ClearanceDocument.tagged_psrs.clear(self)

    def num_tagged_psr(self) -> int:
        return ClearanceDocument.tagged_psrs.count(self)

    def get_tagged_psr_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return ClearanceDocument.tagged_psrs.get_by_mrid(self, mrid)
