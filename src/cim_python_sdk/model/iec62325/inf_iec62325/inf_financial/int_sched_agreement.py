"""CIM class IntSchedAgreement (TC57CIM/IEC62325/InfIEC62325/InfFinancial). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class IntSchedAgreement(Agreement):
    """A type of agreement that provides the default method by which interchange schedules are
    to be integrated to obtain hourly MWh schedules for accounting."""

    __slots__ = ("default_integration_method",)

    default_integration_method: str | None

    _cim_meta = ClassMeta(
        cim_name="IntSchedAgreement",
        package="TC57CIM/IEC62325/InfIEC62325/InfFinancial",
        guid="{9B01D3C0-7F3E-44b5-A45E-B6585D9B253B}",
        attributes=(
            AttrMeta(
                "default_integration_method", "defaultIntegrationMethod", "str", 0, 1, "primitive"
            ),
        ),
    )

    def __init__(
        self,
        *,
        default_integration_method: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.default_integration_method = default_integration_method
