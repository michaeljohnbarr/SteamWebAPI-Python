# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from ..common.items import BaseITFPromos, BaseIEconItems
from ...core import SteamWebAPI
from ...util.decorators import public


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ITFItems_520(SteamWebAPI):
    """"""

    def GetGoldenWrenches(self, **kwargs):
        parameters = {}
        return self.api_query(
            method='GetGoldenWrenches',
            version=kwargs.get('method_version', 2),
            params=parameters,
            key=True
        )


@public
class ITFPromos_520(BaseITFPromos):
    """Methods for retrieving and and granting promo items."""


@public
class IEconItems_520(BaseIEconItems):
    """Methods relating to in-game items for supported games."""

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
