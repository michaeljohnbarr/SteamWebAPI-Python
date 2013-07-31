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


@public
class IEconItems_440(ExtendedIEconItems):
    """Methods relating to in-game items for TF2."""


@public
class ITFItems_440(SteamWebAPI):
    """Contains method for retrieving Golden Wrenches for TF2."""

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
