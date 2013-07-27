# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import BaseIGCVersion
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class IGCVersion_520(BaseIGCVersion):
    """Methods for retrieving TF2 Beta version information."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseIGCVersion, which initializes SteamWebAPI."""
        super(IGCVersion_520, self).__init__(*args, **kwargs)
