"""CIM compound Version (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class Version(CimCompound):
    """This is the version for a group of devices or objects. This could be used to track the
    version for any group of objects or devices over time. For example, for a DERGroup, the
    requesting system may want to get the details of a specific version of a DERGroup."""

    __slots__ = ("date", "major", "minor", "revision")

    date: _dt.datetime | None
    major: int | None
    minor: int | None
    revision: int | None

    _cim_meta = ClassMeta(
        cim_name="Version",
        package="TC57CIM/IEC61968/Common",
        guid="{2CE9983F-D902-48d7-859B-398F47403ACD}",
        kind="compound",
        attributes=(
            AttrMeta("date", "date", "datetime", 0, 1, "primitive"),
            AttrMeta("major", "major", "int", 1, 1, "primitive"),
            AttrMeta("minor", "minor", "int", 0, 1, "primitive"),
            AttrMeta("revision", "revision", "int", 0, 1, "primitive"),
        ),
    )
