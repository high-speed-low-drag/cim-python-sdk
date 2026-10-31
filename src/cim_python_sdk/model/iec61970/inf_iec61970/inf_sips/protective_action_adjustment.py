"""CIM class ProtectiveActionAdjustment (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action import ProtectiveAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment import DCConductingEquipment
    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_adjustment_kind import (
        ProtectiveActionAdjustmentKind,
    )


class ProtectiveActionAdjustment(ProtectiveAction):
    """Protective actions on non-switching equipment. The operating condition is adjusted."""

    __slots__ = (
        "_conducting_equipment",
        "_dc_conducting_equipment",
        "_measurement",
        "by_percentage",
        "by_value",
        "kind",
        "reduce",
        "set_value",
    )

    by_percentage: float | None  # PerCent
    by_value: float | None
    kind: ProtectiveActionAdjustmentKind | None
    reduce: bool | None
    set_value: float | None

    conducting_equipment: One[ConductingEquipment] = One(
        EndMeta(
            name="conducting_equipment",
            cim_role="ConductingEquipment",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=False,
            lower=1,
            upper=1,
            inverse="protective_action_adjustment",
            aggregation="none",
        )
    )
    dc_conducting_equipment: One[DCConductingEquipment] = One(
        EndMeta(
            name="dc_conducting_equipment",
            cim_role="DCConductingEquipment",
            target="cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment:DCConductingEquipment",
            many=False,
            lower=1,
            upper=1,
            inverse="protective_action_adjustment",
            aggregation="none",
        )
    )
    measurement: One[Measurement] = One(
        EndMeta(
            name="measurement",
            cim_role="Measurement",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=False,
            lower=0,
            upper=1,
            inverse="protective_action_adjustment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProtectiveActionAdjustment",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{8C1CFD32-6C07-45fa-A0CF-E91B76443855}",
        attributes=(
            AttrMeta("by_percentage", "byPercentage", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("by_value", "byValue", "float", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "ProtectiveActionAdjustmentKind", 0, 1, "enumeration"),
            AttrMeta("reduce", "reduce", "bool", 0, 1, "primitive"),
            AttrMeta("set_value", "setValue", "float", 0, 1, "primitive"),
        ),
        ends=(
            conducting_equipment.meta,
            dc_conducting_equipment.meta,
            measurement.meta,
        ),
    )

    def __init__(
        self,
        *,
        by_percentage: float | None = None,
        by_value: float | None = None,
        kind: ProtectiveActionAdjustmentKind | None = None,
        reduce: bool | None = None,
        set_value: float | None = None,
        conducting_equipment: ConductingEquipment | None = None,
        dc_conducting_equipment: DCConductingEquipment | None = None,
        measurement: Measurement | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.by_percentage = by_percentage
        self.by_value = by_value
        self.kind = kind
        self.reduce = reduce
        self.set_value = set_value
        if conducting_equipment is not None:
            self.conducting_equipment = conducting_equipment
        if dc_conducting_equipment is not None:
            self.dc_conducting_equipment = dc_conducting_equipment
        if measurement is not None:
            self.measurement = measurement
