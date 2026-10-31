"""CIM class Channel (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.reading_type import ReadingType
    from cim_python_sdk.model.iec61968.metering.register import Register


class Channel(IdentifiedObject):
    """A single path for the collection or reporting of register values over a period of time.
    For example, a register which measures forward energy can have two channels, one
    providing bulk quantity readings and the other providing interval readings of a fixed
    interval size."""

    __slots__ = ("_reading_type", "_register", "is_virtual")

    is_virtual: bool | None

    register: One[Register] = One(
        EndMeta(
            name="register",
            cim_role="Register",
            target="cim_python_sdk.model.iec61968.metering.register:Register",
            many=False,
            lower=0,
            upper=1,
            inverse="channels",
            aggregation="none",
        )
    )
    reading_type: One[ReadingType] = One(
        EndMeta(
            name="reading_type",
            cim_role="ReadingType",
            target="cim_python_sdk.model.iec61968.metering.reading_type:ReadingType",
            many=False,
            lower=0,
            upper=1,
            inverse="channel",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Channel",
        package="TC57CIM/IEC61968/Metering",
        guid="{EACF932A-D491-416b-9507-B0D9ED77CC37}",
        attributes=(AttrMeta("is_virtual", "isVirtual", "bool", 0, 1, "primitive"),),
        ends=(
            register.meta,
            reading_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        is_virtual: bool | None = None,
        register: Register | None = None,
        reading_type: ReadingType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_virtual = is_virtual
        if register is not None:
            self.register = register
        if reading_type is not None:
            self.reading_type = reading_type
