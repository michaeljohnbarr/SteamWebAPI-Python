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
class ITFPromos_260(BaseITFPromos):
    """Methods for retrieving and granting promo items for CS:S Beta."""


@public
class IEconItems_260(BaseIEconItems):
    """Methods relating to in-game items for CS:S Beta."""
