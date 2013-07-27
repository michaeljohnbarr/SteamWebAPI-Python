# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ...core import SteamWebAPI
from ...util.decorators import public
from ..common.items import BaseITFPromos, ExtendedIEconItems


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ITFPromos_440(BaseITFPromos):
    """Methods for retrieving and granting promo items for TF2."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_440, self).__init__(*args, **kwargs)


@public
class IEconItems_440(ExtendedIEconItems):
    """Methods relating to in-game items for TF2."""
    def __init__(self, *args, **kwargs):
        """Initialize ExtendedIEconItems, which initializes SteamWebAPI."""
        super(IEconItems_440, self).__init__(*args, **kwargs)


@public
class ITFItems_440(SteamWebAPI):
    """Contains method for retrieving Golden Wrenches for TF2."""
    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(ITFPromos_440, self).__init__(*args, **kwargs)

    def GetGoldenWrenches(self, method_version=2):
        """Retrieves a list of all owners of golden wrenches."""
        # Set up the parameters
        parameters = {
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetGoldenWrenches',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
