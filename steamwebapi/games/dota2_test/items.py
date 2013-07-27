# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import BaseITFPromos, BaseIEconDOTA2, IEconItems
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class IEconDOTA2_205790(BaseIEconDOTA2):
    """Methods relating to in-game items for DOTA2 Test."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseIEconDOTA2, which initializes SteamWebAPI."""
        super(IEconDOTA2_205790, self).__init__(*args, **kwargs)


@public
class ITFPromos_205790(BaseITFPromos):
    """Methods for retrieving and granting promo items for Dota2 Test."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_205790, self).__init__(*args, **kwargs)


@public
class IEconItems_205790(IEconItems):
    """Methods relating to in-game items for Dota2 Test."""
    def __init__(self, *args, **kwargs):
        """Initialize IEconItems, which initializes SteamWebAPI."""
        super(IEconItems_205790, self).__init__(*args, **kwargs)
