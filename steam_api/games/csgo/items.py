# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import BaseITFPromos, ExtendedIEconItems


# =============================================================================
# >> CLASSES
# =============================================================================
class ITFPromos_730(BaseITFPromos):
    """Methods for retrieving and granting promo items for CS:GO."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_730, self).__init__(*args, **kwargs)


class IEconItems_730(ExtendedIEconItems):
    """Methods relating to in-game items for CS:GO."""
    def __init__(self, *args, **kwargs):
        """Initialize ExtendedIEconItems, which initializes SteamWebAPI."""
        super(IEconItems_730, self).__init__(*args, **kwargs)
