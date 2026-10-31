"""CIM class Specification (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.medium import Medium
    from cim_python_sdk.model.iec61968.common.user_attribute import UserAttribute
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.asset_property_curve import (
        AssetPropertyCurve,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.dimensions_info import DimensionsInfo
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reliability_info import (
        ReliabilityInfo,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement import (
        QualificationRequirement,
    )


class Specification(Document):
    """Specification can be used for various purposes relative to an asset, a logical device
    (PowerSystemResource), location, etc. Examples include documents supplied by
    manufacturers such as asset installation instructions, asset maintenance instructions,
    etc."""

    __slots__ = (
        "_asset_properites",
        "_asset_property_curves",
        "_dimensions_infos",
        "_mediums",
        "_qualification_requirements",
        "_ratings",
        "_reliability_infos",
    )

    dimensions_infos: Many[DimensionsInfo] = Many(
        EndMeta(
            name="dimensions_infos",
            cim_role="DimensionsInfos",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.dimensions_info:DimensionsInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="specifications",
            aggregation="none",
        )
    )
    qualification_requirements: Many[QualificationRequirement] = Many(
        EndMeta(
            name="qualification_requirements",
            cim_role="QualificationRequirements",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement:QualificationRequirement",
            many=True,
            lower=0,
            upper=None,
            inverse="specifications",
            aggregation="none",
        )
    )
    asset_property_curves: Many[AssetPropertyCurve] = Many(
        EndMeta(
            name="asset_property_curves",
            cim_role="AssetPropertyCurves",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.asset_property_curve:AssetPropertyCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="specification",
            aggregation="none",
        )
    )
    asset_properites: Many[UserAttribute] = Many(
        EndMeta(
            name="asset_properites",
            cim_role="AssetProperites",
            target="cim_python_sdk.model.iec61968.common.user_attribute:UserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="property_specification",
            aggregation="none",
        )
    )
    ratings: Many[UserAttribute] = Many(
        EndMeta(
            name="ratings",
            cim_role="Ratings",
            target="cim_python_sdk.model.iec61968.common.user_attribute:UserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="rating_specification",
            aggregation="none",
        )
    )
    reliability_infos: Many[ReliabilityInfo] = Many(
        EndMeta(
            name="reliability_infos",
            cim_role="ReliabilityInfos",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reliability_info:ReliabilityInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="specification",
            aggregation="none",
        )
    )
    mediums: Many[Medium] = Many(
        EndMeta(
            name="mediums",
            cim_role="Mediums",
            target="cim_python_sdk.model.iec61968.assets.medium:Medium",
            many=True,
            lower=0,
            upper=None,
            inverse="specification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Specification",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{E2672086-449E-4a8a-ADBD-82485754DF76}",
        ends=(
            dimensions_infos.meta,
            qualification_requirements.meta,
            asset_property_curves.meta,
            asset_properites.meta,
            ratings.meta,
            reliability_infos.meta,
            mediums.meta,
        ),
    )

    def __init__(
        self,
        *,
        dimensions_infos: Iterable[DimensionsInfo] | None = None,
        qualification_requirements: Iterable[QualificationRequirement] | None = None,
        asset_property_curves: Iterable[AssetPropertyCurve] | None = None,
        asset_properites: Iterable[UserAttribute] | None = None,
        ratings: Iterable[UserAttribute] | None = None,
        reliability_infos: Iterable[ReliabilityInfo] | None = None,
        mediums: Iterable[Medium] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dimensions_infos is not None:
            Specification.dimensions_infos.extend(self, dimensions_infos)
        if qualification_requirements is not None:
            Specification.qualification_requirements.extend(self, qualification_requirements)
        if asset_property_curves is not None:
            Specification.asset_property_curves.extend(self, asset_property_curves)
        if asset_properites is not None:
            Specification.asset_properites.extend(self, asset_properites)
        if ratings is not None:
            Specification.ratings.extend(self, ratings)
        if reliability_infos is not None:
            Specification.reliability_infos.extend(self, reliability_infos)
        if mediums is not None:
            Specification.mediums.extend(self, mediums)

    def add_dimensions_info(self, dimensions_info: DimensionsInfo) -> Self:
        return Specification.dimensions_infos.add(self, dimensions_info)

    def remove_dimensions_info(self, dimensions_info: DimensionsInfo) -> Self:
        return Specification.dimensions_infos.remove(self, dimensions_info)

    def clear_dimensions_infos(self) -> Self:
        return Specification.dimensions_infos.clear(self)

    def num_dimensions_info(self) -> int:
        return Specification.dimensions_infos.count(self)

    def get_dimensions_info_by_mrid(self, mrid: str) -> DimensionsInfo | None:
        return Specification.dimensions_infos.get_by_mrid(self, mrid)

    def add_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return Specification.qualification_requirements.add(self, qualification_requirement)

    def remove_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return Specification.qualification_requirements.remove(self, qualification_requirement)

    def clear_qualification_requirements(self) -> Self:
        return Specification.qualification_requirements.clear(self)

    def num_qualification_requirement(self) -> int:
        return Specification.qualification_requirements.count(self)

    def get_qualification_requirement_by_mrid(self, mrid: str) -> QualificationRequirement | None:
        return Specification.qualification_requirements.get_by_mrid(self, mrid)

    def add_asset_property_curve(self, asset_property_curve: AssetPropertyCurve) -> Self:
        return Specification.asset_property_curves.add(self, asset_property_curve)

    def remove_asset_property_curve(self, asset_property_curve: AssetPropertyCurve) -> Self:
        return Specification.asset_property_curves.remove(self, asset_property_curve)

    def clear_asset_property_curves(self) -> Self:
        return Specification.asset_property_curves.clear(self)

    def num_asset_property_curve(self) -> int:
        return Specification.asset_property_curves.count(self)

    def get_asset_property_curve_by_mrid(self, mrid: str) -> AssetPropertyCurve | None:
        return Specification.asset_property_curves.get_by_mrid(self, mrid)

    def add_asset_properite(self, asset_properite: UserAttribute) -> Self:
        return Specification.asset_properites.add(self, asset_properite)

    def remove_asset_properite(self, asset_properite: UserAttribute) -> Self:
        return Specification.asset_properites.remove(self, asset_properite)

    def clear_asset_properites(self) -> Self:
        return Specification.asset_properites.clear(self)

    def num_asset_properite(self) -> int:
        return Specification.asset_properites.count(self)

    def add_rating(self, rating: UserAttribute) -> Self:
        return Specification.ratings.add(self, rating)

    def remove_rating(self, rating: UserAttribute) -> Self:
        return Specification.ratings.remove(self, rating)

    def clear_ratings(self) -> Self:
        return Specification.ratings.clear(self)

    def num_rating(self) -> int:
        return Specification.ratings.count(self)

    def add_reliability_info(self, reliability_info: ReliabilityInfo) -> Self:
        return Specification.reliability_infos.add(self, reliability_info)

    def remove_reliability_info(self, reliability_info: ReliabilityInfo) -> Self:
        return Specification.reliability_infos.remove(self, reliability_info)

    def clear_reliability_infos(self) -> Self:
        return Specification.reliability_infos.clear(self)

    def num_reliability_info(self) -> int:
        return Specification.reliability_infos.count(self)

    def get_reliability_info_by_mrid(self, mrid: str) -> ReliabilityInfo | None:
        return Specification.reliability_infos.get_by_mrid(self, mrid)

    def add_medium(self, medium: Medium) -> Self:
        return Specification.mediums.add(self, medium)

    def remove_medium(self, medium: Medium) -> Self:
        return Specification.mediums.remove(self, medium)

    def clear_mediums(self) -> Self:
        return Specification.mediums.clear(self)

    def num_medium(self) -> int:
        return Specification.mediums.count(self)

    def get_medium_by_mrid(self, mrid: str) -> Medium | None:
        return Specification.mediums.get_by_mrid(self, mrid)
