# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import BaseITFPromos, ExtendedIEconItems
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ITFPromos_730(BaseITFPromos):
    """Methods for retrieving and granting promo items for CS:GO."""


@public
class IEconItems_730(ExtendedIEconItems):
    """Methods relating to in-game items for CS:GO."""
