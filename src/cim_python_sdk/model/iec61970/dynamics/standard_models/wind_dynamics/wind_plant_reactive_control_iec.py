"""CIM class WindPlantReactiveControlIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table import (
        WindDynamicsLookupTable,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_iec import (
        WindPlantIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_qcontrol_mode_kind import (
        WindPlantQcontrolModeKind,
    )


class WindPlantReactiveControlIEC(IdentifiedObject):
    """Simplified plant voltage and reactive power control model for use with type 3 and type 4
    wind turbine models.

    Reference: IEC 61400-27-1:2015, Annex D."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_plant_iec",
        "dxrefmax",
        "dxrefmin",
        "kiwpx",
        "kiwpxmax",
        "kiwpxmin",
        "kpwpx",
        "kwpqref",
        "kwpqu",
        "tuqfilt",
        "twppfiltq",
        "twpqfiltq",
        "twpufiltq",
        "txft",
        "txfv",
        "uwpqdip",
        "wind_plant_qcontrol_modes_type",
        "xrefmax",
        "xrefmin",
    )

    dxrefmax: float | None  # PU
    dxrefmin: float | None  # PU
    kiwpx: float | None
    kiwpxmax: float | None  # PU
    kiwpxmin: float | None  # PU
    kpwpx: float | None
    kwpqref: float | None  # PU
    kwpqu: float | None  # PU
    tuqfilt: float | None  # Seconds
    twppfiltq: float | None  # Seconds
    twpqfiltq: float | None  # Seconds
    twpufiltq: float | None  # Seconds
    txft: float | None  # Seconds
    txfv: float | None  # Seconds
    uwpqdip: float | None  # PU
    wind_plant_qcontrol_modes_type: WindPlantQcontrolModeKind | None
    xrefmax: float | None  # PU
    xrefmin: float | None  # PU

    wind_plant_iec: One[WindPlantIEC] = One(
        EndMeta(
            name="wind_plant_iec",
            cim_role="WindPlantIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_iec:WindPlantIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_plant_reactive_control_iec",
            aggregation="none",
        )
    )
    wind_dynamics_lookup_table: Many[WindDynamicsLookupTable] = Many(
        EndMeta(
            name="wind_dynamics_lookup_table",
            cim_role="WindDynamicsLookupTable",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table:WindDynamicsLookupTable",
            many=True,
            lower=1,
            upper=None,
            inverse="wind_plant_reactive_control_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindPlantReactiveControlIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{EC65930A-5B76-4f27-921D-4694BCAADDC1}",
        attributes=(
            AttrMeta("dxrefmax", "dxrefmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dxrefmin", "dxrefmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiwpx", "kiwpx", "float", 0, 1, "primitive"),
            AttrMeta("kiwpxmax", "kiwpxmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiwpxmin", "kiwpxmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpwpx", "kpwpx", "float", 0, 1, "primitive"),
            AttrMeta("kwpqref", "kwpqref", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kwpqu", "kwpqu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tuqfilt", "tuqfilt", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twppfiltq", "twppfiltq", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twpqfiltq", "twpqfiltq", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twpufiltq", "twpufiltq", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("txft", "txft", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("txfv", "txfv", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uwpqdip", "uwpqdip", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "wind_plant_qcontrol_modes_type",
                "windPlantQcontrolModesType",
                "WindPlantQcontrolModeKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("xrefmax", "xrefmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xrefmin", "xrefmin", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_plant_iec.meta,
            wind_dynamics_lookup_table.meta,
        ),
    )

    def __init__(
        self,
        *,
        dxrefmax: float | None = None,
        dxrefmin: float | None = None,
        kiwpx: float | None = None,
        kiwpxmax: float | None = None,
        kiwpxmin: float | None = None,
        kpwpx: float | None = None,
        kwpqref: float | None = None,
        kwpqu: float | None = None,
        tuqfilt: float | None = None,
        twppfiltq: float | None = None,
        twpqfiltq: float | None = None,
        twpufiltq: float | None = None,
        txft: float | None = None,
        txfv: float | None = None,
        uwpqdip: float | None = None,
        wind_plant_qcontrol_modes_type: WindPlantQcontrolModeKind | None = None,
        xrefmax: float | None = None,
        xrefmin: float | None = None,
        wind_plant_iec: WindPlantIEC | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dxrefmax = dxrefmax
        self.dxrefmin = dxrefmin
        self.kiwpx = kiwpx
        self.kiwpxmax = kiwpxmax
        self.kiwpxmin = kiwpxmin
        self.kpwpx = kpwpx
        self.kwpqref = kwpqref
        self.kwpqu = kwpqu
        self.tuqfilt = tuqfilt
        self.twppfiltq = twppfiltq
        self.twpqfiltq = twpqfiltq
        self.twpufiltq = twpufiltq
        self.txft = txft
        self.txfv = txfv
        self.uwpqdip = uwpqdip
        self.wind_plant_qcontrol_modes_type = wind_plant_qcontrol_modes_type
        self.xrefmax = xrefmax
        self.xrefmin = xrefmin
        if wind_plant_iec is not None:
            self.wind_plant_iec = wind_plant_iec
        if wind_dynamics_lookup_table is not None:
            WindPlantReactiveControlIEC.wind_dynamics_lookup_table.extend(
                self, wind_dynamics_lookup_table
            )

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindPlantReactiveControlIEC.wind_dynamics_lookup_table.add(
            self, wind_dynamics_lookup_table
        )

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindPlantReactiveControlIEC.wind_dynamics_lookup_table.remove(
            self, wind_dynamics_lookup_table
        )

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindPlantReactiveControlIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindPlantReactiveControlIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindPlantReactiveControlIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)
