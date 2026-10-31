"""CIM class DimensionsInfo (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification import Specification


class DimensionsInfo(IdentifiedObject):
    """As applicable, the basic linear, area, or volume dimensions of an asset, asset type
    (AssetModel) or other type of object (such as land area). Units and multipliers are
    specified per dimension."""

    __slots__ = (
        "_specifications",
        "orientation",
        "size_depth",
        "size_diameter",
        "size_length",
        "size_width",
    )

    size_length: float | None  # Length
    size_depth: float | None  # Length
    size_width: float | None  # Length
    size_diameter: float | None  # Length
    orientation: str | None

    specifications: Many[Specification] = Many(
        EndMeta(
            name="specifications",
            cim_role="Specifications",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification:Specification",
            many=True,
            lower=0,
            upper=None,
            inverse="dimensions_infos",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DimensionsInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{7E0E8F43-9DFD-4c50-9367-E7C7F65E648D}",
        attributes=(
            AttrMeta("size_length", "sizeLength", "Length", 0, 1, "cimdatatype"),
            AttrMeta("size_depth", "sizeDepth", "Length", 0, 1, "cimdatatype"),
            AttrMeta("size_width", "sizeWidth", "Length", 0, 1, "cimdatatype"),
            AttrMeta("size_diameter", "sizeDiameter", "Length", 0, 1, "cimdatatype"),
            AttrMeta("orientation", "orientation", "str", 0, 1, "primitive"),
        ),
        ends=(specifications.meta,),
    )

    def __init__(
        self,
        *,
        size_length: float | None = None,
        size_depth: float | None = None,
        size_width: float | None = None,
        size_diameter: float | None = None,
        orientation: str | None = None,
        specifications: Iterable[Specification] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.size_length = size_length
        self.size_depth = size_depth
        self.size_width = size_width
        self.size_diameter = size_diameter
        self.orientation = orientation
        if specifications is not None:
            DimensionsInfo.specifications.extend(self, specifications)

    def add_specification(self, specification: Specification) -> Self:
        return DimensionsInfo.specifications.add(self, specification)

    def remove_specification(self, specification: Specification) -> Self:
        return DimensionsInfo.specifications.remove(self, specification)

    def clear_specifications(self) -> Self:
        return DimensionsInfo.specifications.clear(self)

    def num_specification(self) -> int:
        return DimensionsInfo.specifications.count(self)

    def get_specification_by_mrid(self, mrid: str) -> Specification | None:
        return DimensionsInfo.specifications.get_by_mrid(self, mrid)
