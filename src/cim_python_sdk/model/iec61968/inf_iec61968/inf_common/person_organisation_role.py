"""CIM class PersonOrganisationRole (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson


class PersonOrganisationRole(OrganisationRole):
    """Role an organisation plays with respect to persons."""

    __slots__ = ("_erp_person", "client_id")

    client_id: str | None

    erp_person: One[OldPerson] = One(
        EndMeta(
            name="erp_person",
            cim_role="ErpPerson",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=False,
            lower=1,
            upper=1,
            inverse="organisation_roles",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PersonOrganisationRole",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{0E229F32-EC45-4bf8-BEAA-344389063127}",
        attributes=(AttrMeta("client_id", "clientID", "str", 0, 1, "primitive"),),
        ends=(erp_person.meta,),
    )

    def __init__(
        self,
        *,
        client_id: str | None = None,
        erp_person: OldPerson | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.client_id = client_id
        if erp_person is not None:
            self.erp_person = erp_person
