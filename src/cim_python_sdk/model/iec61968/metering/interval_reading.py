"""CIM class IntervalReading (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.metering.base_reading import BaseReading

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.interval_block import IntervalBlock


class IntervalReading(BaseReading):
    """Data captured at regular intervals of time. Interval data could be captured as
    incremental data, absolute data, or relative data. The source for the data is usually a
    tariff quantity or an engineering quantity. Data is typically captured in time-tagged,
    uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min.

    Note: Interval Data is sometimes also called "Interval Data Readings" (IDR)."""

    __slots__ = ("_interval_blocks",)

    interval_blocks: Many[IntervalBlock] = Many(
        EndMeta(
            name="interval_blocks",
            cim_role="IntervalBlocks",
            target="cim_python_sdk.model.iec61968.metering.interval_block:IntervalBlock",
            many=True,
            lower=0,
            upper=None,
            inverse="interval_readings",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IntervalReading",
        package="TC57CIM/IEC61968/Metering",
        guid="{779A4909-8E4E-4587-B2DB-C60366EAE9F4}",
        ends=(interval_blocks.meta,),
    )

    def __init__(
        self,
        *,
        interval_blocks: Iterable[IntervalBlock] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if interval_blocks is not None:
            IntervalReading.interval_blocks.extend(self, interval_blocks)

    def add_interval_block(self, interval_block: IntervalBlock) -> Self:
        return IntervalReading.interval_blocks.add(self, interval_block)

    def remove_interval_block(self, interval_block: IntervalBlock) -> Self:
        return IntervalReading.interval_blocks.remove(self, interval_block)

    def clear_interval_blocks(self) -> Self:
        return IntervalReading.interval_blocks.clear(self)

    def num_interval_block(self) -> int:
        return IntervalReading.interval_blocks.count(self)
