"""CIM class MutualCoupling (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal


class MutualCoupling(IdentifiedObject):
    """This class represents the zero sequence line mutual coupling."""

    __slots__ = (
        "_first_terminal",
        "_second_terminal",
        "b0ch",
        "distance11",
        "distance12",
        "distance21",
        "distance22",
        "g0ch",
        "r0",
        "x0",
    )

    b0ch: float | None  # Susceptance
    distance11: float | None  # Length
    distance12: float | None  # Length
    distance21: float | None  # Length
    distance22: float | None  # Length
    g0ch: float | None  # Conductance
    r0: float | None  # Resistance
    x0: float | None  # Reactance

    second_terminal: One[Terminal] = One(
        EndMeta(
            name="second_terminal",
            cim_role="Second_Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="has_second_mutual_coupling",
            aggregation="none",
        )
    )
    first_terminal: One[Terminal] = One(
        EndMeta(
            name="first_terminal",
            cim_role="First_Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=1,
            upper=1,
            inverse="has_first_mutual_coupling",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MutualCoupling",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{A46F0441-DB66-4ff2-A892-7C5F9F54FA38}",
        attributes=(
            AttrMeta("b0ch", "b0ch", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("distance11", "distance11", "Length", 0, 1, "cimdatatype"),
            AttrMeta("distance12", "distance12", "Length", 0, 1, "cimdatatype"),
            AttrMeta("distance21", "distance21", "Length", 0, 1, "cimdatatype"),
            AttrMeta("distance22", "distance22", "Length", 0, 1, "cimdatatype"),
            AttrMeta("g0ch", "g0ch", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(
            second_terminal.meta,
            first_terminal.meta,
        ),
    )

    def __init__(
        self,
        *,
        b0ch: float | None = None,
        distance11: float | None = None,
        distance12: float | None = None,
        distance21: float | None = None,
        distance22: float | None = None,
        g0ch: float | None = None,
        r0: float | None = None,
        x0: float | None = None,
        second_terminal: Terminal | None = None,
        first_terminal: Terminal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b0ch = b0ch
        self.distance11 = distance11
        self.distance12 = distance12
        self.distance21 = distance21
        self.distance22 = distance22
        self.g0ch = g0ch
        self.r0 = r0
        self.x0 = x0
        if second_terminal is not None:
            self.second_terminal = second_terminal
        if first_terminal is not None:
            self.first_terminal = first_terminal
