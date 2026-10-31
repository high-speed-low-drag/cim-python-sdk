"""CIM compound BankAccountDetail (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class BankAccountDetail(CimCompound):
    """Details of a bank account."""

    __slots__ = ("account_number", "bank_name", "branch_code", "holder_id", "holder_name")

    account_number: str | None
    holder_name: str | None
    holder_id: str | None
    bank_name: str | None
    branch_code: str | None

    _cim_meta = ClassMeta(
        cim_name="BankAccountDetail",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{1945A7C3-F822-45c2-B83E-EA1C5A11F43C}",
        kind="compound",
        attributes=(
            AttrMeta("account_number", "accountNumber", "str", 0, 1, "primitive"),
            AttrMeta("holder_name", "holderName", "str", 0, 1, "primitive"),
            AttrMeta("holder_id", "holderID", "str", 0, 1, "primitive"),
            AttrMeta("bank_name", "bankName", "str", 0, 1, "primitive"),
            AttrMeta("branch_code", "branchCode", "str", 0, 1, "primitive"),
        ),
    )
