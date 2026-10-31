"""CIM class TransformerCoreAdmittance (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo
    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd


class TransformerCoreAdmittance(IdentifiedObject):
    """The transformer core admittance. Used to specify the core admittance of a transformer in
    a manner that can be shared among power transformers."""

    __slots__ = ("_transformer_end", "_transformer_end_info", "b", "b0", "g", "g0")

    b: float | None  # Susceptance
    b0: float | None  # Susceptance
    g: float | None  # Conductance
    g0: float | None  # Conductance

    transformer_end_info: One[TransformerEndInfo] = One(
        EndMeta(
            name="transformer_end_info",
            cim_role="TransformerEndInfo",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="core_admittance",
            aggregation="none",
        )
    )
    transformer_end: Many[TransformerEnd] = Many(
        EndMeta(
            name="transformer_end",
            cim_role="TransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=True,
            lower=0,
            upper=None,
            inverse="core_admittance",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerCoreAdmittance",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{25B2D790-161A-45c8-8551-E77A34DE684C}",
        attributes=(
            AttrMeta("b", "b", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("b0", "b0", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("g", "g", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("g0", "g0", "Conductance", 0, 1, "cimdatatype"),
        ),
        ends=(
            transformer_end_info.meta,
            transformer_end.meta,
        ),
    )

    def __init__(
        self,
        *,
        b: float | None = None,
        b0: float | None = None,
        g: float | None = None,
        g0: float | None = None,
        transformer_end_info: TransformerEndInfo | None = None,
        transformer_end: Iterable[TransformerEnd] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b = b
        self.b0 = b0
        self.g = g
        self.g0 = g0
        if transformer_end_info is not None:
            self.transformer_end_info = transformer_end_info
        if transformer_end is not None:
            TransformerCoreAdmittance.transformer_end.extend(self, transformer_end)

    def add_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return TransformerCoreAdmittance.transformer_end.add(self, transformer_end)

    def remove_transformer_end(self, transformer_end: TransformerEnd) -> Self:
        return TransformerCoreAdmittance.transformer_end.remove(self, transformer_end)

    def clear_transformer_end(self) -> Self:
        return TransformerCoreAdmittance.transformer_end.clear(self)

    def num_transformer_end(self) -> int:
        return TransformerCoreAdmittance.transformer_end.count(self)

    def get_transformer_end_by_mrid(self, mrid: str) -> TransformerEnd | None:
        return TransformerCoreAdmittance.transformer_end.get_by_mrid(self, mrid)
