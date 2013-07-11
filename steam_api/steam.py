# =============================================================================
# >> IMPORTS
# =============================================================================
# Python imports
import re

# API Imports
from api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ISteamEconomy(SteamWebAPI):
    """Methods relating to games' store's assets."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(self, ISteamEconomy).__init__(*args, **kwargs)

    def GetAssetPrices(self, appid, currency='usd', language='',
                       method_version=1):
        """Retrieves the prices of game assets/items from the Steam Store.

        http://wiki.teamfortress.com/wiki/WebAPI/GetAssetPrices

        """
        # Set up the parameters
        parameters = {
            'appid': appid,
            'currency': currency,
            'language': self.language or language,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            method='GetAssetPrices',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )

    def GetAssetClassInfo(self, appid, class_count, language='',
                          method_version=1, **kwargs):
        """Retrieves the class information of game assets/items from the Steam
        Store.

        http://wiki.teamfortress.com/wiki/WebAPI/GetAssetClassInfo

        """
        # Retrieve any instanceidN keyword arguments
        instanceidN = [
            i for i in kwargs.iteritems() if re.match('instanceid(\d+)', i[0])
        ]

        # Retrieve any classidN keyword arguments
        classidN = [
            i for i in kwargs.iteritems() if re.match('classid(\d+)', i[0])
        ]

        # Set up the parameters
        parameters = {
            'appid': appid,
            'language': self.language or language,
            'class_count': class_count,
        }

        # Update the parameters with instanceidN/classidN
        parameters.update(instanceidN)
        parameters.update(classidN)

        # Return the APIQuery
        return self.api_query(
            method='GetAssetClassInfo',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )


class ISteamGameServerAccount(SteamWebAPI):
    """"""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(self, ISteamGameServerAccount).__init__(*args, **kwargs)

    def GetAccountPublicInfoBySteamID(self, steamid, method_version=1):
        """Retrieves information when given a game server's steamid.

        Notes:
            * Undocumented on http://wiki.teamfortress.com
            * Returns error "SteamID does not refer to a persistent gameserver
              account" even if given a valid steamid as reported on
              https://developer.valvesoftware.com/wiki/Steam_Web_API/Feedback

        """
        # Set up the parameters
        parameters = {
            'steamID': steamid,
        }

        # Return the APIQuery
        return self.api_query(
            method='GetAccountPublicInfoBySteamID',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )


class ISteamApps(SteamWebAPI):
    """Methods relating to Steam Apps in general."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(self, ISteamApps).__init__(*args, **kwargs)

    def GetAppList(self, method_version=1):
        """Returns a full list of every publicly facing program in the
        store/library.

        http://wiki.teamfortress.com/wiki/WebAPI/GetAppList

        """
        # Set up the parameters
        parameters = {}

        # Return the APIQuery
        return self.api_query(
            method='GetAppList',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )

    def GetServersAtAddress(self, addr, method_version=1):
        """Retrieves servers listed on the master server or their rejection
        message.

        Notes:
            * Undocumented on http://wiki.teamfortress.com
            http://list-archives.org/2012/08/09/hlds-list-valvesoftware-com/
            new-webapi-is-my-server-listed-on-the-master-server/f/5340992970

        """
        # Set up the parameters
        parameters = {
            'addr': addr,
        }

        # Return the APIQuery
        return self.api_query(
            method='GetServersAtAddress',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )

    def UpToDateCheck(self, appid, version, method_version=1):
        """Determines if a game server is up to date.

        http://wiki.teamfortress.com/wiki/WebAPI/UpToDateCheck
        """
        # Set up the parameters
        parameters = {
            'appid': appid,
            'version': version,
        }

        # Return the APIQuery
        return self.api_query(
            method='UpToDateCheck',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )


class ISteamNews(SteamWebAPI):
    """Methods relating to Steam News."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(self, ISteamNews).__init__(*args, **kwargs)

    def GetNewsForApp(self, appid, maxlength='', enddate='', count='',
                      feeds='', method_version=2):
        """Retrieves news for the given appid.

        http://wiki.teamfortress.com/wiki/WebAPI/GetNewsForApp

        """
        # Set up the parameters
        parameters = {
            'appid': appid,
            'maxlength': maxlength,
            'enddate': enddate,
            'count': count,
            'feeds': feeds,
        }

        # Return the APIQuery
        return self.api_query(
            method='GetNewsForApp',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )


class ISteamWebAPIUtil(SteamWebAPI):
    """Methods relating to the WebAPI itself."""

    def __init__(self, *args, **kwargs):
        """Initialize SteamWebAPI."""
        super(self, ISteamWebAPIUtil).__init__(*args, **kwargs)

    def GetServerInfo(self, method_version=1):
        """Retrieves the Steam Web API server's time information

        http://wiki.teamfortress.com/wiki/WebAPI/GetServerInfo

        """
        # Set up the parameters
        parameters = {}

        # Return the APIQuery
        return self.api_query(
            method='GetServerInfo',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )

    def GetSupportedAPIList(self, key='', method_version=1):
        """Retrieves all available methods & interfaces for the Steam Web API.

        Note:
            * Presence of a Steam Web API key will display all available methods
              & interfaces allowed for that key.

        http://wiki.teamfortress.com/wiki/WebAPI/GetSupportedAPIList

        """
        # Set up the parameters
        parameters = {
            'key': key or self.key,
        }

        # Return the APIQuery
        return self.api_query(
            method='GetSupportedAPIList',
            method_version=method_version,
            httpmethod='GET',
            params=parameters,
        )
