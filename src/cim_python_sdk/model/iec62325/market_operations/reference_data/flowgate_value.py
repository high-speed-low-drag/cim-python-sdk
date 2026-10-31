"""CIM class FlowgateValue (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.flow_direction_type import (
        FlowDirectionType,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_partner import (
        FlowgatePartner,
    )


class FlowgateValue(CimObject):
    """Day Ahead, Network Native Load, Economic Dispatch, values used for calculation of
    Network Native Load (NNL) Determinator process."""

    __slots__ = (
        "_flowgate",
        "_flowgate_partner",
        "economic_dispatch_limit",
        "effective_date",
        "firm_network_limit",
        "flow_direction_flag",
        "mkt_flow",
        "net_firm_network_limit",
    )

    economic_dispatch_limit: int | None
    effective_date: _dt.datetime | None
    firm_network_limit: int | None
    flow_direction_flag: FlowDirectionType | None
    mkt_flow: int | None
    net_firm_network_limit: int | None

    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=1,
            upper=1,
            inverse="flowgate_value",
            aggregation="none",
        )
    )
    flowgate_partner: One[FlowgatePartner] = One(
        EndMeta(
            name="flowgate_partner",
            cim_role="FlowgatePartner",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate_partner:FlowgatePartner",
            many=False,
            lower=0,
            upper=1,
            inverse="flowgate_value",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FlowgateValue",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{16B3D002-934F-4986-B30C-96188561F813}",
        attributes=(
            AttrMeta("economic_dispatch_limit", "economicDispatchLimit", "int", 0, 1, "primitive"),
            AttrMeta("effective_date", "effectiveDate", "datetime", 0, 1, "primitive"),
            AttrMeta("firm_network_limit", "firmNetworkLimit", "int", 0, 1, "primitive"),
            AttrMeta(
                "flow_direction_flag", "flowDirectionFlag", "FlowDirectionType", 0, 1, "enumeration"
            ),
            AttrMeta("mkt_flow", "mktFlow", "int", 0, 1, "primitive"),
            AttrMeta("net_firm_network_limit", "netFirmNetworkLimit", "int", 0, 1, "primitive"),
        ),
        ends=(
            flowgate.meta,
            flowgate_partner.meta,
        ),
    )

    def __init__(
        self,
        *,
        economic_dispatch_limit: int | None = None,
        effective_date: _dt.datetime | None = None,
        firm_network_limit: int | None = None,
        flow_direction_flag: FlowDirectionType | None = None,
        mkt_flow: int | None = None,
        net_firm_network_limit: int | None = None,
        flowgate: Flowgate | None = None,
        flowgate_partner: FlowgatePartner | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.economic_dispatch_limit = economic_dispatch_limit
        self.effective_date = effective_date
        self.firm_network_limit = firm_network_limit
        self.flow_direction_flag = flow_direction_flag
        self.mkt_flow = mkt_flow
        self.net_firm_network_limit = net_firm_network_limit
        if flowgate is not None:
            self.flowgate = flowgate
        if flowgate_partner is not None:
            self.flowgate_partner = flowgate_partner
