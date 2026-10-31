"""CIM class StartUpEnergyCurve (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )


class StartUpEnergyCurve(Curve):
    """The energy consumption of a generating resource to complete a start-up from the
    StartUpEnergyCurve. Definition of the StartUpEnergyCurve includes, xvalue as the cooling
    time and y1value as the MW value."""

    __slots__ = ("_registered_generator",)

    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="start_up_energy_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StartUpEnergyCurve",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{22697274-C38F-4f5b-ADD7-F5345FA159E2}",
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
