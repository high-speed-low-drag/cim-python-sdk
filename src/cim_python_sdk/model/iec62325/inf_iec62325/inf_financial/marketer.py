"""CIM class Marketer (TC57CIM/IEC62325/InfIEC62325/InfFinancial). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation import Organisation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.energy_product import (
        EnergyProduct,
    )


class Marketer(Organisation):
    """Matches buyers and sellers, and secures transmission (and other ancillary services)
    needed to complete the energy transaction."""

    __slots__ = ("_holds_title_to_energy_products", "_resells_energy_product")

    holds_title_to_energy_products: Many[EnergyProduct] = Many(
        EndMeta(
            name="holds_title_to_energy_products",
            cim_role="HoldsTitleTo_EnergyProducts",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.energy_product:EnergyProduct",
            many=True,
            lower=0,
            upper=None,
            inverse="title_held_by_marketer",
            aggregation="none",
        )
    )
    resells_energy_product: Many[EnergyProduct] = Many(
        EndMeta(
            name="resells_energy_product",
            cim_role="Resells_EnergyProduct",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.energy_product:EnergyProduct",
            many=True,
            lower=0,
            upper=None,
            inverse="resold_by_marketer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Marketer",
        package="TC57CIM/IEC62325/InfIEC62325/InfFinancial",
        guid="{037CF759-5512-4012-8753-3922B3D2B8C4}",
        ends=(
            holds_title_to_energy_products.meta,
            resells_energy_product.meta,
        ),
    )

    def __init__(
        self,
        *,
        holds_title_to_energy_products: Iterable[EnergyProduct] | None = None,
        resells_energy_product: Iterable[EnergyProduct] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if holds_title_to_energy_products is not None:
            Marketer.holds_title_to_energy_products.extend(self, holds_title_to_energy_products)
        if resells_energy_product is not None:
            Marketer.resells_energy_product.extend(self, resells_energy_product)

    def add_holds_title_to_energy_product(
        self, holds_title_to_energy_product: EnergyProduct
    ) -> Self:
        return Marketer.holds_title_to_energy_products.add(self, holds_title_to_energy_product)

    def remove_holds_title_to_energy_product(
        self, holds_title_to_energy_product: EnergyProduct
    ) -> Self:
        return Marketer.holds_title_to_energy_products.remove(self, holds_title_to_energy_product)

    def clear_holds_title_to_energy_products(self) -> Self:
        return Marketer.holds_title_to_energy_products.clear(self)

    def num_holds_title_to_energy_product(self) -> int:
        return Marketer.holds_title_to_energy_products.count(self)

    def get_holds_title_to_energy_product_by_mrid(self, mrid: str) -> EnergyProduct | None:
        return Marketer.holds_title_to_energy_products.get_by_mrid(self, mrid)

    def add_resells_energy_product(self, resells_energy_product: EnergyProduct) -> Self:
        return Marketer.resells_energy_product.add(self, resells_energy_product)

    def remove_resells_energy_product(self, resells_energy_product: EnergyProduct) -> Self:
        return Marketer.resells_energy_product.remove(self, resells_energy_product)

    def clear_resells_energy_product(self) -> Self:
        return Marketer.resells_energy_product.clear(self)

    def num_resells_energy_product(self) -> int:
        return Marketer.resells_energy_product.count(self)

    def get_resells_energy_product_by_mrid(self, mrid: str) -> EnergyProduct | None:
        return Marketer.resells_energy_product.get_by_mrid(self, mrid)
