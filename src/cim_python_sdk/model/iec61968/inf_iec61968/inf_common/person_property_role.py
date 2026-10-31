"""CIM class PersonPropertyRole (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.role import Role

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property import LandProperty


class PersonPropertyRole(Role):
    """The role of a person relative to a given piece of property. Examples of roles include:
    owner, renter, contractor, etc."""

    __slots__ = ("_land_property", "_person")

    person: One[OldPerson] = One(
        EndMeta(
            name="person",
            cim_role="Person",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=False,
            lower=1,
            upper=1,
            inverse="land_property_roles",
            aggregation="none",
        )
    )
    land_property: One[LandProperty] = One(
        EndMeta(
            name="land_property",
            cim_role="LandProperty",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.land_property:LandProperty",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_person_roles",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PersonPropertyRole",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{0D27C992-8058-48c7-BFD1-494CC3F24130}",
        ends=(
            person.meta,
            land_property.meta,
        ),
    )

    def __init__(
        self,
        *,
        person: OldPerson | None = None,
        land_property: LandProperty | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if person is not None:
            self.person = person
        if land_property is not None:
            self.land_property = land_property
