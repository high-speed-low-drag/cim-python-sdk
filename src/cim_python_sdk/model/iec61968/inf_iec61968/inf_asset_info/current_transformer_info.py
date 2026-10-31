"""CIM class CurrentTransformerInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.ratio import Ratio


class CurrentTransformerInfo(AssetInfo):
    """Properties of current transformer asset."""

    __slots__ = (
        "accuracy_class",
        "accuracy_limit",
        "core_count",
        "ct_class",
        "knee_point_current",
        "knee_point_voltage",
        "max_ratio",
        "nominal_ratio",
        "primary_fls_rating",
        "primary_ratio",
        "rated_current",
        "secondary_fls_rating",
        "secondary_ratio",
        "tertiary_fls_rating",
        "tertiary_ratio",
        "usage",
    )

    rated_current: float | None  # CurrentFlow
    ct_class: str | None
    accuracy_limit: float | None  # CurrentFlow
    accuracy_class: str | None
    max_ratio: Ratio | None
    core_count: int | None
    usage: str | None
    knee_point_voltage: float | None  # Voltage
    knee_point_current: float | None  # CurrentFlow
    nominal_ratio: Ratio | None
    primary_ratio: Ratio | None
    secondary_ratio: Ratio | None
    tertiary_ratio: Ratio | None
    primary_fls_rating: float | None  # CurrentFlow
    secondary_fls_rating: float | None  # CurrentFlow
    tertiary_fls_rating: float | None  # CurrentFlow

    _cim_meta = ClassMeta(
        cim_name="CurrentTransformerInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{33A8D4FA-A8E0-4882-B023-3EE729876FC1}",
        attributes=(
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("ct_class", "ctClass", "str", 0, 1, "primitive"),
            AttrMeta("accuracy_limit", "accuracyLimit", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("accuracy_class", "accuracyClass", "str", 0, 1, "primitive"),
            AttrMeta("max_ratio", "maxRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("core_count", "coreCount", "int", 0, 1, "primitive"),
            AttrMeta("usage", "usage", "str", 0, 1, "primitive"),
            AttrMeta("knee_point_voltage", "kneePointVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("knee_point_current", "kneePointCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("nominal_ratio", "nominalRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("primary_ratio", "primaryRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("secondary_ratio", "secondaryRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("tertiary_ratio", "tertiaryRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("primary_fls_rating", "primaryFlsRating", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta(
                "secondary_fls_rating", "secondaryFlsRating", "CurrentFlow", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "tertiary_fls_rating", "tertiaryFlsRating", "CurrentFlow", 0, 1, "cimdatatype"
            ),
        ),
    )

    def __init__(
        self,
        *,
        rated_current: float | None = None,
        ct_class: str | None = None,
        accuracy_limit: float | None = None,
        accuracy_class: str | None = None,
        max_ratio: Ratio | None = None,
        core_count: int | None = None,
        usage: str | None = None,
        knee_point_voltage: float | None = None,
        knee_point_current: float | None = None,
        nominal_ratio: Ratio | None = None,
        primary_ratio: Ratio | None = None,
        secondary_ratio: Ratio | None = None,
        tertiary_ratio: Ratio | None = None,
        primary_fls_rating: float | None = None,
        secondary_fls_rating: float | None = None,
        tertiary_fls_rating: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_current = rated_current
        self.ct_class = ct_class
        self.accuracy_limit = accuracy_limit
        self.accuracy_class = accuracy_class
        self.max_ratio = max_ratio
        self.core_count = core_count
        self.usage = usage
        self.knee_point_voltage = knee_point_voltage
        self.knee_point_current = knee_point_current
        self.nominal_ratio = nominal_ratio
        self.primary_ratio = primary_ratio
        self.secondary_ratio = secondary_ratio
        self.tertiary_ratio = tertiary_ratio
        self.primary_fls_rating = primary_fls_rating
        self.secondary_fls_rating = secondary_fls_rating
        self.tertiary_fls_rating = tertiary_fls_rating
