"""CIM class RegulatingLimit (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )


class RegulatingLimit(IdentifiedObject):
    """This class represents the physical characteristic of a generator regarding the
    regulating limit."""

    __slots__ = ("_registered_generator", "high_limit", "low_limit")

    high_limit: float | None  # ActivePower
    low_limit: float | None  # ActivePower

    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="regulating_limit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegulatingLimit",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{B9C0775A-9238-4f30-8872-3BC702394185}",
        attributes=(
            AttrMeta("high_limit", "highLimit", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("low_limit", "lowLimit", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(registered_generator.meta,),
    )

    def __init__(
        self,
        *,
        high_limit: float | None = None,
        low_limit: float | None = None,
        registered_generator: RegisteredGenerator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.high_limit = high_limit
        self.low_limit = low_limit
        if registered_generator is not None:
            self.registered_generator = registered_generator
