"""CIM class AreaReserveSpec (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class AreaReserveSpec(CimObject):
    """The control area's reserve specification."""

    __slots__ = (
        "_sub_control_area",
        "description",
        "lower_reg_margin_reqt",
        "op_reserve_reqt",
        "primary_reserve_reqt",
        "raise_reg_margin_reqt",
        "spinning_reserve_reqt",
    )

    description: str | None
    lower_reg_margin_reqt: float | None  # ActivePower
    op_reserve_reqt: float | None  # ActivePower
    primary_reserve_reqt: float | None  # ActivePower
    raise_reg_margin_reqt: float | None  # ActivePower
    spinning_reserve_reqt: float | None  # ActivePower

    sub_control_area: Many[SubControlArea] = Many(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=True,
            lower=0,
            upper=None,
            inverse="area_reserve_specification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AreaReserveSpec",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{C493C9B4-DF5E-476c-8EBE-5B14C1E37306}",
        attributes=(
            AttrMeta("description", "Description", "str", 0, 1, "primitive"),
            AttrMeta(
                "lower_reg_margin_reqt", "lowerRegMarginReqt", "ActivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta("op_reserve_reqt", "opReserveReqt", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "primary_reserve_reqt", "primaryReserveReqt", "ActivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "raise_reg_margin_reqt", "raiseRegMarginReqt", "ActivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "spinning_reserve_reqt", "spinningReserveReqt", "ActivePower", 0, 1, "cimdatatype"
            ),
        ),
        ends=(sub_control_area.meta,),
    )

    def __init__(
        self,
        *,
        description: str | None = None,
        lower_reg_margin_reqt: float | None = None,
        op_reserve_reqt: float | None = None,
        primary_reserve_reqt: float | None = None,
        raise_reg_margin_reqt: float | None = None,
        spinning_reserve_reqt: float | None = None,
        sub_control_area: Iterable[SubControlArea] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.description = description
        self.lower_reg_margin_reqt = lower_reg_margin_reqt
        self.op_reserve_reqt = op_reserve_reqt
        self.primary_reserve_reqt = primary_reserve_reqt
        self.raise_reg_margin_reqt = raise_reg_margin_reqt
        self.spinning_reserve_reqt = spinning_reserve_reqt
        if sub_control_area is not None:
            AreaReserveSpec.sub_control_area.extend(self, sub_control_area)

    def add_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return AreaReserveSpec.sub_control_area.add(self, sub_control_area)

    def remove_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return AreaReserveSpec.sub_control_area.remove(self, sub_control_area)

    def clear_sub_control_area(self) -> Self:
        return AreaReserveSpec.sub_control_area.clear(self)

    def num_sub_control_area(self) -> int:
        return AreaReserveSpec.sub_control_area.count(self)

    def get_sub_control_area_by_mrid(self, mrid: str) -> SubControlArea | None:
        return AreaReserveSpec.sub_control_area.get_by_mrid(self, mrid)
