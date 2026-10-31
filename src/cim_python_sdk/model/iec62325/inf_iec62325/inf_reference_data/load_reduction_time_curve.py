"""CIM class LoadReductionTimeCurve (TC57CIM/IEC62325/InfIEC62325/InfReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class LoadReductionTimeCurve(Curve):
    """This is the cureve that describes the load reduction time. Relationship between time
    (Y1-axis) vs. MW (X-axis)."""

    __slots__ = ("load_reduction_time_curve_type",)

    load_reduction_time_curve_type: str | None

    _cim_meta = ClassMeta(
        cim_name="LoadReductionTimeCurve",
        package="TC57CIM/IEC62325/InfIEC62325/InfReferenceData",
        guid="{47191455-BCF8-45a0-B1FA-5E205AC82308}",
        attributes=(
            AttrMeta(
                "load_reduction_time_curve_type",
                "loadReductionTimeCurveType",
                "str",
                0,
                1,
                "primitive",
            ),
        ),
    )

    def __init__(
        self,
        *,
        load_reduction_time_curve_type: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.load_reduction_time_curve_type = load_reduction_time_curve_type
