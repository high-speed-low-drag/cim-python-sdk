"""CIM enumeration FuelSource (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FuelSource(CimEnum):
    """For example:

    Bio Gas (Landfill, Sewage, Digester, etc.)

    Biomass

    Coal

    DIST

    Natural Gas

    Geothermal

    HRCV

    None

    Nuclear

    Oil

    Other

    Solar

    Waste to Energy

    Water

    Wind"""

    NG = "NG"
    NNG = "NNG"
    BGAS = "BGAS"
    BIOM = "BIOM"
    COAL = "COAL"
    DIST = "DIST"
    GAS = "GAS"
    GEOT = "GEOT"
    HRCV = "HRCV"
    NONE = "NONE"
    NUCL = "NUCL"
    OIL = "OIL"
    OTHR = "OTHR"
    SOLR = "SOLR"
    WAST = "WAST"
    WATR = "WATR"
    WIND = "WIND"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FuelSource",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{E635DEB6-EC30-43bf-A794-170EDB83721B}",
            kind="enumeration",
        )
    )
