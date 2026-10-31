"""CIM compound DeploymentDate (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class DeploymentDate(CimCompound):
    """Dates for deployment events of an asset. May have multiple deployment type dates for
    this device and a compound type allows a query to return multiple dates."""

    __slots__ = (
        "in_service_date",
        "installed_date",
        "not_yet_installed_date",
        "out_of_service_date",
        "removed_date",
    )

    not_yet_installed_date: _dt.datetime | None
    installed_date: _dt.datetime | None
    in_service_date: _dt.datetime | None
    out_of_service_date: _dt.datetime | None
    removed_date: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="DeploymentDate",
        package="TC57CIM/IEC61968/Assets",
        guid="{FEF8B54C-8942-42b9-897B-C5B2D481E997}",
        kind="compound",
        attributes=(
            AttrMeta(
                "not_yet_installed_date", "notYetInstalledDate", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("installed_date", "installedDate", "datetime", 0, 1, "primitive"),
            AttrMeta("in_service_date", "inServiceDate", "datetime", 0, 1, "primitive"),
            AttrMeta("out_of_service_date", "outOfServiceDate", "datetime", 0, 1, "primitive"),
            AttrMeta("removed_date", "removedDate", "datetime", 0, 1, "primitive"),
        ),
    )
