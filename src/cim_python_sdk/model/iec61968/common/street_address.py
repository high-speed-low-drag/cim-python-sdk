"""CIM compound StreetAddress (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.common.street_detail import StreetDetail
    from cim_python_sdk.model.iec61968.common.town_detail import TownDetail


class StreetAddress(CimCompound):
    """General purpose street and postal address information."""

    __slots__ = ("language", "po_box", "postal_code", "status", "street_detail", "town_detail")

    street_detail: StreetDetail | None
    town_detail: TownDetail | None
    status: Status | None
    postal_code: str | None
    po_box: str | None
    language: str | None

    _cim_meta = ClassMeta(
        cim_name="StreetAddress",
        package="TC57CIM/IEC61968/Common",
        guid="{90007399-BB87-4f28-9898-853DAB696115}",
        kind="compound",
        attributes=(
            AttrMeta("street_detail", "streetDetail", "StreetDetail", 0, 1, "compound"),
            AttrMeta("town_detail", "townDetail", "TownDetail", 0, 1, "compound"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
            AttrMeta("postal_code", "postalCode", "str", 0, 1, "primitive"),
            AttrMeta("po_box", "poBox", "str", 0, 1, "primitive"),
            AttrMeta("language", "language", "str", 0, 1, "primitive"),
        ),
    )
