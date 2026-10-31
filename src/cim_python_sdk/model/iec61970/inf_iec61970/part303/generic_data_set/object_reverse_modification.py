"""CIM class ObjectReverseModification (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set_member import (
    ChangeSetMember,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.object_modification import (
        ObjectModification,
    )


class ObjectReverseModification(ChangeSetMember):
    """Used to specify precondition properties for a preconditioned update."""

    __slots__ = ("_object_modification",)

    object_modification: One[ObjectModification] = One(
        EndMeta(
            name="object_modification",
            cim_role="ObjectModification",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.object_modification:ObjectModification",
            many=False,
            lower=0,
            upper=1,
            inverse="object_reverse_modification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ObjectReverseModification",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{1EB8623A-48DC-441d-A6CB-BFDEE6F305FA}",
        ends=(object_modification.meta,),
    )

    def __init__(
        self,
        *,
        object_modification: ObjectModification | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if object_modification is not None:
            self.object_modification = object_modification
