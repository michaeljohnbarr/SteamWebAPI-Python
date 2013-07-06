# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ITFPromos_260(SteamWebAPI):
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


class IEconItems_260(SteamWebAPI):
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
