"""CIM class Agreement (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class Agreement(Document):
    """Formal agreement between two parties defining the terms and conditions for a set of
    services. The specifics of the services are, in turn, defined via one or more service
    agreements."""

    __slots__ = ("sign_date", "validity_interval")

    sign_date: _dt.date | None
    validity_interval: DateTimeInterval | None

    _cim_meta = ClassMeta(
        cim_name="Agreement",
        package="TC57CIM/IEC61968/Common",
        guid="{17B1479C-FC7D-4621-AF7F-BBA624EE6037}",
        attributes=(
            AttrMeta("sign_date", "signDate", "date", 0, 1, "primitive"),
            AttrMeta("validity_interval", "validityInterval", "DateTimeInterval", 0, 1, "compound"),
        ),
    )

    def __init__(
        self,
        *,
        sign_date: _dt.date | None = None,
        validity_interval: DateTimeInterval | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sign_date = sign_date
        self.validity_interval = validity_interval
