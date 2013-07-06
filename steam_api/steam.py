# =============================================================================
# >> IMPORTS
# =============================================================================
# API Imports
from api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ISteamEconomy(SteamWebAPI):
    def GetAssetPrices(self, appid, currency='usd', language='', **kwargs):
        parameters = {
            'appid': appid,
            'currency': currency,
            'language': language,
            'key': self.key,        # Required
        }
        version = kwargs.pop('method_version', 1)
        return self.generate_api_url(
            method='GetAssetPrices',
            version=version,
            parameters=parameters,
            key=True
        )

    def GetAssetClassInfo(self, appid, class_count, language='', **kwargs):
        parameters = {
            'appid': appid,
            'language': language,
            'class_count': class_count,
        }
        version = kwargs.pop('method_version', 1)
        parameters.extend(kwargs)
        return self.generate_api_url(
            method='GetAssetClassInfo',
            version=version,
            parameters=parameters,
            key=False
        )


class ISteamGameServerAccount(SteamWebAPI):
    def GetAccountPublicInfoBySteamID(self, steamid, **kwargs):
        parameters = {
            'steamID': steamid,
        }
        return self.generate_api_url(
            method='GetAccountPublicInfoBySteamID',
            version=kwargs.get('method_version', 1),
            parameters=parameters,
            key=False
        )


class ISteamApps(SteamWebAPI):
    def GetAppList(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetAppList',
            version=kwargs.get('method_version', 2),
            parameters=parameters,
            key=False
        )

    def GetServersAtAddress(self, addr, **kwargs):
        parameters = {
            'addr': addr,
        }
        return self.generate_api_url(
            method='GetServersAtAddress',
            version=kwargs.get('method_version', 1),
            parameters=parameters,
            key=False
        )

    def UpToDateCheck(self, appid, version, **kwargs):
        parameters = {
            'appid': appid,
            'method_version': version,
        }
        return self.generate_api_url(
            method='UpToDateCheck',
            version=kwargs.get('method_version', 1),
            parameters=parameters,
            key=False
        )


class ISteamNews(SteamWebAPI):
    def GetNewsForApp(self, appid, maxlength='', enddate='', count='',
                      feeds='', **kwargs):
        parameters = {
            'appid': appid,
            'maxlength': maxlength,
            'enddate': enddate,
            'count': count,
            'feeds': feeds,
        }
        return self.generate_api_url(
            method='GetNewsForApp',
            version=kwargs.get('method_version', 2),
            parameters=parameters,
            key=False
        )


class ISteamWebAPIUtil(SteamWebAPI):
    def GetServerInfo(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            metod='GetServerInfo',
            version=kwargs.get('method_version', 1),
            parameters=parameters,
            key=False
        )

    def GetSupportedAPIList(self, **kwargs):
        parameters = {}
        return self.generate_api_url(
            method='GetSupportedAPIList',
            version=kwargs.get('method_version', 1),
            parameters=parameters,
            key=True
        )
