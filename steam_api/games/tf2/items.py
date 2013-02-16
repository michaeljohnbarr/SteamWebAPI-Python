# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from steam_api.api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ITFPromos_440(SteamWebAPI):
    def __init__(self):
        self.interface = 'ITFPromos_440'
        super(ITFPromos_440, self).__init__()

    def GetItemID(self, steamid, promoid):
        params = {
            'steamid': steamid,
            'PromoID': promoid,
            }
        return self.generate_api_url(self.interface, 'GetItemID', 1,
            params, key=True)

    def GrantItem(self, steamid, promoid):
        params = {
            'steamid': steamid,
            'PromoID': promoid,
            }
        return self.generate_api_url(self.interface, 'GrantItem', 1,
            params, key=True)


class ITFItems_440(SteamWebAPI):
    def __init__(self):
        self.interface = 'ITFItems_440'
        super(ITFItems_440, self).__init__()

    def GetGoldenWrenches(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetGoldenWrenches', 2,
            params, key=True)

    def GetPlayerItems(self, steamid):
        params = {
            'steamid': steamid,
            }
        return self.generate_api_url(self.interface, 'GetPlayerItems', 1,
            params, key=True)

    def GetSchema(self, language=''):
        params = {
            'language': language,
            }
        return self.generate_api_url(self.interface, 'GetSchema', 1,
            params, key=True)


class IEconItems_440(SteamWebAPI):
    def __init__(self):
        self.interface = 'IEconItems_440'
        super(IEconItems_440, self).__init__()

    def GetPlayerItems(self, steamid):
        params = {
            'steamid': steamid,
            }
        return self.generate_api_url(self.interface, 'GetPlayerItems', 1,
            params, key=True)

    def GetSchema(self, language=''):
        params = {
            'language': language,
            }
        return self.generate_api_url(self.interface, 'GetSchema', 1,
            params, key=True)
