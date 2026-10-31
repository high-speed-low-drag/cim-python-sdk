"""CIM class PublicX509Certificate (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.iccp_configuration.iso_upper_layer import ISOUpperLayer
    from cim_python_sdk.model.iec61970.base.iccp_configuration.tcp_access_point import (
        TCPAccessPoint,
    )


class PublicX509Certificate(CimObject):
    """Used to convey information that will allow matching in order to determine which
    certificate to use. Actual certificates are exchanged externally to the CIM exchange."""

    __slots__ = ("_iso_upper_layer", "_tcp_access_point", "issuer_name", "serial_number")

    issuer_name: str | None
    serial_number: str | None

    iso_upper_layer: One[ISOUpperLayer] = One(
        EndMeta(
            name="iso_upper_layer",
            cim_role="ISOUpperLayer",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.iso_upper_layer:ISOUpperLayer",
            many=False,
            lower=0,
            upper=1,
            inverse="upper_layer_public_x509_certificate",
            aggregation="none",
        )
    )
    tcp_access_point: One[TCPAccessPoint] = One(
        EndMeta(
            name="tcp_access_point",
            cim_role="TCPAccessPoint",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.tcp_access_point:TCPAccessPoint",
            many=False,
            lower=0,
            upper=1,
            inverse="public_x509_certificate",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PublicX509Certificate",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{277F7762-AB0C-4ed7-B2FB-E3B9917CD28B}",
        attributes=(
            AttrMeta("issuer_name", "issuerName", "str", 0, 1, "primitive"),
            AttrMeta("serial_number", "serialNumber", "str", 0, 1, "primitive"),
        ),
        ends=(
            iso_upper_layer.meta,
            tcp_access_point.meta,
        ),
    )

    def __init__(
        self,
        *,
        issuer_name: str | None = None,
        serial_number: str | None = None,
        iso_upper_layer: ISOUpperLayer | None = None,
        tcp_access_point: TCPAccessPoint | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.issuer_name = issuer_name
        self.serial_number = serial_number
        if iso_upper_layer is not None:
            self.iso_upper_layer = iso_upper_layer
        if tcp_access_point is not None:
            self.tcp_access_point = tcp_access_point
