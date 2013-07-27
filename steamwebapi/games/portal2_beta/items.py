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
class ITFPromos_841(BaseITFPromos):
    """Methods for retrieving and granting promo items for Portal 2 Beta."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_841, self).__init__(*args, **kwargs)


@public
class IEconItems_841(BaseIEconItems):
    """Methods relating to in-game items for Portal 2 Beta.."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseIEconItems, which initializes SteamWebAPI."""
        super(IEconItems_841, self).__init__(*args, **kwargs)
