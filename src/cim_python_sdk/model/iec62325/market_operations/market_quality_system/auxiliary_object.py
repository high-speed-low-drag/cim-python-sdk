"""CIM class AuxiliaryObject (TC57CIM/IEC62325/MarketOperations/MarketQualitySystem). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_load import (
        RegisteredLoad,
    )


class AuxiliaryObject(CimObject):
    """Models Auxiliary Values."""

    __slots__ = ("_registered_generator", "_registered_load")

    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="auxillary_object",
            aggregation="none",
        )
    )
    registered_load: One[RegisteredLoad] = One(
        EndMeta(
            name="registered_load",
            cim_role="RegisteredLoad",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_load:RegisteredLoad",
            many=False,
            lower=0,
            upper=1,
            inverse="auxillary_object",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AuxiliaryObject",
        package="TC57CIM/IEC62325/MarketOperations/MarketQualitySystem",
        guid="{F12818E1-7F34-4989-95D1-919A475D2FA8}",
        ends=(
            registered_generator.meta,
            registered_load.meta,
        ),
    )

    def __init__(
        self,
        *,
        registered_generator: RegisteredGenerator | None = None,
        registered_load: RegisteredLoad | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if registered_generator is not None:
            self.registered_generator = registered_generator
        if registered_load is not None:
            self.registered_load = registered_load
