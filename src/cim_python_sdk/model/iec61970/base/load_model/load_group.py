"""CIM class LoadGroup (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.load_model.sub_load_area import SubLoadArea


class LoadGroup(IdentifiedObject):
    """The class is the third level in a hierarchical structure for grouping of loads for the
    purpose of load flow load scaling."""

    __slots__ = ("_sub_load_area",)

    sub_load_area: One[SubLoadArea] = One(
        EndMeta(
            name="sub_load_area",
            cim_role="SubLoadArea",
            target="cim_python_sdk.model.iec61970.base.load_model.sub_load_area:SubLoadArea",
            many=False,
            lower=1,
            upper=1,
            inverse="load_groups",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadGroup",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{BC60B72D-57A5-4705-96C2-21180B040E5B}",
        ends=(sub_load_area.meta,),
    )

    def __init__(
        self,
        *,
        sub_load_area: SubLoadArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if sub_load_area is not None:
            self.sub_load_area = sub_load_area
