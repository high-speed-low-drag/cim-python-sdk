"""CIM class GenerationProvider (TC57CIM/IEC62325/InfIEC62325/InfFinancial). Generated code: do not edit."""

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


class GenerationProvider(Organisation):
    """The energy seller in the energy marketplace."""

    __slots__ = ("_provided_by",)

    provided_by: Many[EnergyProduct] = Many(
        EndMeta(
            name="provided_by",
            cim_role="ProvidedBy",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.energy_product:EnergyProduct",
            many=True,
            lower=1,
            upper=None,
            inverse="generation_provider",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GenerationProvider",
        package="TC57CIM/IEC62325/InfIEC62325/InfFinancial",
        guid="{62C1A922-74F9-4148-A30A-E65774AE8B84}",
        ends=(provided_by.meta,),
    )

    def __init__(
        self,
        *,
        provided_by: Iterable[EnergyProduct] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if provided_by is not None:
            GenerationProvider.provided_by.extend(self, provided_by)

    def add_provided_by(self, provided_by: EnergyProduct) -> Self:
        return GenerationProvider.provided_by.add(self, provided_by)

    def remove_provided_by(self, provided_by: EnergyProduct) -> Self:
        return GenerationProvider.provided_by.remove(self, provided_by)

    def clear_provided_by(self) -> Self:
        return GenerationProvider.provided_by.clear(self)

    def num_provided_by(self) -> int:
        return GenerationProvider.provided_by.count(self)

    def get_provided_by_by_mrid(self, mrid: str) -> EnergyProduct | None:
        return GenerationProvider.provided_by.get_by_mrid(self, mrid)
