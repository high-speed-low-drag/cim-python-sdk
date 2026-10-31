"""CIM class PendingCalculation (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.interval_block import IntervalBlock
    from cim_python_sdk.model.iec61968.metering.reading_type import ReadingType


class PendingCalculation(CimObject):
    """When present, a scalar conversion that needs to be applied to every
    IntervalReading.value contained in IntervalBlock. This conversion results in a new
    associated ReadingType, reflecting the true dimensions of IntervalReading values after
    the conversion."""

    __slots__ = (
        "_interval_blocks",
        "_reading_type",
        "multiply_before_add",
        "offset",
        "scalar_denominator",
        "scalar_float",
        "scalar_numerator",
    )

    scalar_float: float | None
    scalar_numerator: int | None
    scalar_denominator: int | None
    offset: int | None
    multiply_before_add: bool | None

    reading_type: One[ReadingType] = One(
        EndMeta(
            name="reading_type",
            cim_role="ReadingType",
            target="cim_python_sdk.model.iec61968.metering.reading_type:ReadingType",
            many=False,
            lower=1,
            upper=1,
            inverse="pending_calculation",
            aggregation="none",
        )
    )
    interval_blocks: Many[IntervalBlock] = Many(
        EndMeta(
            name="interval_blocks",
            cim_role="IntervalBlocks",
            target="cim_python_sdk.model.iec61968.metering.interval_block:IntervalBlock",
            many=True,
            lower=0,
            upper=None,
            inverse="pending_calculation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PendingCalculation",
        package="TC57CIM/IEC61968/Metering",
        guid="{AEB2AE35-E037-462d-ACFE-BDEBC3AD5285}",
        attributes=(
            AttrMeta("scalar_float", "scalarFloat", "float", 0, 1, "primitive"),
            AttrMeta("scalar_numerator", "scalarNumerator", "int", 0, 1, "primitive"),
            AttrMeta("scalar_denominator", "scalarDenominator", "int", 0, 1, "primitive"),
            AttrMeta("offset", "offset", "int", 0, 1, "primitive"),
            AttrMeta("multiply_before_add", "multiplyBeforeAdd", "bool", 0, 1, "primitive"),
        ),
        ends=(
            reading_type.meta,
            interval_blocks.meta,
        ),
    )

    def __init__(
        self,
        *,
        scalar_float: float | None = None,
        scalar_numerator: int | None = None,
        scalar_denominator: int | None = None,
        offset: int | None = None,
        multiply_before_add: bool | None = None,
        reading_type: ReadingType | None = None,
        interval_blocks: Iterable[IntervalBlock] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.scalar_float = scalar_float
        self.scalar_numerator = scalar_numerator
        self.scalar_denominator = scalar_denominator
        self.offset = offset
        self.multiply_before_add = multiply_before_add
        if reading_type is not None:
            self.reading_type = reading_type
        if interval_blocks is not None:
            PendingCalculation.interval_blocks.extend(self, interval_blocks)

    def add_interval_block(self, interval_block: IntervalBlock) -> Self:
        return PendingCalculation.interval_blocks.add(self, interval_block)

    def remove_interval_block(self, interval_block: IntervalBlock) -> Self:
        return PendingCalculation.interval_blocks.remove(self, interval_block)

    def clear_interval_blocks(self) -> Self:
        return PendingCalculation.interval_blocks.clear(self)

    def num_interval_block(self) -> int:
        return PendingCalculation.interval_blocks.count(self)
