"""Typing stand-ins so the runtime never imports `typing` (it costs ~15 ms).

Type checkers treat a module-level ``TYPE_CHECKING = False`` like ``typing.TYPE_CHECKING``
and see the real `Generic`; at runtime it is a no-op substitute.
"""

TYPE_CHECKING = False

if TYPE_CHECKING:
    from typing import Generic
else:

    class Generic:
        """Runtime stand-in: ``Cls[X]`` returns ``Cls`` itself."""

        __slots__ = ()

        def __class_getitem__(cls, item):
            return cls


__all__ = ["TYPE_CHECKING", "Generic"]
