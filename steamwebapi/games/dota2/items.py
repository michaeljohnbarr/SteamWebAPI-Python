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
class IEconDOTA2_570(_BaseIEconDOTA2):
    """Methods relating to in-game items for DOTA2."""


@public
class ITFPromos_570(_BaseITFPromos):
    """Methods for retrieving and granting promo items for DOTA2."""


@public
class IEconItems_570(_IEconItems):
    """Methods relating to in-game items for DOTA2."""
