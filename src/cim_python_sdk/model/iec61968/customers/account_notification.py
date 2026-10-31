"""CIM class AccountNotification (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.customers.customer_account import CustomerAccount


class AccountNotification(CimObject):
    """Notifications for move-in, move-out, delinquencies, etc."""

    __slots__ = ("_customer_account", "customer_notification_type", "method_type", "note", "time")

    time: _dt.datetime | None
    note: str | None
    customer_notification_type: str | None
    method_type: str | None

    customer_account: One[CustomerAccount] = One(
        EndMeta(
            name="customer_account",
            cim_role="CustomerAccount",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=False,
            lower=1,
            upper=1,
            inverse="account_notification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AccountNotification",
        package="TC57CIM/IEC61968/Customers",
        guid="{78D31291-F409-42c5-8671-BB2914DE33FB}",
        attributes=(
            AttrMeta("time", "time", "datetime", 0, 1, "primitive"),
            AttrMeta("note", "note", "str", 0, 1, "primitive"),
            AttrMeta(
                "customer_notification_type", "customerNotificationType", "str", 0, 1, "primitive"
            ),
            AttrMeta("method_type", "methodType", "str", 1, 1, "primitive"),
        ),
        ends=(customer_account.meta,),
    )

    def __init__(
        self,
        *,
        time: _dt.datetime | None = None,
        note: str | None = None,
        customer_notification_type: str | None = None,
        method_type: str | None = None,
        customer_account: CustomerAccount | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time = time
        self.note = note
        self.customer_notification_type = customer_notification_type
        self.method_type = method_type
        if customer_account is not None:
            self.customer_account = customer_account
