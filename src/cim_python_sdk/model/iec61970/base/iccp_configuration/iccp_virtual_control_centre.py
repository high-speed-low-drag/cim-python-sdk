"""CIM class ICCPVirtualControlCentre (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor import (
    BilateralExchangeActor,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.iccp_configuration.application_security_kind import (
        ApplicationSecurityKind,
    )


class ICCPVirtualControlCentre(BilateralExchangeActor):
    """This contains the information that a particular actor exposes for a particular agreed
    upon ICCP Bilateral Table."""

    __slots__ = (
        "application_security_requirement",
        "calling",
        "client_and_server",
        "minimum_update_interval",
        "name_of_local_icc",
        "support_for_block1",
        "support_for_block2",
        "support_for_block3",
        "support_for_block4",
        "support_for_block5",
        "support_for_depriciated_block8",
        "transport_security_requirement",
    )

    application_security_requirement: ApplicationSecurityKind | None
    client_and_server: bool | None
    calling: bool | None
    minimum_update_interval: int | None
    name_of_local_icc: str | None
    transport_security_requirement: bool | None
    support_for_block1: bool | None
    support_for_block2: bool | None
    support_for_block3: bool | None
    support_for_block4: bool | None
    support_for_block5: bool | None
    support_for_depriciated_block8: bool | None

    _cim_meta = ClassMeta(
        cim_name="ICCPVirtualControlCentre",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{290E9B5B-AAC5-4e36-A858-BE5AC797E8E0}",
        attributes=(
            AttrMeta(
                "application_security_requirement",
                "applicationSecurityRequirement",
                "ApplicationSecurityKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("client_and_server", "clientAndServer", "bool", 0, 1, "primitive"),
            AttrMeta("calling", "calling", "bool", 0, 1, "primitive"),
            AttrMeta("minimum_update_interval", "minimumUpdateInterval", "int", 0, 1, "primitive"),
            AttrMeta("name_of_local_icc", "nameOfLocalICC", "str", 0, 1, "primitive"),
            AttrMeta(
                "transport_security_requirement",
                "transportSecurityRequirement",
                "bool",
                0,
                1,
                "primitive",
            ),
            AttrMeta("support_for_block1", "supportForBlock1", "bool", 0, 1, "primitive"),
            AttrMeta("support_for_block2", "supportForBlock2", "bool", 0, 1, "primitive"),
            AttrMeta("support_for_block3", "supportForBlock3", "bool", 0, 1, "primitive"),
            AttrMeta("support_for_block4", "supportForBlock4", "bool", 0, 1, "primitive"),
            AttrMeta("support_for_block5", "supportForBlock5", "bool", 0, 1, "primitive"),
            AttrMeta(
                "support_for_depriciated_block8",
                "supportForDepriciatedBlock8",
                "bool",
                0,
                1,
                "primitive",
            ),
        ),
    )

    def __init__(
        self,
        *,
        application_security_requirement: ApplicationSecurityKind | None = None,
        client_and_server: bool | None = None,
        calling: bool | None = None,
        minimum_update_interval: int | None = None,
        name_of_local_icc: str | None = None,
        transport_security_requirement: bool | None = None,
        support_for_block1: bool | None = None,
        support_for_block2: bool | None = None,
        support_for_block3: bool | None = None,
        support_for_block4: bool | None = None,
        support_for_block5: bool | None = None,
        support_for_depriciated_block8: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.application_security_requirement = application_security_requirement
        self.client_and_server = client_and_server
        self.calling = calling
        self.minimum_update_interval = minimum_update_interval
        self.name_of_local_icc = name_of_local_icc
        self.transport_security_requirement = transport_security_requirement
        self.support_for_block1 = support_for_block1
        self.support_for_block2 = support_for_block2
        self.support_for_block3 = support_for_block3
        self.support_for_block4 = support_for_block4
        self.support_for_block5 = support_for_block5
        self.support_for_depriciated_block8 = support_for_depriciated_block8
