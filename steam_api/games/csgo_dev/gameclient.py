# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.gameclient import IGCVersion


# =============================================================================
# >> CLASSES
# =============================================================================
class IGCVersion_570(IGCVersion):
    """Methods for retrieving DOTA2 version information."""

    def __init__(self, *args, **kwargs):
        """Initialize IGCVersion, which initializes SteamWebAPI."""
        super(IGCVersion_570, self).__init__(*args, **kwargs)