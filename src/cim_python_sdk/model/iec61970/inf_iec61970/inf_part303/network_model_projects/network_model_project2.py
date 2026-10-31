"""CIM class NetworkModelProject2 (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component2 import (
    NetworkModelProjectComponent2,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self


class NetworkModelProject2(NetworkModelProjectComponent2):
    """CIM class NetworkModelProject2."""

    __slots__ = ("_child",)

    child: Many[NetworkModelProjectComponent2] = Many(
        EndMeta(
            name="child",
            cim_role="Child",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_projects.network_model_project_component2:NetworkModelProjectComponent2",
            many=True,
            lower=0,
            upper=None,
            inverse="parent",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NetworkModelProject2",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelProjects",
        guid="{122073A1-D327-4ccf-BAEF-8092D3C71117}",
        ends=(child.meta,),
    )

    def __init__(
        self,
        *,
        child: Iterable[NetworkModelProjectComponent2] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if child is not None:
            NetworkModelProject2.child.extend(self, child)

    def add_child(self, child: NetworkModelProjectComponent2) -> Self:
        return NetworkModelProject2.child.add(self, child)

    def remove_child(self, child: NetworkModelProjectComponent2) -> Self:
        return NetworkModelProject2.child.remove(self, child)

    def clear_child(self) -> Self:
        return NetworkModelProject2.child.clear(self)

    def num_child(self) -> int:
        return NetworkModelProject2.child.count(self)

    def get_child_by_mrid(self, mrid: str) -> NetworkModelProjectComponent2 | None:
        return NetworkModelProject2.child.get_by_mrid(self, mrid)
