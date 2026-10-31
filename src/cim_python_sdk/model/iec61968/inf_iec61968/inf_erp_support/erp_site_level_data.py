"""CIM class ErpSiteLevelData (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property import LandProperty


class ErpSiteLevelData(ErpIdentifiedObject):
    """For a utility, general information that describes physical locations of organizations or
    the location codes and their meanings. This enables ERP applications to ensure that the
    physical location identifiers are synchronized between the business applications."""

    __slots__ = ("_land_property", "status")

    status: Status | None

    land_property: One[LandProperty] = One(
        EndMeta(
            name="land_property",
            cim_role="LandProperty",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property:LandProperty",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_site_level_datas",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpSiteLevelData",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{4625CE64-B06A-49a8-A819-9CF8A454876B}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(land_property.meta,),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        land_property: LandProperty | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if land_property is not None:
            self.land_property = land_property
