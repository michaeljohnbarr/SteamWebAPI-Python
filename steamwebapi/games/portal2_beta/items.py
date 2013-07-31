# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import _BaseITFPromos, _BaseIEconItems
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ITFPromos_841(_BaseITFPromos):
    """Methods for retrieving and granting promo items for Portal 2 Beta."""


@public
class IEconItems_841(_BaseIEconItems):
    """Methods relating to in-game items for Portal 2 Beta.."""
