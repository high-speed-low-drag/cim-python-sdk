"""CIM class EnvironmentalDiscrete (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.discrete import Discrete

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.env_domain.environmental_discrete_kind import (
        EnvironmentalDiscreteKind,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_information import (
        EnvironmentalInformation,
    )


class EnvironmentalDiscrete(Discrete):
    """Discrete (integer) measurement of relevance in the environmental domain."""

    __slots__ = ("_environmental_information", "kind")

    kind: EnvironmentalDiscreteKind | None

    environmental_information: One[EnvironmentalInformation] = One(
        EndMeta(
            name="environmental_information",
            cim_role="EnvironmentalInformation",
            target="cim_python_sdk.model.iec62325.environmental.environmental_information:EnvironmentalInformation",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_discrete",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalDiscrete",
        package="TC57CIM/IEC62325/Environmental",
        guid="{B5D41EB6-5CB8-4f32-81DE-854FC340F244}",
        attributes=(AttrMeta("kind", "kind", "EnvironmentalDiscreteKind", 1, 1, "enumeration"),),
        ends=(environmental_information.meta,),
    )

    def __init__(
        self,
        *,
        kind: EnvironmentalDiscreteKind | None = None,
        environmental_information: EnvironmentalInformation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if environmental_information is not None:
            self.environmental_information = environmental_information
