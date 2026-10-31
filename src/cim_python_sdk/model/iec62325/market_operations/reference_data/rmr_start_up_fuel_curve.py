"""CIM class RMRStartUpFuelCurve (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )


class RMRStartUpFuelCurve(Curve):
    """Model to support processing of reliability must run units."""

    __slots__ = ("_registered_generator",)

    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="rmr_start_up_fuel_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RMRStartUpFuelCurve",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{BBF0FCA0-4E32-4456-906A-AADBB77DD257}",
        ends=(registered_generator.meta,),
    )

    def __init__(
        self,
        *,
        registered_generator: RegisteredGenerator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if registered_generator is not None:
            self.registered_generator = registered_generator
