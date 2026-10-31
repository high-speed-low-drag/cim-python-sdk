"""CIM class TransmissionProduct (TC57CIM/IEC62325/InfIEC62325/InfFinancial). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_provider import (
        TransmissionProvider,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path import (
        TransmissionPath,
    )


class TransmissionProduct(IdentifiedObject):
    """CIM class TransmissionProduct."""

    __slots__ = ("_location_for", "_transmission_provider", "transmission_product_type")

    transmission_product_type: str | None

    location_for: Many[TransmissionPath] = Many(
        EndMeta(
            name="location_for",
            cim_role="LocationFor",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path:TransmissionPath",
            many=True,
            lower=0,
            upper=None,
            inverse="located_on",
            aggregation="none",
        )
    )
    transmission_provider: One[TransmissionProvider] = One(
        EndMeta(
            name="transmission_provider",
            cim_role="TransmissionProvider",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_provider:TransmissionProvider",
            many=False,
            lower=1,
            upper=1,
            inverse="transmission_products",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionProduct",
        package="TC57CIM/IEC62325/InfIEC62325/InfFinancial",
        guid="{355728E0-DBFF-4ff5-A9DE-28FBAD39E465}",
        attributes=(
            AttrMeta(
                "transmission_product_type", "transmissionProductType", "str", 0, 1, "primitive"
            ),
        ),
        ends=(
            location_for.meta,
            transmission_provider.meta,
        ),
    )

    def __init__(
        self,
        *,
        transmission_product_type: str | None = None,
        location_for: Iterable[TransmissionPath] | None = None,
        transmission_provider: TransmissionProvider | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.transmission_product_type = transmission_product_type
        if location_for is not None:
            TransmissionProduct.location_for.extend(self, location_for)
        if transmission_provider is not None:
            self.transmission_provider = transmission_provider

    def add_location_for(self, location_for: TransmissionPath) -> Self:
        return TransmissionProduct.location_for.add(self, location_for)

    def remove_location_for(self, location_for: TransmissionPath) -> Self:
        return TransmissionProduct.location_for.remove(self, location_for)

    def clear_location_for(self) -> Self:
        return TransmissionProduct.location_for.clear(self)

    def num_location_for(self) -> int:
        return TransmissionProduct.location_for.count(self)

    def get_location_for_by_mrid(self, mrid: str) -> TransmissionPath | None:
        return TransmissionProduct.location_for.get_by_mrid(self, mrid)
