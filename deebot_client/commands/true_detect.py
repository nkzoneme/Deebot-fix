"""True detect command module."""

from ..events import TrueDetectEvent
from .common import SetEnableCommand, _GetEnableCommand


class GetTrueDetect(_GetEnableCommand):
    """Get multimap state command."""

    name = "getTrueDetect"
    event_type = TrueDetectEvent


class SetTrueDetect(SetEnableCommand):
    """Set multimap state command."""

    name = "setTrueDetect"
    get_command = GetTrueDetect
