"""CIM class Tariff (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.pricing_structure import PricingStructure
    from cim_python_sdk.model.iec61968.payment_metering.tariff_profile import TariffProfile


class Tariff(Document):
    """Document, approved by the responsible regulatory agency, listing the terms and
    conditions, including a schedule of prices, under which utility services will be
    provided. It has a unique number within the state or province. For rate schedules it is
    frequently allocated by the affiliated Public utilities commission (PUC)."""

    __slots__ = ("_pricing_structures", "_tariff_profiles", "end_date", "start_date")

    start_date: _dt.date | None
    end_date: _dt.date | None

    pricing_structures: Many[PricingStructure] = Many(
        EndMeta(
            name="pricing_structures",
            cim_role="PricingStructures",
            target="cim_python_sdk.model.iec61968.customers.pricing_structure:PricingStructure",
            many=True,
            lower=0,
            upper=None,
            inverse="tariffs",
            aggregation="none",
        )
    )
    tariff_profiles: Many[TariffProfile] = Many(
        EndMeta(
            name="tariff_profiles",
            cim_role="TariffProfiles",
            target="cim_python_sdk.model.iec61968.payment_metering.tariff_profile:TariffProfile",
            many=True,
            lower=0,
            upper=None,
            inverse="tariffs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Tariff",
        package="TC57CIM/IEC61968/Customers",
        guid="{0BE74F01-4122-4e79-A801-A70BCEAE82B2}",
        attributes=(
            AttrMeta("start_date", "startDate", "date", 0, 1, "primitive"),
            AttrMeta("end_date", "endDate", "date", 0, 1, "primitive"),
        ),
        ends=(
            pricing_structures.meta,
            tariff_profiles.meta,
        ),
    )

    def __init__(
        self,
        *,
        start_date: _dt.date | None = None,
        end_date: _dt.date | None = None,
        pricing_structures: Iterable[PricingStructure] | None = None,
        tariff_profiles: Iterable[TariffProfile] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.start_date = start_date
        self.end_date = end_date
        if pricing_structures is not None:
            Tariff.pricing_structures.extend(self, pricing_structures)
        if tariff_profiles is not None:
            Tariff.tariff_profiles.extend(self, tariff_profiles)

    def add_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return Tariff.pricing_structures.add(self, pricing_structure)

    def remove_pricing_structure(self, pricing_structure: PricingStructure) -> Self:
        return Tariff.pricing_structures.remove(self, pricing_structure)

    def clear_pricing_structures(self) -> Self:
        return Tariff.pricing_structures.clear(self)

    def num_pricing_structure(self) -> int:
        return Tariff.pricing_structures.count(self)

    def get_pricing_structure_by_mrid(self, mrid: str) -> PricingStructure | None:
        return Tariff.pricing_structures.get_by_mrid(self, mrid)

    def add_tariff_profile(self, tariff_profile: TariffProfile) -> Self:
        return Tariff.tariff_profiles.add(self, tariff_profile)

    def remove_tariff_profile(self, tariff_profile: TariffProfile) -> Self:
        return Tariff.tariff_profiles.remove(self, tariff_profile)

    def clear_tariff_profiles(self) -> Self:
        return Tariff.tariff_profiles.clear(self)

    def num_tariff_profile(self) -> int:
        return Tariff.tariff_profiles.count(self)

    def get_tariff_profile_by_mrid(self, mrid: str) -> TariffProfile | None:
        return Tariff.tariff_profiles.get_by_mrid(self, mrid)
