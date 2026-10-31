"""CIM class AssetDiscrete (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.discrete import Discrete

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.test_standard import TestStandard


class AssetDiscrete(Discrete):
    """Definition of type of discrete useful in asset domain."""

    __slots__ = ("_test_standard",)

    test_standard: One[TestStandard] = One(
        EndMeta(
            name="test_standard",
            cim_role="TestStandard",
            target="cim_python_sdk.model.iec61968.assets.test_standard:TestStandard",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_discrete",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetDiscrete",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{7033E036-B936-481d-9868-D636510904E7}",
        ends=(test_standard.meta,),
    )

    def __init__(
        self,
        *,
        test_standard: TestStandard | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if test_standard is not None:
            self.test_standard = test_standard
