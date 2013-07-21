# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ...common.items import BaseITFPromos, BaseIEconItems
from ...api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ITFItems_520(SteamWebAPI):
    def GetGoldenWrenches(self, **kwargs):
        parameters = {}
        return self.api_query(
            method='GetGoldenWrenches',
            version=kwargs.get('method_version', 2),
            params=parameters,
            key=True
        )


class ITFPromos_520(BaseITFPromos):
    """Methods for retrieving and and granting promo items."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseITFPromos, which initializes SteamWebAPI."""
        super(ITFPromos_520, self).__init__(*args, **kwargs)


class IEconItems_520(BaseIEconItems):
    """Methods relating to in-game items for supported games."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseIEconItems, which initializes SteamWebAPI."""
        super(IEconItems_520, self).__init__(*args, **kwargs)

    def GetSchemaURL(self, **kwargs):
        parameters = {}
        return self.api_query(
            method='GetSchemaURL',
            version=kwargs.get('method_version', 1),
            params=parameters,
            key=True
        )

    def GetStoreMetaData(self, language='', **kwargs):
        parameters = {
            'language': language,
        }
        return self.api_query(
            method='GetStoreMetaData',
            version=kwargs.get('method_version', 1),
            params=parameters,
            key=True
        )

    def GetStoreStatus(self, **kwargs):
        parameters = {}
        return self.api_query(
            method='GetStoreStatus',
            version=kwargs.get('method_version', 1),
            params=parameters,
            key=True
        )
