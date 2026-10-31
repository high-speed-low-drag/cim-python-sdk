"""CIM class TCPAccessPoint (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.iccp_configuration.ip_access_point import IPAccessPoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.iccp_configuration.public_x509_certificate import (
        PublicX509Certificate,
    )


class TCPAccessPoint(IPAccessPoint):
    """Allows addressing and behavioural information regarding the use of TCP by ICCP links."""

    __slots__ = ("_public_x509_certificate", "keep_alive_time", "port")

    keep_alive_time: int | None
    port: int | None

    public_x509_certificate: Many[PublicX509Certificate] = Many(
        EndMeta(
            name="public_x509_certificate",
            cim_role="PublicX509Certificate",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.public_x509_certificate:PublicX509Certificate",
            many=True,
            lower=0,
            upper=None,
            inverse="tcp_access_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TCPAccessPoint",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{9A1BFBDE-2EDA-4512-9BA4-0281C6966DA9}",
        attributes=(
            AttrMeta("keep_alive_time", "keepAliveTime", "int", 0, 1, "primitive"),
            AttrMeta("port", "port", "int", 0, 1, "primitive"),
        ),
        ends=(public_x509_certificate.meta,),
    )

    def __init__(
        self,
        *,
        keep_alive_time: int | None = None,
        port: int | None = None,
        public_x509_certificate: Iterable[PublicX509Certificate] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.keep_alive_time = keep_alive_time
        self.port = port
        if public_x509_certificate is not None:
            TCPAccessPoint.public_x509_certificate.extend(self, public_x509_certificate)

    def add_public_x509_certificate(self, public_x509_certificate: PublicX509Certificate) -> Self:
        return TCPAccessPoint.public_x509_certificate.add(self, public_x509_certificate)

    def remove_public_x509_certificate(
        self, public_x509_certificate: PublicX509Certificate
    ) -> Self:
        return TCPAccessPoint.public_x509_certificate.remove(self, public_x509_certificate)

    def clear_public_x509_certificate(self) -> Self:
        return TCPAccessPoint.public_x509_certificate.clear(self)

    def num_public_x509_certificate(self) -> int:
        return TCPAccessPoint.public_x509_certificate.count(self)
