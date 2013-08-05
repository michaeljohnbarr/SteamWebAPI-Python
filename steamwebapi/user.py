# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
import re
from collections import Iterable

# API Imports
from .core import SteamWebAPI
from .util.decorators import public, api_key_required


# =============================================================================
# >> CLASSES
# =============================================================================
@public
class ISteamUser(SteamWebAPI):
    """"""

    @api_key_required
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
        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetFriendList',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetPlayerBans(self, steamids=[], method_version=1):
        """"""
        # If we are passed a non-string iterable, join steamids with ","
        if not isinstance(steamids, str) and isinstance(steamids, Iterable):
            ",".join(steamids)
        else:
            steamids = str(steamids)

        # Set up the parameters
        parameters = {
            'steamids': steamids,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetPlayerBans',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetPlayerSummaries(self, steamids=[], method_version=2):
        """"""
        # If we are passed a non-string iterable, join steamids with ","
        if not isinstance(steamids, str) and isinstance(steamids, Iterable):
            ",".join(steamids)
        else:
            steamids = str(steamids)

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

    @api_key_required
    def GetUserGroupList(self, steamid, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetUserGroupList',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def ResolveVanityURL(self, vanityURL, method_version=1):
        """"""
        # Set up the parameters
        parameters = {
            'vanityurl': vanityURL,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='ResolveVanityURL',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


@public
class ISteamUserStats(SteamWebAPI):
    """"""
    def GetGlobalAchievementPercentagesForApp(self, gameid, method_version=2):
        """"""
        # Set up the parameters
        parameters = {
            'gameid': gameid,
        }

        # Return the APIQuery
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

        # Return the APIQuery
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

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetNumberOfCurrentPlayers',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetSchemaForGame(self, appid, l='', method_version=2):
        """Retrieves the game schema for the given appid."""
        # Set up the parameters
        parameters = {
            'appid': appid,
            'l': l or self.language,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchemaForGame',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetUserStatsForGame(self, steamid, appid, method_version=2):
        """Retrieves the stats for the given SteamID and appid."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'appid': appid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSchemaForGame',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetPlayerAchievements(self, steamid, appid, l='', method_version=1):
        """Retrieves the achievements for the given SteamID and appid."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'appid': appid,
            'l': l or self.language,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetPlayerAchievements',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )


@public
class IPlayerService(SteamWebAPI):
    """"""
    @api_key_required
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

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetRecentlyPlayedGames',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
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

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetOwnedGames',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetSteamLevel(self, steamid, method_version=1):
        """Retrieves the Steam Level for the given SteamID."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetSteamLevel',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetBadges(self, steamid, method_version=1):
        """Retrieves badge information for the given SteamID."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetBadges',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )

    @api_key_required
    def GetCommunityBadgeProgress(self, steamid, badgeid, method_version=1):
        """Retrieves badge progress for the given SteamID."""
        # Set up the parameters
        parameters = {
            'steamid': steamid,
            'badgeid': badgeid,
            'key': self.key,
        }

        # Return the APIQuery
        return self.api_query(
            interface=self.__class__.__name__,
            method='GetCommunityBadgeProgress',
            method_version=method_version,
            httpmethod='GET',
            parameters=parameters,
        )
