"""CIM class ICCPVCC (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor import (
    BilateralExchangeActor,
)


class ICCPVCC(BilateralExchangeActor):
    """Indicates that the ICCP information is global in nature and normally is available to all
    authorized peers."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="ICCPVCC",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{2688C5F0-9A0D-4275-8AB5-9BF09B233FDD}",
    )
