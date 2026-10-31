"""CIM compound RelativeDisplacement (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from cim_python_sdk.model.iec62325.environmental.env_domain.relative_displacement_kind import (
        RelativeDisplacementKind,
    )


class RelativeDisplacement(CimCompound):
    """Vertical displacement relative to either sealevel, ground or the center of the earth."""

    __slots__ = ("displacement", "kind")

    displacement: float | None  # Displacement
    kind: RelativeDisplacementKind | None

    _cim_meta = ClassMeta(
        cim_name="RelativeDisplacement",
        package="TC57CIM/IEC62325/Environmental/EnvDomain",
        guid="{3F066029-C493-49ce-A282-54B245B31FD6}",
        kind="compound",
        attributes=(
            AttrMeta("displacement", "displacement", "Displacement", 0, 1, "cimdatatype"),
            AttrMeta("kind", "kind", "RelativeDisplacementKind", 0, 1, "enumeration"),
        ),
    )
