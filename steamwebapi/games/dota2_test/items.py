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


@public
class ITFPromos_205790(BaseITFPromos):
    """Methods for retrieving and granting promo items for Dota2 Test."""


@public
class IEconItems_205790(IEconItems):
    """Methods relating to in-game items for Dota2 Test."""
