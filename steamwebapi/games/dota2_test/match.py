# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.match import BaseIDOTA2Match


# =============================================================================
# >> CLASSES
# =============================================================================
class IDOTA2Match_205790(BaseIDOTA2Match):
    """Methods relating to Dota 2 Beta matches."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(IDOTA2Match_205790, self).__init__(*args, **kwargs)
