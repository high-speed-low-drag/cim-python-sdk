"""CIM class TransformerEndInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.no_load_test import NoLoadTest
    from cim_python_sdk.model.iec61968.asset_info.open_circuit_test import OpenCircuitTest
    from cim_python_sdk.model.iec61968.asset_info.short_circuit_test import ShortCircuitTest
    from cim_python_sdk.model.iec61968.asset_info.transformer_tank_info import TransformerTankInfo
    from cim_python_sdk.model.iec61970.base.wires.transformer_core_admittance import (
        TransformerCoreAdmittance,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_mesh_impedance import (
        TransformerMeshImpedance,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_star_impedance import (
        TransformerStarImpedance,
    )
    from cim_python_sdk.model.iec61970.base.wires.winding_connection import WindingConnection


class TransformerEndInfo(AssetInfo):
    """Transformer end data."""

    __slots__ = (
        "_core_admittance",
        "_energised_end_no_load_tests",
        "_energised_end_open_circuit_tests",
        "_energised_end_short_circuit_tests",
        "_from_mesh_impedances",
        "_grounded_end_short_circuit_tests",
        "_open_end_open_circuit_tests",
        "_to_mesh_impedances",
        "_transformer_star_impedance",
        "_transformer_tank_info",
        "connection_kind",
        "emergency_s",
        "end_number",
        "insulation_u",
        "phase_angle_clock",
        "r",
        "rated_s",
        "rated_u",
        "short_term_s",
    )

    end_number: int | None
    phase_angle_clock: int | None
    connection_kind: WindingConnection | None
    r: float | None  # Resistance
    rated_u: float | None  # Voltage
    insulation_u: float | None  # Voltage
    rated_s: float | None  # ApparentPower
    emergency_s: float | None  # ApparentPower
    short_term_s: float | None  # ApparentPower

    energised_end_short_circuit_tests: Many[ShortCircuitTest] = Many(
        EndMeta(
            name="energised_end_short_circuit_tests",
            cim_role="EnergisedEndShortCircuitTests",
            target="cim_python_sdk.model.iec61968.asset_info.short_circuit_test:ShortCircuitTest",
            many=True,
            lower=0,
            upper=None,
            inverse="energised_end",
            aggregation="none",
        )
    )
    to_mesh_impedances: Many[TransformerMeshImpedance] = Many(
        EndMeta(
            name="to_mesh_impedances",
            cim_role="ToMeshImpedances",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_mesh_impedance:TransformerMeshImpedance",
            many=True,
            lower=0,
            upper=None,
            inverse="to_transformer_end_infos",
            aggregation="none",
        )
    )
    transformer_tank_info: One[TransformerTankInfo] = One(
        EndMeta(
            name="transformer_tank_info",
            cim_role="TransformerTankInfo",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_tank_info:TransformerTankInfo",
            many=False,
            lower=1,
            upper=1,
            inverse="transformer_end_infos",
            aggregation="none",
        )
    )
    transformer_star_impedance: One[TransformerStarImpedance] = One(
        EndMeta(
            name="transformer_star_impedance",
            cim_role="TransformerStarImpedance",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_star_impedance:TransformerStarImpedance",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_end_info",
            aggregation="none",
        )
    )
    energised_end_open_circuit_tests: Many[OpenCircuitTest] = Many(
        EndMeta(
            name="energised_end_open_circuit_tests",
            cim_role="EnergisedEndOpenCircuitTests",
            target="cim_python_sdk.model.iec61968.asset_info.open_circuit_test:OpenCircuitTest",
            many=True,
            lower=0,
            upper=None,
            inverse="energised_end",
            aggregation="none",
        )
    )
    from_mesh_impedances: Many[TransformerMeshImpedance] = Many(
        EndMeta(
            name="from_mesh_impedances",
            cim_role="FromMeshImpedances",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_mesh_impedance:TransformerMeshImpedance",
            many=True,
            lower=0,
            upper=None,
            inverse="from_transformer_end_info",
            aggregation="none",
        )
    )
    open_end_open_circuit_tests: Many[OpenCircuitTest] = Many(
        EndMeta(
            name="open_end_open_circuit_tests",
            cim_role="OpenEndOpenCircuitTests",
            target="cim_python_sdk.model.iec61968.asset_info.open_circuit_test:OpenCircuitTest",
            many=True,
            lower=0,
            upper=None,
            inverse="open_end",
            aggregation="none",
        )
    )
    core_admittance: One[TransformerCoreAdmittance] = One(
        EndMeta(
            name="core_admittance",
            cim_role="CoreAdmittance",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_core_admittance:TransformerCoreAdmittance",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_end_info",
            aggregation="none",
        )
    )
    grounded_end_short_circuit_tests: Many[ShortCircuitTest] = Many(
        EndMeta(
            name="grounded_end_short_circuit_tests",
            cim_role="GroundedEndShortCircuitTests",
            target="cim_python_sdk.model.iec61968.asset_info.short_circuit_test:ShortCircuitTest",
            many=True,
            lower=0,
            upper=None,
            inverse="grounded_ends",
            aggregation="none",
        )
    )
    energised_end_no_load_tests: Many[NoLoadTest] = Many(
        EndMeta(
            name="energised_end_no_load_tests",
            cim_role="EnergisedEndNoLoadTests",
            target="cim_python_sdk.model.iec61968.asset_info.no_load_test:NoLoadTest",
            many=True,
            lower=0,
            upper=None,
            inverse="energised_end",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerEndInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{EE451097-1E73-4a48-98F7-5558C8D4D5AB}",
        attributes=(
            AttrMeta("end_number", "endNumber", "int", 0, 1, "primitive"),
            AttrMeta("phase_angle_clock", "phaseAngleClock", "int", 0, 1, "primitive"),
            AttrMeta("connection_kind", "connectionKind", "WindingConnection", 0, 1, "enumeration"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("rated_u", "ratedU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("insulation_u", "insulationU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("rated_s", "ratedS", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("emergency_s", "emergencyS", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("short_term_s", "shortTermS", "ApparentPower", 0, 1, "cimdatatype"),
        ),
        ends=(
            energised_end_short_circuit_tests.meta,
            to_mesh_impedances.meta,
            transformer_tank_info.meta,
            transformer_star_impedance.meta,
            energised_end_open_circuit_tests.meta,
            from_mesh_impedances.meta,
            open_end_open_circuit_tests.meta,
            core_admittance.meta,
            grounded_end_short_circuit_tests.meta,
            energised_end_no_load_tests.meta,
        ),
    )

    def __init__(
        self,
        *,
        end_number: int | None = None,
        phase_angle_clock: int | None = None,
        connection_kind: WindingConnection | None = None,
        r: float | None = None,
        rated_u: float | None = None,
        insulation_u: float | None = None,
        rated_s: float | None = None,
        emergency_s: float | None = None,
        short_term_s: float | None = None,
        energised_end_short_circuit_tests: Iterable[ShortCircuitTest] | None = None,
        to_mesh_impedances: Iterable[TransformerMeshImpedance] | None = None,
        transformer_tank_info: TransformerTankInfo | None = None,
        transformer_star_impedance: TransformerStarImpedance | None = None,
        energised_end_open_circuit_tests: Iterable[OpenCircuitTest] | None = None,
        from_mesh_impedances: Iterable[TransformerMeshImpedance] | None = None,
        open_end_open_circuit_tests: Iterable[OpenCircuitTest] | None = None,
        core_admittance: TransformerCoreAdmittance | None = None,
        grounded_end_short_circuit_tests: Iterable[ShortCircuitTest] | None = None,
        energised_end_no_load_tests: Iterable[NoLoadTest] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.end_number = end_number
        self.phase_angle_clock = phase_angle_clock
        self.connection_kind = connection_kind
        self.r = r
        self.rated_u = rated_u
        self.insulation_u = insulation_u
        self.rated_s = rated_s
        self.emergency_s = emergency_s
        self.short_term_s = short_term_s
        if energised_end_short_circuit_tests is not None:
            TransformerEndInfo.energised_end_short_circuit_tests.extend(
                self, energised_end_short_circuit_tests
            )
        if to_mesh_impedances is not None:
            TransformerEndInfo.to_mesh_impedances.extend(self, to_mesh_impedances)
        if transformer_tank_info is not None:
            self.transformer_tank_info = transformer_tank_info
        if transformer_star_impedance is not None:
            self.transformer_star_impedance = transformer_star_impedance
        if energised_end_open_circuit_tests is not None:
            TransformerEndInfo.energised_end_open_circuit_tests.extend(
                self, energised_end_open_circuit_tests
            )
        if from_mesh_impedances is not None:
            TransformerEndInfo.from_mesh_impedances.extend(self, from_mesh_impedances)
        if open_end_open_circuit_tests is not None:
            TransformerEndInfo.open_end_open_circuit_tests.extend(self, open_end_open_circuit_tests)
        if core_admittance is not None:
            self.core_admittance = core_admittance
        if grounded_end_short_circuit_tests is not None:
            TransformerEndInfo.grounded_end_short_circuit_tests.extend(
                self, grounded_end_short_circuit_tests
            )
        if energised_end_no_load_tests is not None:
            TransformerEndInfo.energised_end_no_load_tests.extend(self, energised_end_no_load_tests)

    def add_energised_end_short_circuit_test(
        self, energised_end_short_circuit_test: ShortCircuitTest
    ) -> Self:
        return TransformerEndInfo.energised_end_short_circuit_tests.add(
            self, energised_end_short_circuit_test
        )

    def remove_energised_end_short_circuit_test(
        self, energised_end_short_circuit_test: ShortCircuitTest
    ) -> Self:
        return TransformerEndInfo.energised_end_short_circuit_tests.remove(
            self, energised_end_short_circuit_test
        )

    def clear_energised_end_short_circuit_tests(self) -> Self:
        return TransformerEndInfo.energised_end_short_circuit_tests.clear(self)

    def num_energised_end_short_circuit_test(self) -> int:
        return TransformerEndInfo.energised_end_short_circuit_tests.count(self)

    def get_energised_end_short_circuit_test_by_mrid(self, mrid: str) -> ShortCircuitTest | None:
        return TransformerEndInfo.energised_end_short_circuit_tests.get_by_mrid(self, mrid)

    def add_to_mesh_impedance(self, to_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEndInfo.to_mesh_impedances.add(self, to_mesh_impedance)

    def remove_to_mesh_impedance(self, to_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEndInfo.to_mesh_impedances.remove(self, to_mesh_impedance)

    def clear_to_mesh_impedances(self) -> Self:
        return TransformerEndInfo.to_mesh_impedances.clear(self)

    def num_to_mesh_impedance(self) -> int:
        return TransformerEndInfo.to_mesh_impedances.count(self)

    def get_to_mesh_impedance_by_mrid(self, mrid: str) -> TransformerMeshImpedance | None:
        return TransformerEndInfo.to_mesh_impedances.get_by_mrid(self, mrid)

    def add_energised_end_open_circuit_test(
        self, energised_end_open_circuit_test: OpenCircuitTest
    ) -> Self:
        return TransformerEndInfo.energised_end_open_circuit_tests.add(
            self, energised_end_open_circuit_test
        )

    def remove_energised_end_open_circuit_test(
        self, energised_end_open_circuit_test: OpenCircuitTest
    ) -> Self:
        return TransformerEndInfo.energised_end_open_circuit_tests.remove(
            self, energised_end_open_circuit_test
        )

    def clear_energised_end_open_circuit_tests(self) -> Self:
        return TransformerEndInfo.energised_end_open_circuit_tests.clear(self)

    def num_energised_end_open_circuit_test(self) -> int:
        return TransformerEndInfo.energised_end_open_circuit_tests.count(self)

    def get_energised_end_open_circuit_test_by_mrid(self, mrid: str) -> OpenCircuitTest | None:
        return TransformerEndInfo.energised_end_open_circuit_tests.get_by_mrid(self, mrid)

    def add_from_mesh_impedance(self, from_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEndInfo.from_mesh_impedances.add(self, from_mesh_impedance)

    def remove_from_mesh_impedance(self, from_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEndInfo.from_mesh_impedances.remove(self, from_mesh_impedance)

    def clear_from_mesh_impedances(self) -> Self:
        return TransformerEndInfo.from_mesh_impedances.clear(self)

    def num_from_mesh_impedance(self) -> int:
        return TransformerEndInfo.from_mesh_impedances.count(self)

    def get_from_mesh_impedance_by_mrid(self, mrid: str) -> TransformerMeshImpedance | None:
        return TransformerEndInfo.from_mesh_impedances.get_by_mrid(self, mrid)

    def add_open_end_open_circuit_test(self, open_end_open_circuit_test: OpenCircuitTest) -> Self:
        return TransformerEndInfo.open_end_open_circuit_tests.add(self, open_end_open_circuit_test)

    def remove_open_end_open_circuit_test(
        self, open_end_open_circuit_test: OpenCircuitTest
    ) -> Self:
        return TransformerEndInfo.open_end_open_circuit_tests.remove(
            self, open_end_open_circuit_test
        )

    def clear_open_end_open_circuit_tests(self) -> Self:
        return TransformerEndInfo.open_end_open_circuit_tests.clear(self)

    def num_open_end_open_circuit_test(self) -> int:
        return TransformerEndInfo.open_end_open_circuit_tests.count(self)

    def get_open_end_open_circuit_test_by_mrid(self, mrid: str) -> OpenCircuitTest | None:
        return TransformerEndInfo.open_end_open_circuit_tests.get_by_mrid(self, mrid)

    def add_grounded_end_short_circuit_test(
        self, grounded_end_short_circuit_test: ShortCircuitTest
    ) -> Self:
        return TransformerEndInfo.grounded_end_short_circuit_tests.add(
            self, grounded_end_short_circuit_test
        )

    def remove_grounded_end_short_circuit_test(
        self, grounded_end_short_circuit_test: ShortCircuitTest
    ) -> Self:
        return TransformerEndInfo.grounded_end_short_circuit_tests.remove(
            self, grounded_end_short_circuit_test
        )

    def clear_grounded_end_short_circuit_tests(self) -> Self:
        return TransformerEndInfo.grounded_end_short_circuit_tests.clear(self)

    def num_grounded_end_short_circuit_test(self) -> int:
        return TransformerEndInfo.grounded_end_short_circuit_tests.count(self)

    def get_grounded_end_short_circuit_test_by_mrid(self, mrid: str) -> ShortCircuitTest | None:
        return TransformerEndInfo.grounded_end_short_circuit_tests.get_by_mrid(self, mrid)

    def add_energised_end_no_load_test(self, energised_end_no_load_test: NoLoadTest) -> Self:
        return TransformerEndInfo.energised_end_no_load_tests.add(self, energised_end_no_load_test)

    def remove_energised_end_no_load_test(self, energised_end_no_load_test: NoLoadTest) -> Self:
        return TransformerEndInfo.energised_end_no_load_tests.remove(
            self, energised_end_no_load_test
        )

    def clear_energised_end_no_load_tests(self) -> Self:
        return TransformerEndInfo.energised_end_no_load_tests.clear(self)

    def num_energised_end_no_load_test(self) -> int:
        return TransformerEndInfo.energised_end_no_load_tests.count(self)

    def get_energised_end_no_load_test_by_mrid(self, mrid: str) -> NoLoadTest | None:
        return TransformerEndInfo.energised_end_no_load_tests.get_by_mrid(self, mrid)
