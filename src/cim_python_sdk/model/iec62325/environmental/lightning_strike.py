"""CIM class LightningStrike (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec62325.environmental.geospheric_phenomenon import GeosphericPhenomenon

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class LightningStrike(GeosphericPhenomenon):
    """A cloud-to-ground lightning strike at a particular location."""

    __slots__ = (
        "error_ellipse_confidence",
        "error_ellipse_major_semi_axis",
        "error_ellipse_minor_semi_axis",
        "error_ellipse_orientation",
        "negative_polarity",
        "peak_amplitude",
    )

    error_ellipse_confidence: float | None  # PerCent
    error_ellipse_major_semi_axis: float | None  # Length
    error_ellipse_minor_semi_axis: float | None  # Length
    error_ellipse_orientation: float | None  # Bearing
    negative_polarity: bool | None
    peak_amplitude: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="LightningStrike",
        package="TC57CIM/IEC62325/Environmental",
        guid="{A68FB6F4-6463-4937-A1E8-B22BB98F453C}",
        attributes=(
            AttrMeta(
                "error_ellipse_confidence", "errorEllipseConfidence", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "error_ellipse_major_semi_axis",
                "errorEllipseMajorSemiAxis",
                "Length",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "error_ellipse_minor_semi_axis",
                "errorEllipseMinorSemiAxis",
                "Length",
                1,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "error_ellipse_orientation",
                "errorEllipseOrientation",
                "Bearing",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("negative_polarity", "negativePolarity", "bool", 0, 1, "primitive"),
            AttrMeta("peak_amplitude", "peakAmplitude", "CurrentFlow", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        error_ellipse_confidence: float | None = None,
        error_ellipse_major_semi_axis: float | None = None,
        error_ellipse_minor_semi_axis: float | None = None,
        error_ellipse_orientation: float | None = None,
        negative_polarity: bool | None = None,
        peak_amplitude: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.error_ellipse_confidence = error_ellipse_confidence
        self.error_ellipse_major_semi_axis = error_ellipse_major_semi_axis
        self.error_ellipse_minor_semi_axis = error_ellipse_minor_semi_axis
        self.error_ellipse_orientation = error_ellipse_orientation
        self.negative_polarity = negative_polarity
        self.peak_amplitude = peak_amplitude
