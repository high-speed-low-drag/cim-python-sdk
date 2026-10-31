"""CGMES European extension class BoundaryPoint (EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuCore). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.connectivity_node import ConnectivityNode


class BoundaryPoint(PowerSystemResource):
    """Designates a connection point at which one or more model authority sets shall connect
    to. The location of the connection point as well as other properties are agreed between
    organisations responsible for the interconnection, hence all attributes of the class
    represent this agreement. It is primarily used in a boundary model authority set which
    can contain one or many BoundaryPoint-s among other Equipment-s and their connections."""

    __slots__ = (
        "_connectivity_node",
        "from_end_iso_code",
        "from_end_name",
        "from_end_name_tso",
        "is_direct_current",
        "is_excluded_from_area_interchange",
        "to_end_iso_code",
        "to_end_name",
        "to_end_name_tso",
    )

    from_end_iso_code: str | None
    from_end_name: str | None
    from_end_name_tso: str | None
    to_end_iso_code: str | None
    to_end_name: str | None
    to_end_name_tso: str | None
    is_direct_current: bool | None
    is_excluded_from_area_interchange: bool | None

    connectivity_node: One[ConnectivityNode] = One(
        EndMeta(
            name="connectivity_node",
            cim_role="ConnectivityNode",
            target="cim_python_sdk.model.iec61970.base.core.connectivity_node:ConnectivityNode",
            many=False,
            lower=1,
            upper=1,
            inverse="boundary_point",
            aggregation="none",
            namespace="eu",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BoundaryPoint",
        package="EuropeanCIMExtensions/ExtIEC61970/ExtEuBase/ExtEuCore",
        guid="{22106B32-87E4-4296-B0FC-1F9DB3D9D70A}",
        namespace="eu",
        attributes=(
            AttrMeta(
                "from_end_iso_code", "fromEndIsoCode", "str", 0, 1, "primitive", namespace="eu"
            ),
            AttrMeta("from_end_name", "fromEndName", "str", 0, 1, "primitive", namespace="eu"),
            AttrMeta(
                "from_end_name_tso", "fromEndNameTso", "str", 0, 1, "primitive", namespace="eu"
            ),
            AttrMeta("to_end_iso_code", "toEndIsoCode", "str", 0, 1, "primitive", namespace="eu"),
            AttrMeta("to_end_name", "toEndName", "str", 0, 1, "primitive", namespace="eu"),
            AttrMeta("to_end_name_tso", "toEndNameTso", "str", 0, 1, "primitive", namespace="eu"),
            AttrMeta(
                "is_direct_current", "isDirectCurrent", "bool", 0, 1, "primitive", namespace="eu"
            ),
            AttrMeta(
                "is_excluded_from_area_interchange",
                "isExcludedFromAreaInterchange",
                "bool",
                0,
                1,
                "primitive",
                namespace="eu",
            ),
        ),
        ends=(connectivity_node.meta,),
    )

    def __init__(
        self,
        *,
        from_end_iso_code: str | None = None,
        from_end_name: str | None = None,
        from_end_name_tso: str | None = None,
        to_end_iso_code: str | None = None,
        to_end_name: str | None = None,
        to_end_name_tso: str | None = None,
        is_direct_current: bool | None = None,
        is_excluded_from_area_interchange: bool | None = None,
        connectivity_node: ConnectivityNode | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.from_end_iso_code = from_end_iso_code
        self.from_end_name = from_end_name
        self.from_end_name_tso = from_end_name_tso
        self.to_end_iso_code = to_end_iso_code
        self.to_end_name = to_end_name
        self.to_end_name_tso = to_end_name_tso
        self.is_direct_current = is_direct_current
        self.is_excluded_from_area_interchange = is_excluded_from_area_interchange
        if connectivity_node is not None:
            self.connectivity_node = connectivity_node
