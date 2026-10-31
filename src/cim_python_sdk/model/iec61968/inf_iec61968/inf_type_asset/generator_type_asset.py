"""CIM class GeneratorTypeAsset (TC57CIM/IEC61968/InfIEC61968/InfTypeAsset). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.catalog_asset_type import CatalogAssetType

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class GeneratorTypeAsset(CatalogAssetType):
    """Generic generation equipment that may be used for various purposes such as work
    planning. It defines both the Real and Reactive power properties (modelled at the PSR
    level as a GeneratingUnit + SynchronousMachine)."""

    __slots__ = (
        "max_p",
        "max_q",
        "min_p",
        "min_q",
        "r_direct_subtrans",
        "r_direct_sync",
        "r_direct_trans",
        "r_quad_subtrans",
        "r_quad_sync",
        "r_quad_trans",
        "x_direct_subtrans",
        "x_direct_sync",
        "x_direct_trans",
        "x_quad_subtrans",
        "x_quad_sync",
        "x_quad_trans",
    )

    max_q: float | None  # ReactivePower
    max_p: float | None  # ActivePower
    min_q: float | None  # ReactivePower
    min_p: float | None  # ActivePower
    r_direct_subtrans: float | None  # Resistance
    r_direct_sync: float | None  # Resistance
    r_direct_trans: float | None  # Resistance
    r_quad_subtrans: float | None  # Resistance
    r_quad_sync: float | None  # Resistance
    r_quad_trans: float | None  # Resistance
    x_direct_subtrans: float | None  # Reactance
    x_direct_sync: float | None  # Reactance
    x_direct_trans: float | None  # Reactance
    x_quad_subtrans: float | None  # Reactance
    x_quad_sync: float | None  # Reactance
    x_quad_trans: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="GeneratorTypeAsset",
        package="TC57CIM/IEC61968/InfIEC61968/InfTypeAsset",
        guid="{2DCA6CE9-F4BC-443c-A5F7-4140642C4A92}",
        attributes=(
            AttrMeta("max_q", "maxQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_p", "maxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_q", "minQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_p", "minP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("r_direct_subtrans", "rDirectSubtrans", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r_direct_sync", "rDirectSync", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r_direct_trans", "rDirectTrans", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r_quad_subtrans", "rQuadSubtrans", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r_quad_sync", "rQuadSync", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r_quad_trans", "rQuadTrans", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("x_direct_subtrans", "xDirectSubtrans", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_direct_sync", "xDirectSync", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_direct_trans", "xDirectTrans", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_quad_subtrans", "xQuadSubtrans", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_quad_sync", "xQuadSync", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x_quad_trans", "xQuadTrans", "Reactance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        max_q: float | None = None,
        max_p: float | None = None,
        min_q: float | None = None,
        min_p: float | None = None,
        r_direct_subtrans: float | None = None,
        r_direct_sync: float | None = None,
        r_direct_trans: float | None = None,
        r_quad_subtrans: float | None = None,
        r_quad_sync: float | None = None,
        r_quad_trans: float | None = None,
        x_direct_subtrans: float | None = None,
        x_direct_sync: float | None = None,
        x_direct_trans: float | None = None,
        x_quad_subtrans: float | None = None,
        x_quad_sync: float | None = None,
        x_quad_trans: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_q = max_q
        self.max_p = max_p
        self.min_q = min_q
        self.min_p = min_p
        self.r_direct_subtrans = r_direct_subtrans
        self.r_direct_sync = r_direct_sync
        self.r_direct_trans = r_direct_trans
        self.r_quad_subtrans = r_quad_subtrans
        self.r_quad_sync = r_quad_sync
        self.r_quad_trans = r_quad_trans
        self.x_direct_subtrans = x_direct_subtrans
        self.x_direct_sync = x_direct_sync
        self.x_direct_trans = x_direct_trans
        self.x_quad_subtrans = x_quad_subtrans
        self.x_quad_sync = x_quad_sync
        self.x_quad_trans = x_quad_trans
