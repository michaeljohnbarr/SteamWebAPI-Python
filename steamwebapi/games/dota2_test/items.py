# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import _BaseITFPromos, _BaseIEconDOTA2, _IEconItems
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class IEconDOTA2_205790(_BaseIEconDOTA2):
    """Methods relating to in-game items for DOTA2 Test."""


@public
class ITFPromos_205790(_BaseITFPromos):
    """Methods for retrieving and granting promo items for Dota2 Test."""


@public
class IEconItems_205790(_IEconItems):
    """Methods relating to in-game items for Dota2 Test."""
