"""CIM class TransformerMeshImpedance (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo
    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd


class TransformerMeshImpedance(IdentifiedObject):
    """Transformer mesh impedance (Delta-model) between transformer ends.

    The typical case is that this class describes the impedance between two transformer ends
    pair-wise, i.e. the cardinalities at both transformer end associations are 1. However,
    in cases where two or more transformer ends are modelled the cardinalities are larger
    than 1."""

    __slots__ = (
        "_from_transformer_end",
        "_from_transformer_end_info",
        "_to_transformer_end",
        "_to_transformer_end_infos",
        "r",
        "r0",
        "x",
        "x0",
    )

    r: float | None  # Resistance
    r0: float | None  # Resistance
    x: float | None  # Reactance
    x0: float | None  # Reactance

    from_transformer_end: One[TransformerEnd] = One(
        EndMeta(
            name="from_transformer_end",
            cim_role="FromTransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=False,
            lower=1,
            upper=1,
            inverse="from_mesh_impedance",
            aggregation="none",
        )
    )
    to_transformer_end_infos: Many[TransformerEndInfo] = Many(
        EndMeta(
            name="to_transformer_end_infos",
            cim_role="ToTransformerEndInfos",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="to_mesh_impedances",
            aggregation="none",
        )
    )
    from_transformer_end_info: One[TransformerEndInfo] = One(
        EndMeta(
            name="from_transformer_end_info",
            cim_role="FromTransformerEndInfo",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="from_mesh_impedances",
            aggregation="none",
        )
    )
    to_transformer_end: Many[TransformerEnd] = Many(
        EndMeta(
            name="to_transformer_end",
            cim_role="ToTransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=True,
            lower=1,
            upper=None,
            inverse="to_mesh_impedance",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerMeshImpedance",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{49FE2028-1AD5-4550-A55A-FA43C4D07C38}",
        attributes=(
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(
            from_transformer_end.meta,
            to_transformer_end_infos.meta,
            from_transformer_end_info.meta,
            to_transformer_end.meta,
        ),
    )

    def __init__(
        self,
        *,
        r: float | None = None,
        r0: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        from_transformer_end: TransformerEnd | None = None,
        to_transformer_end_infos: Iterable[TransformerEndInfo] | None = None,
        from_transformer_end_info: TransformerEndInfo | None = None,
        to_transformer_end: Iterable[TransformerEnd] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.r = r
        self.r0 = r0
        self.x = x
        self.x0 = x0
        if from_transformer_end is not None:
            self.from_transformer_end = from_transformer_end
        if to_transformer_end_infos is not None:
            TransformerMeshImpedance.to_transformer_end_infos.extend(self, to_transformer_end_infos)
        if from_transformer_end_info is not None:
            self.from_transformer_end_info = from_transformer_end_info
        if to_transformer_end is not None:
            TransformerMeshImpedance.to_transformer_end.extend(self, to_transformer_end)

    def add_to_transformer_end_info(self, to_transformer_end_info: TransformerEndInfo) -> Self:
        return TransformerMeshImpedance.to_transformer_end_infos.add(self, to_transformer_end_info)

    def remove_to_transformer_end_info(self, to_transformer_end_info: TransformerEndInfo) -> Self:
        return TransformerMeshImpedance.to_transformer_end_infos.remove(
            self, to_transformer_end_info
        )

    def clear_to_transformer_end_infos(self) -> Self:
        return TransformerMeshImpedance.to_transformer_end_infos.clear(self)

    def num_to_transformer_end_info(self) -> int:
        return TransformerMeshImpedance.to_transformer_end_infos.count(self)

    def get_to_transformer_end_info_by_mrid(self, mrid: str) -> TransformerEndInfo | None:
        return TransformerMeshImpedance.to_transformer_end_infos.get_by_mrid(self, mrid)

    def add_to_transformer_end(self, to_transformer_end: TransformerEnd) -> Self:
        return TransformerMeshImpedance.to_transformer_end.add(self, to_transformer_end)

    def remove_to_transformer_end(self, to_transformer_end: TransformerEnd) -> Self:
        return TransformerMeshImpedance.to_transformer_end.remove(self, to_transformer_end)

    def clear_to_transformer_end(self) -> Self:
        return TransformerMeshImpedance.to_transformer_end.clear(self)

    def num_to_transformer_end(self) -> int:
        return TransformerMeshImpedance.to_transformer_end.count(self)

    def get_to_transformer_end_by_mrid(self, mrid: str) -> TransformerEnd | None:
        return TransformerMeshImpedance.to_transformer_end.get_by_mrid(self, mrid)
