# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.match import BaseIDOTA2Match
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class IDOTA2Match_570(BaseIDOTA2Match):
    """Methods relating to Dota 2 matches."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(IDOTA2Match_570, self).__init__(*args, **kwargs)
