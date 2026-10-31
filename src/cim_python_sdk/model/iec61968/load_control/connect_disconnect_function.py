"""CIM class ConnectDisconnectFunction (TC57CIM/IEC61968/LoadControl). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.metering.end_device_function import EndDeviceFunction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.load_control.remote_connect_disconnect_info import (
        RemoteConnectDisconnectInfo,
    )
    from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class ConnectDisconnectFunction(EndDeviceFunction):
    """A function that will disconnect and reconnect the customer's load under defined
    conditions."""

    __slots__ = (
        "_switches",
        "event_count",
        "is_connected",
        "is_delayed_discon",
        "is_local_auto_discon_op",
        "is_local_auto_recon_op",
        "is_remote_auto_discon_op",
        "is_remote_auto_recon_op",
        "rcd_info",
    )

    is_local_auto_discon_op: bool | None
    is_local_auto_recon_op: bool | None
    is_remote_auto_discon_op: bool | None
    is_remote_auto_recon_op: bool | None
    is_delayed_discon: bool | None
    event_count: int | None
    is_connected: bool | None
    rcd_info: RemoteConnectDisconnectInfo | None

    switches: Many[Switch] = Many(
        EndMeta(
            name="switches",
            cim_role="Switches",
            target="cim_python_sdk.model.iec61970.base.wires.switch:Switch",
            many=True,
            lower=0,
            upper=None,
            inverse="connect_disconnect_functions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConnectDisconnectFunction",
        package="TC57CIM/IEC61968/LoadControl",
        guid="{8CFA1D56-DA8D-460e-B04A-8E95D3042C26}",
        attributes=(
            AttrMeta("is_local_auto_discon_op", "isLocalAutoDisconOp", "bool", 0, 1, "primitive"),
            AttrMeta("is_local_auto_recon_op", "isLocalAutoReconOp", "bool", 0, 1, "primitive"),
            AttrMeta("is_remote_auto_discon_op", "isRemoteAutoDisconOp", "bool", 0, 1, "primitive"),
            AttrMeta("is_remote_auto_recon_op", "isRemoteAutoReconOp", "bool", 0, 1, "primitive"),
            AttrMeta("is_delayed_discon", "isDelayedDiscon", "bool", 0, 1, "primitive"),
            AttrMeta("event_count", "eventCount", "int", 0, 1, "primitive"),
            AttrMeta("is_connected", "isConnected", "bool", 0, 1, "primitive"),
            AttrMeta("rcd_info", "rcdInfo", "RemoteConnectDisconnectInfo", 0, 1, "compound"),
        ),
        ends=(switches.meta,),
    )

    def __init__(
        self,
        *,
        is_local_auto_discon_op: bool | None = None,
        is_local_auto_recon_op: bool | None = None,
        is_remote_auto_discon_op: bool | None = None,
        is_remote_auto_recon_op: bool | None = None,
        is_delayed_discon: bool | None = None,
        event_count: int | None = None,
        is_connected: bool | None = None,
        rcd_info: RemoteConnectDisconnectInfo | None = None,
        switches: Iterable[Switch] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_local_auto_discon_op = is_local_auto_discon_op
        self.is_local_auto_recon_op = is_local_auto_recon_op
        self.is_remote_auto_discon_op = is_remote_auto_discon_op
        self.is_remote_auto_recon_op = is_remote_auto_recon_op
        self.is_delayed_discon = is_delayed_discon
        self.event_count = event_count
        self.is_connected = is_connected
        self.rcd_info = rcd_info
        if switches is not None:
            ConnectDisconnectFunction.switches.extend(self, switches)

    def add_switche(self, switche: Switch) -> Self:
        return ConnectDisconnectFunction.switches.add(self, switche)

    def remove_switche(self, switche: Switch) -> Self:
        return ConnectDisconnectFunction.switches.remove(self, switche)

    def clear_switches(self) -> Self:
        return ConnectDisconnectFunction.switches.clear(self)

    def num_switche(self) -> int:
        return ConnectDisconnectFunction.switches.count(self)

    def get_switche_by_mrid(self, mrid: str) -> Switch | None:
        return ConnectDisconnectFunction.switches.get_by_mrid(self, mrid)
