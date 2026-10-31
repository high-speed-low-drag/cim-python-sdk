"""CIM class TestStandard (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_meas.asset_analog import AssetAnalog
    from cim_python_sdk.model.iec61968.asset_meas.asset_discrete import AssetDiscrete
    from cim_python_sdk.model.iec61968.asset_meas.asset_string_measurement import (
        AssetStringMeasurement,
    )
    from cim_python_sdk.model.iec61968.assets.astm_standard import ASTMStandard
    from cim_python_sdk.model.iec61968.assets.cigre_standard import CIGREStandard
    from cim_python_sdk.model.iec61968.assets.din_standard import DINStandard
    from cim_python_sdk.model.iec61968.assets.doble_standard import DobleStandard
    from cim_python_sdk.model.iec61968.assets.epa_standard import EPAStandard
    from cim_python_sdk.model.iec61968.assets.iec_standard import IECStandard
    from cim_python_sdk.model.iec61968.assets.ieee_standard import IEEEStandard
    from cim_python_sdk.model.iec61968.assets.iso_standard import ISOStandard
    from cim_python_sdk.model.iec61968.assets.laborelec_standard import LaborelecStandard
    from cim_python_sdk.model.iec61968.assets.tappi_standard import TAPPIStandard
    from cim_python_sdk.model.iec61968.assets.test_method import TestMethod
    from cim_python_sdk.model.iec61968.assets.test_variant_kind import TestVariantKind
    from cim_python_sdk.model.iec61968.assets.uk_ministry_of_defence_standard import (
        UKMinistryOfDefenceStandard,
    )
    from cim_python_sdk.model.iec61968.assets.wep_standard import WEPStandard


class TestStandard(IdentifiedObject):
    """The precise standard used in executing a lab test, including the standard, and standard
    version, test method and variant, if needed."""

    __slots__ = (
        "_asset_analog",
        "_asset_discrete",
        "_asset_string",
        "test_method",
        "test_standard_astm",
        "test_standard_cigre",
        "test_standard_din",
        "test_standard_doble",
        "test_standard_epa",
        "test_standard_iec",
        "test_standard_ieee",
        "test_standard_iso",
        "test_standard_laborelec",
        "test_standard_tappi",
        "test_standard_uk_ministry_of_defence",
        "test_standard_wep",
        "test_variant",
    )

    test_standard_astm: ASTMStandard | None
    test_standard_cigre: CIGREStandard | None
    test_standard_din: DINStandard | None
    test_standard_doble: DobleStandard | None
    test_standard_epa: EPAStandard | None
    test_standard_iec: IECStandard | None
    test_standard_ieee: IEEEStandard | None
    test_standard_iso: ISOStandard | None
    test_standard_laborelec: LaborelecStandard | None
    test_standard_tappi: TAPPIStandard | None
    test_standard_uk_ministry_of_defence: UKMinistryOfDefenceStandard | None
    test_standard_wep: WEPStandard | None
    test_method: TestMethod | None
    test_variant: TestVariantKind | None

    asset_string: Many[AssetStringMeasurement] = Many(
        EndMeta(
            name="asset_string",
            cim_role="AssetString",
            target="cim_python_sdk.model.iec61968.asset_meas.asset_string_measurement:AssetStringMeasurement",
            many=True,
            lower=0,
            upper=None,
            inverse="test_standard",
            aggregation="none",
        )
    )
    asset_analog: Many[AssetAnalog] = Many(
        EndMeta(
            name="asset_analog",
            cim_role="AssetAnalog",
            target="cim_python_sdk.model.iec61968.asset_meas.asset_analog:AssetAnalog",
            many=True,
            lower=0,
            upper=None,
            inverse="test_standard",
            aggregation="none",
        )
    )
    asset_discrete: Many[AssetDiscrete] = Many(
        EndMeta(
            name="asset_discrete",
            cim_role="AssetDiscrete",
            target="cim_python_sdk.model.iec61968.asset_meas.asset_discrete:AssetDiscrete",
            many=True,
            lower=0,
            upper=None,
            inverse="test_standard",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TestStandard",
        package="TC57CIM/IEC61968/Assets",
        guid="{D1CACECC-8319-4326-9871-BD2DB19CA4CB}",
        attributes=(
            AttrMeta("test_standard_astm", "testStandardASTM", "ASTMStandard", 0, 1, "compound"),
            AttrMeta("test_standard_cigre", "testStandardCIGRE", "CIGREStandard", 0, 1, "compound"),
            AttrMeta("test_standard_din", "testStandardDIN", "DINStandard", 0, 1, "compound"),
            AttrMeta("test_standard_doble", "testStandardDoble", "DobleStandard", 0, 1, "compound"),
            AttrMeta("test_standard_epa", "testStandardEPA", "EPAStandard", 0, 1, "compound"),
            AttrMeta("test_standard_iec", "testStandardIEC", "IECStandard", 0, 1, "compound"),
            AttrMeta("test_standard_ieee", "testStandardIEEE", "IEEEStandard", 0, 1, "compound"),
            AttrMeta("test_standard_iso", "testStandardISO", "ISOStandard", 0, 1, "compound"),
            AttrMeta(
                "test_standard_laborelec",
                "testStandardLaborelec",
                "LaborelecStandard",
                0,
                1,
                "compound",
            ),
            AttrMeta("test_standard_tappi", "testStandardTAPPI", "TAPPIStandard", 0, 1, "compound"),
            AttrMeta(
                "test_standard_uk_ministry_of_defence",
                "testStandardUKMinistryOfDefence",
                "UKMinistryOfDefenceStandard",
                0,
                1,
                "compound",
            ),
            AttrMeta("test_standard_wep", "testStandardWEP", "WEPStandard", 0, 1, "compound"),
            AttrMeta("test_method", "testMethod", "TestMethod", 0, 1, "enumeration"),
            AttrMeta("test_variant", "testVariant", "TestVariantKind", 0, 1, "enumeration"),
        ),
        ends=(
            asset_string.meta,
            asset_analog.meta,
            asset_discrete.meta,
        ),
    )

    def __init__(
        self,
        *,
        test_standard_astm: ASTMStandard | None = None,
        test_standard_cigre: CIGREStandard | None = None,
        test_standard_din: DINStandard | None = None,
        test_standard_doble: DobleStandard | None = None,
        test_standard_epa: EPAStandard | None = None,
        test_standard_iec: IECStandard | None = None,
        test_standard_ieee: IEEEStandard | None = None,
        test_standard_iso: ISOStandard | None = None,
        test_standard_laborelec: LaborelecStandard | None = None,
        test_standard_tappi: TAPPIStandard | None = None,
        test_standard_uk_ministry_of_defence: UKMinistryOfDefenceStandard | None = None,
        test_standard_wep: WEPStandard | None = None,
        test_method: TestMethod | None = None,
        test_variant: TestVariantKind | None = None,
        asset_string: Iterable[AssetStringMeasurement] | None = None,
        asset_analog: Iterable[AssetAnalog] | None = None,
        asset_discrete: Iterable[AssetDiscrete] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.test_standard_astm = test_standard_astm
        self.test_standard_cigre = test_standard_cigre
        self.test_standard_din = test_standard_din
        self.test_standard_doble = test_standard_doble
        self.test_standard_epa = test_standard_epa
        self.test_standard_iec = test_standard_iec
        self.test_standard_ieee = test_standard_ieee
        self.test_standard_iso = test_standard_iso
        self.test_standard_laborelec = test_standard_laborelec
        self.test_standard_tappi = test_standard_tappi
        self.test_standard_uk_ministry_of_defence = test_standard_uk_ministry_of_defence
        self.test_standard_wep = test_standard_wep
        self.test_method = test_method
        self.test_variant = test_variant
        if asset_string is not None:
            TestStandard.asset_string.extend(self, asset_string)
        if asset_analog is not None:
            TestStandard.asset_analog.extend(self, asset_analog)
        if asset_discrete is not None:
            TestStandard.asset_discrete.extend(self, asset_discrete)

    def add_asset_string(self, asset_string: AssetStringMeasurement) -> Self:
        return TestStandard.asset_string.add(self, asset_string)

    def remove_asset_string(self, asset_string: AssetStringMeasurement) -> Self:
        return TestStandard.asset_string.remove(self, asset_string)

    def clear_asset_string(self) -> Self:
        return TestStandard.asset_string.clear(self)

    def num_asset_string(self) -> int:
        return TestStandard.asset_string.count(self)

    def get_asset_string_by_mrid(self, mrid: str) -> AssetStringMeasurement | None:
        return TestStandard.asset_string.get_by_mrid(self, mrid)

    def add_asset_analog(self, asset_analog: AssetAnalog) -> Self:
        return TestStandard.asset_analog.add(self, asset_analog)

    def remove_asset_analog(self, asset_analog: AssetAnalog) -> Self:
        return TestStandard.asset_analog.remove(self, asset_analog)

    def clear_asset_analog(self) -> Self:
        return TestStandard.asset_analog.clear(self)

    def num_asset_analog(self) -> int:
        return TestStandard.asset_analog.count(self)

    def get_asset_analog_by_mrid(self, mrid: str) -> AssetAnalog | None:
        return TestStandard.asset_analog.get_by_mrid(self, mrid)

    def add_asset_discrete(self, asset_discrete: AssetDiscrete) -> Self:
        return TestStandard.asset_discrete.add(self, asset_discrete)

    def remove_asset_discrete(self, asset_discrete: AssetDiscrete) -> Self:
        return TestStandard.asset_discrete.remove(self, asset_discrete)

    def clear_asset_discrete(self) -> Self:
        return TestStandard.asset_discrete.clear(self)

    def num_asset_discrete(self) -> int:
        return TestStandard.asset_discrete.count(self)

    def get_asset_discrete_by_mrid(self, mrid: str) -> AssetDiscrete | None:
        return TestStandard.asset_discrete.get_by_mrid(self, mrid)
