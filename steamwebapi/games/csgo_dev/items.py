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


@public
class IEconItems_710(BaseIEconItems):
    """Methods relating to in-game items for CS:GO Dev."""
