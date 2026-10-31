"""CIM class AlternateModelGroup (TC57CIM/IEC61970/InfIEC61970/InfPart303/AlternateModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.alternate_models.alternate_model import (
        AlternateModel,
    )


class AlternateModelGroup(IdentifiedObject):
    """CIM class AlternateModelGroup."""

    __slots__ = ("_alternate_model",)

    alternate_model: Many[AlternateModel] = Many(
        EndMeta(
            name="alternate_model",
            cim_role="AlternateModel",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.alternate_models.alternate_model:AlternateModel",
            many=True,
            lower=0,
            upper=None,
            inverse="alternate_model_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AlternateModelGroup",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/AlternateModels",
        guid="{E0956F63-50B6-4390-91B4-2E1194FB9B0D}",
        ends=(alternate_model.meta,),
    )

    def __init__(
        self,
        *,
        alternate_model: Iterable[AlternateModel] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if alternate_model is not None:
            AlternateModelGroup.alternate_model.extend(self, alternate_model)

    def add_alternate_model(self, alternate_model: AlternateModel) -> Self:
        return AlternateModelGroup.alternate_model.add(self, alternate_model)

    def remove_alternate_model(self, alternate_model: AlternateModel) -> Self:
        return AlternateModelGroup.alternate_model.remove(self, alternate_model)

    def clear_alternate_model(self) -> Self:
        return AlternateModelGroup.alternate_model.clear(self)

    def num_alternate_model(self) -> int:
        return AlternateModelGroup.alternate_model.count(self)

    def get_alternate_model_by_mrid(self, mrid: str) -> AlternateModel | None:
        return AlternateModelGroup.alternate_model.get_by_mrid(self, mrid)
