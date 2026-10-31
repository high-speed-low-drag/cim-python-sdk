"""CIM class RatioTapChangerTable (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer import RatioTapChanger
    from cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer_table_point import (
        RatioTapChangerTablePoint,
    )


class RatioTapChangerTable(IdentifiedObject):
    """Describes a curve for how the voltage magnitude and impedance varies with the tap step."""

    __slots__ = ("_ratio_tap_changer", "_ratio_tap_changer_table_point")

    ratio_tap_changer_table_point: Many[RatioTapChangerTablePoint] = Many(
        EndMeta(
            name="ratio_tap_changer_table_point",
            cim_role="RatioTapChangerTablePoint",
            target="cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer_table_point:RatioTapChangerTablePoint",
            many=True,
            lower=1,
            upper=None,
            inverse="ratio_tap_changer_table",
            aggregation="none",
        )
    )
    ratio_tap_changer: Many[RatioTapChanger] = Many(
        EndMeta(
            name="ratio_tap_changer",
            cim_role="RatioTapChanger",
            target="cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer:RatioTapChanger",
            many=True,
            lower=0,
            upper=None,
            inverse="ratio_tap_changer_table",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RatioTapChangerTable",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{8A7FA923-A193-4c6f-B315-1DF1A13C9AA1}",
        ends=(
            ratio_tap_changer_table_point.meta,
            ratio_tap_changer.meta,
        ),
    )

    def __init__(
        self,
        *,
        ratio_tap_changer_table_point: Iterable[RatioTapChangerTablePoint] | None = None,
        ratio_tap_changer: Iterable[RatioTapChanger] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ratio_tap_changer_table_point is not None:
            RatioTapChangerTable.ratio_tap_changer_table_point.extend(
                self, ratio_tap_changer_table_point
            )
        if ratio_tap_changer is not None:
            RatioTapChangerTable.ratio_tap_changer.extend(self, ratio_tap_changer)

    def add_ratio_tap_changer_table_point(
        self, ratio_tap_changer_table_point: RatioTapChangerTablePoint
    ) -> Self:
        return RatioTapChangerTable.ratio_tap_changer_table_point.add(
            self, ratio_tap_changer_table_point
        )

    def remove_ratio_tap_changer_table_point(
        self, ratio_tap_changer_table_point: RatioTapChangerTablePoint
    ) -> Self:
        return RatioTapChangerTable.ratio_tap_changer_table_point.remove(
            self, ratio_tap_changer_table_point
        )

    def clear_ratio_tap_changer_table_point(self) -> Self:
        return RatioTapChangerTable.ratio_tap_changer_table_point.clear(self)

    def num_ratio_tap_changer_table_point(self) -> int:
        return RatioTapChangerTable.ratio_tap_changer_table_point.count(self)

    def add_ratio_tap_changer(self, ratio_tap_changer: RatioTapChanger) -> Self:
        return RatioTapChangerTable.ratio_tap_changer.add(self, ratio_tap_changer)

    def remove_ratio_tap_changer(self, ratio_tap_changer: RatioTapChanger) -> Self:
        return RatioTapChangerTable.ratio_tap_changer.remove(self, ratio_tap_changer)

    def clear_ratio_tap_changer(self) -> Self:
        return RatioTapChangerTable.ratio_tap_changer.clear(self)

    def num_ratio_tap_changer(self) -> int:
        return RatioTapChangerTable.ratio_tap_changer.count(self)

    def get_ratio_tap_changer_by_mrid(self, mrid: str) -> RatioTapChanger | None:
        return RatioTapChangerTable.ratio_tap_changer.get_by_mrid(self, mrid)
