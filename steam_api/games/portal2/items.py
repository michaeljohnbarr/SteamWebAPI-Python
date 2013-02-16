class ITFPromos_620(SteamWebAPI):
    def __init__(self):
        self.interface = 'ITFPromos_620'
        super(ITFPromos_620, self).__init__()

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


class IEconItems_620(SteamWebAPI):
    def __init__(self):
        self.interface = 'IEconItems_620'
        super(IEconItems_620, self).__init__()

    def GetPlayerItems(self, steamid):
        params = {
            'steamid': steamid,
            }
        return self.generate_api_url(self.interface, 'GetPlayerItems', 1,
            params, key=True)

    def GetSchema(self, language='en'):
        params = {
            'language': language,
            }
        return self.generate_api_url(self.interface, 'GetSchema', 1,
            params, key=True)