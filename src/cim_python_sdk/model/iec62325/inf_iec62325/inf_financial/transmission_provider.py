"""CIM class TransmissionProvider (TC57CIM/IEC62325/InfIEC62325/InfFinancial). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation import Organisation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.loss_profile import (
        LossProfile,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_product import (
        TransmissionProduct,
    )


class TransmissionProvider(Organisation):
    """Provider of the transmission capacity (interconnecting wires between Generation and
    Consumption) required to fulfill and Energy Transaction's energy exchange. Posts
    information for transmission paths and AvailableTransmissionCapacities on a reservation
    node. Buys and sells its products and services on the same reservation node."""

    __slots__ = ("_for_", "_transmission_products")

    for_: Many[LossProfile] = Many(
        EndMeta(
            name="for_",
            cim_role="For",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.loss_profile:LossProfile",
            many=True,
            lower=0,
            upper=None,
            inverse="has_loss",
            aggregation="none",
        )
    )
    transmission_products: Many[TransmissionProduct] = Many(
        EndMeta(
            name="transmission_products",
            cim_role="TransmissionProducts",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_product:TransmissionProduct",
            many=True,
            lower=1,
            upper=None,
            inverse="transmission_provider",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionProvider",
        package="TC57CIM/IEC62325/InfIEC62325/InfFinancial",
        guid="{C8BC0391-9D15-4c2e-A491-15A73845C406}",
        ends=(
            for_.meta,
            transmission_products.meta,
        ),
    )

    def __init__(
        self,
        *,
        for_: Iterable[LossProfile] | None = None,
        transmission_products: Iterable[TransmissionProduct] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if for_ is not None:
            TransmissionProvider.for_.extend(self, for_)
        if transmission_products is not None:
            TransmissionProvider.transmission_products.extend(self, transmission_products)

    def add_for_(self, for_: LossProfile) -> Self:
        return TransmissionProvider.for_.add(self, for_)

    def remove_for_(self, for_: LossProfile) -> Self:
        return TransmissionProvider.for_.remove(self, for_)

    def clear_for_(self) -> Self:
        return TransmissionProvider.for_.clear(self)

    def num_for_(self) -> int:
        return TransmissionProvider.for_.count(self)

    def get_for__by_mrid(self, mrid: str) -> LossProfile | None:
        return TransmissionProvider.for_.get_by_mrid(self, mrid)

    def add_transmission_product(self, transmission_product: TransmissionProduct) -> Self:
        return TransmissionProvider.transmission_products.add(self, transmission_product)

    def remove_transmission_product(self, transmission_product: TransmissionProduct) -> Self:
        return TransmissionProvider.transmission_products.remove(self, transmission_product)

    def clear_transmission_products(self) -> Self:
        return TransmissionProvider.transmission_products.clear(self)

    def num_transmission_product(self) -> int:
        return TransmissionProvider.transmission_products.count(self)

    def get_transmission_product_by_mrid(self, mrid: str) -> TransmissionProduct | None:
        return TransmissionProvider.transmission_products.get_by_mrid(self, mrid)
