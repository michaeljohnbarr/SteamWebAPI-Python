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


@public
class ITFPromos_816(BaseITFPromos):
    """Methods for retrieving and granting promo items for Dota2 Beta."""


@public
class IEconItems_816(IEconItems):
    """Methods relating to in-game items for Dota2 Beta."""
