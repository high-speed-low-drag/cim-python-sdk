"""CIM class BaseVoltage (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset_deployment import AssetDeployment
    from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment
    from cim_python_sdk.model.iec61970.base.core.voltage_level import VoltageLevel
    from cim_python_sdk.model.iec61970.base.topology.topological_node import TopologicalNode
    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd


class BaseVoltage(IdentifiedObject):
    """Defines a system base voltage which is referenced."""

    __slots__ = (
        "_conducting_equipment",
        "_network_asset_deployment",
        "_topological_node",
        "_transformer_ends",
        "_voltage_level",
        "nominal_voltage",
    )

    nominal_voltage: float | None  # Voltage

    topological_node: Many[TopologicalNode] = Many(
        EndMeta(
            name="topological_node",
            cim_role="TopologicalNode",
            target="cim_python_sdk.model.iec61970.base.topology.topological_node:TopologicalNode",
            many=True,
            lower=0,
            upper=None,
            inverse="base_voltage",
            aggregation="none",
        )
    )
    conducting_equipment: Many[ConductingEquipment] = Many(
        EndMeta(
            name="conducting_equipment",
            cim_role="ConductingEquipment",
            target="cim_python_sdk.model.iec61970.base.core.conducting_equipment:ConductingEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="base_voltage",
            aggregation="none",
        )
    )
    transformer_ends: Many[TransformerEnd] = Many(
        EndMeta(
            name="transformer_ends",
            cim_role="TransformerEnds",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=True,
            lower=0,
            upper=None,
            inverse="base_voltage",
            aggregation="none",
        )
    )
    network_asset_deployment: Many[AssetDeployment] = Many(
        EndMeta(
            name="network_asset_deployment",
            cim_role="NetworkAssetDeployment",
            target="cim_python_sdk.model.iec61968.assets.asset_deployment:AssetDeployment",
            many=True,
            lower=0,
            upper=None,
            inverse="base_voltage",
            aggregation="none",
        )
    )
    voltage_level: Many[VoltageLevel] = Many(
        EndMeta(
            name="voltage_level",
            cim_role="VoltageLevel",
            target="cim_python_sdk.model.iec61970.base.core.voltage_level:VoltageLevel",
            many=True,
            lower=0,
            upper=None,
            inverse="base_voltage",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BaseVoltage",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{2E70DC9D-AEAE-46cc-B20A-C20A636AE9B0}",
        attributes=(AttrMeta("nominal_voltage", "nominalVoltage", "Voltage", 0, 1, "cimdatatype"),),
        ends=(
            topological_node.meta,
            conducting_equipment.meta,
            transformer_ends.meta,
            network_asset_deployment.meta,
            voltage_level.meta,
        ),
    )

    def __init__(
        self,
        *,
        nominal_voltage: float | None = None,
        topological_node: Iterable[TopologicalNode] | None = None,
        conducting_equipment: Iterable[ConductingEquipment] | None = None,
        transformer_ends: Iterable[TransformerEnd] | None = None,
        network_asset_deployment: Iterable[AssetDeployment] | None = None,
        voltage_level: Iterable[VoltageLevel] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.nominal_voltage = nominal_voltage
        if topological_node is not None:
            BaseVoltage.topological_node.extend(self, topological_node)
        if conducting_equipment is not None:
            BaseVoltage.conducting_equipment.extend(self, conducting_equipment)
        if transformer_ends is not None:
            BaseVoltage.transformer_ends.extend(self, transformer_ends)
        if network_asset_deployment is not None:
            BaseVoltage.network_asset_deployment.extend(self, network_asset_deployment)
        if voltage_level is not None:
            BaseVoltage.voltage_level.extend(self, voltage_level)

    def add_topological_node(self, topological_node: TopologicalNode) -> Self:
        return BaseVoltage.topological_node.add(self, topological_node)

    def remove_topological_node(self, topological_node: TopologicalNode) -> Self:
        return BaseVoltage.topological_node.remove(self, topological_node)

    def clear_topological_node(self) -> Self:
        return BaseVoltage.topological_node.clear(self)

    def num_topological_node(self) -> int:
        return BaseVoltage.topological_node.count(self)

    def get_topological_node_by_mrid(self, mrid: str) -> TopologicalNode | None:
        return BaseVoltage.topological_node.get_by_mrid(self, mrid)

    def add_conducting_equipment(self, conducting_equipment: ConductingEquipment) -> Self:
        return BaseVoltage.conducting_equipment.add(self, conducting_equipment)

    def remove_conducting_equipment(self, conducting_equipment: ConductingEquipment) -> Self:
        return BaseVoltage.conducting_equipment.remove(self, conducting_equipment)

    def clear_conducting_equipment(self) -> Self:
        return BaseVoltage.conducting_equipment.clear(self)

    def num_conducting_equipment(self) -> int:
        return BaseVoltage.conducting_equipment.count(self)

    def get_conducting_equipment_by_mrid(self, mrid: str) -> ConductingEquipment | None:
        return BaseVoltage.conducting_equipment.get_by_mrid(self, mrid)

    def add_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return BaseVoltage.transformer_ends.add(self, transformer_end)

    def remove_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return BaseVoltage.transformer_ends.remove(self, transformer_end)

    def clear_transformer_ends(self) -> Self:
        return BaseVoltage.transformer_ends.clear(self)

    def num_transformer_end(self) -> int:
        return BaseVoltage.transformer_ends.count(self)

    def get_transformer_end_by_mrid(self, mrid: str) -> TransformerEnd | None:
        return BaseVoltage.transformer_ends.get_by_mrid(self, mrid)

    def add_network_asset_deployment(self, network_asset_deployment: AssetDeployment) -> Self:
        return BaseVoltage.network_asset_deployment.add(self, network_asset_deployment)

    def remove_network_asset_deployment(self, network_asset_deployment: AssetDeployment) -> Self:
        return BaseVoltage.network_asset_deployment.remove(self, network_asset_deployment)

    def clear_network_asset_deployment(self) -> Self:
        return BaseVoltage.network_asset_deployment.clear(self)

    def num_network_asset_deployment(self) -> int:
        return BaseVoltage.network_asset_deployment.count(self)

    def get_network_asset_deployment_by_mrid(self, mrid: str) -> AssetDeployment | None:
        return BaseVoltage.network_asset_deployment.get_by_mrid(self, mrid)

    def add_voltage_level(self, voltage_level: VoltageLevel) -> Self:
        return BaseVoltage.voltage_level.add(self, voltage_level)

    def remove_voltage_level(self, voltage_level: VoltageLevel) -> Self:
        return BaseVoltage.voltage_level.remove(self, voltage_level)

    def clear_voltage_level(self) -> Self:
        return BaseVoltage.voltage_level.clear(self)

    def num_voltage_level(self) -> int:
        return BaseVoltage.voltage_level.count(self)

    def get_voltage_level_by_mrid(self, mrid: str) -> VoltageLevel | None:
        return BaseVoltage.voltage_level.get_by_mrid(self, mrid)
