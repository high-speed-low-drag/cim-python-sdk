"""CIM class RedLine (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status


class RedLine(IdentifiedObject):
    """This class is used for handling the accompanying annotations, time stamp, author, etc.
    of designs, drawings and maps. A red line can be associated with any Location object."""

    __slots__ = ("status",)

    status: Status | None

    _cim_meta = ClassMeta(
        cim_name="RedLine",
        package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
        guid="{504F964D-F017-4062-B152-1B845265C22D}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
