# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import BaseITFPromos, BaseIEconItems
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ITFPromos_710(BaseITFPromos):
    """Methods for retrieving and granting promo items for CS:GO Dev."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_710, self).__init__(*args, **kwargs)


@public
class IEconItems_710(BaseIEconItems):
    """Methods relating to in-game items for CS:GO Dev."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseIEconItems, which initializes SteamWebAPI."""
        super(IEconItems_710, self).__init__(*args, **kwargs)
