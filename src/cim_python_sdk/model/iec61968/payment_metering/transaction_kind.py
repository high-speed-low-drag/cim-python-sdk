"""CIM enumeration TransactionKind (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransactionKind(CimEnum):
    """Kind of transaction."""

    serviceChargePayment = "serviceChargePayment"
    taxChargePayment = "taxChargePayment"
    auxiliaryChargePayment = "auxiliaryChargePayment"
    accountPayment = "accountPayment"
    diversePayment = "diversePayment"
    transactionReversal = "transactionReversal"
    tokenSalePayment = "tokenSalePayment"
    tokenFreeIssue = "tokenFreeIssue"
    tokenGrant = "tokenGrant"
    tokenExchange = "tokenExchange"
    tokenCancellation = "tokenCancellation"
    meterConfigurationToken = "meterConfigurationToken"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransactionKind",
            package="TC57CIM/IEC61968/PaymentMetering",
            guid="{E6FA723B-B828-4ed5-8F99-28E3C70CAFC7}",
            kind="enumeration",
        )
    )
