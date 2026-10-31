"""CIM compound ServicePointOutageSummary (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class ServicePointOutageSummary(CimCompound):
    """Summary counts of service points affected by an outage. These counts are sometimes
    referred to as total and critical customer count."""

    __slots__ = ("critical_count", "total_count")

    total_count: int | None
    critical_count: int | None

    _cim_meta = ClassMeta(
        cim_name="ServicePointOutageSummary",
        package="TC57CIM/IEC61968/Operations",
        guid="{AE9E2743-9D59-4dd9-BFA9-8798985B6200}",
        kind="compound",
        attributes=(
            AttrMeta("total_count", "totalCount", "int", 0, 1, "primitive"),
            AttrMeta("critical_count", "criticalCount", "int", 0, 1, "primitive"),
        ),
    )
