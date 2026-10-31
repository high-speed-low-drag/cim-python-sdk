"""CIM class ModelAuthoritySet (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_authority import (
        ModelAuthority,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_specification import (
        ModelPartSpecification,
    )


class ModelAuthoritySet(IdentifiedObject):
    """A Modeling Authority Set is a group of objects in a network model where the data is
    supplied and maintained by the same Modeling Authority.

    This class is typically not included in instance data exchange as this information is
    tracked by other mechanisms in the exchange."""

    __slots__ = ("_model_specification", "_modeling_authority")

    modeling_authority: One[ModelAuthority] = One(
        EndMeta(
            name="modeling_authority",
            cim_role="ModelingAuthority",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_authority:ModelAuthority",
            many=False,
            lower=1,
            upper=1,
            inverse="modeling_authority_sets",
            aggregation="none",
        )
    )
    model_specification: Many[ModelPartSpecification] = Many(
        EndMeta(
            name="model_specification",
            cim_role="ModelSpecification",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.model_part_specification:ModelPartSpecification",
            many=True,
            lower=0,
            upper=None,
            inverse="framework_part",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ModelAuthoritySet",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{6D6E62ED-DCB6-4e54-9159-8469729C9828}",
        ends=(
            modeling_authority.meta,
            model_specification.meta,
        ),
    )

    def __init__(
        self,
        *,
        modeling_authority: ModelAuthority | None = None,
        model_specification: Iterable[ModelPartSpecification] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if modeling_authority is not None:
            self.modeling_authority = modeling_authority
        if model_specification is not None:
            ModelAuthoritySet.model_specification.extend(self, model_specification)

    def add_model_specification(self, model_specification: ModelPartSpecification) -> Self:
        return ModelAuthoritySet.model_specification.add(self, model_specification)

    def remove_model_specification(self, model_specification: ModelPartSpecification) -> Self:
        return ModelAuthoritySet.model_specification.remove(self, model_specification)

    def clear_model_specification(self) -> Self:
        return ModelAuthoritySet.model_specification.clear(self)

    def num_model_specification(self) -> int:
        return ModelAuthoritySet.model_specification.count(self)

    def get_model_specification_by_mrid(self, mrid: str) -> ModelPartSpecification | None:
        return ModelAuthoritySet.model_specification.get_by_mrid(self, mrid)
