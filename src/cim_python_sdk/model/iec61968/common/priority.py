"""CIM compound Priority (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class Priority(CimCompound):
    """Priority definition."""

    __slots__ = ("justification", "rank", "type")

    rank: int | None
    type: str | None
    justification: str | None

    _cim_meta = ClassMeta(
        cim_name="Priority",
        package="TC57CIM/IEC61968/Common",
        guid="{3E61C9C1-97C4-413e-B585-28CF83B90EC7}",
        kind="compound",
        attributes=(
            AttrMeta("rank", "rank", "int", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("justification", "justification", "str", 0, 1, "primitive"),
        ),
    )
