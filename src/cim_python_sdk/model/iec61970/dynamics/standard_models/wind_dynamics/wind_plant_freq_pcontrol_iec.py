"""CIM class WindPlantFreqPcontrolIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

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


class WindPlantFreqPcontrolIEC(IdentifiedObject):
    """Frequency and active power controller model.

    Reference: IEC 61400-27-1:2015, Annex D."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_plant_iec",
        "dprefmax",
        "dprefmin",
        "dpwprefmax",
        "dpwprefmin",
        "kiwpp",
        "kiwppmax",
        "kiwppmin",
        "kpwpp",
        "kwppref",
        "prefmax",
        "prefmin",
        "tpft",
        "tpfv",
        "twpffiltp",
        "twppfiltp",
    )

    dprefmax: float | None  # PU
    dprefmin: float | None  # PU
    dpwprefmax: float | None  # PU
    dpwprefmin: float | None  # PU
    kiwpp: float | None
    kiwppmax: float | None  # PU
    kiwppmin: float | None  # PU
    kpwpp: float | None
    kwppref: float | None  # PU
    prefmax: float | None  # PU
    prefmin: float | None  # PU
    tpft: float | None  # Seconds
    tpfv: float | None  # Seconds
    twpffiltp: float | None  # Seconds
    twppfiltp: float | None  # Seconds

    wind_dynamics_lookup_table: Many[WindDynamicsLookupTable] = Many(
        EndMeta(
            name="wind_dynamics_lookup_table",
            cim_role="WindDynamicsLookupTable",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table:WindDynamicsLookupTable",
            many=True,
            lower=1,
            upper=None,
            inverse="wind_plant_freq_pcontrol_iec",
            aggregation="none",
        )
    )
    wind_plant_iec: One[WindPlantIEC] = One(
        EndMeta(
            name="wind_plant_iec",
            cim_role="WindPlantIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_plant_iec:WindPlantIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_plant_freq_pcontrol_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindPlantFreqPcontrolIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{A6A0C6E1-3076-4cef-B5CA-3913BC3C0440}",
        attributes=(
            AttrMeta("dprefmax", "dprefmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dprefmin", "dprefmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dpwprefmax", "dpwprefmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dpwprefmin", "dpwprefmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiwpp", "kiwpp", "float", 0, 1, "primitive"),
            AttrMeta("kiwppmax", "kiwppmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kiwppmin", "kiwppmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpwpp", "kpwpp", "float", 0, 1, "primitive"),
            AttrMeta("kwppref", "kwppref", "PU", 0, 1, "cimdatatype"),
            AttrMeta("prefmax", "prefmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("prefmin", "prefmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpft", "tpft", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpfv", "tpfv", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twpffiltp", "twpffiltp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("twppfiltp", "twppfiltp", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_dynamics_lookup_table.meta,
            wind_plant_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        dprefmax: float | None = None,
        dprefmin: float | None = None,
        dpwprefmax: float | None = None,
        dpwprefmin: float | None = None,
        kiwpp: float | None = None,
        kiwppmax: float | None = None,
        kiwppmin: float | None = None,
        kpwpp: float | None = None,
        kwppref: float | None = None,
        prefmax: float | None = None,
        prefmin: float | None = None,
        tpft: float | None = None,
        tpfv: float | None = None,
        twpffiltp: float | None = None,
        twppfiltp: float | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        wind_plant_iec: WindPlantIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dprefmax = dprefmax
        self.dprefmin = dprefmin
        self.dpwprefmax = dpwprefmax
        self.dpwprefmin = dpwprefmin
        self.kiwpp = kiwpp
        self.kiwppmax = kiwppmax
        self.kiwppmin = kiwppmin
        self.kpwpp = kpwpp
        self.kwppref = kwppref
        self.prefmax = prefmax
        self.prefmin = prefmin
        self.tpft = tpft
        self.tpfv = tpfv
        self.twpffiltp = twpffiltp
        self.twppfiltp = twppfiltp
        if wind_dynamics_lookup_table is not None:
            WindPlantFreqPcontrolIEC.wind_dynamics_lookup_table.extend(
                self, wind_dynamics_lookup_table
            )
        if wind_plant_iec is not None:
            self.wind_plant_iec = wind_plant_iec

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindPlantFreqPcontrolIEC.wind_dynamics_lookup_table.add(
            self, wind_dynamics_lookup_table
        )

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindPlantFreqPcontrolIEC.wind_dynamics_lookup_table.remove(
            self, wind_dynamics_lookup_table
        )

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindPlantFreqPcontrolIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindPlantFreqPcontrolIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindPlantFreqPcontrolIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)
