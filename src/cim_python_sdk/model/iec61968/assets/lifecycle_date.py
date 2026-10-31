"""CIM compound LifecycleDate (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class LifecycleDate(CimCompound):
    """Dates for asset lifecycle state changes. May have multiple lifecycle dates for this
    device and a compound type allows a query to return multiple dates."""

    __slots__ = (
        "installation_date",
        "manufactured_date",
        "purchase_date",
        "received_date",
        "removal_date",
        "retired_date",
    )

    manufactured_date: _dt.date | None
    purchase_date: _dt.date | None
    received_date: _dt.date | None
    installation_date: _dt.date | None
    removal_date: _dt.date | None
    retired_date: _dt.date | None

    _cim_meta = ClassMeta(
        cim_name="LifecycleDate",
        package="TC57CIM/IEC61968/Assets",
        guid="{67AECABD-F376-4a6e-B6E0-F84A33F324EC}",
        kind="compound",
        attributes=(
            AttrMeta("manufactured_date", "manufacturedDate", "date", 0, 1, "primitive"),
            AttrMeta("purchase_date", "purchaseDate", "date", 0, 1, "primitive"),
            AttrMeta("received_date", "receivedDate", "date", 0, 1, "primitive"),
            AttrMeta("installation_date", "installationDate", "date", 0, 1, "primitive"),
            AttrMeta("removal_date", "removalDate", "date", 0, 1, "primitive"),
            AttrMeta("retired_date", "retiredDate", "date", 0, 1, "primitive"),
        ),
    )
