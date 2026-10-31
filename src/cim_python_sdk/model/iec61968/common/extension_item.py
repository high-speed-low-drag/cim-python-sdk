"""CIM compound ExtensionItem (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class ExtensionItem(CimCompound):
    """Specifies the extensions list items"""

    __slots__ = ("ext_name", "ext_type", "ext_value")

    ext_name: str | None
    ext_type: str | None
    ext_value: str | None

    _cim_meta = ClassMeta(
        cim_name="ExtensionItem",
        package="TC57CIM/IEC61968/Common",
        guid="{6A0ED3D3-488C-46b0-ADF5-BA4FECD1C76C}",
        kind="compound",
        attributes=(
            AttrMeta("ext_name", "extName", "str", 0, 1, "primitive"),
            AttrMeta("ext_type", "extType", "str", 0, 1, "primitive"),
            AttrMeta("ext_value", "extValue", "str", 0, 1, "primitive"),
        ),
    )
