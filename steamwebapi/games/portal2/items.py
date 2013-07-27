# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import BaseITFPromos, BaseIEconItems


# =============================================================================
# >> CLASSES
# =============================================================================
class ITFPromos_620(BaseITFPromos):
    """Methods for retrieving and granting promo items for Portal 2."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_620, self).__init__(*args, **kwargs)


class IEconItems_620(BaseIEconItems):
    """Methods relating to in-game items for Portal 2."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseIEconItems, which initializes SteamWebAPI."""
        super(IEconItems_620, self).__init__(*args, **kwargs)
