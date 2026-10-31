"""CIM class SvStatus (TC57CIM/IEC61970/Base/StateVariables). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.state_variables.state_variable import StateVariable

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class SvStatus(StateVariable):
    """State variable for status."""

    __slots__ = ("_conducting_equipment", "in_service", "phase")

    in_service: bool | None
    phase: SinglePhaseKind | None

    conducting_equipment: One[ConductingEquipment] = One(
        EndMeta(
            name="conducting_equipment",
            cim_role="ConductingEquipment",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=False,
            lower=1,
            upper=1,
            inverse="sv_status",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SvStatus",
        package="TC57CIM/IEC61970/Base/StateVariables",
        guid="{5DB950E7-EA86-4bc2-B627-D05EDF9131A2}",
        attributes=(
            AttrMeta("in_service", "inService", "bool", 0, 1, "primitive"),
            AttrMeta("phase", "phase", "SinglePhaseKind", 0, 1, "enumeration"),
        ),
        ends=(conducting_equipment.meta,),
    )

    def __init__(
        self,
        *,
        in_service: bool | None = None,
        phase: SinglePhaseKind | None = None,
        conducting_equipment: ConductingEquipment | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.in_service = in_service
        self.phase = phase
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
