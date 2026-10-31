"""CIM class ObjectModification (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.change_set_member import (
    ChangeSetMember,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.object_reverse_modification import (
        ObjectReverseModification,
    )


class ObjectModification(ChangeSetMember):
    """The object already exists and is to be modified."""

    __slots__ = ("_object_reverse_modification",)

    object_reverse_modification: One[ObjectReverseModification] = One(
        EndMeta(
            name="object_reverse_modification",
            cim_role="ObjectReverseModification",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.object_reverse_modification:ObjectReverseModification",
            many=False,
            lower=0,
            upper=1,
            inverse="object_modification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ObjectModification",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{CBEFB19D-8A18-4e4e-8E97-E8A6669744B9}",
        ends=(object_reverse_modification.meta,),
    )

    def __init__(
        self,
        *,
        object_reverse_modification: ObjectReverseModification | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if object_reverse_modification is not None:
            self.object_reverse_modification = object_reverse_modification
