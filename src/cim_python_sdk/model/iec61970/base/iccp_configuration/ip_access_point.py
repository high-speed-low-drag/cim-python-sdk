"""CIM class IPAccessPoint (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.scada.communication_link import CommunicationLink

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.iccp_configuration.ip_address_kind import IPAddressKind


class IPAccessPoint(CommunicationLink):
    """Internet Protocol Access Point – used to represent an addressing structure is based upon
    an Internet Protocol (IP) address."""

    __slots__ = ("address", "address_type", "gateway", "subnet")

    address: str | None
    address_type: IPAddressKind | None
    gateway: str | None
    subnet: str | None

    _cim_meta = ClassMeta(
        cim_name="IPAccessPoint",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{11EB184F-AA94-4954-9B70-2F3D5F358790}",
        attributes=(
            AttrMeta("address", "address", "str", 0, 1, "primitive"),
            AttrMeta("address_type", "addressType", "IPAddressKind", 0, 1, "enumeration"),
            AttrMeta("gateway", "gateway", "str", 0, 1, "primitive"),
            AttrMeta("subnet", "subnet", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        address: str | None = None,
        address_type: IPAddressKind | None = None,
        gateway: str | None = None,
        subnet: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.address = address
        self.address_type = address_type
        self.gateway = gateway
        self.subnet = subnet
