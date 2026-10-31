"""Fast default mRIDs: random RFC 4122 version-4 UUID strings.

``str(uuid.uuid4())`` costs ~6 us per call here (plus ~7 ms to import `uuid`); this costs
~1 us. The bits come from a private `random.Random` seeded from `os.urandom` and reseeded
in forked children, so ids stay unique across processes and are unaffected by
``random.seed()``. They are identifiers, not secrets.
"""

from __future__ import annotations

import os
import random

from cim_python_sdk._runtime._compat import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

_rng = random.Random()
if hasattr(os, "register_at_fork"):
    os.register_at_fork(after_in_child=_rng.seed)

_KEEP = 0xFFFFFFFF_FFFF_0FFF_3FFF_FFFFFFFFFFFF  # clear version nibble and variant bits
_SET = 0x00000000_0000_4000_8000_000000000000  # version 4, RFC 4122 variant


def new_mrid(_bits: Callable[[int], int] = _rng.getrandbits) -> str:  # default bound for speed
    """A new random UUID4 string, e.g. ``'c4606c2a-d5a7-4bd9-b4d3-574af670778b'``."""
    h = f"{(_bits(128) & _KEEP) | _SET:032x}"
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"
