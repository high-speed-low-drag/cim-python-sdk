"""CIM class ErpCompetency (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson


class ErpCompetency(ErpIdentifiedObject):
    """Information that describes aptitudes of a utility employee. Unlike Skills that an
    ErpPerson must be certified to perform before undertaking certain type of assignments
    (to be able to perfrom a Craft), ErpCompetency has more to do with typical Human
    Resource (HR) matters such as schooling, training, etc."""

    __slots__ = ("_erp_persons",)

    erp_persons: Many[OldPerson] = Many(
        EndMeta(
            name="erp_persons",
            cim_role="ErpPersons",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_competency",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpCompetency",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{EC751E99-286F-44d5-9C43-E7EA516D766C}",
        ends=(erp_persons.meta,),
    )

    def __init__(
        self,
        *,
        erp_persons: Iterable[OldPerson] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_persons is not None:
            ErpCompetency.erp_persons.extend(self, erp_persons)

    def add_erp_person(self, erp_person: OldPerson) -> Self:
        return ErpCompetency.erp_persons.add(self, erp_person)

    def remove_erp_person(self, erp_person: OldPerson) -> Self:
        return ErpCompetency.erp_persons.remove(self, erp_person)

    def clear_erp_persons(self) -> Self:
        return ErpCompetency.erp_persons.clear(self)

    def num_erp_person(self) -> int:
        return ErpCompetency.erp_persons.count(self)

    def get_erp_person_by_mrid(self, mrid: str) -> OldPerson | None:
        return ErpCompetency.erp_persons.get_by_mrid(self, mrid)
