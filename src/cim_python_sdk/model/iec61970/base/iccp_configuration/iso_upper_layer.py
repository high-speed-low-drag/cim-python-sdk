"""CIM class ISOUpperLayer (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.iccp_configuration.tcp_access_point import TCPAccessPoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.iccp_configuration.public_x509_certificate import (
        PublicX509Certificate,
    )


class ISOUpperLayer(TCPAccessPoint):
    """Is a set of configure addressing information that is required since ICCP utilizes
    addressing other than a TCP port."""

    __slots__ = (
        "_upper_layer_public_x509_certificate",
        "ae_invoke",
        "ae_qual",
        "ap_invoke",
        "ap_title",
        "osi_psel",
        "osi_ssel",
        "osi_tsel",
    )

    ap_title: str | None
    osi_psel: str | None
    osi_ssel: str | None
    osi_tsel: str | None
    ap_invoke: int | None
    ae_invoke: int | None
    ae_qual: int | None

    upper_layer_public_x509_certificate: Many[PublicX509Certificate] = Many(
        EndMeta(
            name="upper_layer_public_x509_certificate",
            cim_role="UpperLayerPublicX509Certificate",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.public_x509_certificate:PublicX509Certificate",
            many=True,
            lower=0,
            upper=None,
            inverse="iso_upper_layer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ISOUpperLayer",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{E56AA980-565B-4931-AB9E-DA88591B48E8}",
        attributes=(
            AttrMeta("ap_title", "apTitle", "str", 0, 1, "primitive"),
            AttrMeta("osi_psel", "osiPsel", "str", 0, 1, "primitive"),
            AttrMeta("osi_ssel", "osiSsel", "str", 0, 1, "primitive"),
            AttrMeta("osi_tsel", "osiTsel", "str", 0, 1, "primitive"),
            AttrMeta("ap_invoke", "apInvoke", "int", 0, 1, "primitive"),
            AttrMeta("ae_invoke", "aeInvoke", "int", 0, 1, "primitive"),
            AttrMeta("ae_qual", "aeQual", "int", 0, 1, "primitive"),
        ),
        ends=(upper_layer_public_x509_certificate.meta,),
    )

    def __init__(
        self,
        *,
        ap_title: str | None = None,
        osi_psel: str | None = None,
        osi_ssel: str | None = None,
        osi_tsel: str | None = None,
        ap_invoke: int | None = None,
        ae_invoke: int | None = None,
        ae_qual: int | None = None,
        upper_layer_public_x509_certificate: Iterable[PublicX509Certificate] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ap_title = ap_title
        self.osi_psel = osi_psel
        self.osi_ssel = osi_ssel
        self.osi_tsel = osi_tsel
        self.ap_invoke = ap_invoke
        self.ae_invoke = ae_invoke
        self.ae_qual = ae_qual
        if upper_layer_public_x509_certificate is not None:
            ISOUpperLayer.upper_layer_public_x509_certificate.extend(
                self, upper_layer_public_x509_certificate
            )

    def add_upper_layer_public_x509_certificate(
        self, upper_layer_public_x509_certificate: PublicX509Certificate
    ) -> Self:
        return ISOUpperLayer.upper_layer_public_x509_certificate.add(
            self, upper_layer_public_x509_certificate
        )

    def remove_upper_layer_public_x509_certificate(
        self, upper_layer_public_x509_certificate: PublicX509Certificate
    ) -> Self:
        return ISOUpperLayer.upper_layer_public_x509_certificate.remove(
            self, upper_layer_public_x509_certificate
        )

    def clear_upper_layer_public_x509_certificate(self) -> Self:
        return ISOUpperLayer.upper_layer_public_x509_certificate.clear(self)

    def num_upper_layer_public_x509_certificate(self) -> int:
        return ISOUpperLayer.upper_layer_public_x509_certificate.count(self)
