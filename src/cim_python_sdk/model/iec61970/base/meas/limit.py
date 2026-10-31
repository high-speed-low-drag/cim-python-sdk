"""CIM class Limit (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.procedure import Procedure


class Limit(IdentifiedObject):
    """Specifies one limit value for a Measurement. A Measurement typically has several limits
    that are kept together by the LimitSet class. The actual meaning and use of a Limit
    instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is
    not captured in the Limit class. However the name of a Limit instance may indicate both
    meaning and use."""

    __slots__ = ("_procedures",)

    procedures: Many[Procedure] = Many(
        EndMeta(
            name="procedures",
            cim_role="Procedures",
            target="cim_python_sdk.model.iec61968.assets.procedure:Procedure",
            many=True,
            lower=0,
            upper=None,
            inverse="limits",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Limit",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{ED3F9694-F2AC-43af-B3CA-57395E31AD94}",
        ends=(procedures.meta,),
    )

    def __init__(
        self,
        *,
        procedures: Iterable[Procedure] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if procedures is not None:
            Limit.procedures.extend(self, procedures)

    def add_procedure(self, procedure: Procedure) -> Self:
        return Limit.procedures.add(self, procedure)

    def remove_procedure(self, procedure: Procedure) -> Self:
        return Limit.procedures.remove(self, procedure)

    def clear_procedures(self) -> Self:
        return Limit.procedures.clear(self)

    def num_procedure(self) -> int:
        return Limit.procedures.count(self)

    def get_procedure_by_mrid(self, mrid: str) -> Procedure | None:
        return Limit.procedures.get_by_mrid(self, mrid)
