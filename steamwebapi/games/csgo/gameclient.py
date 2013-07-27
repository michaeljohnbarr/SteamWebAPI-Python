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
class IGCVersion_730(IGCVersion):
    """Methods for retrieving CS:GO version information."""

    def __init__(self, *args, **kwargs):
        """Initialize IGCVersion, which initializes SteamWebAPI."""
        super(IGCVersion_730, self).__init__(*args, **kwargs)
