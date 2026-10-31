"""CIM class BushingInsulationPF (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.bushing import Bushing
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.bushing_insulation_pf_test_kind import (
        BushingInsulationPfTestKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation import (
        TransformerObservation,
    )


class BushingInsulationPF(IdentifiedObject):
    """Bushing insulation power factor condition as a result of a test.

    Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major
    Deterioration or Moisture Absorption, Failed."""

    __slots__ = ("_bushing", "_transformer_observation", "status", "test_kind")

    test_kind: BushingInsulationPfTestKind | None
    status: Status | None

    bushing: One[Bushing] = One(
        EndMeta(
            name="bushing",
            cim_role="Bushing",
            target="cim_python_sdk.model.iec61968.assets.bushing:Bushing",
            many=False,
            lower=0,
            upper=1,
            inverse="bushing_insulation_pfs",
            aggregation="none",
        )
    )
    transformer_observation: One[TransformerObservation] = One(
        EndMeta(
            name="transformer_observation",
            cim_role="TransformerObservation",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation:TransformerObservation",
            many=False,
            lower=0,
            upper=1,
            inverse="bushing_insultation_pfs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BushingInsulationPF",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{86C23E36-C99E-40d6-867B-C28F0EEEA996}",
        attributes=(
            AttrMeta("test_kind", "testKind", "BushingInsulationPfTestKind", 0, 1, "enumeration"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            bushing.meta,
            transformer_observation.meta,
        ),
    )

    def __init__(
        self,
        *,
        test_kind: BushingInsulationPfTestKind | None = None,
        status: Status | None = None,
        bushing: Bushing | None = None,
        transformer_observation: TransformerObservation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.test_kind = test_kind
        self.status = status
        if bushing is not None:
            self.bushing = bushing
        if transformer_observation is not None:
            self.transformer_observation = transformer_observation
