"""CIM class Operation (TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_model_case_definition import (
        NetworkModelCaseDefinition,
    )


class Operation(CimObject):
    """CIM class Operation."""

    __slots__ = ("_network_model_case_definition",)

    network_model_case_definition: One[NetworkModelCaseDefinition] = One(
        EndMeta(
            name="network_model_case_definition",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.network_model_frames.network_model_case_definition:NetworkModelCaseDefinition",
            many=False,
            lower=1,
            upper=1,
            inverse="operations",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Operation",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/NetworkModelFrames",
        guid="{CCD5ED72-C1C1-4cd3-86DD-3BE1FE65BC5F}",
        ends=(network_model_case_definition.meta,),
    )

    def __init__(
        self,
        *,
        network_model_case_definition: NetworkModelCaseDefinition | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if network_model_case_definition is not None:
            self.network_model_case_definition = network_model_case_definition
