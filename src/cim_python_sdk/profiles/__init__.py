"""Profiles over the cim_python_sdk classes: which classes and properties a profile carries, and
validation of objects against selected profiles.

    from cim_python_sdk.profiles import cgmes3, validate_profile

    cgmes3.EQ.required(cim_python_sdk.ACLineSegment)         # r, x, bch, ... (PropertyInfo)
    cgmes3.profiles_of(cim_python_sdk.Terminal, "connected")  # (SSH,)
    validate_profile(objects, [cgmes3.EQ, cgmes3.TP])

`cim_python_sdk.profiles.cgmes3` is the CGMES 3.0 profile set and, at the same time, a facade that
re-exports exactly the CGMES 3.0 classes (``from cim_python_sdk.profiles.cgmes3 import ACLineSegment``).
Further profile sets load with ``ProfileSet.load("<snapshot>.json", "<name>")``.
"""

from cim_python_sdk.profiles._model import Profile, ProfileSet, PropertyInfo
from cim_python_sdk.profiles._validate import ProfileIssue, validate_profile

__all__ = [
    "Profile",
    "ProfileIssue",
    "ProfileSet",
    "PropertyInfo",
    "validate_profile",
]
