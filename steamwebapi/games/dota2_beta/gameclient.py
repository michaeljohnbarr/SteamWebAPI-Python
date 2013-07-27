# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import IGCVersion


# =============================================================================
# >> CLASSES
# =============================================================================
class IGCVersion_816(IGCVersion):
    """Methods for retrieving DOTA2 Beta version information."""

    def __init__(self, *args, **kwargs):
        """Initialize IGCVersion, which initializes SteamWebAPI."""
        super(IGCVersion_816, self).__init__(*args, **kwargs)
