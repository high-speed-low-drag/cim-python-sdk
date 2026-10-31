"""CIM class NoLoadTest (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.asset_info.transformer_test import TransformerTest

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo


class NoLoadTest(TransformerTest):
    """No-load test results determine core admittance parameters. They include exciting current
    and core loss measurements from applying voltage to one winding. The excitation may be
    positive sequence or zero sequence. The test may be repeated at different voltages to
    measure saturation."""

    __slots__ = (
        "_energised_end",
        "energised_end_voltage",
        "exciting_current",
        "exciting_current_zero",
        "loss",
        "loss_zero",
    )

    exciting_current: float | None  # PerCent
    exciting_current_zero: float | None  # PerCent
    loss: float | None  # KiloActivePower
    loss_zero: float | None  # KiloActivePower
    energised_end_voltage: float | None  # Voltage

    energised_end: One[TransformerEndInfo] = One(
        EndMeta(
            name="energised_end",
            cim_role="EnergisedEnd",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="energised_end_no_load_tests",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NoLoadTest",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{ED8C37BD-DF33-447e-8A17-96B22ECA0228}",
        attributes=(
            AttrMeta("exciting_current", "excitingCurrent", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta(
                "exciting_current_zero", "excitingCurrentZero", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta("loss", "loss", "KiloActivePower", 0, 1, "cimdatatype"),
            AttrMeta("loss_zero", "lossZero", "KiloActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "energised_end_voltage", "energisedEndVoltage", "Voltage", 0, 1, "cimdatatype"
            ),
        ),
        ends=(energised_end.meta,),
    )

    def __init__(
        self,
        *,
        exciting_current: float | None = None,
        exciting_current_zero: float | None = None,
        loss: float | None = None,
        loss_zero: float | None = None,
        energised_end_voltage: float | None = None,
        energised_end: TransformerEndInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.exciting_current = exciting_current
        self.exciting_current_zero = exciting_current_zero
        self.loss = loss
        self.loss_zero = loss_zero
        self.energised_end_voltage = energised_end_voltage
        if energised_end is not None:
            self.energised_end = energised_end
