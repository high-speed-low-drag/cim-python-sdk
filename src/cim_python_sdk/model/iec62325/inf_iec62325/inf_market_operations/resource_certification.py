"""CIM class ResourceCertification (TC57CIM/IEC62325/InfIEC62325/InfMarketOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class ResourceCertification(CimObject):
    """This class represent the resource certification for a specific product type. For
    example, a resource is certified for Non-Spinning reserve for RTM."""

    __slots__ = (
        "_registered_resource",
        "certified_dam",
        "certified_nonspin_dam",
        "certified_nonspin_dam_mw",
        "certified_nonspin_rtm",
        "certified_nonspin_rtm_mw",
        "certified_pirp",
        "certified_regulation",
        "certified_regulation_mw",
        "certified_replace_as",
        "certified_rtm",
        "certified_ruc",
        "certified_spin",
        "certified_spin_mw",
    )

    certified_dam: YesNo | None
    certified_nonspin_dam: YesNo | None
    certified_nonspin_dam_mw: float | None
    certified_nonspin_rtm: YesNo | None
    certified_nonspin_rtm_mw: float | None
    certified_pirp: YesNo | None
    certified_regulation: YesNo | None
    certified_regulation_mw: float | None
    certified_replace_as: YesNo | None
    certified_spin: YesNo | None
    certified_spin_mw: float | None
    certified_rtm: YesNo | None
    certified_ruc: YesNo | None

    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_certification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceCertification",
        package="TC57CIM/IEC62325/InfIEC62325/InfMarketOperations",
        guid="{82B48F0E-EC60-4e73-AC59-4A134991765F}",
        attributes=(
            AttrMeta("certified_dam", "certifiedDAM", "YesNo", 0, 1, "enumeration"),
            AttrMeta("certified_nonspin_dam", "certifiedNonspinDAM", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "certified_nonspin_dam_mw", "certifiedNonspinDAMMw", "float", 0, 1, "primitive"
            ),
            AttrMeta("certified_nonspin_rtm", "certifiedNonspinRTM", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "certified_nonspin_rtm_mw", "certifiedNonspinRTMMw", "float", 0, 1, "primitive"
            ),
            AttrMeta("certified_pirp", "certifiedPIRP", "YesNo", 0, 1, "enumeration"),
            AttrMeta("certified_regulation", "certifiedRegulation", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "certified_regulation_mw", "certifiedRegulationMw", "float", 0, 1, "primitive"
            ),
            AttrMeta("certified_replace_as", "certifiedReplaceAS", "YesNo", 0, 1, "enumeration"),
            AttrMeta("certified_spin", "certifiedSpin", "YesNo", 0, 1, "enumeration"),
            AttrMeta("certified_spin_mw", "certifiedSpinMw", "float", 0, 1, "primitive"),
            AttrMeta("certified_rtm", "certifiedRTM", "YesNo", 0, 1, "enumeration"),
            AttrMeta("certified_ruc", "certifiedRUC", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        certified_dam: YesNo | None = None,
        certified_nonspin_dam: YesNo | None = None,
        certified_nonspin_dam_mw: float | None = None,
        certified_nonspin_rtm: YesNo | None = None,
        certified_nonspin_rtm_mw: float | None = None,
        certified_pirp: YesNo | None = None,
        certified_regulation: YesNo | None = None,
        certified_regulation_mw: float | None = None,
        certified_replace_as: YesNo | None = None,
        certified_spin: YesNo | None = None,
        certified_spin_mw: float | None = None,
        certified_rtm: YesNo | None = None,
        certified_ruc: YesNo | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.certified_dam = certified_dam
        self.certified_nonspin_dam = certified_nonspin_dam
        self.certified_nonspin_dam_mw = certified_nonspin_dam_mw
        self.certified_nonspin_rtm = certified_nonspin_rtm
        self.certified_nonspin_rtm_mw = certified_nonspin_rtm_mw
        self.certified_pirp = certified_pirp
        self.certified_regulation = certified_regulation
        self.certified_regulation_mw = certified_regulation_mw
        self.certified_replace_as = certified_replace_as
        self.certified_spin = certified_spin
        self.certified_spin_mw = certified_spin_mw
        self.certified_rtm = certified_rtm
        self.certified_ruc = certified_ruc
        if registered_resource is not None:
            ResourceCertification.registered_resource.extend(self, registered_resource)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ResourceCertification.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ResourceCertification.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return ResourceCertification.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return ResourceCertification.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return ResourceCertification.registered_resource.get_by_mrid(self, mrid)
