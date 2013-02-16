# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ISteamEconomy(SteamWebAPI):
    def __init__(self):
        self.interface = 'ISteamEconomy'
        super(ISteamEconomy, self).__init__()

    def GetAssetPrices(self, appid, currency='usd', language=''):
        params = {
            'appid': appid,
            'currency': currency,
            'language': language,
        }
        return self.generate_api_url(self.interface, 'GetAssetPrices', 1,
            params, key=True)

    def GetAssetClassInfo(self, appid, class_count, language='', **kwargs):
        params = {
            'appid': appid,
            'language': language,
            'class_count': class_count,
            }
        params.extend(kwargs)
        return self.generate_api_url(self.interface, 'GetAssetClassInfo', 1,
            params, key=False)


class ISteamGameServerAccount(SteamWebAPI):
    def __init__(self):
        self.interface = 'ISteamGameServerAccount'
        super(ISteamGameServerAccount, self).__init__()

    def GetAccountPublicInfoBySteamID(self, steamid):
        params = {
            'steamID': steamid,
            }
        return self.generate_api_url(self.interface,
            'GetAccountPublicInfoBySteamID', 1, params, key=False)


class ISteamApps(SteamWebAPI):
    def __init__(self):
        self.interface = 'ISteamApps'
        super(ISteamApps, self).__init__()

    def GetAppList(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetAppList', 2,
            params, key=False)#['applist']['apps']

    def GetServersAtAddress(self, addr):
        params = {
            'addr': addr,
            }
        return self.generate_api_url(self.interface, 'GetServersAtAddress', 1,
            params, key=False)

    def UpToDateCheck(self, appid, version):
        params = {
            'appid': appid,
            'version': version,
            }
        return self.generate_api_url(self.interface, 'UpToDateCheck', 1,
            params, key=False)


class ISteamNews(SteamWebAPI):
    def __init__(self):
        self.interface = 'ISteamNews'
        super(ISteamNews, self).__init__()

    def GetNewsForApp(self, appid, maxlength='', enddate='', count='',
        feeds=''):
        params = {
            'appid': appid,
            'maxlength': maxlength,
            'enddate': enddate,
            'count': count,
            'feeds': feeds,
            }
        return self.generate_api_url(self.interface, 'GetNewsForApp', 2,
            params, key=False)


class ISteamWebAPIUtil(SteamWebAPI):
    def __init__(self):
        self.interface = 'ISteamWebAPIUtil'
        super(ISteamWebAPIUtil, self).__init__()
        
    def GetServerInfo(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetServerInfo', 1,
            params, key=False)

    def GetSupportedAPIList(self):
        params = {}
        return self.generate_api_url(self.interface, 'GetSupportedAPIList', 1,
            params, key=True)