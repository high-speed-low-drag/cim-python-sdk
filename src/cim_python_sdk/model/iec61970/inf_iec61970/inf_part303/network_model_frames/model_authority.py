"""CIM class ModelAuthority (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_authority_set import (
        ModelAuthoritySet,
    )


class ModelAuthority(IdentifiedObject):
    """A Modeling Authority is an entity responsible for supplying and maintaining the data
    defining a specific set of objects in a network model."""

    __slots__ = ("_modeling_authority_sets",)

    modeling_authority_sets: Many[ModelAuthoritySet] = Many(
        EndMeta(
            name="modeling_authority_sets",
            cim_role="ModelingAuthoritySets",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_authority_set:ModelAuthoritySet",
            many=True,
            lower=1,
            upper=None,
            inverse="modeling_authority",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelAuthority",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{C2D644C3-20C1-408d-86F0-738AD512C121}",
        ends=(modeling_authority_sets.meta,),
    )

    def __init__(
        self,
        *,
        modeling_authority_sets: Iterable[ModelAuthoritySet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if modeling_authority_sets is not None:
            ModelAuthority.modeling_authority_sets.extend(self, modeling_authority_sets)

    def add_modeling_authority_set(self, modeling_authority_set: ModelAuthoritySet) -> Self:
        return ModelAuthority.modeling_authority_sets.add(self, modeling_authority_set)

    def remove_modeling_authority_set(self, modeling_authority_set: ModelAuthoritySet) -> Self:
        return ModelAuthority.modeling_authority_sets.remove(self, modeling_authority_set)

    def clear_modeling_authority_sets(self) -> Self:
        return ModelAuthority.modeling_authority_sets.clear(self)

    def num_modeling_authority_set(self) -> int:
        return ModelAuthority.modeling_authority_sets.count(self)

    def get_modeling_authority_set_by_mrid(self, mrid: str) -> ModelAuthoritySet | None:
        return ModelAuthority.modeling_authority_sets.get_by_mrid(self, mrid)
