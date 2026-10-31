"""CIM class TransformerStarImpedance (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo
    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd


class TransformerStarImpedance(IdentifiedObject):
    """Transformer star impedance (Pi-model) that accurately reflects impedance for
    transformers with 2 or 3 windings. For transformers with 4 or more windings,
    TransformerMeshImpedance class shall be used.

    For transmission networks use PowerTransformerEnd impedances (r, r0, x, x0, b, b0, g and
    g0)."""

    __slots__ = ("_transformer_end", "_transformer_end_info", "r", "r0", "x", "x0")

    r: float | None  # Resistance
    r0: float | None  # Resistance
    x: float | None  # Reactance
    x0: float | None  # Reactance

    transformer_end: Many[TransformerEnd] = Many(
        EndMeta(
            name="transformer_end",
            cim_role="TransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=True,
            lower=0,
            upper=None,
            inverse="star_impedance",
            aggregation="none",
        )
    )
    transformer_end_info: One[TransformerEndInfo] = One(
        EndMeta(
            name="transformer_end_info",
            cim_role="TransformerEndInfo",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_star_impedance",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerStarImpedance",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{35D1EE00-F393-4e93-A01A-B4E816466033}",
        attributes=(
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(
            transformer_end.meta,
            transformer_end_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        r: float | None = None,
        r0: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        transformer_end: Iterable[TransformerEnd] | None = None,
        transformer_end_info: TransformerEndInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.r = r
        self.r0 = r0
        self.x = x
        self.x0 = x0
        if transformer_end is not None:
            TransformerStarImpedance.transformer_end.extend(self, transformer_end)
        if transformer_end_info is not None:
            self.transformer_end_info = transformer_end_info

    def add_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return TransformerStarImpedance.transformer_end.add(self, transformer_end)

    def remove_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return TransformerStarImpedance.transformer_end.remove(self, transformer_end)

    def clear_transformer_end(self) -> Self:
        return TransformerStarImpedance.transformer_end.clear(self)

    def num_transformer_end(self) -> int:
        return TransformerStarImpedance.transformer_end.count(self)

    def get_transformer_end_by_mrid(self, mrid: str) -> TransformerEnd | None:
        return TransformerStarImpedance.transformer_end.get_by_mrid(self, mrid)
