"""CIM class ProvidedBilateralPoint (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor import (
        BilateralExchangeActor,
    )
    from cim_python_sdk.model.iec61970.base.meas.io_point import IOPoint


class ProvidedBilateralPoint(IdentifiedObject):
    """Allows declaration of ICCP points to be provided through a Bilateral Table agreement."""

    __slots__ = ("_bilateral_exchange_actor", "_io_point")

    io_point: One[IOPoint] = One(
        EndMeta(
            name="io_point",
            cim_role="IOPoint",
            target="cim_python_sdk.model.iec61970.base.meas.io_point:IOPoint",
            many=False,
            lower=0,
            upper=1,
            inverse="bilateral_to_io_point",
            aggregation="none",
        )
    )
    bilateral_exchange_actor: One[BilateralExchangeActor] = One(
        EndMeta(
            name="bilateral_exchange_actor",
            cim_role="BilateralExchangeActor",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor:BilateralExchangeActor",
            many=False,
            lower=1,
            upper=1,
            inverse="provided_bilateral_io_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProvidedBilateralPoint",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{1D2F8BB4-43BC-4f56-A274-90C964668491}",
        ends=(
            io_point.meta,
            bilateral_exchange_actor.meta,
        ),
    )

    def __init__(
        self,
        *,
        io_point: IOPoint | None = None,
        bilateral_exchange_actor: BilateralExchangeActor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if io_point is not None:
            self.io_point = io_point
        if bilateral_exchange_actor is not None:
            self.bilateral_exchange_actor = bilateral_exchange_actor
