"""CIM class RemoteUnit (TC57CIM/IEC61970/Base/SCADA). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.scada.communication_link import CommunicationLink
    from cim_python_sdk.model.iec61970.base.scada.remote_point import RemotePoint
    from cim_python_sdk.model.iec61970.base.scada.remote_unit_type import RemoteUnitType


class RemoteUnit(PowerSystemResource):
    """A remote unit can be an RTU, IED, substation control system, control centre, etc. The
    communication with the remote unit can be through various standard protocols (e.g. IEC
    61870, IEC 61850) or non standard protocols (e.g. DNP, RP570, etc.). A remote unit
    contains remote data points that might be telemetered, collected or calculated. The
    RemoteUnit class inherits PowerSystemResource. The intention is to allow RemoteUnits to
    have Measurements. These Measurements can be used to model unit status as operational,
    out of service, unit failure, etc."""

    __slots__ = ("_communication_links", "_remote_points", "remote_unit_type")

    remote_unit_type: RemoteUnitType | None

    remote_points: Many[RemotePoint] = Many(
        EndMeta(
            name="remote_points",
            cim_role="RemotePoints",
            target="cim_python_sdk.model.iec61970.base.scada.remote_point:RemotePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="remote_unit",
            aggregation="shared",
        )
    )
    communication_links: Many[CommunicationLink] = Many(
        EndMeta(
            name="communication_links",
            cim_role="CommunicationLinks",
            target="cim_python_sdk.model.iec61970.base.scada.communication_link:CommunicationLink",
            many=True,
            lower=1,
            upper=None,
            inverse="remote_units",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RemoteUnit",
        package="TC57CIM/IEC61970/Base/SCADA",
        guid="{93AA36A5-8421-432f-89ED-64774D6A10A3}",
        attributes=(
            AttrMeta("remote_unit_type", "remoteUnitType", "RemoteUnitType", 0, 1, "enumeration"),
        ),
        ends=(
            remote_points.meta,
            communication_links.meta,
        ),
    )

    def __init__(
        self,
        *,
        remote_unit_type: RemoteUnitType | None = None,
        remote_points: Iterable[RemotePoint] | None = None,
        communication_links: Iterable[CommunicationLink] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.remote_unit_type = remote_unit_type
        if remote_points is not None:
            RemoteUnit.remote_points.extend(self, remote_points)
        if communication_links is not None:
            RemoteUnit.communication_links.extend(self, communication_links)

    def add_remote_point(self, remote_point: RemotePoint) -> Self:
        return RemoteUnit.remote_points.add(self, remote_point)

    def remove_remote_point(self, remote_point: RemotePoint) -> Self:
        return RemoteUnit.remote_points.remove(self, remote_point)

    def clear_remote_points(self) -> Self:
        return RemoteUnit.remote_points.clear(self)

    def num_remote_point(self) -> int:
        return RemoteUnit.remote_points.count(self)

    def get_remote_point_by_mrid(self, mrid: str) -> RemotePoint | None:
        return RemoteUnit.remote_points.get_by_mrid(self, mrid)

    def add_communication_link(self, communication_link: CommunicationLink) -> Self:
        return RemoteUnit.communication_links.add(self, communication_link)

    def remove_communication_link(self, communication_link: CommunicationLink) -> Self:
        return RemoteUnit.communication_links.remove(self, communication_link)

    def clear_communication_links(self) -> Self:
        return RemoteUnit.communication_links.clear(self)

    def num_communication_link(self) -> int:
        return RemoteUnit.communication_links.count(self)

    def get_communication_link_by_mrid(self, mrid: str) -> CommunicationLink | None:
        return RemoteUnit.communication_links.get_by_mrid(self, mrid)
