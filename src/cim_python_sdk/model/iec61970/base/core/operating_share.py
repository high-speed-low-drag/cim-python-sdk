"""CIM class OperatingShare (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.operating_participant import OperatingParticipant
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class OperatingShare(CimObject):
    """Specifies the operations contract relationship between a power system resource and a
    contract participant."""

    __slots__ = ("_operating_participant", "_power_system_resource", "percentage")

    percentage: float | None  # PerCent

    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=1,
            upper=1,
            inverse="operating_share",
            aggregation="none",
        )
    )
    operating_participant: One[OperatingParticipant] = One(
        EndMeta(
            name="operating_participant",
            cim_role="OperatingParticipant",
            target="cim_python_sdk.model.iec61970.base.core.operating_participant:OperatingParticipant",
            many=False,
            lower=1,
            upper=1,
            inverse="operating_share",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperatingShare",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{D615EDD6-6E2D-40b3-8190-3555A34BF9FF}",
        attributes=(AttrMeta("percentage", "percentage", "PerCent", 0, 1, "cimdatatype"),),
        ends=(
            power_system_resource.meta,
            operating_participant.meta,
        ),
    )

    def __init__(
        self,
        *,
        percentage: float | None = None,
        power_system_resource: PowerSystemResource | None = None,
        operating_participant: OperatingParticipant | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.percentage = percentage
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource
        if operating_participant is not None:
            self.operating_participant = operating_participant
