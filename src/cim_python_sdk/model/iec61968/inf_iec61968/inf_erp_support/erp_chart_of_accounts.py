"""CIM class ErpChartOfAccounts (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument


class ErpChartOfAccounts(ErpDocument):
    """Accounting structure of a business. Each account represents a financial aspect of a
    business, such as its Accounts Payable, or the value of its inventory, or its office
    supply expenses."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="ErpChartOfAccounts",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{0A12D145-2CE5-48dd-A067-F52E6F11113B}",
    )
