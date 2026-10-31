"""CIM class PotentialTransformerInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.ratio import Ratio


class PotentialTransformerInfo(AssetInfo):
    """Properties of potential transformer asset."""

    __slots__ = (
        "accuracy_class",
        "nominal_ratio",
        "primary_ratio",
        "pt_class",
        "rated_voltage",
        "secondary_ratio",
        "tertiary_ratio",
    )

    rated_voltage: float | None  # Voltage
    accuracy_class: str | None
    pt_class: str | None
    nominal_ratio: Ratio | None
    primary_ratio: Ratio | None
    secondary_ratio: Ratio | None
    tertiary_ratio: Ratio | None

    _cim_meta = ClassMeta(
        cim_name="PotentialTransformerInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{3C463B88-5774-44cb-8C78-4EBD99CD3691}",
        attributes=(
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("accuracy_class", "accuracyClass", "str", 0, 1, "primitive"),
            AttrMeta("pt_class", "ptClass", "str", 0, 1, "primitive"),
            AttrMeta("nominal_ratio", "nominalRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("primary_ratio", "primaryRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("secondary_ratio", "secondaryRatio", "Ratio", 0, 1, "compound"),
            AttrMeta("tertiary_ratio", "tertiaryRatio", "Ratio", 0, 1, "compound"),
        ),
    )

    def __init__(
        self,
        *,
        rated_voltage: float | None = None,
        accuracy_class: str | None = None,
        pt_class: str | None = None,
        nominal_ratio: Ratio | None = None,
        primary_ratio: Ratio | None = None,
        secondary_ratio: Ratio | None = None,
        tertiary_ratio: Ratio | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_voltage = rated_voltage
        self.accuracy_class = accuracy_class
        self.pt_class = pt_class
        self.nominal_ratio = nominal_ratio
        self.primary_ratio = primary_ratio
        self.secondary_ratio = secondary_ratio
        self.tertiary_ratio = tertiary_ratio
