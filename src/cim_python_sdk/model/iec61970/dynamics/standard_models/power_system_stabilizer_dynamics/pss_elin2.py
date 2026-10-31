"""CIM class PssELIN2 (TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.power_system_stabilizer_dynamics.power_system_stabilizer_dynamics import (
    PowerSystemStabilizerDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PssELIN2(PowerSystemStabilizerDynamics):
    """Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B
    can also be used)."""

    __slots__ = ("apss", "ks1", "ks2", "ppss", "psslim", "ts1", "ts2", "ts3", "ts4", "ts5", "ts6")

    ts1: float | None  # Seconds
    ts2: float | None  # Seconds
    ts3: float | None  # Seconds
    ts4: float | None  # Seconds
    ts5: float | None  # Seconds
    ts6: float | None  # Seconds
    ks1: float | None  # PU
    ks2: float | None  # PU
    ppss: float | None  # PU
    apss: float | None  # PU
    psslim: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PssELIN2",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/PowerSystemStabilizerDynamics",
        guid="{00471B64-A672-4065-A78A-36E806FFC2FB}",
        attributes=(
            AttrMeta("ts1", "ts1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts2", "ts2", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts3", "ts3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts4", "ts4", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts5", "ts5", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ts6", "ts6", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ks1", "ks1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ks2", "ks2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("ppss", "ppss", "PU", 0, 1, "cimdatatype"),
            AttrMeta("apss", "apss", "PU", 0, 1, "cimdatatype"),
            AttrMeta("psslim", "psslim", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        ts1: float | None = None,
        ts2: float | None = None,
        ts3: float | None = None,
        ts4: float | None = None,
        ts5: float | None = None,
        ts6: float | None = None,
        ks1: float | None = None,
        ks2: float | None = None,
        ppss: float | None = None,
        apss: float | None = None,
        psslim: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ts1 = ts1
        self.ts2 = ts2
        self.ts3 = ts3
        self.ts4 = ts4
        self.ts5 = ts5
        self.ts6 = ts6
        self.ks1 = ks1
        self.ks2 = ks2
        self.ppss = ppss
        self.apss = apss
        self.psslim = psslim
