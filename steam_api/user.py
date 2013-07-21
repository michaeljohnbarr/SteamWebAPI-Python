# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import re
from urllib2 import HTTPError

# API Imports
from api_base import SteamWebAPI


# =============================================================================
# >> CLASSES
# =============================================================================
class ISteamUser(SteamWebAPI):
    def GetFriendList(self, steamid, relationship='all', method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'relationship': relationship,
            'key': self.key,
        }
        # According to http://wiki.teamfortress.com/wiki/WebAPI/GetFriendList,
        #   "If the profile is not public or there are no available entries for
        #   the given relationship only an empty object will be returned."
        #   However, this is not the case. It gives a 401 Unauthorized
        #   HTTPError. Thus, we must create this workaround.
        try:
            return self.api_query(
                interface=self.__class__.__name__,
                method='GetFriendList',
                method_version=method_version,
                httpmethod='GET',
                parameters=parameters,
            )
        except HTTPError, e:
            # The expected 401 Unauthorized Error
            if e.code == 401:
                return {}
            # Expect the unexpected
            raise

    def GetPlayerBans(self, steamids=[], method_version=1):
        if isinstance(steamids, str):
            pass
        else:
            ",".join(steamids)

        # Set up the parameters
        parameters = {
            'steamids': steamids,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetPlayerBans',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetPlayerSummaries(self, steamids=[], method_version=2):
        """"""
        if isinstance(steamids, str):
            pass
        else:
            ",".join(steamids)

        # Set up the parameters
        parameters = {
            'steamids': steamids,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetPlayerSummaries',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetUserGroupList(self, steamid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetUserGroupList',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def ResolveVanityURL(self, vanityURL, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'vanityurl': vanityURL,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='ResolveVanityURL',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class ISteamUserStats(SteamWebAPI):
    """"""
    def GetGlobalAchievementPercentagesForApp(self, gameid, method_version=2):
        """"""
        # Set up the parameters
        parameters = {
            'gameid': gameid,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetGlobalAchievementPercentagesForApp',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetGlobalStatsForGame(self, appid, count, startdate, enddate,
                              method_version=1, **kwargs):
        """"""
        # Retrieve any nameN keyword arguments
        nameN = [
            i for i in kwargs.iteritems() if re.match('name(\d+)', i[0])
        ]

        # Set up the parameters
        parameters = {
            'appid': appid,
            'count': count,
            'startdate': startdate,
            'enddate': enddate,
        }

        # Update the parameters with nameN
        parameters.update(nameN)

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetGlobalStatsForGame',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetNumberOfCurrentPlayers(self, appid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'appid': appid,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetNumberOfCurrentPlayers',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetSchemaForGame(self, appid, l='', method_version=2):
        """Retrieves the game schema for the given appid."""
        # Set up the parameters
        parameters = {
            'appid': appid,
            'l': l or self.language,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchemaForGame',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetUserStatsForGame(self, steamid, appid, method_version=2):
        """Retrieves the stats for the given SteamID and appid."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'appid': appid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchemaForGame',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetPlayerAchievements(self, steamid, appid, l='', method_version=1):
        """Retrieves the achievements for the given SteamID and appid."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'appid': appid,
            'l': l or self.language,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetPlayerAchievements',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


class IPlayerService(SteamWebAPI):
    """"""
    def GetRecentlyPlayedGames(self, steamid, count=0, method_version=1):
        """Retrieves the recently played games for the given SteamID up to
        the given count.

        """
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'count': count,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetRecentlyPlayedGames',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetOwnedGames(self, steamid, include_appinfo=True,
                      include_played_free_games=True, appids_filter=[],
                      method_version=1):
        """Retrieves games owned by the given SteamID."""
        if isinstance(appids_filter, str):
            pass
        else:
            ",".join(appids_filter)

        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'include_appinfo': bool(include_appinfo),
            'include_played_free_games': bool(include_played_free_games),
            'appids_filter': appids_filter,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetOwnedGames',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetSteamLevel(self, steamid, method_version=1):
        """Retrieves the Steam Level for the given SteamID."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSteamLevel',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    def GetBadges(self, steamid, method_version=1):
        """Retrieves badge information for the given SteamID."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        return self.api_query(
            interface=self.__class__.__name__,
            method='GetBadges',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
