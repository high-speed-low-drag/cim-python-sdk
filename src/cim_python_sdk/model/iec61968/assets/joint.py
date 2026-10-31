"""CIM class Joint (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.joint_configuration_kind import (
        JointConfigurationKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.joint_fill_kind import JointFillKind


class Joint(Asset):
    """Joint connects two or more cables. It includes the portion of cable under wipes, welds,
    or other seals."""

    __slots__ = ("configuration_kind", "fill_kind", "insulation")

    configuration_kind: JointConfigurationKind | None
    fill_kind: JointFillKind | None
    insulation: str | None

    _cim_meta = ClassMeta(
        cim_name="Joint",
        package="TC57CIM/IEC61968/Assets",
        guid="{CAE9DEC7-39E9-4f9e-80FC-6AA9FF086528}",
        attributes=(
            AttrMeta(
                "configuration_kind",
                "configurationKind",
                "JointConfigurationKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("fill_kind", "fillKind", "JointFillKind", 0, 1, "enumeration"),
            AttrMeta("insulation", "insulation", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        configuration_kind: JointConfigurationKind | None = None,
        fill_kind: JointFillKind | None = None,
        insulation: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.configuration_kind = configuration_kind
        self.fill_kind = fill_kind
        self.insulation = insulation
