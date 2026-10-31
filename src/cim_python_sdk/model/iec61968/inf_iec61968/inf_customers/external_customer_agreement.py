"""CIM class ExternalCustomerAgreement (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61968.common.agreement import Agreement


class ExternalCustomerAgreement(Agreement):
    """A type of customer agreement involving an external agency. For example, a customer may
    form a contracts with an Energy Service Supplier if Direct Access is permitted."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="ExternalCustomerAgreement",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{1575CDC5-2EC2-4697-8D9F-E2AE90C2C282}",
    )
