"""CIM class RatioTapChangerTablePoint (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.tap_changer_table_point import TapChangerTablePoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer_table import (
        RatioTapChangerTable,
    )


class RatioTapChangerTablePoint(TapChangerTablePoint):
    """Describes each tap step in the ratio tap changer tabular curve."""

    __slots__ = ("_ratio_tap_changer_table",)

    ratio_tap_changer_table: One[RatioTapChangerTable] = One(
        EndMeta(
            name="ratio_tap_changer_table",
            cim_role="RatioTapChangerTable",
            target="cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer_table:RatioTapChangerTable",
            many=False,
            lower=1,
            upper=1,
            inverse="ratio_tap_changer_table_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RatioTapChangerTablePoint",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{607E97C8-E4A3-4721-8592-1AE1B256EB77}",
        ends=(ratio_tap_changer_table.meta,),
    )

    def __init__(
        self,
        *,
        ratio_tap_changer_table: RatioTapChangerTable | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ratio_tap_changer_table is not None:
            self.ratio_tap_changer_table = ratio_tap_changer_table
