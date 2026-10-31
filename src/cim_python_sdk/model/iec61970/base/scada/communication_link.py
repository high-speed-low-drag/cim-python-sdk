"""CIM class CommunicationLink (TC57CIM/IEC61970/Base/SCADA). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor import (
        BilateralExchangeActor,
    )
    from cim_python_sdk.model.iec61970.base.scada.remote_unit import RemoteUnit


class CommunicationLink(PowerSystemResource):
    """The connection to remote units is through one or more communication links. Reduntant
    links may exist. The CommunicationLink class inherits PowerSystemResource. The intention
    is to allow CommunicationLinks to have Measurements. These Measurements can be used to
    model link status as operational, out of service, unit failure etc."""

    __slots__ = ("_bilateral_exchange_actor", "_remote_units")

    remote_units: Many[RemoteUnit] = Many(
        EndMeta(
            name="remote_units",
            cim_role="RemoteUnits",
            target="cim_python_sdk.model.iec61970.base.scada.remote_unit:RemoteUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="communication_links",
            aggregation="none",
        )
    )
    bilateral_exchange_actor: One[BilateralExchangeActor] = One(
        EndMeta(
            name="bilateral_exchange_actor",
            cim_role="BilateralExchangeActor",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor:BilateralExchangeActor",
            many=False,
            lower=0,
            upper=1,
            inverse="communication_link",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CommunicationLink",
        package="TC57CIM/IEC61970/Base/SCADA",
        guid="{7F2B8FC0-FCB8-4dfb-9C1C-AF982DA0ABCC}",
        ends=(
            remote_units.meta,
            bilateral_exchange_actor.meta,
        ),
    )

    def __init__(
        self,
        *,
        remote_units: Iterable[RemoteUnit] | None = None,
        bilateral_exchange_actor: BilateralExchangeActor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if remote_units is not None:
            CommunicationLink.remote_units.extend(self, remote_units)
        if bilateral_exchange_actor is not None:
            self.bilateral_exchange_actor = bilateral_exchange_actor

    def add_remote_unit(self, remote_unit: RemoteUnit) -> Self:
        return CommunicationLink.remote_units.add(self, remote_unit)

    def remove_remote_unit(self, remote_unit: RemoteUnit) -> Self:
        return CommunicationLink.remote_units.remove(self, remote_unit)

    def clear_remote_units(self) -> Self:
        return CommunicationLink.remote_units.clear(self)

    def num_remote_unit(self) -> int:
        return CommunicationLink.remote_units.count(self)

    def get_remote_unit_by_mrid(self, mrid: str) -> RemoteUnit | None:
        return CommunicationLink.remote_units.get_by_mrid(self, mrid)
