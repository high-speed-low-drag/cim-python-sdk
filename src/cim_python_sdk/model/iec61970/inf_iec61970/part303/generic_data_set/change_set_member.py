"""CIM class ChangeSetMember (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set import (
        ChangeSet,
    )


class ChangeSetMember(CimObject):
    """A CRUD-style data object."""

    __slots__ = ("_changeset", "_properties_object", "_target_object")

    target_object: One[IdentifiedObject] = One(
        EndMeta(
            name="target_object",
            cim_role="TargetObject",
            target="cim_python_sdk.model.iec61970.base.core.identified_object:IdentifiedObject",
            many=False,
            lower=1,
            upper=1,
            inverse="targeting_cim_data_object",
            aggregation="none",
        )
    )
    changeset: One[ChangeSet] = One(
        EndMeta(
            name="changeset",
            cim_role="Changeset",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set:ChangeSet",
            many=False,
            lower=0,
            upper=1,
            inverse="change_set_member",
            aggregation="none",
        )
    )
    properties_object: One[IdentifiedObject] = One(
        EndMeta(
            name="properties_object",
            cim_role="PropertiesObject",
            target="cim_python_sdk.model.iec61970.base.core.identified_object:IdentifiedObject",
            many=False,
            lower=0,
            upper=1,
            inverse="properties_cim_data_object",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ChangeSetMember",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{B579C575-1165-4e6c-AFEF-991BBA193E2B}",
        ends=(
            target_object.meta,
            changeset.meta,
            properties_object.meta,
        ),
    )

    def __init__(
        self,
        *,
        target_object: IdentifiedObject | None = None,
        changeset: ChangeSet | None = None,
        properties_object: IdentifiedObject | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if target_object is not None:
            self.target_object = target_object
        if changeset is not None:
            self.changeset = changeset
        if properties_object is not None:
            self.properties_object = properties_object
