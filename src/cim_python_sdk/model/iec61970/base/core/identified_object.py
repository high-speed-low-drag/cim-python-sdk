"""CIM class IdentifiedObject (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One, new_mrid

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.name import Name
    from cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object import DiagramObject
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set_member import (
        ChangeSetMember,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.instance_set import (
        InstanceSet,
    )


class IdentifiedObject(CimObject):
    """This is a root class to provide common identification for all classes needing
    identification and naming attributes."""

    __slots__ = (
        "_diagram_objects",
        "_instance_set",
        "_names",
        "_properties_cim_data_object",
        "_targeting_cim_data_object",
        "alias_name",
        "description",
        "energy_ident_code_eic",
        "mrid",
        "name",
        "short_name",
    )

    alias_name: str | None
    description: str | None
    mrid: str | None
    name: str | None
    energy_ident_code_eic: str | None
    short_name: str | None

    diagram_objects: Many[DiagramObject] = Many(
        EndMeta(
            name="diagram_objects",
            cim_role="DiagramObjects",
            target="cim_python_sdk.model.iec61970.base.diagram_layout.diagram_object:DiagramObject",
            many=True,
            lower=0,
            upper=None,
            inverse="identified_object",
            aggregation="none",
        )
    )
    names: Many[Name] = Many(
        EndMeta(
            name="names",
            cim_role="Names",
            target="cim_python_sdk.model.iec61970.base.core.name:Name",
            many=True,
            lower=0,
            upper=None,
            inverse="identified_object",
            aggregation="none",
        )
    )
    instance_set: One[InstanceSet] = One(
        EndMeta(
            name="instance_set",
            cim_role="InstanceSet",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.instance_set:InstanceSet",
            many=False,
            lower=1,
            upper=1,
            inverse="instance_set_member",
            aggregation="none",
        )
    )
    targeting_cim_data_object: Many[ChangeSetMember] = Many(
        EndMeta(
            name="targeting_cim_data_object",
            cim_role="TargetingCIMDataObject",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set_member:ChangeSetMember",
            many=True,
            lower=0,
            upper=None,
            inverse="target_object",
            aggregation="none",
        )
    )
    properties_cim_data_object: One[ChangeSetMember] = One(
        EndMeta(
            name="properties_cim_data_object",
            cim_role="PropertiesCIMDataObject",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set_member:ChangeSetMember",
            many=False,
            lower=0,
            upper=1,
            inverse="properties_object",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IdentifiedObject",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{055C5806-E9D8-4a7a-9307-DAF7C31763C7}",
        attributes=(
            AttrMeta("alias_name", "aliasName", "str", 0, 1, "primitive"),
            AttrMeta("description", "description", "str", 0, 1, "primitive"),
            AttrMeta("mrid", "mRID", "str", 0, 1, "primitive"),
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta(
                "energy_ident_code_eic",
                "energyIdentCodeEic",
                "str",
                0,
                1,
                "primitive",
                namespace="eu",
            ),
            AttrMeta("short_name", "shortName", "str", 0, 1, "primitive", namespace="eu"),
        ),
        ends=(
            diagram_objects.meta,
            names.meta,
            instance_set.meta,
            targeting_cim_data_object.meta,
            properties_cim_data_object.meta,
        ),
    )

    def __init__(
        self,
        *,
        alias_name: str | None = None,
        description: str | None = None,
        mrid: str | None = None,
        name: str | None = None,
        energy_ident_code_eic: str | None = None,
        short_name: str | None = None,
        diagram_objects: Iterable[DiagramObject] | None = None,
        names: Iterable[Name] | None = None,
        instance_set: InstanceSet | None = None,
        targeting_cim_data_object: Iterable[ChangeSetMember] | None = None,
        properties_cim_data_object: ChangeSetMember | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.alias_name = alias_name
        self.description = description
        self.mrid = new_mrid() if mrid is None else mrid
        self.name = name
        self.energy_ident_code_eic = energy_ident_code_eic
        self.short_name = short_name
        if diagram_objects is not None:
            IdentifiedObject.diagram_objects.extend(self, diagram_objects)
        if names is not None:
            IdentifiedObject.names.extend(self, names)
        if instance_set is not None:
            self.instance_set = instance_set
        if targeting_cim_data_object is not None:
            IdentifiedObject.targeting_cim_data_object.extend(self, targeting_cim_data_object)
        if properties_cim_data_object is not None:
            self.properties_cim_data_object = properties_cim_data_object

    def add_diagram_object(self, diagram_object: DiagramObject) -> Self:
        return IdentifiedObject.diagram_objects.add(self, diagram_object)

    def remove_diagram_object(self, diagram_object: DiagramObject) -> Self:
        return IdentifiedObject.diagram_objects.remove(self, diagram_object)

    def clear_diagram_objects(self) -> Self:
        return IdentifiedObject.diagram_objects.clear(self)

    def num_diagram_object(self) -> int:
        return IdentifiedObject.diagram_objects.count(self)

    def get_diagram_object_by_mrid(self, mrid: str) -> DiagramObject | None:
        return IdentifiedObject.diagram_objects.get_by_mrid(self, mrid)

    def add_names(self, names: Name) -> Self:
        return IdentifiedObject.names.add(self, names)

    def remove_names(self, names: Name) -> Self:
        return IdentifiedObject.names.remove(self, names)

    def clear_names(self) -> Self:
        return IdentifiedObject.names.clear(self)

    def num_names(self) -> int:
        return IdentifiedObject.names.count(self)

    def add_targeting_cim_data_object(self, targeting_cim_data_object: ChangeSetMember) -> Self:
        return IdentifiedObject.targeting_cim_data_object.add(self, targeting_cim_data_object)

    def remove_targeting_cim_data_object(self, targeting_cim_data_object: ChangeSetMember) -> Self:
        return IdentifiedObject.targeting_cim_data_object.remove(self, targeting_cim_data_object)

    def clear_targeting_cim_data_object(self) -> Self:
        return IdentifiedObject.targeting_cim_data_object.clear(self)

    def num_targeting_cim_data_object(self) -> int:
        return IdentifiedObject.targeting_cim_data_object.count(self)
