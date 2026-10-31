"""CIM compound ExtensionsList (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec61968.common.extension_item import ExtensionItem


class ExtensionsList(CimCompound):
    """Specifies the enumeration of the extension item"""

    __slots__ = ("extensions_item",)

    extensions_item: ExtensionItem | None

    _cim_meta = ClassMeta(
        cim_name="ExtensionsList",
        package="TC57CIM/IEC61968/Common",
        guid="{B7ADD1FE-36AB-4d66-B1F4-CFE0938D6E23}",
        kind="compound",
        attributes=(
            AttrMeta("extensions_item", "extensionsItem", "ExtensionItem", 0, 1, "compound"),
        ),
    )
