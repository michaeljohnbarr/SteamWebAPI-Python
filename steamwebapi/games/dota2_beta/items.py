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
class IEconDOTA2_816(_BaseIEconDOTA2):
    """Methods relating to in-game items for DOTA2 Beta."""


@public
class ITFPromos_816(_BaseITFPromos):
    """Methods for retrieving and granting promo items for Dota2 Beta."""


@public
class IEconItems_816(_IEconItems):
    """Methods relating to in-game items for Dota2 Beta."""
