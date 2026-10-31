"""CIM class MaintenanceWorkTask (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.work.work_task import WorkTask

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.work.breaker_maintenance_kind import BreakerMaintenanceKind
    from cim_python_sdk.model.iec61968.work.transformer_maintenance_kind import (
        TransformerMaintenanceKind,
    )


class MaintenanceWorkTask(WorkTask):
    """Maintenance work task. Costs associated with this are considered preventive maintenance
    (PM) costs."""

    __slots__ = ("breaker_maintenance_kind", "transformer_maintenance_kind")

    breaker_maintenance_kind: BreakerMaintenanceKind | None
    transformer_maintenance_kind: TransformerMaintenanceKind | None

    _cim_meta = ClassMeta(
        cim_name="MaintenanceWorkTask",
        package="TC57CIM/IEC61968/Work",
        guid="{F2865AF9-CDD2-4194-A533-260CA1AEED79}",
        attributes=(
            AttrMeta(
                "breaker_maintenance_kind",
                "breakerMaintenanceKind",
                "BreakerMaintenanceKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "transformer_maintenance_kind",
                "transformerMaintenanceKind",
                "TransformerMaintenanceKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )

    def __init__(
        self,
        *,
        breaker_maintenance_kind: BreakerMaintenanceKind | None = None,
        transformer_maintenance_kind: TransformerMaintenanceKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.breaker_maintenance_kind = breaker_maintenance_kind
        self.transformer_maintenance_kind = transformer_maintenance_kind
