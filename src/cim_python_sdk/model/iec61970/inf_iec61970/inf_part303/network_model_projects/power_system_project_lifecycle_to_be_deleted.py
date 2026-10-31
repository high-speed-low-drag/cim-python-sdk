"""CIM compound PowerSystemProjectLifecycleToBeDeleted (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt


class PowerSystemProjectLifecycleToBeDeleted(CimCompound):
    """Represent the base lifecycle of a functional model change that could be a construction
    of new elements."""

    __slots__ = ("cancelled", "committed", "in_build", "in_plan")

    cancelled: _dt.date | None
    committed: _dt.date | None
    in_build: _dt.date | None
    in_plan: _dt.date | None

    _cim_meta = ClassMeta(
        cim_name="PowerSystemProjectLifecycleToBeDeleted",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{AB23472D-DDD3-443d-9A82-4256A71DA7A5}",
        kind="compound",
        attributes=(
            AttrMeta("cancelled", "cancelled", "date", 0, 1, "primitive"),
            AttrMeta("committed", "committed", "date", 0, 1, "primitive"),
            AttrMeta("in_build", "inBuild", "date", 0, 1, "primitive"),
            AttrMeta("in_plan", "inPlan", "date", 0, 1, "primitive"),
        ),
    )
