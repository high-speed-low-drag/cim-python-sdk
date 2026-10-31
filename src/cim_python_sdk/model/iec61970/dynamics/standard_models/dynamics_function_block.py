"""CIM class DynamicsFunctionBlock (TC57CIM/IEC61970/Dynamics/StandardModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class DynamicsFunctionBlock(IdentifiedObject):
    """Abstract parent class for all Dynamics function blocks."""

    __slots__ = ("enabled",)

    enabled: bool | None

    _cim_meta = ClassMeta(
        cim_name="DynamicsFunctionBlock",
        package="TC57CIM/IEC61970/Dynamics/StandardModels",
        guid="{1CD8BBD4-A285-4466-A0D2-C02CB645EFBB}",
        attributes=(AttrMeta("enabled", "enabled", "bool", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        enabled: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.enabled = enabled
