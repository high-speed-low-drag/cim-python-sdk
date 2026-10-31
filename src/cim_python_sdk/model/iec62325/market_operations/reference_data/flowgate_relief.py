"""CIM class FlowgateRelief (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class FlowgateRelief(CimObject):
    """IDC (Interchange Distribution Calulator) sends data for a TLR (Transmission Loading
    Relief)."""

    __slots__ = ("_flowgate", "effective_date", "idc_target_mkt_flow", "terminate_date")

    effective_date: _dt.datetime | None
    terminate_date: _dt.datetime | None
    idc_target_mkt_flow: int | None

    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=1,
            upper=1,
            inverse="flowgate_relief",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FlowgateRelief",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{B419B7DC-C747-4501-95FF-E94F159157D8}",
        attributes=(
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("terminate_date", "terminateDate", "datetime", 0, 1, "primitive"),
            AttrMeta("idc_target_mkt_flow", "idcTargetMktFlow", "int", 0, 1, "primitive"),
        ),
        ends=(flowgate.meta,),
    )

    def __init__(
        self,
        *,
        effective_date: _dt.datetime | None = None,
        terminate_date: _dt.datetime | None = None,
        idc_target_mkt_flow: int | None = None,
        flowgate: Flowgate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.effective_date = effective_date
        self.terminate_date = terminate_date
        self.idc_target_mkt_flow = idc_target_mkt_flow
        if flowgate is not None:
            self.flowgate = flowgate
