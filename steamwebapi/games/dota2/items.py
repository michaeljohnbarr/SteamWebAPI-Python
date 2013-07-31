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
class IEconDOTA2_570(BaseIEconDOTA2):
    """Methods relating to in-game items for DOTA2."""


@public
class ITFPromos_570(BaseITFPromos):
    """Methods for retrieving and granting promo items for DOTA2."""


@public
class IEconItems_570(IEconItems):
    """Methods relating to in-game items for DOTA2."""
