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


@public
class IEconItems_841(BaseIEconItems):
    """Methods relating to in-game items for Portal 2 Beta.."""
