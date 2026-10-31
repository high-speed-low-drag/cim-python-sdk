"""CIM class ICCPProvidedPoint (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.iccp_configuration.provided_bilateral_point import (
    ProvidedBilateralPoint,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.iccp_configuration.iccp_access_privilege_kind import (
        ICCPAccessPrivilegeKind,
    )
    from cim_python_sdk.model.iec61970.base.iccp_configuration.iccp_point_kind import ICCPPointKind
    from cim_python_sdk.model.iec61970.base.iccp_configuration.iccp_quality_kind import (
        ICCPQualityKind,
    )
    from cim_python_sdk.model.iec61970.base.iccp_configuration.iccp_scope_kind import ICCPScopeKind


class ICCPProvidedPoint(ProvidedBilateralPoint):
    """The IdentifiedObject.name attribute must have a value. The name attribute shall be used
    as the DataValue name used for the exchange."""

    __slots__ = ("access_priviledge", "point_quality", "point_type", "scope")

    scope: ICCPScopeKind | None
    point_type: ICCPPointKind | None
    point_quality: ICCPQualityKind | None
    access_priviledge: ICCPAccessPrivilegeKind | None

    _cim_meta = ClassMeta(
        cim_name="ICCPProvidedPoint",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{33160A9A-23C7-4086-A723-E674D19B3892}",
        attributes=(
            AttrMeta("scope", "scope", "ICCPScopeKind", 0, 1, "enumeration"),
            AttrMeta("point_type", "pointType", "ICCPPointKind", 0, 1, "enumeration"),
            AttrMeta("point_quality", "pointQuality", "ICCPQualityKind", 0, 1, "enumeration"),
            AttrMeta(
                "access_priviledge",
                "accessPriviledge",
                "ICCPAccessPrivilegeKind",
                0,
                1,
                "enumeration",
            ),
        ),
    )

    def __init__(
        self,
        *,
        scope: ICCPScopeKind | None = None,
        point_type: ICCPPointKind | None = None,
        point_quality: ICCPQualityKind | None = None,
        access_priviledge: ICCPAccessPrivilegeKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.scope = scope
        self.point_type = point_type
        self.point_quality = point_quality
        self.access_priviledge = access_priviledge
