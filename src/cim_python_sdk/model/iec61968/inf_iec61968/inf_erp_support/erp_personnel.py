"""CIM class ErpPersonnel (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson


class ErpPersonnel(ErpIdentifiedObject):
    """Information that applies to the basic data about a utility person, used by ERP
    applications to transfer Personnel data for a worker."""

    __slots__ = ("_erp_persons", "status")

    status: Status | None

    erp_persons: Many[OldPerson] = Many(
        EndMeta(
            name="erp_persons",
            cim_role="ErpPersons",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_personnel",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpPersonnel",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{40C9A7CC-0257-4961-8051-2EF29DABECD9}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(erp_persons.meta,),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        erp_persons: Iterable[OldPerson] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if erp_persons is not None:
            ErpPersonnel.erp_persons.extend(self, erp_persons)

    def add_erp_person(self, erp_person: OldPerson) -> Self:
        return ErpPersonnel.erp_persons.add(self, erp_person)

    def remove_erp_person(self, erp_person: OldPerson) -> Self:
        return ErpPersonnel.erp_persons.remove(self, erp_person)

    def clear_erp_persons(self) -> Self:
        return ErpPersonnel.erp_persons.clear(self)

    def num_erp_person(self) -> int:
        return ErpPersonnel.erp_persons.count(self)

    def get_erp_person_by_mrid(self, mrid: str) -> OldPerson | None:
        return ErpPersonnel.erp_persons.get_by_mrid(self, mrid)
