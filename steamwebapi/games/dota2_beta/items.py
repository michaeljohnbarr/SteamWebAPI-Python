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
class IEconDOTA2_816(BaseIEconDOTA2):
    """Methods relating to in-game items for DOTA2 Beta."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseIEconDOTA2, which initializes SteamWebAPI."""
        super(IEconDOTA2_816, self).__init__(*args, **kwargs)


@public
class ITFPromos_816(BaseITFPromos):
    """Methods for retrieving and granting promo items for Dota2 Beta."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_816, self).__init__(*args, **kwargs)


@public
class IEconItems_816(IEconItems):
    """Methods relating to in-game items for Dota2 Beta."""
    def __init__(self, *args, **kwargs):
        """Initialize IEconItems, which initializes SteamWebAPI."""
        super(IEconItems_816, self).__init__(*args, **kwargs)
