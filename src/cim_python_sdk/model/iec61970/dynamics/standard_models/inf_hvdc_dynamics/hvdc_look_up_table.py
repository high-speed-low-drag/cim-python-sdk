"""CIM class HVDCLookUpTable (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.vdcol import (
        VDCOL,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.look_up_table_function_kind import (
        LookUpTableFunctionKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qregulator import (
        Qregulator,
    )


class HVDCLookUpTable(CimObject):
    """CIM class HVDCLookUpTable."""

    __slots__ = ("_qregulator", "_vdcol", "function_kind", "input", "output", "sequence")

    input: float | None
    output: float | None
    sequence: int | None
    function_kind: LookUpTableFunctionKind | None

    vdcol: One[VDCOL] = One(
        EndMeta(
            name="vdcol",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.vdcol:VDCOL",
            many=False,
            lower=0,
            upper=1,
            inverse="hvdc_look_up_tables",
            aggregation="none",
        )
    )
    qregulator: One[Qregulator] = One(
        EndMeta(
            name="qregulator",
            cim_role="Qregulator",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.qregulator:Qregulator",
            many=False,
            lower=0,
            upper=1,
            inverse="hvd_clook_up_table",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="HVDCLookUpTable",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics",
        guid="{9B759B51-5C5D-4f1f-9015-DA8CA821B75F}",
        attributes=(
            AttrMeta("input", "input", "float", 0, 1, "primitive"),
            AttrMeta("output", "output", "float", 0, 1, "primitive"),
            AttrMeta("sequence", "sequence", "int", 0, 1, "primitive"),
            AttrMeta(
                "function_kind", "functionKind", "LookUpTableFunctionKind", 0, 1, "enumeration"
            ),
        ),
        ends=(
            vdcol.meta,
            qregulator.meta,
        ),
    )

    def __init__(
        self,
        *,
        input: float | None = None,
        output: float | None = None,
        sequence: int | None = None,
        function_kind: LookUpTableFunctionKind | None = None,
        vdcol: VDCOL | None = None,
        qregulator: Qregulator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.input = input
        self.output = output
        self.sequence = sequence
        self.function_kind = function_kind
        if vdcol is not None:
            self.vdcol = vdcol
        if qregulator is not None:
            self.qregulator = qregulator
