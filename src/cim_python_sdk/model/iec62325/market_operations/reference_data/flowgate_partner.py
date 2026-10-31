"""CIM class FlowgatePartner (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_value import (
        FlowgateValue,
    )


class FlowgatePartner(IdentifiedObject):
    """Flowgate defined partner."""

    __slots__ = ("_flowgate_value",)

    flowgate_value: One[FlowgateValue] = One(
        EndMeta(
            name="flowgate_value",
            cim_role="FlowgateValue",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_value:FlowgateValue",
            many=False,
            lower=0,
            upper=1,
            inverse="flowgate_partner",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FlowgatePartner",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{54949507-20B9-4135-B5B6-7D373BE45C8B}",
        ends=(flowgate_value.meta,),
    )

    def __init__(
        self,
        *,
        flowgate_value: FlowgateValue | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if flowgate_value is not None:
            self.flowgate_value = flowgate_value
