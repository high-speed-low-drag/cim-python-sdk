"""CIM class ErpSalesOrder (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument


class ErpSalesOrder(ErpDocument):
    """General purpose Sales Order is used for utility service orders, etc.

    As used by the OAG, the SalesOrder is a step beyond a PurchaseOrder in that the
    receiving entity of the order also communicates SalesInformoration about the Order along
    with the Order itself."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="ErpSalesOrder",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{B4F609BD-F167-4d16-A382-99CEB1054332}",
    )
