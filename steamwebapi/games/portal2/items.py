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
class ITFPromos_620(BaseITFPromos):
    """Methods for retrieving and granting promo items for Portal 2."""


@public
class IEconItems_620(BaseIEconItems):
    """Methods relating to in-game items for Portal 2."""
