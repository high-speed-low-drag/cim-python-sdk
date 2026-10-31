"""CIM class OperatingParticipant (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.operating_share import OperatingShare


class OperatingParticipant(IdentifiedObject):
    """An operator of multiple power system resource objects. Note multple operating
    participants may operate the same power system resource object. This can be used for
    modeling jointly owned units where each owner operates as a contractual share."""

    __slots__ = ("_operating_share",)

    operating_share: Many[OperatingShare] = Many(
        EndMeta(
            name="operating_share",
            cim_role="OperatingShare",
            target="cim_python_sdk.model.iec61970.base.core.operating_share:OperatingShare",
            many=True,
            lower=0,
            upper=None,
            inverse="operating_participant",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperatingParticipant",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{04AAF1AE-4A67-4130-8259-DEA85BBCD65F}",
        ends=(operating_share.meta,),
    )

    def __init__(
        self,
        *,
        operating_share: Iterable[OperatingShare] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if operating_share is not None:
            OperatingParticipant.operating_share.extend(self, operating_share)

    def add_operating_share(self, operating_share: OperatingShare) -> Self:
        return OperatingParticipant.operating_share.add(self, operating_share)

    def remove_operating_share(self, operating_share: OperatingShare) -> Self:
        return OperatingParticipant.operating_share.remove(self, operating_share)

    def clear_operating_share(self) -> Self:
        return OperatingParticipant.operating_share.clear(self)

    def num_operating_share(self) -> int:
        return OperatingParticipant.operating_share.count(self)
