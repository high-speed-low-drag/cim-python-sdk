"""CIM datatype Money (TC57CIM/IEC61970/Base/Domain). Generated code: do not edit."""

from __future__ import annotations

from decimal import Decimal

from cim_python_sdk._runtime import AttrMeta, CimDatatype, ClassMeta


class Money(CimDatatype):
    """Amount of money."""

    __slots__ = ()

    value_type = Decimal

    _cim_meta = ClassMeta(
        cim_name="Money",
        package="TC57CIM/IEC61970/Base/Domain",
        guid="{5E4B6DE1-9115-4fce-9859-6714580E5C66}",
        kind="cimdatatype",
        attributes=(
            AttrMeta("multiplier", "multiplier", "UnitMultiplier", 0, 1, "enumeration"),
            AttrMeta("unit", "unit", "Currency", 0, 1, "enumeration"),
            AttrMeta("value", "value", "Decimal", 0, 1, "primitive"),
        ),
    )
