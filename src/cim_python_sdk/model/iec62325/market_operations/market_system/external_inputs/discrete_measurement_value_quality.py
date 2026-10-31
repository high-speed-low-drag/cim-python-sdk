"""CIM class DiscreteMeasurementValueQuality (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.meas.measurement_value_quality import (
    MeasurementValueQuality,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DiscreteMeasurementValueQuality(MeasurementValueQuality):
    """Measurement quality flags for Discrete Values."""

    __slots__ = ("manual_replace_indicator", "remove_from_operation_indicator")

    manual_replace_indicator: bool | None
    remove_from_operation_indicator: bool | None

    _cim_meta = ClassMeta(
        cim_name="DiscreteMeasurementValueQuality",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{735537BE-F1C8-49da-8742-CD2F148BA9D4}",
        attributes=(
            AttrMeta(
                "manual_replace_indicator", "manualReplaceIndicator", "bool", 0, 1, "primitive"
            ),
            AttrMeta(
                "remove_from_operation_indicator",
                "removeFromOperationIndicator",
                "bool",
                0,
                1,
                "primitive",
            ),
        ),
    )

    def __init__(
        self,
        *,
        manual_replace_indicator: bool | None = None,
        remove_from_operation_indicator: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.manual_replace_indicator = manual_replace_indicator
        self.remove_from_operation_indicator = remove_from_operation_indicator
