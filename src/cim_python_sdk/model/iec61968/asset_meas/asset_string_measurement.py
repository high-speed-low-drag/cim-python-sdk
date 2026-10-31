"""CIM class AssetStringMeasurement (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.string_measurement import StringMeasurement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.asset_string_kind import AssetStringKind
    from cim_python_sdk.model.iec61968.assets.test_standard import TestStandard


class AssetStringMeasurement(StringMeasurement):
    """Definition of type of string measurement useful in asset domain."""

    __slots__ = ("_test_standard", "kind")

    kind: AssetStringKind | None

    test_standard: One[TestStandard] = One(
        EndMeta(
            name="test_standard",
            cim_role="TestStandard",
            target="cim_python_sdk.model.iec61968.assets.test_standard:TestStandard",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_string",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetStringMeasurement",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{355C200B-C09D-451c-A775-875CA3DC724D}",
        attributes=(AttrMeta("kind", "kind", "AssetStringKind", 0, 1, "enumeration"),),
        ends=(test_standard.meta,),
    )

    def __init__(
        self,
        *,
        kind: AssetStringKind | None = None,
        test_standard: TestStandard | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if test_standard is not None:
            self.test_standard = test_standard
