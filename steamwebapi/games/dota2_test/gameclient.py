# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import IGCVersion
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class IGCVersion_205790(IGCVersion):
    """Methods for retrieving DOTA2 Test version information."""

    def __init__(self, *args, **kwargs):
        """Initialize IGCVersion, which initializes SteamWebAPI."""
        super(IGCVersion_205790, self).__init__(*args, **kwargs)
