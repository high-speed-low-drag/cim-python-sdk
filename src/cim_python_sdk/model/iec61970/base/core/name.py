"""CIM class Name (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject
    from cim_python_sdk.model.iec61970.base.core.name_type import NameType


class Name(CimObject):
    """The Name class provides the means to define any number of human readable names for an
    object. A name is not to be used for defining inter-object relationships. For
    inter-object relationships instead use the object identification 'mRID'."""

    __slots__ = ("_identified_object", "_name_type", "name")

    name: str | None

    identified_object: One[IdentifiedObject] = One(
        EndMeta(
            name="identified_object",
            cim_role="IdentifiedObject",
            target="cim_python_sdk.model.iec61970.base.core.identified_object:IdentifiedObject",
            many=False,
            lower=1,
            upper=1,
            inverse="names",
            aggregation="none",
        )
    )
    name_type: One[NameType] = One(
        EndMeta(
            name="name_type",
            cim_role="NameType",
            target="cim_python_sdk.model.iec61970.base.core.name_type:NameType",
            many=False,
            lower=1,
            upper=1,
            inverse="names",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Name",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{D6F3DF4E-3363-48d2-AB61-7872E337C422}",
        attributes=(AttrMeta("name", "name", "str", 0, 1, "primitive"),),
        ends=(
            identified_object.meta,
            name_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        name: str | None = None,
        identified_object: IdentifiedObject | None = None,
        name_type: NameType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        if identified_object is not None:
            self.identified_object = identified_object
        if name_type is not None:
            self.name_type = name_type
