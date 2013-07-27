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
class IDOTA2Match_816(BaseIDOTA2Match):
    """Methods relating to Dota 2 Beta matches."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(IDOTA2Match_816, self).__init__(*args, **kwargs)
