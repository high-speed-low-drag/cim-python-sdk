"""CIM class OldPerson (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.person import Person

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.craft import Craft
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.person_organisation_role import (
        PersonOrganisationRole,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.person_property_role import (
        PersonPropertyRole,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.skill import Skill
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_competency import (
        ErpCompetency,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_personnel import (
        ErpPersonnel,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.labor_item import LaborItem
    from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue


class OldPerson(Person):
    """General purpose information for name and other information to contact people."""

    __slots__ = (
        "_crafts",
        "_customer_data",
        "_erp_competency",
        "_erp_personnel",
        "_labor_items",
        "_land_property_roles",
        "_measurement_values",
        "_organisation_roles",
        "_skills",
        "status",
        "type",
    )

    type: str | None
    status: Status | None

    customer_data: One[Customer] = One(
        EndMeta(
            name="customer_data",
            cim_role="CustomerData",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_persons",
            aggregation="none",
        )
    )
    crafts: Many[Craft] = Many(
        EndMeta(
            name="crafts",
            cim_role="Crafts",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.craft:Craft",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_persons",
            aggregation="none",
        )
    )
    erp_personnel: One[ErpPersonnel] = One(
        EndMeta(
            name="erp_personnel",
            cim_role="ErpPersonnel",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_personnel:ErpPersonnel",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_persons",
            aggregation="none",
        )
    )
    organisation_roles: Many[PersonOrganisationRole] = Many(
        EndMeta(
            name="organisation_roles",
            cim_role="OrganisationRoles",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.person_organisation_role:PersonOrganisationRole",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_person",
            aggregation="none",
        )
    )
    skills: Many[Skill] = Many(
        EndMeta(
            name="skills",
            cim_role="Skills",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.skill:Skill",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_person",
            aggregation="none",
        )
    )
    labor_items: Many[LaborItem] = Many(
        EndMeta(
            name="labor_items",
            cim_role="LaborItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.labor_item:LaborItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_persons",
            aggregation="none",
        )
    )
    erp_competency: One[ErpCompetency] = One(
        EndMeta(
            name="erp_competency",
            cim_role="ErpCompetency",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_competency:ErpCompetency",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_persons",
            aggregation="none",
        )
    )
    land_property_roles: Many[PersonPropertyRole] = Many(
        EndMeta(
            name="land_property_roles",
            cim_role="LandPropertyRoles",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.person_property_role:PersonPropertyRole",
            many=True,
            lower=0,
            upper=None,
            inverse="person",
            aggregation="none",
        )
    )
    measurement_values: Many[MeasurementValue] = Many(
        EndMeta(
            name="measurement_values",
            cim_role="MeasurementValues",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value:MeasurementValue",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_person",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OldPerson",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{C5A7D63A-BE27-4f6b-BC2F-A070401B38DA}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            customer_data.meta,
            crafts.meta,
            erp_personnel.meta,
            organisation_roles.meta,
            skills.meta,
            labor_items.meta,
            erp_competency.meta,
            land_property_roles.meta,
            measurement_values.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        status: Status | None = None,
        customer_data: Customer | None = None,
        crafts: Iterable[Craft] | None = None,
        erp_personnel: ErpPersonnel | None = None,
        organisation_roles: Iterable[PersonOrganisationRole] | None = None,
        skills: Iterable[Skill] | None = None,
        labor_items: Iterable[LaborItem] | None = None,
        erp_competency: ErpCompetency | None = None,
        land_property_roles: Iterable[PersonPropertyRole] | None = None,
        measurement_values: Iterable[MeasurementValue] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        if customer_data is not None:
            self.customer_data = customer_data
        if crafts is not None:
            OldPerson.crafts.extend(self, crafts)
        if erp_personnel is not None:
            self.erp_personnel = erp_personnel
        if organisation_roles is not None:
            OldPerson.organisation_roles.extend(self, organisation_roles)
        if skills is not None:
            OldPerson.skills.extend(self, skills)
        if labor_items is not None:
            OldPerson.labor_items.extend(self, labor_items)
        if erp_competency is not None:
            self.erp_competency = erp_competency
        if land_property_roles is not None:
            OldPerson.land_property_roles.extend(self, land_property_roles)
        if measurement_values is not None:
            OldPerson.measurement_values.extend(self, measurement_values)

    def add_craft(self, craft: Craft) -> Self:
        return OldPerson.crafts.add(self, craft)

    def remove_craft(self, craft: Craft) -> Self:
        return OldPerson.crafts.remove(self, craft)

    def clear_crafts(self) -> Self:
        return OldPerson.crafts.clear(self)

    def num_craft(self) -> int:
        return OldPerson.crafts.count(self)

    def get_craft_by_mrid(self, mrid: str) -> Craft | None:
        return OldPerson.crafts.get_by_mrid(self, mrid)

    def add_organisation_role(self, organisation_role: PersonOrganisationRole) -> Self:
        return OldPerson.organisation_roles.add(self, organisation_role)

    def remove_organisation_role(self, organisation_role: PersonOrganisationRole) -> Self:
        return OldPerson.organisation_roles.remove(self, organisation_role)

    def clear_organisation_roles(self) -> Self:
        return OldPerson.organisation_roles.clear(self)

    def num_organisation_role(self) -> int:
        return OldPerson.organisation_roles.count(self)

    def get_organisation_role_by_mrid(self, mrid: str) -> PersonOrganisationRole | None:
        return OldPerson.organisation_roles.get_by_mrid(self, mrid)

    def add_skill(self, skill: Skill) -> Self:
        return OldPerson.skills.add(self, skill)

    def remove_skill(self, skill: Skill) -> Self:
        return OldPerson.skills.remove(self, skill)

    def clear_skills(self) -> Self:
        return OldPerson.skills.clear(self)

    def num_skill(self) -> int:
        return OldPerson.skills.count(self)

    def get_skill_by_mrid(self, mrid: str) -> Skill | None:
        return OldPerson.skills.get_by_mrid(self, mrid)

    def add_labor_item(self, labor_item: LaborItem) -> Self:
        return OldPerson.labor_items.add(self, labor_item)

    def remove_labor_item(self, labor_item: LaborItem) -> Self:
        return OldPerson.labor_items.remove(self, labor_item)

    def clear_labor_items(self) -> Self:
        return OldPerson.labor_items.clear(self)

    def num_labor_item(self) -> int:
        return OldPerson.labor_items.count(self)

    def get_labor_item_by_mrid(self, mrid: str) -> LaborItem | None:
        return OldPerson.labor_items.get_by_mrid(self, mrid)

    def add_land_property_role(self, land_property_role: PersonPropertyRole) -> Self:
        return OldPerson.land_property_roles.add(self, land_property_role)

    def remove_land_property_role(self, land_property_role: PersonPropertyRole) -> Self:
        return OldPerson.land_property_roles.remove(self, land_property_role)

    def clear_land_property_roles(self) -> Self:
        return OldPerson.land_property_roles.clear(self)

    def num_land_property_role(self) -> int:
        return OldPerson.land_property_roles.count(self)

    def get_land_property_role_by_mrid(self, mrid: str) -> PersonPropertyRole | None:
        return OldPerson.land_property_roles.get_by_mrid(self, mrid)

    def add_measurement_value(self, measurement_value: MeasurementValue) -> Self:
        return OldPerson.measurement_values.add(self, measurement_value)

    def remove_measurement_value(self, measurement_value: MeasurementValue) -> Self:
        return OldPerson.measurement_values.remove(self, measurement_value)

    def clear_measurement_values(self) -> Self:
        return OldPerson.measurement_values.clear(self)

    def num_measurement_value(self) -> int:
        return OldPerson.measurement_values.count(self)

    def get_measurement_value_by_mrid(self, mrid: str) -> MeasurementValue | None:
        return OldPerson.measurement_values.get_by_mrid(self, mrid)
