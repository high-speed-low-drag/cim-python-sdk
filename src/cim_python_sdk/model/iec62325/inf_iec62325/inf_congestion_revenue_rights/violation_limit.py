"""CIM class ViolationLimit (TC57CIM/IEC62325/InfIEC62325/InfCongestionRevenueRights). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.limit import Limit

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement import (
        MktMeasurement,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class ViolationLimit(Limit):
    """A type of limit that indicates if it is enforced and, through association, the
    organisation responsible for setting the limit."""

    __slots__ = ("_flowgate", "_mkt_measurement", "enforced")

    enforced: bool | None

    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="violation_limits",
            aggregation="none",
        )
    )
    mkt_measurement: One[MktMeasurement] = One(
        EndMeta(
            name="mkt_measurement",
            cim_role="MktMeasurement",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_measurement:MktMeasurement",
            many=False,
            lower=0,
            upper=1,
            inverse="violation_limit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ViolationLimit",
        package="TC57CIM/IEC62325/InfIEC62325/InfCongestionRevenueRights",
        guid="{77CA79D6-C66C-4a28-9AC8-7779395E8416}",
        attributes=(AttrMeta("enforced", "enforced", "bool", 0, 1, "primitive"),),
        ends=(
            flowgate.meta,
            mkt_measurement.meta,
        ),
    )

    def __init__(
        self,
        *,
        enforced: bool | None = None,
        flowgate: Flowgate | None = None,
        mkt_measurement: MktMeasurement | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.enforced = enforced
        if flowgate is not None:
            self.flowgate = flowgate
        if mkt_measurement is not None:
            self.mkt_measurement = mkt_measurement
