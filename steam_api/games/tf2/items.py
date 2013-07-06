# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ITFPromos_440(SteamWebAPI):
    def GetItemID(self, steamid, promoid, **kwargs):
        parameters = {
            'steamid': steamid,
            'PromoID': promoid,
        }
        return self.generate_api_url(
            method='GetItemID',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GrantItem(self, steamid, promoid, **kwargs):
        parameters = {
            'steamid': steamid,
            'PromoID': promoid,
        }
        return self.generate_api_url(
            method='GrantItem',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )


class ITFItems_440(SteamWebAPI):
    def GetGoldenWrenches(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetGoldenWrenches',
            version=kwargs.get('version', 2),
            parameters=parameters,
            key=True
        )


class IEconItems_440(SteamWebAPI):
    def GetPlayerItems(self, steamid, **kwargs):
        parameters = {
            'steamid': steamid,
        }
        return self.generate_api_url(
            method='GetPlayerItems',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetSchema(self, language='', **kwargs):
        parameters = {
            'language': language,
        }
        return self.generate_api_url(
            method='GetSchema',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetSchemaURL(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetSchemaURL',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetStoreMetaData(self, language='', **kwargs):
        parameters = {
            'language': language,
        }
        return self.generate_api_url(
            method='GetStoreMetaData',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )

    def GetStoreStatus(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetStoreStatus',
            version=kwargs.get('version', 1),
            parameters=parameters,
            key=True
        )
